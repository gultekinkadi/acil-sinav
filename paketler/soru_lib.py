# Özgün soru bankası paketleri (yalnız soru; sanal hasta yok)
# Her soru: (kök, [doğru, çeldirici×4], açıklama) — doğru şık ilk yazılır, paket üretilirken
# sabit tohumla karıştırılır (doğru şıkların konumu dengeli dağılsın).
import json, random, sys

SOURCE = "Gazi Acil Tıp — özgün sorular (güncel kılavuzlara dayanır; klinik kontrol sonrası alıştırmaya açın)"

def build(no, name, desc, qs, out):
    pid = f"soru-{no:02d}"
    title = f"Acil Tıp Soru Bankası — {no:02d}. {name}"
    assert len(qs) == 30, (pid, len(qs))
    Q = []; pos = [0]*5; seen = set()
    target = [k % 5 for k in range(len(qs))]; random.Random(pid).shuffle(target)  # her şık eşit sayıda doğru
    for i, (stem, opts, expl) in enumerate(qs, 1):
        assert len(opts) == 5 and len(set(opts)) == 5, (pid, i, opts)
        assert stem not in seen, (pid, i); seen.add(stem)
        key = f"q{i:02d}"
        wrong = opts[1:]; random.Random(f"{pid}:{key}").shuffle(wrong)
        correct = target[i-1]; options = wrong[:correct] + [opts[0]] + wrong[correct:]; pos[correct] += 1
        Q.append({"key": key, "stem": stem, "options": options, "correct": correct, "explanation": expl, "topic": name})
    P = {"id": pid, "title": title, "desc": desc, "source": SOURCE, "pool": title, "sims": [], "questions": Q}
    json.dump(P, open(out, "w"), ensure_ascii=False, indent=1)
    print(pid, len(Q), "soru", "doğru şık dağılımı", pos)
