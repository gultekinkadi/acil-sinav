# Acil Tıp Online Sınav — Kurulum

Tek sayfalık sınav sitesi: GitHub Pages'te çalışır, veriler Firebase Firestore'da tutulur, giriş Google hesabıyla yapılır. Ücretsiz Firebase planı (Spark) yeterlidir; Storage gerekmez (görseller sıkıştırılıp Firestore'a kaydedilir).

## 1. Firebase projesi (≈10 dk)

1. https://console.firebase.google.com → **Proje ekle** → ad: `acil-sinav` (Analytics gerekmez).
2. **Build → Authentication → Get started → Sign-in method → Google**'ı etkinleştirin.
3. Authentication → **Settings → Authorized domains** → `gultekinkadi.github.io` ekleyin.
4. **Build → Firestore Database → Create database** → konum `europe-west3 (Frankfurt)` → *production mode*.
5. Firestore → **Rules** sekmesi → `firestore.rules` dosyasının tamamını yapıştırın → **Publish**.
6. Proje ayarları (⚙️) → **Your apps → Web (</>)** → uygulama kaydedin → gösterilen `firebaseConfig` nesnesini kopyalayın.

## 2. index.html'i ayarlayın

Dosyanın başındaki `firebaseConfig` alanına 6. adımda kopyaladığınız değerleri yapıştırın.
Başka yönetici eklemek isterseniz e-postasını hem `ADMIN_EMAILS` listesine hem `firestore.rules` içindeki `isAdmin()` listesine ekleyin.

## 3. GitHub Pages

1. GitHub'da yeni depo: `acil-sinav` (public).
2. `index.html` dosyasını yükleyin.
3. Settings → Pages → Branch: `main` / root → Save.
4. Birkaç dakika sonra: `https://gultekinkadi.github.io/acil-sinav/`

## 4. İlk kullanım

1. Siteye kendi Google hesabınızla girin → yönetici paneli açılır.
2. **Asistanlar**: asistanların Google e-postalarını ekleyin (Excel'den kopyala-yapıştır ile toplu ekleme var). Kendinizi de eklerseniz sağ üstte "Asistan görünümü" ile sınavı deneyebilirsiniz.
3. **Soru Bankası**: tek tek soru/vaka ekleyin veya şablonu indirip Excel'den toplu aktarın.
4. **Sınavlar → Yeni sınav**: soruları seçin, süreyi ve açık kalma aralığını girin, "Yayında"yı işaretleyin.
5. Asistanlara site linkini gönderin.
6. Sınav bitince **Sonuçlar**: açık uçluları puanlayın → **Sonuçları asistanlara yayınla** → **Excel'e aktar**.

## Güvenlik özeti

- Cevap anahtarı ayrı koleksiyonda; asistanın tarayıcısına hiç gönderilmez.
- Listede olmayan Google hesapları hiçbir veriyi göremez.
- Asistan yalnız kendi cevabını, yalnız süresi içinde (+2 dk tolerans) ve teslimden önce değiştirebilir — bu kural sunucuda uygulanır, tarayıcıdan atlatılamaz.
- Asistan yalnız kendi sonucunu, siz yayınladıktan sonra görür.

## Bilinen sınırlar

- Sınav sırasında sekme değiştirme/kopyalama engellenmez (gözetimli ortam varsayılmıştır).
- Bir soruyu bankada düzenlediğinizde, mevcut sınava yansıması için sınavı açıp yeniden **Kaydet**'e basın.
- Teknik sorun yaşayan asistan için: Sonuçlar → asistan satırı → **Oturumu sıfırla**.

## Özellik özeti (Ekim 2026 güncellemesi)

- **Soru iptali / cevap anahtarı düzeltme:** Sonuçlar → Madde analizi → “Düzenle”. Birden fazla doğru şık, “herkese doğru” veya “puanlama dışı” iptal. Puanlar ve yayınlanmış sonuçlar yeniden hesaplanır.
- **İtiraz:** Sonuçlar yayınlandığında asistan soru bazında itiraz eder; Sonuçlar → İtirazlar’dan kabul/ret. İtirazlar sınav bazında kapatılabilir.
- **Sınav planı:** Havuz + konu + adet satırlarıyla rastgele seçim; herkese aynı set veya her asistana farklı set.
- **Alıştırma modu:** Soru Bankası’nda bir havuzu “Alıştırmaya aç” → asistanlar Alıştırma sekmesinden çözer. Alıştırmadaki soruları sınavda kullanmayın.
- **Ek süre / yeniden açma / geç başlama / cihaz kilidi kaldırma:** asistanın sonuç detayından veya sonuç tablosundan.
- **Soru geçmişi:** Soru Bankası’nda her sorunun kullanıldığı sınavlardaki güçlük ve ayırt edicilik değerleri; “İstatistik” filtresi.
- **Sınav kopyalama, geçme notu, sıralı mod, tam ekran, tek cihaz kilidi, paylaşma bağlantısı + QR.**
- **Soru yazarı rolü:** Ayarlar → Soru yazarları. Yazarların soruları onayınızdan sonra kullanılabilir.
- **Excel’e aktarma** (soru bankası) ve **Yazdır / PDF** (sonuç belgesi, gelişim raporu).

## Güvenlik kuralı testleri

`tests/rules.test.mjs` her kural değişikliğinde GitHub Actions’ta Firestore emülatöründe çalışır; testler geçmezse kurallar Firebase’e yüklenmez.
