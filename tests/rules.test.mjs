// Firestore güvenlik kuralı testleri — emülatörde çalışır: firebase emulators:exec --only firestore "node tests/rules.test.mjs"
import { initializeTestEnvironment, assertSucceeds, assertFails } from "@firebase/rules-unit-testing";
import { doc, getDoc, setDoc, updateDoc, getDocs, collection, query, where, serverTimestamp, Timestamp } from "firebase/firestore";
import { readFileSync } from "node:fs";

const env = await initializeTestEnvironment({
  projectId: "demo-acil-sinav",
  firestore: { rules: readFileSync(new URL("../firestore.rules", import.meta.url), "utf8"), host: "127.0.0.1", port: 8085 },
});
const now = Date.now(), H = 3600e3;
const ts = ms => Timestamp.fromMillis(ms);
const user = (uid, email) => env.authenticatedContext(uid, { email, email_verified: true }).firestore();
const admin = user("adm", "gultekinkadi@gmail.com");
const ayse = user("u1", "ayse@gmail.com");      // asistan, atanmış
const ali = user("u2", "ali@gmail.com");        // asistan, atanmamış
const yazar = user("au1", "yazar@gmail.com");   // soru yazarı
const yabanci = user("x1", "yabanci@gmail.com");

let pass = 0, failN = 0;
async function t(name, fn) { try { await fn(); pass++; console.log("  ✓", name); } catch (e) { failN++; console.log("  ✗", name, "\n     ", e?.message || e); } }

await env.withSecurityRulesDisabled(async c => {
  const d = c.firestore();
  await setDoc(doc(d, "residents/ayse@gmail.com"), { name: "Ayşe", kidem: 2 });
  await setDoc(doc(d, "residents/ali@gmail.com"), { name: "Ali", kidem: 3 });
  await setDoc(doc(d, "meta/roles"), { authors: ["yazar@gmail.com"] });
  const base = { title: "S", durationMin: 30, published: true, items: [], cases: {} };
  await setDoc(doc(d, "exams/e1"), { ...base, startAt: ts(now - H), endAt: ts(now + H), assigned: ["ayse@gmail.com"] });
  await setDoc(doc(d, "exams/e2"), { ...base, startAt: ts(now - 3 * H), endAt: ts(now - 2 * H), assigned: ["ayse@gmail.com"], lateUntil: { "ayse@gmail.com": ts(now + H) } });
  await setDoc(doc(d, "exams/e3"), { ...base, startAt: ts(now - H), endAt: ts(now + H), drawCount: 2, plan: { perResident: true } });
  await setDoc(doc(d, "exams/e4"), { ...base, startAt: ts(now - H), endAt: ts(now + H), appealsOpen: false });
  await setDoc(doc(d, "exams/old"), { ...base, startAt: ts(now - H), endAt: ts(now + H) }); // assigned alanı yok → herkes
  await setDoc(doc(d, "grades/e1_u1"), { pct: 50 });
  await setDoc(doc(d, "grades/e4_u1"), { pct: 50 });
  await setDoc(doc(d, "attempts/old_u1"), { examId: "old", uid: "u1", status: "started", startedAt: ts(now - 40 * 60e3), pos: 3, device: "devA", answers: {} });
  await setDoc(doc(d, "attempts/e4_u1"), { examId: "e4", uid: "u1", status: "started", startedAt: ts(now - 10 * 60e3), pos: 0, device: null, answers: {} });
  await setDoc(doc(d, "questions/qp"), { stem: "p", practice: true, status: "approved" });
  await setDoc(doc(d, "questions/qn"), { stem: "n", practice: false });
  await setDoc(doc(d, "questions/qy"), { stem: "y", status: "pending", author: "yazar@gmail.com", practice: false });
  await setDoc(doc(d, "questions/qo"), { stem: "o", status: "pending", author: "baska@gmail.com", practice: false });
});

console.log("Sınav erişimi");
await t("atanan asistan sınavı okur", () => assertSucceeds(getDoc(doc(ayse, "exams/e1"))));
await t("atanmayan asistan sınavı okuyamaz", () => assertFails(getDoc(doc(ali, "exams/e1"))));
await t("assigned alanı olmayan eski sınav herkese açık", () => assertSucceeds(getDoc(doc(ali, "exams/old"))));
await t("listede olmayan hesap sınavı okuyamaz", () => assertFails(getDoc(doc(yabanci, "exams/old"))));
await t("asistan sınav listesini sorgulayamaz", () => assertFails(getDocs(collection(ayse, "exams"))));
await t("asistan cevap anahtarını okuyamaz", () => assertFails(getDoc(doc(ayse, "examKeys/e1"))));

console.log("Sınava başlama");
const att = (ex, uid, extra = {}) => ({ examId: ex, uid, email: "x", name: "x", status: "started", startedAt: serverTimestamp(), order: [], optOrder: {}, answers: {}, flags: {}, qtime: {}, pos: 0, device: null, ...extra });
await t("atanan asistan başlatabilir", () => assertSucceeds(setDoc(doc(ayse, "attempts/e1_u1"), att("e1", "u1"))));
await t("atanmayan asistan başlatamaz", () => assertFails(setDoc(doc(ali, "attempts/e1_u2"), att("e1", "u2"))));
await t("kapanmış sınava geç başlama izniyle başlanır", () => assertSucceeds(setDoc(doc(ayse, "attempts/e2_u1"), att("e2", "u1"))));
await t("kendine ek süre yazamaz (deadlineAt)", () => assertFails(setDoc(doc(ali, "attempts/old_u2"), att("old", "u2", { deadlineAt: ts(now + 9 * H) }))));
await t("kişiye özel sette soru sayısı plana uymalı (eksik)", () => assertFails(setDoc(doc(ali, "attempts/e3_u2"), att("e3", "u2", { order: ["a"] }))));
await t("kişiye özel sette doğru sayı kabul edilir", () => assertSucceeds(setDoc(doc(ali, "attempts/e3_u2"), att("e3", "u2", { order: ["a", "b"] }))));

console.log("Sınav sırasında");
await t("cevap kaydı süre içinde kabul", () => assertSucceeds(updateDoc(doc(ayse, "attempts/e4_u1"), { answers: { q: 1 }, pos: 1, qtime: { q: 12 } })));
await t("sıralı sınavda geri dönülemez (pos azalamaz)", () => assertFails(updateDoc(doc(ayse, "attempts/e4_u1"), { pos: 0 })));
await t("boş cihaz kilidi alınabilir", () => assertSucceeds(updateDoc(doc(ayse, "attempts/e4_u1"), { device: "devB" })));
await t("dolu cihaz kilidi değiştirilemez", () => assertFails(updateDoc(doc(ayse, "attempts/e4_u1"), { device: "devC" })));
await t("puan alanı yazılamaz", () => assertFails(updateDoc(doc(ayse, "attempts/e4_u1"), { openScores: { q: 5 } })));
await t("süresi dolmuş oturuma yazılamaz", () => assertFails(updateDoc(doc(ayse, "attempts/old_u1"), { answers: { q: 2 } })));
await t("yönetici ek süre verir", () => assertSucceeds(updateDoc(doc(admin, "attempts/old_u1"), { deadlineAt: ts(now + H) })));
await t("ek süreden sonra asistan yazabilir", () => assertSucceeds(updateDoc(doc(ayse, "attempts/old_u1"), { answers: { q: 2 } })));

console.log("İtiraz");
const ap = (ex, q, extra = {}) => ({ examId: ex, uid: "u1", email: "ayse@gmail.com", name: "Ayşe", qid: q, text: "Gerekçe metni", status: "pending", createdAt: serverTimestamp(), ...extra });
await t("sonucu yayınlanmış sınava itiraz edilir", () => assertSucceeds(setDoc(doc(ayse, "appeals/e1_u1_q1"), ap("e1", "q1"))));
await t("itirazlar kapalıysa edilemez", () => assertFails(setDoc(doc(ayse, "appeals/e4_u1_q1"), ap("e4", "q1"))));
await t("sonuç yayınlanmadan itiraz edilemez", () => assertFails(setDoc(doc(ayse, "appeals/old_u1_q1"), ap("old", "q1"))));
await t("itiraz kabul edilmiş olarak yazılamaz", () => assertFails(setDoc(doc(ayse, "appeals/e1_u1_q2"), ap("e1", "q2", { status: "accepted" }))));
await t("asistan kendi itirazını okur", () => assertSucceeds(getDocs(query(collection(ayse, "appeals"), where("examId", "==", "e1"), where("uid", "==", "u1")))));
await t("asistan itirazına karar veremez", () => assertFails(updateDoc(doc(ayse, "appeals/e1_u1_q1"), { status: "accepted" })));
await t("yönetici itiraza karar verir", () => assertSucceeds(updateDoc(doc(admin, "appeals/e1_u1_q1"), { status: "accepted", reply: "ok" })));

console.log("Alıştırma");
await t("asistan alıştırma sorusunu okur", () => assertSucceeds(getDoc(doc(ayse, "questions/qp"))));
await t("asistan alıştırma dışı soruyu okuyamaz", () => assertFails(getDoc(doc(ayse, "questions/qn"))));
await t("asistan alıştırma sorgusu yapar", () => assertSucceeds(getDocs(query(collection(ayse, "questions"), where("practice", "==", true)))));
await t("asistan tüm bankayı sorgulayamaz", () => assertFails(getDocs(collection(ayse, "questions"))));
await t("asistan kendi alıştırma kaydını yazar", () => assertSucceeds(setDoc(doc(ayse, "practice/u1"), { email: "ayse@gmail.com", q: { qp: { c: 1 } } })));
await t("başkasının alıştırma kaydına yazamaz", () => assertFails(setDoc(doc(ali, "practice/u1"), { q: {} })));

console.log("Soru yazarı");
await t("yazar bankayı okur", () => assertSucceeds(getDocs(collection(yazar, "questions"))));
await t("yazar onay bekleyen soru ekler", () => assertSucceeds(setDoc(doc(yazar, "questions/n1"), { stem: "x", status: "pending", author: "yazar@gmail.com", practice: false })));
await t("yazar onaylı soru ekleyemez", () => assertFails(setDoc(doc(yazar, "questions/n2"), { stem: "x", status: "approved", author: "yazar@gmail.com" })));
await t("yazar alıştırmaya açık soru ekleyemez", () => assertFails(setDoc(doc(yazar, "questions/n3"), { stem: "x", status: "pending", author: "yazar@gmail.com", practice: true })));
await t("yazar kendi taslağını düzenler", () => assertSucceeds(updateDoc(doc(yazar, "questions/qy"), { stem: "yy" })));
await t("yazar başkasının taslağını düzenleyemez", () => assertFails(updateDoc(doc(yazar, "questions/qo"), { stem: "zz" })));
await t("yazar sınavları okuyamaz", () => assertFails(getDoc(doc(yazar, "exams/e1"))));
await t("yazar sonuçları okuyamaz", () => assertFails(getDoc(doc(yazar, "grades/e1_u1"))));
await t("yazar rolleri değiştiremez", () => assertFails(setDoc(doc(yazar, "meta/roles"), { authors: ["yazar@gmail.com", "x@gmail.com"] })));
await t("yönetici rolleri değiştirir", () => assertSucceeds(setDoc(doc(admin, "meta/roles"), { authors: ["yazar@gmail.com"] })));

await env.cleanup();
console.log(`\n${pass} geçti, ${failN} başarısız`);
process.exit(failN ? 1 : 0);
