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

## BT / MR görüntüleri (DICOM)

- Soru veya vaka düzenlerken **DICOM yükle** → PACS/CD klasörünü seçin → seriyi seçin → kesit aralığını ve çözünürlüğü ayarlayın → **Anonimleştir ve yükle**.
- Hasta adı, kimlik no, doğum tarihi, kurum, tarih gibi DICOM etiketleri tarayıcıda ayıklanır; Firebase'e yalnız piksel değerleri (HU) ve ölçü bilgisi gider. Görüntünün üzerine yazılmış metin (bazı topogram/ekran görüntüleri) temizlenemez.
- Görüntüleyici: fare tekerleği / kaydırıcı / ok tuşları ile kesit, hazır pencereler (beyin, subdural, inme, kemik, akciğer, mediasten, abdomen, karaciğer), sürükleyerek P/S, yakınlaştırma, taşıma, mm ölçüm, HU okuma, tam ekran. Telefonda parmakla kaydırma ve iki parmakla yakınlaştırma.
- Boyut: 512×512 kafa BT'de kesit başına ≈70 KB; yarı çözünürlükte ≈15–20 KB. Ücretsiz kota 1 GB'tır; Ayarlar → Görüntü arşivi'nden toplam boyutu görüp kullanılmayan serileri silebilirsiniz.

## Eğitim (Öğren) bölümü

Asistanlar siteye girdiğinde **Öğren** sekmesi açılır (açık bir sınavları varsa **Sınavlarım**). Yönetici içeriği **Eğitim** sekmesinden yönetir.

- **Görüntü atlası:** Bir kayda birden çok görsel ve/veya BT/MR serisi ekleyebilirsiniz (ör. PA + lateral, seri EKG); her görüntünün alt yazısı olur, bulgular ilgili görüntüye bağlanır. **Toplu görsel yükle** ile çok sayıda görseli tek seferde (her biri ayrı kayıt ya da tek kayıtta) ekleyin. Görsel veya DICOM yükleyin, bulguları elips / dikdörtgen / serbest çizimle işaretleyip açıklayın, “Her bulgu için” ile bul-tıkla görevleri oluşturun. Asistan *Keşfet*'te bulguları tek tek açar, *Kendini sına*'da bulguyu görüntü üzerinde bulur (3 hak, 2. yanlışta konum ipucu; DICOM'da doğru kesit ±2).
- **Sanal hasta:** Düğümlerden oluşan dallanan vaka. *Tetkik* seçenekleri aynı ekranda sonuç (metin/görsel/DICOM) gösterir; *Karar* seçenekleri başka düğüme götürür. Her seçeneğin puanı (eksi olabilir), süresi ve geri bildirimi vardır. Bitiş düğümü iyi/kısmen/kötü sonuç ve özet gösterir. Düzenleyici ulaşılamayan düğümleri ve kopuk bağlantıları uyarır.
- **Modüller:** Okuma, video (YouTube gömülü), atlas görüntüsü, sanal hasta ve alıştırma öğelerinden sıralı içerik. Kıdeme göre zorunlu yapılabilir; atlas ve vaka öğeleri kendiliğinden tamamlanır.
- **Aralıklı tekrar (Tekrar sekmesi):** Alıştırmada yanlış yapılan sorular ve atlasta ilk denemede bulunamayan bulgular otomatik eklenir; doğru bildikçe 1-3-7-21-60 gün sonra tekrar sorulur.
- **Haftanın görüntüsü:** Açılış ve cevap zamanı belirlenir; asistanlar yorumunu yazar, cevap zamanında cevap ve tüm yorumlar açılır.
- **İlerleme paneli:** Asistan bazında zorunlu modül, atlas, sanal hasta, alıştırma, tekrar kartı ve haftalık katılım; konulara göre en zayıf alanlar; Excel'e aktarma.
- Soru yazarları atlas görüntüsü ve sanal hasta da ekleyebilir; yönetici onayıyla yayınlanır.

## Öğrenci önizleme ve vaka paketleri

- **👁 Öğrenci önizleme** (yönetici üst çubuğu): çıkış yapmadan sitenin asistanlara nasıl göründüğünü dener. Yalnız yayınlanmış içerik görünür, kıdem seçilebilir, hiçbir kayıt yazılmaz; “Yönetici görünümüne dön” ile kaldığınız sayfaya dönersiniz.
- **Vaka paketi içe aktar** (Eğitim → Sanal hasta): `paketler/` klasöründeki hazır paketler ya da bir `.json` dosyası; sanal hastaları, ayrı bir havuzda alıştırma sorularını ve modülü **taslak** olarak ekler. Aynı paket ikinci kez aktarılırsa var olanlar atlanır.
- `paketler/ilk-nobet-1.json` … `ilk-nobet-10.json`: İlk Nöbet Vakaları (100 sanal hasta, 310 alıştırma sorusu, 10 modül). “Hepsini içe aktar” düğmesiyle tek seferde eklenir. Kaynak üretici betikler: `paketler/kaynak-ilk-nobet-*.py` (+ `vaka_lib.py`); paket dosyasını yeniden üretmek için `python3 kaynak-ilk-nobet-2.py ilk-nobet-2.json`.
