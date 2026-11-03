# ACLS — Dönem 6 ön test / son test paketi (20 özgün soru, AHA 2025 algoritmalarına göre)
# Her soru: (kök, [doğru, çeldirici×4], açıklama). Doğru şık ilk yazılır; paket üretilirken
# sabit tohumla karıştırılır ve doğru şıklar A–E arasında eşit dağıtılır.
# Kullanım: python3 kaynak-acls-d6.py acls-donem6.json
import json, random, sys

PID = "acls-donem6"
TITLE = "ACLS — Dönem 6 ön test / son test (AHA 2025)"
DESC = "Yüksek kaliteli KPR, ritim tanıma, kardiyak arrest, bradikardi, taşikardi ve ROSC sonrası bakım: 20 soru. Ders öncesi ön test, staj sonu son test ya da Canlı Yarışma için."
SOURCE = "Gazi Acil Tıp — özgün sorular; AHA 2025 KPR ve AKB kılavuzu algoritmalarına dayanır (klinik kontrol sonrası alıştırmaya açın)"

Q = [
 # --- Yüksek kaliteli KPR ---
 ("Erişkin kardiyak arrestte yüksek kaliteli göğüs basısı için hangisi doğrudur?",
  ["Dakikada 100–120 bası, en az 5 cm derinlik, her basıdan sonra göğsün tam geri gelmesi",
   "Dakikada 80–100 bası, 3–4 cm derinlik",
   "Dakikada 120–140 bası, en az 7 cm derinlik",
   "Her 15 basıda bir nabız kontrolü",
   "Bası yapan kişinin 5 dakikada bir değişmesi"],
  "AHA 2025: hız 100–120/dk, derinlik en az 5 cm (6 cm'yi geçmeden), tam geri gelme, kesintiyi en aza indirme, aşırı ventilasyondan kaçınma; bası yapan kişi 2 dakikada bir (yorulursa daha erken) değişir."),
 ("Entübe bir arrest hastasında ventilasyon nasıl yapılmalıdır?",
  ["Basıya ara vermeden 6 saniyede bir soluk (dakikada 10)",
   "30 basıdan sonra 2 soluk",
   "15 basıdan sonra 2 soluk",
   "Dakikada 20–24 soluk",
   "Yalnızca ritim kontrolü sırasında 2 soluk"],
  "İleri havayolu varsa basıya ara verilmez; 6 saniyede bir (10/dk) ventilasyon yapılır. İleri havayolu yoksa 30:2 uygulanır. Aşırı ventilasyon venöz dönüşü azaltır."),
 ("KPR sırasında dalga formlu kapnografide EtCO₂ 8 mmHg okunuyor. En uygun yorum ve yaklaşım hangisidir?",
  ["Bası kalitesi yetersiz olabilir; hız, derinlik ve geri gelme kontrol edilmeli, bası yapan kişi değiştirilmeli",
   "ROSC sağlanmıştır; bası durdurulmalı",
   "Hiperventilasyon vardır; ventilasyon sayısı artırılmalı",
   "Normal değerdir; değişiklik gerekmez",
   "Endotrakeal tüp kesinlikle özofagustadır; tüp hemen çekilmeli"],
  "KPR sırasında düşük ya da düşen EtCO₂ (< 10 mmHg) bası kalitesinin yetersiz olduğunu düşündürür. EtCO₂'nin ani ve kalıcı yükselmesi (sıklıkla ≥ 40 mmHg) ise ROSC'u düşündürür."),
 # --- Ritim tanıma ---
 ("Yanıtsız, nabızsız hastanın monitöründe düzensiz, kaotik, değişken genlikli dalgalar görülüyor; QRS ve T seçilemiyor. Ritim ve ilk tedavi hangisidir?",
  ["Ventriküler fibrilasyon; hemen defibrilasyon ve ardından 2 dk KPR",
   "Asistoli; adrenalin ve KPR",
   "Nabızsız elektriksel aktivite; adrenalin ve 5H–5T",
   "Atriyal fibrilasyon; senkronize kardiyoversiyon 200 J",
   "Artefakt; hastayı izlemek yeterli"],
  "Kaotik, organize olmayan elektriksel aktivite VF'dir ve şoklanabilir ritimdir: hemen şok, ritme bakmadan 2 dk KPR."),
 ("Monitörde düzenli, dar QRS'li, P dalgalarından sonra gelen 72/dk komplekslerin görüldüğü yanıtsız hastada karotis nabzı alınamıyor. Tanı hangisidir?",
  ["Nabızsız elektriksel aktivite (NEA)",
   "Sinüs ritmi; hasta stabildir",
   "Ventriküler fibrilasyon",
   "Nabızsız ventriküler taşikardi",
   "Tam AV blok"],
  "Organize elektriksel aktiviteye rağmen nabız yoksa NEA'dır. Şoklanamaz ritimdir: KPR, en kısa sürede adrenalin, geri dönüşlü nedenler (5H–5T)."),
 ("Baş dönmesi ile gelen hastanın EKG'sinde P dalgaları düzenli 80/dk, geniş QRS'ler düzenli 32/dk ve P ile QRS arasında ilişki yok. Ritim hangisidir?",
  ["Tam (3. derece) AV blok",
   "2. derece Mobitz I (Wenckebach) AV blok",
   "Sinüs bradikardisi",
   "1. derece AV blok",
   "Atriyal flutter 2:1 blok"],
  "Atriyum ve ventrikülün birbirinden bağımsız atması (AV dissosiyasyon) tam AV bloktur. Geniş QRS'li kaçış ritminde atropin çoğunlukla etkisizdir; pacing veya kronotrop infüzyon gerekir."),
 # --- Şoklanabilir ritim ---
 ("Tanıklı VF arrestte ilk şok verildi. Hemen ardından ne yapılmalıdır?",
  ["Ritme ve nabza bakmadan 2 dakika KPR'ye devam etmek",
   "Hemen nabız kontrolü yapmak",
   "Art arda ikinci ve üçüncü şoku vermek",
   "Önce entübe etmek, sonra KPR'ye başlamak",
   "Ritim kontrolü için 30 saniye beklemek"],
  "Tek şok stratejisi: şoktan hemen sonra 2 dk KPR; ritim kontrolü 2 dakikanın sonunda, 10 saniyeyi geçmeden yapılır."),
 ("Şoklanabilir ritimle seyreden arrestte adrenalin ne zaman verilir?",
  ["İkinci şoktan sonra, ardından 3–5 dakikada bir 1 mg",
   "İlk şoktan önce",
   "Yalnızca üçüncü şoktan sonra bir kez",
   "Hiç verilmez; yalnızca amiodaron kullanılır",
   "Her şoktan hemen önce 1 mg"],
  "Şoklanabilir ritimde adrenalin 1 mg IV/İO, 2. şoktan sonra verilir ve 3–5 dakikada bir tekrarlanır. Şoklanamaz ritimde ise en kısa sürede verilir."),
 ("Üçüncü şoka rağmen VF sürüyor. Bu aşamada önerilen antiaritmik ve dozu hangisidir?",
  ["Amiodaron 300 mg IV/İO bolus (ya da lidokain 1–1,5 mg/kg)",
   "Amiodaron 150 mg 10 dakikada infüzyon",
   "Adenozin 6 mg hızlı IV",
   "Atropin 1 mg IV",
   "Magnezyum 2 g rutin olarak"],
  "Refrakter VF/nVT'de amiodaron ilk doz 300 mg bolus, ikinci doz 150 mg; alternatifi lidokain 1–1,5 mg/kg, sonra 0,5–0,75 mg/kg. Magnezyum yalnızca torsades de pointes'te."),
 ("Bifazik defibrilatörde üreticinin önerdiği enerji bilinmiyorsa ilk şok nasıl verilmelidir?",
  ["Cihazın en yüksek enerjisiyle",
   "50 J ile",
   "Senkronize modda 100 J ile",
   "Hastanın kilosu başına 2 J ile",
   "Önce 360 J monofazik denemesiyle"],
  "Bifazikte üreticinin önerdiği enerji kullanılır (genellikle 120–200 J); bilinmiyorsa en yüksek enerji. Sonraki şoklar eşit veya daha yüksek olabilir. Monofazikte 360 J."),
 # --- Şoklanamaz ritim ---
 ("Asistolik arrestte aşağıdakilerden hangisi doğrudur?",
  ["Şok verilmez; KPR sürdürülür ve adrenalin en kısa sürede verilir",
   "Hemen 200 J şok verilir",
   "Atropin 1 mg rutin olarak verilir",
   "Transkütan pacing ilk tedavidir",
   "Adrenalin ancak 3. ritim kontrolünden sonra verilir"],
  "Asistoli ve NEA şoklanamaz: KPR, en kısa sürede adrenalin 1 mg (3–5 dk'da bir), ileri havayolu ve kapnografi, geri dönüşlü nedenlerin aranması. Arrestte atropin ve pacing önerilmez."),
 ("Hemodiyalize giren, iki seansı kaçırmış hastada geniş QRS'li NEA gelişiyor. Geri dönüşlü neden için hangisi öncelikli düşünülmeli ve tedavi edilmelidir?",
  ["Hiperkalemi; kalsiyum ve potasyumu hücre içine kaydıran tedavi",
   "Hipotermi; aktif ısıtma",
   "Tansiyon pnömotoraks; iğne dekompresyon",
   "Hipoglisemi; dekstroz",
   "Toksin; nalokson"],
  "5H–5T: hipovolemi, hipoksi, hidrojen iyonu (asidoz), hipo/hiperkalemi, hipotermi; tansiyon pnömotoraks, tamponad, toksinler, pulmoner ve koroner tromboz. Diyaliz öyküsü ve geniş QRS hiperkalemiyi düşündürür."),
 # --- Bradikardi ---
 ("Kalp hızı 38/dk olan hastada aşağıdakilerden hangisi bradikardinin 'unstabil' olduğunu GÖSTERMEZ?",
  ["Hastanın çarpıntı hissetmesi",
   "Hipotansiyon",
   "Bilinç bulanıklığı",
   "İskemik göğüs ağrısı",
   "Akut kalp yetmezliği bulguları"],
  "Kardiyopulmoner bozulma bulguları: hipotansiyon, akut bilinç değişikliği, şok bulguları, iskemik göğüs ağrısı ve akut kalp yetmezliği. Bunlardan biri varsa tedavi gerekir."),
 ("Semptomatik bradikardide ilk ilaç tedavisi ve dozu hangisidir?",
  ["Atropin 1 mg IV; 3–5 dakikada bir, en fazla 3 mg",
   "Atropin 0,5 mg IV; en fazla 1 mg",
   "Adrenalin 1 mg IV bolus",
   "Adenozin 6 mg hızlı IV",
   "Amiodaron 150 mg IV"],
  "AHA 2025: atropin 1 mg IV bolus, 3–5 dk'da bir tekrar, toplam en fazla 3 mg. Nabızlı hastada 1 mg bolus adrenalin verilmez."),
 ("Atropine yanıt vermeyen, hipotansif bradikardi hastasında sıradaki adım hangisidir?",
  ["Transkütan pacing ve/veya dopamin (5–20 mcg/kg/dk) ya da adrenalin (2–10 mcg/dk) infüzyonu",
   "Atropini 6 mg'a kadar artırmak",
   "Senkronize kardiyoversiyon",
   "Adenozin vermek",
   "Göğüs basısına başlamak"],
  "Atropin etkisizse transkütan pacing ve/veya dopamin ya da adrenalin infüzyonu; ardından uzman konsültasyonu ve transvenöz pacing."),
 # --- Taşikardi ---
 ("Kalp hızı 186/dk, düzenli, dar QRS'li taşikardisi olan hastanın TA'sı 72/40 mmHg ve bilinci bulanık. En uygun tedavi hangisidir?",
  ["Mümkünse sedasyonla senkronize kardiyoversiyon (100 J)",
   "Vagal manevra ve gözlem",
   "Diltiazem 0,25 mg/kg IV",
   "Amiodaron 150 mg 10 dakikada",
   "Senkronize olmayan 360 J şok"],
  "Unstabil taşikardide hemen senkronize kardiyoversiyon; düzenli dar QRS'de hazırlık sırasında adenozin düşünülebilir. AHA 2025 önerisi: dar QRS'li taşikardi ve monomorfik VT için 100 J, AF ve flutter için 200 J senkronize."),
 ("Stabil, düzenli, dar QRS'li (QRS < 0,12 sn) taşikardide ilk basamak tedavi hangisidir?",
  ["Vagal manevra; yanıt yoksa adenozin 6 mg hızlı IV (gerekirse 12 mg)",
   "Senkronize kardiyoversiyon",
   "Amiodaron 300 mg bolus",
   "Atropin 1 mg",
   "Lidokain 1,5 mg/kg"],
  "Stabil düzenli dar QRS'li taşikardide vagal manevra, ardından adenozin 6 mg hızlı IV + SF ile itme, gerekirse 12 mg; sonra beta bloker ya da kalsiyum kanal blokeri."),
 ("Stabil, geniş QRS'li, düzenli ve monomorfik taşikardide hangisinden KAÇINILMALIDIR?",
  ["Verapamil / diltiazem gibi kalsiyum kanal blokerleri",
   "12 derivasyon EKG çekmek",
   "Uzman konsültasyonu",
   "Amiodaron 150 mg 10 dakikada infüzyon",
   "Damar yolu açmak ve monitörize etmek"],
  "Geniş QRS'li taşikardi VT kabul edilmelidir; kalsiyum kanal blokerleri ağır hipotansiyon ve arreste yol açabilir. Adenozin yalnızca düzenli ve monomorfik ise düşünülür; antiaritmik infüzyon (amiodaron 150 mg 10 dk'da, prokainamid) ve uzman konsültasyonu önerilir."),
 # --- ROSC sonrası ---
 ("ROSC sonrası erken dönemde AHA 2025'e göre oksijenasyon ve kan basıncı hedefleri hangisidir?",
  ["SpO₂ %90–98 ve ortalama arter basıncı ≥ 65 mmHg",
   "SpO₂ %100 ve sistolik TA > 140 mmHg",
   "SpO₂ %85–90 ve OAB ≥ 50 mmHg",
   "SpO₂ %94–100 ve sistolik TA > 70 mmHg",
   "Hedef yoktur; vitaller izlenir"],
  "AHA 2025 ROSC sonrası bakım: SpO₂ güvenilir ölçülene kadar FiO₂ %100, sonra SpO₂ %90–98 (PaO₂ 60–105 mmHg); PaCO₂ 35–45 mmHg; OAB ≥ 65 mmHg; hipoglisemiden kaçınma."),
 ("ROSC sonrası komutlara uymayan hastada hangisi önerilir?",
  ["Mümkün olan en kısa sürede 32–37,5 °C hedefli sıcaklık kontrolü",
   "Sıcaklık takibi gereksizdir",
   "Hastayı 39 °C'ye kadar ısıtmak",
   "Rutin olarak 28 °C'ye soğutmak",
   "Profilaktik antikonvülzan ve 24 saat beklemek"],
  "Komut almayan hastada 32–37,5 °C hedefli sıcaklık kontrolü en kısa sürede başlanır ve ateşten kaçınılır. Ayrıca 12 derivasyon EKG (ST elevasyonu varsa acil koroner anjiyografi), EEG ve gecikmeli çok yönlü prognoz değerlendirmesi."),
]

assert len(Q) == 20, len(Q)
Qs = []; pos = [0]*5; seen = set()
target = [k % 5 for k in range(len(Q))]; random.Random(PID).shuffle(target)
for i, (stem, opts, expl) in enumerate(Q, 1):
    assert len(opts) == 5 and len(set(opts)) == 5, (i, opts)
    assert stem not in seen, i; seen.add(stem)
    key = f"q{i:02d}"
    wrong = opts[1:]; random.Random(f"{PID}:{key}").shuffle(wrong)
    c = target[i-1]; options = wrong[:c] + [opts[0]] + wrong[c:]; pos[c] += 1
    topic = ["Yüksek kaliteli KPR"]*3+["Ritim tanıma"]*3+["Şoklanabilir ritim"]*4+["Şoklanamaz ritim"]*2+["Bradikardi"]*3+["Taşikardi"]*3+["ROSC sonrası bakım"]*2
    Qs.append({"key": key, "stem": stem, "options": options, "correct": c, "explanation": expl, "topic": "ACLS · " + topic[i-1]})
P = {"id": PID, "title": TITLE, "desc": DESC, "source": SOURCE, "pool": TITLE, "sims": [], "questions": Qs}
out = sys.argv[1] if len(sys.argv) > 1 else "acls-donem6.json"
json.dump(P, open(out, "w"), ensure_ascii=False, indent=1)
print(PID, len(Qs), "soru · doğru şık dağılımı", pos)
