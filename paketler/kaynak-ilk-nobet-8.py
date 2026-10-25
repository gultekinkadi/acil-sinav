import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 71 CRUSH SENDROMU
S.append(case("c71","Enkaz altından çıkarılan hasta — 34 yaşında erkek","Afet / Travma",
 "Deprem sonrası saha. 34 yaşında erkek 18 saattir enkaz altında; her iki bacağı beton blok altında sıkışmış. Kurtarma ekibi 30 dakika içinde çıkarabileceğini söylüyor. Sağlık ekibiyle birlikte hastaya ulaştınız.",
 {"n1":N("Enkaz altında — kurtarmadan önce","Bilinç açık, susuzluktan yakınıyor. Bacaklar blok altında; üst gövdeye erişim var.","KB 108/70 · Nb 112 · SS 22",[
   A("**Kurtarmadan önce IV sıvı başla**: %0,9 NaCl ≈1 L/saat (potasyum içeren sıvılardan kaçın); monitör/EKG hazır; çıkarma anında hiperkalemi ve hipotansiyona hazırlan (kalsiyum, insülin-glukoz, salbutamol)",4,30,"n2","Doğru. Basının kalkmasıyla potasyum, miyoglobin ve asit dolaşıma geçer; önceden hidrasyon “kurtarma ölümünü” önler."),
   A("Önce çıkarın, sıvıyı hastanede başlarız",-4,30,"n3","Sıvı verilmeden yapılan kurtarma ani hiperkalemi ve şokla ölümle sonuçlanabilir."),
 ]),
 "n3":N("Kurtarmanın hemen ardından","Hasta aniden kötüleşiyor, monitörde geniş QRS.","KB 70/40 · Nb 44",[
   A("Kalsiyum glukonat/klorür IV, insülin-glukoz, salbutamol; hızlı SF; hastaneye acil sevk (diyaliz)",2,20,"n2","Doğru ama gecikmeli; hiperkalemik arrest eşiği."),
   A("Yalnız sıvıya devam et",-4,10,"n9","EKG değişikliğiyle seyreden hiperkalemi acil tedavi gerektirir."),
 ]),
 "n2":N("Hastanede — 2. saat","Bacaklarda ödem; idrar koyu çay renginde.","KB 112/68 · İdrar 60 mL/saat · K 5,9 · CK 48.000 · kreatinin 2,1",[
   A("Saatlik idrar takibi ile sıvıyı sürdür (hedef ≈200–300 mL/saat idrar, sıvı yüklenmesine dikkat); K'yı tedavi et; kompartman basınçlarını izle (fasyotomi kararı cerrahla); erken nefroloji — diyaliz endikasyonları (dirençli hiperkalemi, asidoz, sıvı yüklenmesi, oligüri)",4,20,"n4","Doğru. Crush sendromunda akut böbrek hasarı ve hiperkalemi en büyük ölüm nedenidir."),
   A("Furosemid ile idrar çıkışını artır, sıvıyı kıs",-3,20,"n9","Hipovolemik hastada diüretik böbrek hasarını artırır; önce yeterli hacim."),
 ]),
 "n4":E("Böbrek korundu","Yoğun sıvı tedavisi ve 3 seans hemodiyalizle hasta iyileşti; fasyotomi gerekmedi.\n\n**Akılda kalsın**\n- Uzun süreli sıkışma → rabdomiyoliz: **hiperkalemi, miyoglobinüri, AKI, hipovolemi, kompartman sendromu**.\n- **Kurtarmadan önce sıvı** (SF ≈1 L/saat); K içeren sıvılardan kaçın.\n- Çıkarma sonrası **hiperkalemik arrest** riski: kalsiyum, insülin-glukoz hazır.\n- Hedef yüksek idrar çıkışı (≈200–300 mL/saat); erken **diyaliz** planı.\n- Afet bölgesinde turnike/amputasyon kararları özel durumlara sınırlıdır.\n\n*Kaynak: ISN/ERBP crush sendromu önerileri (Sever ve ark., 2012).*","good"),
 "n9":E("Hiperkalemik arrest / AKI","Hasta hiperkalemik arrest geçirdi / oligürik böbrek yetmezliğine girdi.","bad"),
}))
Qs+=[Q("c71q1","Crush sendromunda sıvı tedavisi ne zaman başlanmalıdır?",["Hastaneye varınca","Kurtarmadan önce, enkaz altında","Kreatinin yükselince","Yalnız idrar koyulaşınca","24 saat sonra"],1,"Basının kalkmasıyla ani hiperkalemi ve şok riski.","Afet / Travma"),
 Q("c71q2","Crush hastasında başlangıç sıvısı olarak hangisinden kaçınılmalıdır?",["%0,9 NaCl","Potasyum içeren sıvılar (ör. Ringer laktat)","İzotonik sıvı","Sıvı vermek","Dekstrozsuz sıvı"],1,"Hiperkalemi riski nedeniyle K içermeyen sıvı tercih edilir.","Afet / Travma"),
 Q("c71q3","Crush sendromunda erken ölümün en önemli nedeni hangisidir?",["Enfeksiyon","Hiperkalemi","Hipoglisemi","Pnömotoraks","Anemi"],1,"Hiperkalemi ve hipovolemi erken ölüm nedenleridir.","Afet / Travma")]

# 72 DEKOMPRESYON HASTALIĞI
S.append(case("c72","Dalış sonrası uyuşma — 38 yaşında erkek","Çevresel aciller",
 "38 yaşında erkek, Kaş'ta tüplü dalış yapmış: 32 metreye inmiş, havası azalınca dekompresyon duraklarını atlayarak hızlı çıkmış. 40 dakika sonra omuz ağrısı, ardından bacaklarda karıncalanma, güçsüzlük ve idrar yapamama başlamış. Akşam İstanbul'a uçacakmış.",
 {"n1":N("Acil servis","Bilinç açık. Alt ekstremitelerde kuvvet 4/5, T10 altında hipoestezi, glob vezikale. Deride mermer görünümü.","KB 122/76 · Nb 98 · SpO₂ %97",[
   T("Nörolojik muayene + mesane USG",2,10,"Spinal tutulum (tip II dekompresyon hastalığı), 700 mL rezidü.","Spinal kord tutulumu ağır formdur."),
   T("Akciğer grafisi",1,15,"Pnömotoraks yok.","Barotravma/pnömotoraks rekompresyon öncesi bilinmeli."),
   A("**%100 O₂** (rezervuarlı maske, kesintisiz); düz yatış; IV izotonik sıvı; mesane kateteri; **hiperbarik oksijen merkezine acil sevk** (rekompresyon; kara yoluyla ya da düşük irtifada/basınçlı kabinle); uçuş yok",4,20,"n2","Doğru. Kesin tedavi rekompresyondur; O₂ köprü tedavisidir."),
   A("Kas ağrısı — NSAİİ ver, akşamki uçuşuna gidebilir",-5,10,"n9","Uçaktaki düşük basınç kabarcıkları büyütür; spinal DCS kalıcı parapleji yapabilir."),
 ]),
 "n2":E("Rekompresyon","Hasta hiperbarik merkezde ABD Donanması Tablo 6 ile tedavi edildi; üçüncü seansta nörolojik bulgular tamamen düzeldi.\n\n**Akılda kalsın**\n- DCS: çözünmüş azotun kabarcık oluşturması — **tip I** (eklem ağrısı, deri), **tip II** (nörolojik, kardiyopulmoner).\n- Arteriyel gaz embolisi: çıkıştan **dakikalar içinde**, inme benzeri; akciğer barotravması.\n- Tedavi: **%100 O₂**, sıvı, **erken rekompresyon (HBO)**.\n- Dalış sonrası **uçuş/yüksek irtifa** riskli; sevk düşük irtifada.\n- Danışma: hiperbarik tıp merkezleri / DAN.\n\n*Kaynak: UHMS 2018 DCS tedavi önerileri.*","good"),
 "n9":E("Kalıcı parapleji","Hasta uçakta kötüleşti; rekompresyon gecikti, kalıcı paraparezi ve mesane disfonksiyonu kaldı.","bad"),
}))
Qs+=[Q("c72q1","Dekompresyon hastalığında hastane öncesi en önemli tedavi hangisidir?",["NSAİİ","%100 oksijen","Antihistaminik","Diüretik","Steroid"],1,"O₂ azotun atılımını hızlandırır; kesin tedavi rekompresyon.","Çevresel aciller"),
 Q("c72q2","Dekompresyon hastalığının kesin tedavisi hangisidir?",["Gözlem","Hiperbarik oksijenle rekompresyon","Tromboliz","Antikoagülan","Cerrahi"],1,"Kabarcıkları küçültür, doku oksijenlenmesini artırır.","Çevresel aciller"),
 Q("c72q3","Dalış sonrası nörolojik belirti gelişen hastada hangisinden kaçınılmalıdır?",["%100 O₂","IV sıvı","Uçakla seyahat","Düz yatış","HBO"],2,"Kabin basıncının düşmesi kabarcıkları büyütür.","Çevresel aciller")]

# 73 TETANOZ
S.append(case("c73","Ağız açamama — 71 yaşında erkek","Enfeksiyon",
 "71 yaşında erkek, çiftçi. 10 gün önce bahçede paslı bir çiviyle ayağını yaralamış, yarayı kendisi pansuman etmiş. 2 gündür ağzını açamıyor, boynu ve sırtı kasılıyor; sesle tetiklenen ağrılı kasılmaları var. Aşı kartı yok; çocukken aşılandığını hatırlamıyor.",
 {"n1":N("Muayene","**Trismus**, risus sardonicus, sırt kaslarında rijidite. Kapı çarpınca jeneralize spazm (opistotonus) oluyor; bilinç açık. Sol ayakta kirli, enfekte yara.","KB 168/96 · Nb 118 · SS 22 · Ateş 37,8",[
   A("Sessiz, karanlık oda; hava yolu ekibi (laringospazm riski); spazm için **benzodiazepin** (diazepam/midazolam); **insan tetanoz immünglobulini (TIG)** — tedavi dozu (ör. 500 Ü IM, protokole göre); **metronidazol** IV; yaranın debridmanı; aşı serisine başla (farklı bölgeden Td)",4,20,"n2","Doğru. TIG yalnız bağlanmamış toksini nötralize eder; erken verilmeli. Hastalık bağışıklık bırakmaz → aşı gerekir."),
   A("Distoni — biperiden ver, taburcu",-5,10,"n9","Yara öyküsü + trismus + uyarana bağlı spazm tetanozdur; ayaktan izlem ölümcül."),
 ]),
 "n2":N("8. saat","Spazmlar sıklaşıyor, bir spazm sırasında SpO₂ %82'ye düştü; KB 210/120 ile 90/50 arasında dalgalanıyor.","",[
   A("Entübasyon (trakeostomi planı), derin sedasyon ± nöromüsküler blok; otonomik instabilite ve spazm için **magnezyum sülfat** infüzyonu; yoğun bakım",4,20,"n3","Doğru. Otonomik disfonksiyon ağır tetanozun önde gelen ölüm nedenidir."),
   A("Hipertansiyon için propranolol (tek başına)",-3,10,"n9","Saf beta blokaj karşılanmamış alfa etkisiyle ani ölüm ve hipotansiyonla ilişkilendirilmiştir."),
 ]),
 "n3":E("Uzun yoğun bakım, iyileşme","Hasta 4 hafta yoğun bakımda kaldı ve iyileşti; taburculukta Td aşı serisi tamamlandı.\n\n**Akılda kalsın**\n- Tetanoz klinik tanıdır: **trismus**, risus sardonicus, opistotonus, **uyarana bağlı spazm**, bilinç açık.\n- Tedavi: **TIG**, **metronidazol**, yara debridmanı, **benzodiazepin**, sessiz ortam, hava yolu; otonomik instabilitede **Mg**.\n- **Hastalık bağışıklık bırakmaz** → aşı serisi.\n- Yara profilaksisi: aşı öyküsü <3 doz/bilinmiyor + kirli yara → **Td + TIG**.\n\n*Kaynak: DSÖ tetanoz klinik yönetimi 2019; CDC.*","good"),
 "n9":E("Ölümcül seyir","Laringospazm/otonomik fırtına sırasında kardiyak arrest gelişti.","bad"),
}))
Qs+=[Q("c73q1","Tetanozda ilk bulgu genellikle hangisidir?",["Ateş","Trismus","Paralizi","Döküntü","Diplopi"],1,"Masseter spazmı en sık ilk bulgudur.","Enfeksiyon"),
 Q("c73q2","Aşı öyküsü bilinmeyen hastada kirli, derin yarada profilaksi hangisidir?",["Hiçbir şey","Yalnız Td","Td + tetanoz immünglobulini","Yalnız antibiyotik","Yalnız TIG"],2,"<3 doz veya bilinmeyen öyküde kirli yarada aşı + TIG.","Enfeksiyon"),
 Q("c73q3","Tetanozda kas spazmı ve otonomik instabilitenin tedavisinde kullanılan ilaçlar hangisidir?",["Antihistaminik + steroid","Benzodiazepin ve magnezyum sülfat","Fenitoin","Haloperidol","Fizostigmin"],1,"Mg spazmı ve otonomik dalgalanmayı azaltır.","Enfeksiyon")]

# 74 HAVA EMBOLİSİ (santral kateter)
S.append(case("c74","Kateter çekilirken kollaps — 63 yaşında kadın","Resüsitasyon",
 "63 yaşında kadın, acil yoğun bakım alanında izleniyor. Sağ internal juguler santral venöz kateteri, hasta yatakta **oturur pozisyondayken** çekildi. Birkaç saniye sonra öksürük, nefes darlığı, göğüs ağrısı başladı; ardından sol kolunda güçsüzlük ve bilinç bulanıklığı.",
 {"n1":N("Kateter çekildikten 1 dakika sonra","Kateter yerinde kan sızıntısı yok. Kalp oskültasyonunda “değirmen çarkı” üfürümü.","KB 78/46 · Nb 132 · SpO₂ %84",[
   T("POCUS",2,3,"Sağ kalp boşluklarında **hava ekojeniteleri**, sağ ventrikül dilate.","Venöz hava embolisi; nörolojik bulgu paradoks (arteriyel) emboliyi düşündürür (PFO)."),
   A("Giriş yerini hemen kapat (oklüzif pansuman); **%100 O₂**; hastayı **sol lateral dekübit + Trendelenburg**; sıvı/vazopresör; nörolojik bulgu var → **hiperbarik oksijen** merkezine acil sevk",4,10,"n2","Doğru. Sol yan + baş aşağı pozisyon havayı sağ ventrikül apeksinde tutar; %100 O₂ kabarcığı küçültür."),
   A("PE olabilir — tromboliz",-5,10,"n9","Tablo kateter manipülasyonu sırasında başladı; hava embolisi. Tromboliz yararsız ve kanama riski."),
 ]),
 "n2":E("HBO ile düzelme","Pozisyon ve O₂ ile KB 110/70'e yükseldi; HBO sonrası nörolojik bulgular geriledi.\n\n**Akılda kalsın**\n- Risk: **santral kateter takma/çıkarma** (özellikle oturur pozisyonda, derin inspiryumda), dalış, cerrahi, travma.\n- Önlem: kateteri **Trendelenburg/supin** pozisyonda, **ekspiryumda veya Valsalva sırasında** çek; oklüzif pansuman.\n- Tedavi: giriş yerini kapat, **%100 O₂**, **sol lateral dekübit + Trendelenburg**, hemodinamik destek; arteriyel emboli/nörolojik bulguda **HBO**.\n\n*Kaynak: Mirski ve ark., Anesthesiology 2007; UHMS.*","good"),
 "n9":E("Ağır serebral emboli","Hasta kalıcı hemiparezi ile kaldı; gereksiz tromboliz sonrası kateter yerinden kanama oldu.","bad"),
}))
Qs+=[Q("c74q1","Venöz hava embolisinde önerilen pozisyon hangisidir?",["Sağ lateral dekübit","Sol lateral dekübit + Trendelenburg","Oturur","Ters Trendelenburg","Yüzüstü"],1,"Havanın sağ ventrikül çıkış yolunu tıkamasını önler.","Resüsitasyon"),
 Q("c74q2","Santral venöz kateter çekilirken hava embolisini önlemek için hangisi yapılmalıdır?",["Hasta oturur pozisyonda olmalı","Supin/Trendelenburg ve ekspiryum/Valsalva sırasında çekmek, oklüzif pansuman","Derin inspiryumda çekmek","Pansuman gerekmez","Hızlı çekip açık bırakmak"],1,"Göğüs içi basınç atmosferik basıncın üstündeyken çekilir.","Resüsitasyon"),
 Q("c74q3","Nörolojik bulgulu arteriyel gaz embolisinde kesin tedavi hangisidir?",["Tromboliz","Hiperbarik oksijen","Heparin","Steroid","Mannitol"],1,"HBO kabarcık hacmini azaltır.","Resüsitasyon")]

# 75 SIADH — MDMA'ya bağlı akut hiponatremi
S.append(case("c75","Festivalde nöbet — 19 yaşında kadın","Toksikoloji / Metabolik",
 "19 yaşında kadın, bir müzik festivalinde “ecstasy” (MDMA) almış ve dans ederken “susuz kalmamak için” 4–5 litre su içmiş. Baş ağrısı, kusma, konfüzyon gelişmiş; ambulansta jeneralize nöbet geçirmiş.",
 {"n1":N("Resüsitasyon alanı","Postiktal, GKS 11. Pupiller midriyatik. Ödem yok.","KB 142/88 · Nb 112 · Ateş 37,9 · Glukoz 96",[
   T("Na (kan gazı)",3,5,"**Na 118 mmol/L**.","MDMA ADH salınımını artırır (SIADH) + aşırı su alımı → **akut** (<48 saat) hiponatremi; kadınlarda daha sık."),
   T("CK, ısı izlemi",1,20,"CK 2400.","MDMA hipertermi ve serotonin sendromu da yapabilir."),
   A("**%3 NaCl 100 mL IV bolus** (10 dakikada), gerekirse 10 dakika arayla 2 kez daha (en çok 3 doz) — semptom düzelene ya da Na 4–6 mmol/L artana kadar; hipotonik sıvı verme; sıvı kısıtla; ısıyı izle",4,15,"n2","Doğru. Akut semptomatik hiponatremide beyin ödemi hızla ilerler; hipertonik bolus hayat kurtarır."),
   A("Dehidrate — %0,9 NaCl 2 L",-3,60,"n3","Hasta hipervolemik/övolemik; SIADH'de izotonik serum yetersizdir ve Na'yı düşürebilir."),
   A("Su içirerek “toksinleri at”",-5,30,"n9","Su alımı hiponatremiyi derinleştirir."),
 ]),
 "n3":N("1 saat sonra","Hasta yeniden nöbet geçiriyor.","Na 116",[
   A("%3 NaCl 100 mL bolus (gerekirse tekrarla)",2,15,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Düzelme","İki bolus sonrası Na 124; nöbet tekrarlamadı, bilinç düzeldi. İlk 24 saatte Na 128'e yükseldi.\n\n**Akılda kalsın**\n- MDMA: **ADH salınımı + aşırı su** → akut hiponatremi; ayrıca hipertermi, serotonin sendromu, rabdomiyoliz.\n- **Akut** semptomatik hiponatremi: **%3 NaCl 100 mL bolus (×3'e kadar)** ya da 150 mL/20 dk.\n- Hipotonik/izotonik sıvı verme; sıvı kısıtla.\n- Akut (<48 saat) hiponatremide ozmotik demiyelinizasyon riski düşüktür ama yine de ≤10 mmol/L/24 saat önerilir.\n- Benzer tablo: maraton koşucusunda **egzersizle ilişkili hiponatremi**.\n\n*Kaynak: Uluslararası Egzersizle İlişkili Hiponatremi Uzlaşısı 2015; Avrupa 2014 kılavuzu.*","good"),
 "n9":E("Beyin ödemi","Hasta beyin ödemi ve herniasyon geliştirdi.","bad"),
}))
Qs+=[Q("c75q1","MDMA'ya bağlı hiponatreminin mekanizması hangisidir?",["Renal tuz kaybı","ADH salınımı + aşırı su alımı","Adrenal yetmezlik","Hipotiroidi","Diüretik etkisi"],1,"MDMA ADH salınımını artırır; bol su içilmesi tabloyu ağırlaştırır.","Toksikoloji / Metabolik"),
 Q("c75q2","Akut semptomatik hiponatremide (nöbet) uygun bolus hangisidir?",["%0,9 NaCl 1 L","%3 NaCl 100 mL (10 dakikada), gerekirse 3 kereye kadar","%5 dekstroz","Sıvı kısıtlaması tek başına","Tolvaptan"],1,"Hızlı ve sınırlı Na artışı beyin ödemini durdurur.","Toksikoloji / Metabolik"),
 Q("c75q3","Maraton koşucusunda konfüzyon ve kusma ile gelen egzersizle ilişkili hiponatremide hangisi yapılmamalıdır?",["Na ölçümü","Hipotonik sıvı veya bol su vermek","%3 NaCl bolus (semptomatikse)","Sıvı kısıtlaması","Isı ölçümü"],1,"Hipotonik sıvı hiponatremiyi derinleştirir.","Toksikoloji / Metabolik")]

# 76 KAUDA EQUİNA SENDROMU
S.append(case("c76","Bel ağrısı ve uyuşma — 42 yaşında erkek","Beyin cerrahisi / Ortopedi",
 "42 yaşında erkek, bilinen L4–L5 disk hernisi. 2 gündür bel ağrısı artmış, her iki bacağa vuruyor. Bugün tuvalette idrar başlatmakta zorlanmış ve “oturduğu yerde hissizlik” fark etmiş.",
 {"n1":N("Muayene","Bilateral siyatalji, sağda ayak bileği plantar fleksiyonu 4/5. **Perianal ve perineal (eyer bölgesi) duyu azalmış**. Aşil refleksleri alınamıyor.","KB 138/82 · Nb 88 · Ateş 36,7",[
   T("İşeme sonrası rezidü (mesane USG)",3,10,"**Rezidü 520 mL**, ağrısız.","Ağrısız retansiyon kauda equinayı güçlü destekler."),
   T("Rektal tuşe (anal tonus)",2,5,"Anal sfinkter tonusu azalmış.","Muayene belgelenmeli."),
   T("Lomber grafi",-1,20,"Dejeneratif değişiklikler.","Tanıya katkısı yok; MR geciktirilmemeli."),
   A("Kauda equina şüphesi: **acil lomber MR** (aynı gün, mesai dışı dahil); kateter; acil beyin cerrahisi — dekompresyon",4,30,"n2","Doğru. Retansiyon gelişmeden (CES-I) yapılan dekompresyon mesane fonksiyonunu daha iyi korur."),
   A("Siyatalji — analjezik ve kas gevşetici ile taburcu, poliklinik MR",-5,10,"n9","Eyer anestezisi + işeme bozukluğu acil cerrahi durumdur."),
 ]),
 "n2":E("Acil dekompresyon","MR'da L4–L5'te büyük santral disk ekstrüzyonu ile kauda equina basısı; 6 saat içinde mikrodiskektomi yapıldı. 3 ayda mesane fonksiyonu normale döndü.\n\n**Akılda kalsın**\n- Kırmızı bayraklar: **bilateral siyatalji, eyer anestezisi, mesane/bağırsak/cinsel fonksiyon bozukluğu**, ilerleyen motor kayıp.\n- **İşeme sonrası rezidü** ölç (>200 mL anlamlı).\n- **Acil MR** (aynı gün) ve **acil cerrahi**.\n- Hastalara “güvenlik ağı” uyarıları verilmeli.\n\n*Kaynak: GIRFT 2023 ulusal kauda equina yolu (İngiltere); NICE.*","good"),
 "n9":E("Kalıcı sfinkter kaybı","Hasta 2 gün sonra tam retansiyon ve inkontinansla döndü; dekompresyona rağmen kalıcı mesane ve cinsel disfonksiyon kaldı.","bad"),
}))
Qs+=[Q("c76q1","Kauda equina sendromunu en çok düşündüren bulgu hangisidir?",["Tek taraflı siyatalji","Eyer bölgesinde duyu kaybı ve işeme bozukluğu","Lomber hassasiyet","Düz bacak kaldırma testi pozitifliği tek başına","Paravertebral spazm"],1,"Sakral kök tutulumu bulguları.","Beyin cerrahisi / Ortopedi"),
 Q("c76q2","Kauda equina şüphesinde ilk görüntüleme hangisidir?",["Lomber grafi","Acil lomber MR","Kemik sintigrafisi","Abdominal USG","EMG"],1,"Aynı gün MR.","Beyin cerrahisi / Ortopedi"),
 Q("c76q3","Kauda equina değerlendirmesinde yatak başı yararlı ölçüm hangisidir?",["Kan şekeri","İşeme sonrası rezidü idrar (mesane USG)","Ateş","Nabız","D-dimer"],1,"Ağrısız retansiyon önemli bir bulgudur.","Beyin cerrahisi / Ortopedi")]

# 77 OZMOTİK DEMİYELİNİZASYON SENDROMU (önleme)
S.append(case("c77","Çok düşük sodyum — 58 yaşında erkek","Nefroloji / Nöroloji",
 "58 yaşında erkek, alkol kullanım bozukluğu, son haftalarda yalnız bira içip neredeyse hiç yemek yemiyor. Halsizlik ve dengesizlikle geldi. Konfüzyon hafif, nöbet yok.",
 {"n1":N("Muayene","Uyanık, dikkat dağınık. Ataksik. Ödem yok. Malnütre.","KB 118/72 · Nb 96",[
   T("Na, K, Mg, P",3,20,"**Na 106**, **K 2,7**, Mg 1,2, P 1,8.","Kronik ağır hiponatremi + hipokalemi + alkol + malnütrisyon: **ozmotik demiyelinizasyon için çok yüksek risk**."),
   A("Hafif-orta semptom: hipertonik sıvıyı ancak semptom artarsa küçük bolusla ver; **24 saatlik artış ≤8 mmol/L** hedefi; 2–4 saatte bir Na; **K replasmanı da Na'yı yükseltir** (hesaba kat); tiamin; idrar çıkışını izle",4,20,"n2","Doğru. Bira içicisi potomanisinde beslenme/tuz alınınca su diürezi başlar ve Na kontrolsüz yükselir."),
   A("Hemen normale getir: %3 NaCl infüzyonu 24 saat sürsün",-5,60,"n9","Kronik hiponatremide hızlı düzeltme ozmotik demiyelinizasyona yol açar."),
 ]),
 "n2":N("10. saat","Hasta bol idrar yapıyor (saatte 350 mL, açık renkli).","Na 113 (+7)",[
   A("Aşırı düzeltmeyi durdur: **desmopressin 2 mcg IV** + gerekirse %5 dekstroz ile Na artışını frenle (gerekirse yeniden düşür); saatlik Na",4,20,"n3","Doğru. Su diürezi başlayınca Na saatler içinde hedefi aşabilir; desmopressin “kelepçe” stratejisi."),
   A("Na hâlâ 113 — %3 NaCl ekle",-5,20,"n9","24 saatte 8 sınırı aşılacak."),
 ]),
 "n3":E("Güvenli düzeltme","24. saatte Na 114 (+8), 48. saatte 121. Hasta nörolojik sekelsiz taburcu edildi.\n\n**Akılda kalsın**\n- **Ozmotik demiyelinizasyon** (santral pontin/ekstrapontin miyelinoliz): hızlı Na düzeltilmesinden **2–6 gün sonra** dizartri, disfaji, kuadriparezi, “kilitli adam”.\n- Yüksek risk: **Na ≤105, hipokalemi, alkol, malnütrisyon, karaciğer hastalığı**.\n- Sınır: **24 saatte ≤8 mmol/L** (yüksek risk).\n- Su diürezi / K replasmanı Na'yı hızla yükseltir → **desmopressin** ve %5 dekstroz ile frenle; aşırıysa yeniden düşür.\n\n*Kaynak: ABD uzman paneli 2013; Avrupa 2014 hiponatremi kılavuzu.*","good"),
 "n9":E("Ozmotik demiyelinizasyon","Na 24 saatte 18 mmol/L yükseldi; 4. günde dizartri, disfaji ve kuadriparezi gelişti (MR'da pontin lezyon).","bad"),
}))
Qs+=[Q("c77q1","Ozmotik demiyelinizasyon için yüksek riskli hastada 24 saatlik Na artış sınırı hangisidir?",["≤4 mmol/L","≤8 mmol/L","≤15 mmol/L","≤20 mmol/L","Sınır yok"],1,"Yüksek riskte ≤8 mmol/L/24 saat.","Nefroloji / Nöroloji"),
 Q("c77q2","Hiponatremi tedavisinde Na beklenenden hızlı yükseliyorsa ne yapılabilir?",["%3 NaCl'yi artırmak","Desmopressin ± %5 dekstroz ile frenlemek","Furosemid","Tuz tableti","Sıvı kısıtlaması"],1,"Desmopressin su diürezini durdurur.","Nefroloji / Nöroloji"),
 Q("c77q3","Ozmotik demiyelinizasyon bulguları ne zaman ortaya çıkar?",["Hemen","2–6 gün sonra","1 ay sonra","1 yıl sonra","Yalnız tedavisiz hastada"],1,"Tipik olarak birkaç gün gecikmeyle (bifazik seyir).","Nefroloji / Nöroloji")]

# 78 ADRENAL KRİZ — uzun süreli steroid kesilmesi (sekonder)
S.append(case("c78","Sıvıya yanıtsız hipotansiyon — 68 yaşında kadın","Endokrin",
 "68 yaşında kadın, KOAH ve romatoid artrit nedeniyle 2 yıldır prednizolon 10 mg/gün kullanıyor; “ilacın yan etkilerinden korktuğu” için 1 hafta önce kendiliğinden bırakmış. 3 gündür öksürük, ateş; bugün çok halsiz.",
 {"n1":N("Resüsitasyon alanı","Konfüze, sağ bazalde raller.","KB 72/40 · Nb 122 · SS 26 · SpO₂ %90 · Ateş 38,6 · Glukoz 62",[
   T("Na, K",1,10,"Na 128, **K 4,2** (normal).","Sekonder (eksojen steroide bağlı) adrenal yetmezlikte mineralokortikoid korunur → hiperkalemi beklenmez."),
   T("Akciğer grafisi",1,15,"Sağ alt lob pnömonisi.","Tetikleyici enfeksiyon."),
   A("Sepsis paketi (kültür, antibiyotik, sıvı) + **hidrokortizon 100 mg IV hemen**, ardından 50 mg 6 saatte bir; hipoglisemi için dekstroz",4,10,"n2","Doğru. Uzun süre steroid kullanan hastada şokta stres dozu steroid gerekir."),
   A("Septik şok — sıvı ve norepinefrin, steroid gereksiz",-3,30,"n3","Steroid öyküsü sorgulanmadan refrakter şok gelişiyor."),
 ]),
 "n3":N("2 saat sonra","3 L sıvı ve artan norepinefrin dozuna rağmen hipotansiyon sürüyor. Kızı annesinin steroidi bıraktığını söylüyor.","KB 76/42 · Norepinefrin 0,4 mcg/kg/dk",[
   A("Hidrokortizon 100 mg IV, ardından 200 mg/24 saat",2,10,"n2","Doğru — vazopresör ihtiyacı hızla azaldı."),
   A("Vazopresin ekle, steroid yine verme",-4,20,"n9","Altta yatan adrenal yetmezlik tedavi edilmeden şok düzelmez."),
 ]),
 "n2":E("Krizden çıkış","Hidrokortizon sonrası 6 saatte vazopresör ihtiyacı kalmadı. Pnömoni tedavisi tamamlandı; steroid kademeli azaltma planı ve hasta gün kuralları anlatıldı.\n\n**Akılda kalsın**\n- **≥3–4 hafta** suprafizyolojik glukokortikoid kullanan herkes adrenal baskılanma açısından risklidir; **ani bırakma** krize yol açar.\n- Sekonder yetmezlikte **hiperkalemi yok**; hiponatremi ve hipoglisemi olabilir.\n- Sıvı ve vazopresöre yanıtsız şokta **steroid öyküsünü sor**.\n- **Hidrokortizon 100 mg IV**, ardından 200 mg/24 saat.\n- Steroid kademeli azaltılır; hastalık/ameliyatta **stres dozu**.\n\n*Kaynak: Society for Endocrinology 2020; ESE/Endocrine Society 2024 glukokortikoide bağlı adrenal yetmezlik kılavuzu.*","good"),
 "n9":E("Refrakter şok","Hasta yüksek doz vazopresöre rağmen arrest oldu.","bad"),
}))
Qs+=[Q("c78q1","Eksojen steroid kesilmesine bağlı (sekonder) adrenal yetmezlikte hangisi beklenmez?",["Hipotansiyon","Hipoglisemi","Hiponatremi","Belirgin hiperkalemi","Halsizlik"],3,"Renin-aldosteron sistemi korunduğu için hiperkalemi tipik değildir.","Endokrin"),
 Q("c78q2","Uzun süreli steroid kullanan hastada adrenal baskılanma riski hangi süreden sonra anlamlıdır?",["1 gün","3 gün","≥3–4 hafta suprafizyolojik doz","Yalnız 1 yıl sonra","Hiçbir zaman"],2,"Suprafizyolojik dozlarda 3–4 haftadan sonra HPA aksı baskılanabilir.","Endokrin"),
 Q("c78q3","Steroid kullanan hastada sıvı ve vazopresöre yanıtsız şokta eklenmesi gereken tedavi hangisidir?",["Hidrokortizon 100 mg IV","Fludrokortizon tek başına","Deksametazon 0,5 mg","Antihistaminik","Kalsiyum"],0,"Stres dozu hidrokortizon.","Endokrin")]

# 79 BRUGADA SENDROMU
S.append(case("c79","Ateşle bayılma — 34 yaşında erkek","Kardiyoloji",
 "34 yaşında erkek. 2 gündür grip, ateş 39,5 °C. Gece uykuda hırıltılı nefes alıp kısa süre yanıtsız kalmış, eşi uyandırınca kendine gelmiş. Babası 40 yaşında uykuda ani ölmüş.",
 {"n1":N("Acil servis","Bilinç açık, nörolojik muayene normal.","KB 124/76 · Nb 108 · Ateş 39,4",[
   T("12 derivasyonlu EKG",4,5,"V1–V2'de **≥2 mm, kubbe (coved) tipi ST elevasyonu ve negatif T** (tip 1 Brugada paterni).","Ateş Brugada paternini ortaya çıkarır ve aritmi riskini artırır."),
   A("Monitörize yatış, **ateşi agresif düşür** (parasetamol, dış soğutma); sodyum kanal blokerlerinden ve tetikleyici ilaçlardan kaçın; kardiyoloji — ICD değerlendirmesi; aile taraması",4,15,"n2","Doğru. Senkop + spontan/ateşle tip 1 patern + ailede ani ölüm → yüksek risk; ICD endikasyonu."),
   A("Vazovagal senkop + üst solunum yolu enfeksiyonu — taburcu",-5,10,"n9","Uykuda agonal solunumla senkop + tip 1 Brugada = ani ölüm riski."),
 ]),
 "n2":N("Gece 03:00","Monitörde tekrarlayan **polimorfik VT** atakları (elektriksel fırtına).","",[
   A("Nabızsız/instabil atakta defibrilasyon; fırtınayı baskılamak için **izoprenalin infüzyonu** (ve/veya kinidin); amiodaron/sınıf I antiaritmik verme",4,10,"n3","Doğru. Brugada'da izoprenalin ST elevasyonunu ve fırtınayı baskılar."),
   A("Amiodaron + prokainamid",-4,10,"n9","Sodyum kanal blokerleri (prokainamid) Brugada'yı ağırlaştırır; amiodaron fırtınada etkisiz kalabilir."),
 ]),
 "n3":E("ICD","İzoprenalinle aritmi baskılandı; hasta ICD ile taburcu edildi. Kardeşlerine EKG ve genetik danışmanlık planlandı.\n\n**Akılda kalsın**\n- Brugada: V1–V2'de **kubbe tipi ST elevasyonu** (tip 1), SCN5A; genç erkekte **uykuda/ateşle ani ölüm**.\n- **Ateş** ve bazı ilaçlar (sınıf I antiaritmik, TCA, lityum, propofol, kokain) paterni ortaya çıkarır → **brugadadrugs.org**.\n- Ateşi agresif düşür; senkop/aritmi öyküsünde **ICD**.\n- Elektriksel fırtına: **izoprenalin**, kinidin.\n\n*Kaynak: ESC 2022 Ventriküler aritmiler kılavuzu.*","good"),
 "n9":E("Ani kardiyak ölüm","Hasta uykuda VF geçirdi.","bad"),
}))
Qs+=[Q("c79q1","Brugada sendromunda tip 1 EKG paterni hangisidir?",["V5–V6'da ST çökmesi","V1–V2'de kubbe tipi ST elevasyonu + negatif T","Delta dalgası","Uzun QT","Epsilon dalgası"],1,"Tanısal patern tip 1'dir.","Kardiyoloji"),
 Q("c79q2","Brugada sendromlu hastada ateş için doğru yaklaşım hangisidir?",["Ateş önemsizdir","Ateş agresif biçimde düşürülmelidir","Ateş koruyucudur","Yalnız antibiyotik","Beta bloker"],1,"Ateş sodyum kanal fonksiyonunu bozarak aritmiyi tetikler.","Kardiyoloji"),
 Q("c79q3","Brugada'da elektriksel fırtınada kullanılan ilaç hangisidir?",["Prokainamid","Flekainid","İzoprenalin","Lidokain","Propafenon"],2,"İzoprenalin ve kinidin; sınıf IC ve IA (prokainamid) zararlıdır.","Kardiyoloji")]

# 80 BOERHAAVE — geç tanı (plevral bulgularla)
S.append(case("c80","“Pnömoni” tanısıyla gelen septik hasta — 55 yaşında erkek","Göğüs cerrahisi",
 "55 yaşında erkek. 2 gün önce aşırı yemek ve alkol sonrası şiddetli kusmuş, ardından göğüs ağrısı başlamış. Başka bir merkezde “pnömoni” denerek oral antibiyotik verilmiş. Bugün nefes darlığı ve yüksek ateşle getirildi.",
 {"n1":N("Resüsitasyon alanı","Toksik görünümlü. Sol hemitoraksta solunum sesleri azalmış.","KB 84/50 · Nb 132 · SS 30 · SpO₂ %88 · Ateş 39,4",[
   T("Akciğer grafisi",2,15,"**Sol hidropnömotoraks** (hava-sıvı seviyesi), mediasten genişlemiş.","Pnömoniyle açıklanamaz."),
   T("Torasentez",3,15,"Bulanık, kötü kokulu sıvı, içinde **yiyecek partikülleri**; **pH 6,7**, plevral amilaz çok yüksek.","Özofagus perforasyonunu düşündürür (tükürük amilazı)."),
   T("Toraks BT (IV + suda çözünür oral kontrast)",3,30,"Distal özofagustan sol plevraya kontrast kaçağı, mediastinal sıvı.","Tanıyı doğrular."),
   A("Septik şok resüsitasyonu; geniş spektrum antibiyotik + antifungal; ağızdan hiçbir şey; sol göğüs tüpü (drenaj); acil göğüs cerrahisi + gastroenteroloji — geç perforasyonda cerrahi onarım/drenaj ya da endoskopik stent/vakum tedavisi kararı",4,20,"n2","Doğru. Geç (>24 saat) tanıda bile kaynak kontrolü ve drenaj hayat kurtarır."),
   A("Pnömoni + parapnömonik efüzyon: IV antibiyotiğe geç, servise yatır",-5,30,"n9","Kusma sonrası göğüs ağrısı + hidropnömotoraks + yiyecek partikülü = özofagus rüptürü."),
 ]),
 "n2":E("Kaynak kontrolü","Ameliyatta sol torakotomi ile dekortikasyon, özofagus onarımı ve geniş drenaj yapıldı; yoğun bakımda 2 hafta sonra iyileşti.\n\n**Akılda kalsın**\n- Boerhaave sıklıkla **AKS, pankreatit, pnömoni** olarak atlanır.\n- Geç bulgular: **sol hidropnömotoraks**, ampiyem, mediastinit, septik şok.\n- Plevral sıvıda **yiyecek partikülü, düşük pH, yüksek amilaz** → özofagus perforasyonu.\n- Tedavi: sepsis, antibiyotik + antifungal, NPO, drenaj, cerrahi/endoskopik onarım.\n- Mortalite tanının gecikmesiyle belirgin artar.\n\n*Kaynak: WSES 2019 özofagus perforasyonu kılavuzu.*","good"),
 "n9":E("Ölüm","Mediastinit ve ampiyem tedavisiz kaldı; hasta çoklu organ yetmezliğiyle kaybedildi.","bad"),
}))
Qs+=[Q("c80q1","Plevral sıvıda hangi bulgu özofagus perforasyonunu düşündürür?",["Düşük amilaz, yüksek pH","Yüksek amilaz, düşük pH ve yiyecek partikülü","Şilöz sıvı","Yüksek glukoz","Transüda"],1,"Tükürük amilazı ve gıda içeriği.","Göğüs cerrahisi"),
 Q("c80q2","Boerhaave sendromunda plevral efüzyon en sık hangi taraftadır?",["Sağ","Sol","Bilateral eşit","Efüzyon olmaz","Perikardiyal"],1,"Distal özofagusun sol posterolateral duvarı yırtılır.","Göğüs cerrahisi"),
 Q("c80q3","Boerhaave sendromunda mortaliteyi en çok etkileyen faktör hangisidir?",["Yaş","Tanı ve tedavinin gecikmesi","Cinsiyet","Kan grubu","Mevsim"],1,"İlk 24 saatte tedavi edilenlerde mortalite belirgin düşüktür.","Göğüs cerrahisi")]

P={"id":"ilk-nobet-8","title":"İlk Nöbet Vakaları — 8. Paket","desc":"Crush sendromu, dekompresyon hastalığı, tetanoz, hava embolisi, MDMA'ya bağlı hiponatremi (SIADH), kauda equina, ozmotik demiyelinizasyon, steroid kesilmesine bağlı adrenal kriz, Brugada, geç tanı Boerhaave.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 8. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 8. Paket","topic":"Acil tıp","order":8,"req":[2],"desc":"Afet, çevresel, nörolojik, endokrin ve aritmik acillerden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
