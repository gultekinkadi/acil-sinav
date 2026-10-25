import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]

# 11 SENKOP — yüksek riskli (iletim sistemi hastalığı)
S.append(case("c11","Bayılma — 74 yaşında erkek","Kardiyoloji",
 "74 yaşında erkek. Evde otururken uyarı vermeden bayılmış, birkaç saniyede kendine gelmiş; düşerken alnını çarpmış. Öncesinde çarpıntı, terleme, bulantı yok. Son ay iki kez “gözlerinin karardığını” söylüyor. Hipertansiyon ve tip 2 diyabet var.",
 {"n1":N("Muayene odası","Bilinç açık, nörolojik muayene normal. Alında 2 cm laserasyon.","KB 142/78 · Nb 64 · SpO₂ %97 · Kapiller glukoz 132",[
   T("12 derivasyonlu EKG",3,5,"Sinüs ritmi 64/dk, **PR 260 ms**, **sağ dal bloğu + sol anterior fasiküler blok** (bifasiküler blok).","Senkopta EKG her hastada çekilir; iletim sistemi hastalığı aritmik senkopu düşündürür."),
   T("Ortostatik KB ölçümü",1,10,"Yatarken 142/78, ayakta 3. dakikada 136/76; semptom yok.","Ortostatik hipotansiyon: 3 dakika içinde sistolikte ≥20 veya diyastolikte ≥10 mmHg düşme."),
   T("Kraniyal BT",-1,30,"Normal.","Nörolojik bulgusu olmayan senkopta rutin beyin BT'nin tanısal verimi çok düşüktür (burada kafa travması nedeniyle düşünülebilir ama senkop nedenini açıklamaz)."),
   A("Yüksek riskli senkop: monitörize et, kardiyoloji ile yatış/telemetri planla",3,10,"n2","Doğru. Uyarısız (prodromsuz) senkop, ileri yaş, bifasiküler blok ve tekrarlayan presenkop aritmik nedeni düşündürür."),
   A("Vazovagal senkop — laserasyonu sütürle, taburcu et",-4,20,"n9","Prodromsuz senkop + iletim sistemi hastalığı yüksek risktir; taburculuk ölümcül aritmiyi kaçırabilir."),
 ]),
 "n2":N("Telemetride 40. dakika","Hasta baş dönmesi tarifliyor.","KB 92/50 · Nb 34",[
   T("Ritim şeridi",2,1,"**Mobitz tip II** ardından geniş QRS'li kaçış ritimli **tam AV blok**.","İnfranodal blok: atropine yanıt beklenmez."),
   A("Transkutan pace (pedler takılı, hız 60–70, yakalamayı nabızla doğrula); gerekirse adrenalin/izoprenalin infüzyonu köprü; acil kardiyoloji — geçici transvenöz/kalıcı pacemaker",4,10,"n3","Doğru. Geniş QRS'li tam blokta atropin genellikle etkisizdir; pace hazır olmalıdır."),
   A("Atropin 3 mg tek doz ver ve bekle",-1,10,"n3","İnfranodal blokta atropin çoğunlukla işe yaramaz; zaman kaybedildi, pace sonra yapıldı."),
   A("Beta bloker ve kalsiyum kanal blokeri dozlarını artır",-4,5,"n9","Bradiaritmide AV nod baskılayıcı ilaçlar asistoliye götürebilir."),
 ]),
 "n3":E("Kalıcı pacemaker","Transkutan pace ile hız 70'e çıktı, KB 118/64. Aynı gün geçici, ertesi gün kalıcı pacemaker takıldı.\n\n**Akılda kalsın**\n- Senkopta **EKG her hastaya**; ortostatik ölçüm yap.\n- **Yüksek risk**: prodromsuz/efor sırasında/yatarken senkop, yapısal kalp hastalığı, anormal EKG (bifasiküler blok, Mobitz II, uzun QT, Brugada, preeksitasyon), ailede ani ölüm, çarpıntıyla başlayan senkop.\n- Düşük riskli vazovagal senkop taburcu edilebilir; yüksek risk monitörize izlenir.\n- Geniş QRS'li tam blokta **pace**; atropin etkisizdir.\n\n*Kaynak: ESC 2018 Senkop Kılavuzu; ERC 2021 Bradikardi algoritması.*","good"),
 "n9":E("Evde ani ölüm riski","Hasta taburculuğun ertesi günü yeniden bayıldı; tam AV blok ve uzun asistoli ile getirildi.\n\nSenkopta öykü + EKG ile risk sınıflaması atlanmamalı.","bad"),
}))
Qs+=[Q("c11q1","Ortostatik hipotansiyon tanımı hangisidir?",["Ayağa kalkınca nabızda 10/dk artış","3 dakika içinde sistolikte ≥20 veya diyastolikte ≥10 mmHg düşme","Sistolik KB <100 mmHg","Ayakta baş dönmesi tarifi","Yatarken KB >160 mmHg"],1,"Klasik tanım: ayağa kalktıktan sonraki 3 dakika içinde sistolik ≥20 veya diyastolik ≥10 mmHg düşme.","Kardiyoloji"),
 Q("c11q2","Aşağıdakilerden hangisi senkopta yüksek risk özelliği değildir?",["Efor sırasında senkop","Bifasiküler blok","Uzun süre ayakta durma sonrası, terleme ve bulantıyla başlayan senkop","Ailede genç yaşta ani ölüm","Yatarken senkop"],2,"Uzun ayakta durma + prodrom (terleme, bulantı) refleks (vazovagal) senkopu düşündürür ve düşük risklidir.","Kardiyoloji"),
 Q("c11q3","Geniş QRS'li kaçış ritmi olan semptomatik tam AV blokta en etkili acil tedavi hangisidir?",["Atropin 0,5 mg","Adenozin","Transkutan pace","Amiodaron","Digoksin"],2,"İnfranodal blokta atropin etkisizdir; transkutan pace ve kronotrop infüzyon köprü tedavidir.","Kardiyoloji")]

# 12 STATUS EPİLEPTİKUS
S.append(case("c12","Durmayan nöbet — 34 yaşında erkek","Nöroloji",
 "34 yaşında erkek, epilepsi tanılı; ilaçlarını son 1 haftadır almamış. Ambulansta jeneralize tonik-klonik nöbet başlamış, acile girişte (6. dakika) sürüyor. Yaklaşık 80 kg.",
 {"n1":N("Resüsitasyon alanı — 6. dakika","Jeneralize tonik-klonik nöbet sürüyor. Damar yolu yok, ağızda köpük.","KB 168/96 · Nb 132 · SpO₂ %88 · Ateş 37,8",[
   T("Kapiller glukoz",2,1,"112 mg/dL.","Her nöbette glukoz bakılır; hipoglisemi düzeltilmeden nöbet durmaz."),
   T("Beyin BT",-2,20,"Yapılamadı — hasta nöbet geçirirken çekim mümkün değil; zaman kaybı.","Önce nöbeti durdur, sonra görüntüle."),
   A("Yan pozisyon, aspirasyon, O₂; ilk basamak benzodiazepin: damar yolu yoksa midazolam 10 mg IM (>40 kg), damar yolu varsa diazepam 10 mg IV (veya lorazepam 4 mg IV); 5 dakikada yanıt yoksa bir kez tekrar",4,5,"n2","Doğru. 5 dakikayı aşan nöbet status epileptikus kabul edilir; benzodiazepin yeterli dozda ve geciktirmeden verilir."),
   A("Önce damar yolu aç, sonra fenitoin yükle",-3,15,"n3","Benzodiazepin ilk basamaktır; damar yolu beklenmez (IM midazolam). İkinci basamak ilaçlar benzodiazepinden sonra gelir."),
   A("Nöbet kendiliğinden durur, gözlemle",-4,15,"n9","5 dakikayı aşan nöbet kendiliğinden durma olasılığı düşüktür ve beyin hasarı riski zamanla artar."),
 ]),
 "n3":N("12. dakika","Nöbet sürüyor; damar yolu açıldı.","SpO₂ %86 · Nb 140",[
   A("Diazepam 10 mg IV (yanıtsızsa 5 dakika sonra tekrar)",1,5,"n2","Doğru ama gecikmeli."),
 ]),
 "n2":N("İki doz benzodiazepinden sonra — 18. dakika","Nöbet sürüyor; sağ elde ritmik kasılmalar ve göz deviasyonu.","KB 150/88 · Nb 128 · SpO₂ %92",[
   A("İkinci basamak: levetirasetam 60 mg/kg IV (en çok 4500 mg) veya valproat 40 mg/kg IV (en çok 3000 mg) veya fosfenitoin 20 mg FE/kg — 10 dakikada; hava yolu hazırlığı",4,15,"n4","Doğru. ESETT çalışmasında üç ilaç benzer etkinlikte; seçimi hastaya göre yap (gebelikte valproattan kaçın)."),
   A("Üçüncü doz benzodiazepin ver",-2,10,"n4","İki dozdan sonra ek benzodiazepin solunum depresyonunu artırır, etkinliği düşüktür; ikinci basamağa geç."),
 ]),
 "n4":N("Yükleme dozundan sonra — 35. dakika","Hareketler durdu ama hasta 20 dakikadır uyanmıyor; gözler hafif sağa deviye.","KB 138/80 · Nb 104 · SpO₂ %95",[
   T("EEG (acil)",3,30,"Sürekli epileptiform aktivite — **nonkonvülzif status**.","Klinik nöbet durup bilinç düzelmiyorsa nonkonvülzif status düşünülür."),
   A("Refrakter status: entübasyon, anestezik infüzyon (midazolam veya propofol), yoğun bakım, sürekli EEG; neden araştır (ilaç düzeyi, elektrolit, BT, gerekirse LP)",3,30,"n5","Doğru. İki basamağa yanıtsız status refrakterdir; anestezik infüzyon ve EEG izlemi gerekir."),
   A("Nöbet durdu, servise yatır",-4,10,"n9","Postiktal dönem 20–30 dakikayı aşar ve bilinç düzelmezse nonkonvülzif status dışlanmalıdır."),
 ]),
 "n5":E("Kontrol altına alındı","Midazolam infüzyonu ile EEG'de nöbet aktivitesi durdu; 24 saat sonra ilaç azaltıldı, hasta uyandı. Neden: antiepileptik bırakılması.\n\n**Akılda kalsın**\n- **5 dakikayı aşan** nöbet = status epileptikus.\n- **Glukoz** hemen; alkol bağımlılığında tiamin.\n- 1. basamak **benzodiazepin** (IM midazolam 10 mg / IV diazepam 10 mg / IV lorazepam 4 mg), bir kez tekrar.\n- 2. basamak: **levetirasetam 60 mg/kg, valproat 40 mg/kg veya fosfenitoin 20 mg FE/kg**.\n- Yanıtsız → anestezik infüzyon + EEG. Bilinç düzelmiyorsa **nonkonvülzif status**.\n\n*Kaynak: AES 2016 status epileptikus kılavuzu; ESETT (NEJM 2019).*","good"),
 "n9":E("Uzamış status","Nöbet 1 saati aştı; aspirasyon pnömonisi, rabdomiyoliz ve kalıcı bilişsel hasar gelişti.\n\nStatusta zaman beyindir: basamaklar dakikalarla ilerler.","bad"),
}))
Qs+=[Q("c12q1","Damar yolu olmayan 80 kg erişkinde status epileptikus için ilk tedavi hangisidir?",["Fenitoin IM","Midazolam 10 mg IM","Levetirasetam PO","Fenobarbital PO","Propofol IV"],1,"RAMPART: IM midazolam 10 mg, damar yolu beklemekten daha hızlı ve etkilidir.","Nöroloji"),
 Q("c12q2","Benzodiazepine dirençli statusta levetirasetamın yükleme dozu hangisidir?",["10 mg/kg","20 mg/kg","30 mg/kg","60 mg/kg (en çok 4500 mg)","100 mg/kg"],3,"Levetirasetam 60 mg/kg IV (en çok 4500 mg); ESETT'te valproat ve fosfenitoinle benzer etkinlik.","Nöroloji"),
 Q("c12q3","Klinik nöbeti duran ama 30 dakikadır bilinci düzelmeyen hastada ilk düşünülmesi gereken hangisidir?",["Normal postiktal dönem","Psikojenik nöbet","Nonkonvülzif status epileptikus","Konversiyon","Uyku"],2,"Uzamış bilinç bozukluğunda EEG ile nonkonvülzif status dışlanmalıdır.","Nöroloji")]

# 13 KARBONMONOKSİT İNTOKSİKASYONU
S.append(case("c13","Ailece baş ağrısı — 41 yaşında kadın","Toksikoloji",
 "41 yaşında kadın, eşi ve 10 yaşındaki oğluyla birlikte geldi. Sabah üçünde de baş ağrısı, bulantı ve halsizlik var. Kadın evde bir an bayılmış. Evde kömür sobası yanıyor. Kadın 14 haftalık gebe.",
 {"n1":N("Triaj","Bilinç açık, konfüzyon yok. Baş ağrısı şiddetli.","KB 118/72 · Nb 108 · SS 22 · **SpO₂ %99**",[
   T("Venöz kan gazı + CO-oksimetri (COHb)",3,10,"**COHb %24**, laktat 2,8 mmol/L, pH 7,36.","Nabız oksimetresi COHb'yi oksihemoglobin gibi okur; SpO₂ normal görünür. Tanı CO-oksimetri ile konur."),
   T("EKG ve troponin",2,30,"Sinüs taşikardisi; troponin normal.","CO miyokard hasarı yapabilir; tüm orta-ağır olgularda EKG ve troponin."),
   T("Nabız oksimetresine güven, kan gazı gereksiz",-3,0,"SpO₂ %99.","Nabız oksimetresi CO zehirlenmesinde yanıltıcıdır."),
   A("Hemen %100 O₂ (rezervuarlı maske, yüksek akım); aileyi de değerlendir; hiperbarik oksijen endikasyonunu değerlendir",3,5,"n2","Doğru. Normobarik %100 O₂ COHb yarılanma ömrünü ≈5 saatten ≈1 saate indirir."),
   A("Analjezik ver, baş ağrısı geçince taburcu et",-4,30,"n9","Ev ortamı CO kaynağı; geri dönen hastada zehirlenme sürer, gecikmiş nörolojik sekel riski yüksek."),
 ]),
 "n2":N("HBO kararı","Hasta %100 O₂ alıyor. Bilinç kaybı öyküsü var, gebe.","COHb (30. dk) %17",[
   A("Hiperbarik oksijen tedavisi için merkezle iletişime geç (bilinç kaybı öyküsü + gebelik); taşıma sırasında %100 O₂ sürsün",4,30,"n3","Doğru. HBO endikasyonları: bilinç kaybı, nörolojik bulgu, COHb >%25 (gebelikte >%15–20), kardiyak iskemi, ağır asidoz, fetal distres."),
   A("COHb düşüyor; HBO gerekmez, 2 saat O₂ ve taburcu",-3,120,"n8","Bilinç kaybı ve gebelik HBO endikasyonudur; fetal hemoglobin CO'yu daha uzun tutar."),
 ]),
 "n3":E("Hiperbarik oksijen tedavisi","Hasta HBO tedavisi aldı; fetal izlem normal. Eşi ve oğlunun COHb %12 ve %9; normobarik O₂ ile izlendiler. Sobanın bacası tıkalı bulundu; ev havalandırılmadan dönmemeleri söylendi.\n\n**Akılda kalsın**\n- Kışın **ailece baş ağrısı/bulantı** = CO düşün.\n- **SpO₂ normal olabilir**; COHb'yi kan gazında (CO-oksimetri) ölç.\n- Hemen **%100 O₂**.\n- HBO: bilinç kaybı, nörolojik bulgu, COHb >%25 (gebede >%15–20), iskemi, ağır asidoz.\n- Gecikmiş nöropsikiyatrik sekel için kontrol; **ev güvenli olmadan taburcu etme**.\n\n*Kaynak: ACEP 2017 CO klinik politikası; UHMS HBO endikasyonları.*","good"),
 "n8":E("Gecikmiş nörolojik sekel riski","Hasta 3 hafta sonra unutkanlık ve dikkat bozukluğuyla başvurdu (gecikmiş nöropsikiyatrik sendrom).\n\nBilinç kaybı ve gebelikte HBO değerlendirmesi atlanmamalı.","mid"),
 "n9":E("Tekrar maruziyet","Aile aynı gece evde bilinç kaybıyla bulundu.\n\nCO zehirlenmesinde kaynak kontrolü ve O₂ tedavisi hayat kurtarır.","bad"),
}))
Qs+=[Q("c13q1","CO zehirlenmesinde nabız oksimetresi neden güvenilir değildir?",["Hipotermi nedeniyle","COHb'yi oksihemoglobin gibi okuduğu için SpO₂ yanlış normal görünür","Methemoglobin oluştuğu için düşük okur","Taşikardi nedeniyle","Anemiden dolayı"],1,"Standart oksimetre iki dalga boyu kullanır ve COHb'yi ayırt edemez.","Toksikoloji"),
 Q("c13q2","Oda havasında yaklaşık 5 saat olan COHb yarılanma ömrü %100 normobarik O₂ ile yaklaşık ne kadara iner?",["4 saat","60–90 dakika","5 dakika","12 saat","Değişmez"],1,"%100 O₂ ile ≈60–90 dakika, HBO ile ≈20–30 dakika.","Toksikoloji"),
 Q("c13q3","Hangisi CO zehirlenmesinde hiperbarik oksijen endikasyonu değildir?",["Bilinç kaybı öyküsü","COHb %30","Gebede COHb %18","Yalnız hafif baş ağrısı ve COHb %8","Miyokard iskemisi"],3,"Hafif semptom ve düşük COHb normobarik O₂ ile tedavi edilir.","Toksikoloji")]

# 14 AKUT APANDİSİT
S.append(case("c14","Karın ağrısı — 22 yaşında erkek","Genel cerrahi",
 "22 yaşında erkek. Dün akşam göbek çevresinde başlayan, sabaha doğru sağ alt kadrana yerleşen ağrı; iştahsızlık ve bir kez kusma. Ateşi var.",
 {"n1":N("Muayene","Sağ alt kadranda (McBurney) hassasiyet, rebound ve istemsiz defans. Yürürken ağrı artıyor.","KB 124/76 · Nb 104 · Ateş 38,2",[
   T("Tam kan sayımı + CRP",2,30,"Lökosit 15.800 (nötrofil %86), CRP 64 mg/L.","Alvarado skoru: göç eden ağrı, iştahsızlık, bulantı/kusma, SAK hassasiyeti, rebound, ateş, lökositoz, sola kayma."),
   T("Abdominal ultrasonografi",2,20,"Çapı 10 mm, basmakla kollabe olmayan, periapendiküler yağ dokusunda kirlenme gösteren apendiks.","Genç, ince hastada ve çocuk/gebede ilk görüntüleme USG; tanısal değilse BT."),
   T("Tam idrar tetkiki",1,20,"Birkaç lökosit, nitrit negatif.","Apendiks üretere komşuysa piyüri görülebilir; tanıyı dışlamaz."),
   A("Analjezi (IV parasetamol/opioid) ver; genel cerrahiye danış; aç bırak, IV sıvı, antibiyotik profilaksisi cerrahla birlikte",4,15,"n2","Doğru. Analjezi tanıyı maskelemez; erken cerrahi değerlendirme."),
   A("Cerrah görmeden analjezik verme, ağrıyı maskeler",-2,60,"n2","Bu eski bir inanış; analjezi muayene bulgularını ve tanı doğruluğunu bozmaz, hasta gereksiz ağrı çekti."),
   A("Gastroenterit — antiemetik ver, taburcu et",-4,20,"n9","Göç eden ağrı, SAK hassasiyeti, rebound, ateş ve lökositoz apandisiti düşündürür."),
 ]),
 "n2":E("Laparoskopik apendektomi","Hasta 4 saat içinde ameliyata alındı; perfore olmamış flegmonöz apendisit. Ertesi gün taburcu edildi.\n\n**Akılda kalsın**\n- Klasik seyir: **göbek çevresinden sağ alt kadrana göç** eden ağrı, iştahsızlık, ateş.\n- **Alvarado** skoru risk sınıflamasında yardımcı.\n- Görüntüleme: çocuk, gebe ve genç ince hastada **önce USG**; erişkinde belirsizse BT.\n- **Analjezi tanıyı maskelemez** — geciktirme.\n- Taburcu edilen şüpheli olguya 12–24 saatte yeniden değerlendirme ve net uyarılar.\n\n*Kaynak: WSES 2020 Jerusalem akut apandisit kılavuzu.*","good"),
 "n9":E("Perforasyon","Hasta 36 saat sonra yaygın peritonit ve sepsisle döndü; perfore apandisit, açık cerrahi ve uzun hastanede kalış.\n\nKarın ağrısında gastroenterit tanısı kusma ve ishal olmadan konmamalı; şüphede yeniden değerlendirme şart.","bad"),
}))
Qs+=[Q("c14q1","Akut apandisit şüphesinde analjezi ile ilgili doğru ifade hangisidir?",["Cerrah muayenesine kadar verilmemelidir","Fizik muayene bulgularını kaybettirir","Tanı doğruluğunu bozmaz; erken verilmelidir","Yalnız NSAİİ verilebilir","Opioid kontrendikedir"],2,"Randomize çalışmalar analjezinin tanı doğruluğunu bozmadığını göstermiştir.","Genel cerrahi"),
 Q("c14q2","Gebe hastada apandisit şüphesinde ilk görüntüleme yöntemi hangisidir?",["Kontrastlı BT","Ultrasonografi","Direkt grafi","Sintigrafi","Görüntüleme gerekmez"],1,"Gebelik ve çocuklarda önce USG; tanısal değilse MR.","Genel cerrahi"),
 Q("c14q3","Hangisi Alvarado skorunun bileşeni değildir?",["Sağ alt kadrana göç eden ağrı","İştahsızlık","Lökositoz","İshal","Rebound hassasiyeti"],3,"Alvarado: göç eden ağrı, iştahsızlık, bulantı/kusma, SAK hassasiyeti, rebound, ateş, lökositoz, sola kayma.","Genel cerrahi")]

# 15 MENENJİT
S.append(case("c15","Ateş ve baş ağrısı — 19 yaşında kadın","Enfeksiyon",
 "19 yaşında üniversite öğrencisi, yurtta kalıyor. Dün başlayan şiddetli baş ağrısı, ateş, kusma; bugün ışıktan rahatsız oluyor ve uykuya meyilli.",
 {"n1":N("Resüsitasyon alanı","GKS 14 (konfüze). Ense sertliği belirgin. Döküntü yok. Fokal nörolojik bulgu yok.","KB 108/66 · Nb 122 · SS 22 · SpO₂ %97 · Ateş 39,6",[
   T("Kan kültürü (2 set)",2,5,"Alındı.","Antibiyotikten önce — ama antibiyotiği geciktirmeden."),
   T("Beyin BT (LP öncesi)",1,30,"Normal.","LP öncesi BT; bilinç bozukluğu, fokal bulgu, yeni nöbet, papilödem, immünsupresyon veya SSS hastalığı öyküsünde önerilir. BT beklenirken antibiyotik geciktirilmez."),
   T("Lomber ponksiyon (BT ve antibiyotik sonrası)",2,30,"Bulanık BOS, açılış basıncı 34 cmH₂O, lökosit 2400/mm³ (%90 PNL), protein 260 mg/dL, glukoz 18 mg/dL (kan 120). Gram boyamada Gram negatif diplokok.","Bakteriyel menenjit. Antibiyotikten sonraki ilk saatlerde BOS bulguları ve kültür hâlâ yol gösterir."),
   A("Hemen deksametazon 10 mg IV (antibiyotikten hemen önce/birlikte) + seftriakson 2 g IV (12 saatte bir) + vankomisin; ardından BT ve LP",4,10,"n2","Doğru. Bakteriyel menenjitte antibiyotik ilk saatte; görüntüleme veya LP için geciktirilmez."),
   A("Önce BT, sonra LP; BOS sonucuna göre antibiyotik başla",-4,90,"n9","BT ve LP'yi beklerken geçen her saat mortaliteyi artırır."),
   A("Viral olabilir — analjezik ve sıvı, sabah tekrar değerlendir",-5,60,"n9","Bilinç değişikliği + ense sertliği + yüksek ateş bakteriyel menenjit kabul edilir."),
 ]),
 "n2":N("Yatış öncesi","BOS'ta Gram negatif diplokok: *Neisseria meningitidis* düşünülüyor. Hasta yurtta oda arkadaşlarıyla yaşıyor.","KB 112/70 · Nb 104",[
   A("Damlacık izolasyonu (ilk 24 saat); halk sağlığına bildirim; yakın temaslılara kemoprofilaksi (siprofloksasin 500 mg tek doz PO ya da rifampisin); yoğun bakım/enfeksiyon yatışı",3,15,"n3","Doğru. Meningokok hastalığı bildirimi zorunludur; yakın temaslılara profilaksi önerilir."),
   A("Temaslılar için önlem gerekmez",-3,5,"n8","Meningokokal hastalıkta yakın temaslılarda ikincil olgu riski yüksektir."),
 ]),
 "n3":E("İyi sonuç","Hasta 7 gün seftriakson ile sekelsiz iyileşti; kültürde *N. meningitidis* üredi. Oda arkadaşları profilaksi aldı.\n\n**Akılda kalsın**\n- Ateş + baş ağrısı + ense sertliği + bilinç değişikliği → **ilk saatte antibiyotik**.\n- **Deksametazon 10 mg IV** antibiyotikten hemen önce veya birlikte (6 saatte bir, 4 gün).\n- Seftriakson 2 g IV + vankomisin; **>50 yaş, gebe, immünsüprese** → **ampisilin** ekle (*Listeria*).\n- LP öncesi BT yalnız endikasyonu varsa; **antibiyotik BT'yi beklemez**.\n- Meningokokta bildirim ve **temaslı profilaksisi**.\n\n*Kaynak: ESCMID 2016 akut bakteriyel menenjit kılavuzu.*","good"),
 "n8":E("İkincil olgu","Oda arkadaşlarından biri 3 gün sonra meningokoksemiyle getirildi.\n\nYakın temaslılara profilaksi ve bildirim, tedavinin parçasıdır.","mid"),
 "n9":E("Gecikmiş tedavi","Antibiyotik 3 saat gecikti; hasta komaya girdi, işitme kaybı ve nörolojik sekel kaldı.\n\nBakteriyel menenjitte antibiyotik görüntüleme ve LP'yi beklemez.","bad"),
}))
Qs+=[Q("c15q1","Erişkin bakteriyel menenjitte deksametazon ne zaman verilmelidir?",["BOS kültürü üredikten sonra","Antibiyotikten hemen önce veya birlikte","3. günde","Yalnız şok varsa","Hiç verilmez"],1,"Deksametazon (10 mg IV, 6 saatte bir) ilk antibiyotik dozundan hemen önce veya birlikte başlanır; özellikle pnömokokta mortaliteyi azaltır.","Enfeksiyon"),
 Q("c15q2","Hangi hastada ampirik menenjit tedavisine ampisilin eklenmelidir?",["25 yaşında sağlıklı erkek","65 yaşında hasta","Viral menenjit şüphesi","Penisilin alerjisi","Çocuk 5 yaş"],1,">50 yaş, gebelik, immünsupresyon ve alkolizmde Listeria kapsaması için ampisilin eklenir.","Enfeksiyon"),
 Q("c15q3","Meningokokal menenjitte yakın temaslı erişkin için kemoprofilaksi seçeneği hangisidir?",["Amoksisilin 7 gün","Siprofloksasin 500 mg tek doz PO","Vankomisin IV","Azitromisin 5 gün","Profilaksi önerilmez"],1,"Siprofloksasin tek doz, rifampisin 2 gün veya seftriakson tek doz IM seçeneklerdir.","Enfeksiyon")]

# 16 ÜST GİS KANAMA
S.append(case("c16","Siyah dışkı ve kan kusma — 61 yaşında erkek","Gastroenteroloji",
 "61 yaşında erkek. Diz ağrısı için 2 haftadır günde 3 kez naproksen kullanıyor. Dünden beri siyah, yapışkan dışkı; bugün bir kez kahve telvesi kusmuş, ayağa kalkınca bayılacak gibi olmuş. Siroz öyküsü yok.",
 {"n1":N("Resüsitasyon alanı","Soluk, terli. Rektal tuşede melena.","KB 88/54 · Nb 122 · SS 20 · SpO₂ %97",[
   T("Hemogram, üre, kreatinin, INR, kan grubu",2,20,"Hb 7,1 g/dL · Üre 118 mg/dL (BUN 55) · Kreatinin 1,0 · INR 1,1.","Üre/kreatinin oranının yükselmesi üst GİS kanamayı destekler. Glasgow-Blatchford skoru yüksek."),
   T("Nazogastrik lavaj",-1,15,"Kahve telvesi.","Rutin NG lavaj önerilmez; tanı ve prognoza katkısı sınırlı."),
   A("İki geniş damar yolu, kristaloid, kan hazırla; eritrosit transfüzyonu (Hb <7 hedefi — kardiyovasküler hastalıkta <8); IV PPI (ör. pantoprazol 80 mg bolus); gastroenteroloji — endoskopi",4,15,"n2","Doğru. Resüsitasyon + kısıtlayıcı transfüzyon + PPI + erken endoskopi."),
   A("Hb 10'un üzerine çıkana kadar transfüzyon yap",-2,30,"n2","Liberal transfüzyon yeniden kanamayı ve mortaliteyi artırabilir; kısıtlayıcı strateji (Hb 7–9 hedefi) önerilir."),
   A("Hasta stabil olunca ertesi gün poliklinik endoskopisi",-4,60,"n9","Hemodinamik bozukluğu olan hastada endoskopi resüsitasyon sonrası ilk 24 saatte (instabilitede daha erken) yapılmalıdır."),
 ]),
 "n2":N("Resüsitasyondan 1 saat sonra","2 ünite eritrosit, 1 L kristaloid verildi.","KB 108/66 · Nb 98",[
   T("Glasgow-Blatchford skoru",1,2,"**14** (yüksek risk).","GBS 0–1 olan hastalar ayaktan izlenebilir; yüksek skorda endoskopik tedavi olasılığı yüksek."),
   A("Endoskopi (ilk 24 saatte; burada uygun ilk fırsatta) — PPI infüzyonu/aralıklı yüksek doz; NSAİİ'yi kes; *H. pylori* testi",3,30,"n3","Doğru."),
   A("Somatostatin + seftriakson başla, varis kanaması tedavisi",-1,15,"n3","Siroz/portal hipertansiyon bulgusu yok; varis tedavisi bu hastada öncelikli değil."),
 ]),
 "n3":E("Endoskopik hemostaz","Duodenum bulbusunda görünür damarlı ülser; adrenalin enjeksiyonu + klips ile hemostaz. Yüksek doz PPI ile yeniden kanama olmadı; *H. pylori* pozitif, eradikasyon başlandı.\n\n**Akılda kalsın**\n- **Resüsitasyon** önce: iki geniş damar yolu, kristaloid, kan.\n- **Kısıtlayıcı transfüzyon**: Hb <7 (koroner hastalıkta <8).\n- Endoskopi öncesi **IV PPI**; endoskopi **ilk 24 saatte**.\n- **Glasgow-Blatchford 0–1** → ayaktan izlenebilir.\n- Siroz/varis şüphesinde **terlipressin (veya somatostatin/oktreotid) + antibiyotik profilaksisi**.\n\n*Kaynak: ESGE 2021 non-varis üst GİS kanama kılavuzu; ACG 2021.*","good"),
 "n9":E("Yeniden kanama — şok","Gece masif hematemez; hasta hemorajik şokla acil endoskopi ve yoğun bakıma alındı.\n\nYüksek riskli üst GİS kanamada erken endoskopi ve yakın izlem şart.","bad"),
}))
Qs+=[Q("c16q1","Akut üst GİS kanamada (koroner hastalığı olmayan) eritrosit transfüzyonu eşiği hangisidir?",["Hb <10 g/dL","Hb <9 g/dL","Hb <7 g/dL","Hb <5 g/dL","Hb düzeyinden bağımsız her hastaya"],2,"Kısıtlayıcı strateji: Hb <7 (hedef 7–9); kardiyovasküler hastalıkta <8.","Gastroenteroloji"),
 Q("c16q2","Hangi Glasgow-Blatchford skorunda hasta ayaktan izlenebilir?",["0–1","3–4","5–6","8","12"],0,"GBS 0–1 olan hastalarda müdahale ve ölüm riski çok düşüktür; erken taburculuk güvenlidir.","Gastroenteroloji"),
 Q("c16q3","Sirozlu hastada varis kanaması şüphesinde endoskopi öncesi verilmesi gerekenler hangisidir?",["Yalnız PPI","Terlipressin (veya somatostatin/oktreotid) + antibiyotik profilaksisi (ör. seftriakson)","Traneksamik asit yüksek doz","Beta bloker IV","K vitamini tek başına"],1,"Vazoaktif ilaç ve antibiyotik profilaksisi mortaliteyi azaltır; HALT-IT'e göre yüksek doz traneksamik asit önerilmez.","Gastroenteroloji")]

# 17 HİPERTANSİF ACİL
S.append(case("c17","Baş ağrısı ve bulanık görme — 48 yaşında erkek","Kardiyoloji",
 "48 yaşında erkek. Hipertansiyonu var, 2 aydır ilaç kullanmıyor. 3 gündür ense ağrısı, bulanık görme ve bulantı. Göğüs ağrısı ve nefes darlığı yok.",
 {"n1":N("Muayene odası","Bilinç açık, nörolojik muayene normal. Fundoskopide alev şeklinde hemorajiler ve eksüdalar, papil sınırları silik.","KB 238/138 (iki kolda benzer) · Nb 92 · SpO₂ %97",[
   T("Kreatinin, idrar, hemogram, LDH",2,40,"Kreatinin **2,6 mg/dL** (bazal bilinmiyor) · idrarda protein ++, eritrosit · Hb 10,8, trombosit 98.000, LDH yüksek, periferik yaymada şistosit.","Akut böbrek hasarı + trombotik mikroanjiyopati → **malign hipertansiyon** (hipertansif acil)."),
   T("EKG ve troponin",1,30,"Sol ventrikül hipertrofisi; troponin hafif yüksek.","Hedef organ hasarı taraması."),
   T("Kontrastsız beyin BT",1,25,"Kanama yok.","Baş ağrısı/bulanık görmede kanama ve PRES ayrımı için."),
   A("Hipertansif acil: monitörize alan; titre edilebilir IV ilaç (labetalol veya nikardipin infüzyonu); ilk saatte ortalama arter basıncını en çok %25 düşür, sonraki 2–6 saatte ≈160/100'e",4,15,"n2","Doğru. Hedef organ hasarı varsa kontrollü IV tedavi; hızlı ve aşırı düşüş iskemiye yol açar."),
   A("Dil altı nifedipin ver",-4,10,"n9","SL nifedipin öngörülemez ve ani düşüşle inme/MI'ye yol açabilir; kullanılmamalıdır."),
   A("Oral ilaçlarını yeniden başla, taburcu et",-4,20,"n9","Hedef organ hasarı (retinopati, böbrek, TMA) olan hasta hipertansif acildir; yatış ve IV tedavi gerekir."),
 ]),
 "n2":N("1 saat sonra","Labetalol infüzyonu ile KB düşüyor. Hemşire “normale indirelim mi?” diye soruyor.","KB 182/112",[
   A("Kademeli devam: 2–6 saatte ≈160/100, sonraki 24–48 saatte normale; nefroloji ile izlem",3,20,"n3","Doğru. Otoregülasyonu yüksek basınca uyum sağlamış dokularda hızlı normalizasyon iskemiye neden olur."),
   A("Hemen 120/80'e indir",-3,20,"n8","Aşırı hızlı düşüş serebral/renal iskemi riskini artırır."),
 ]),
 "n3":E("İyi sonuç","Kontrollü düşüşle 48 saatte oral tedaviye geçildi; kreatinin 1,8'e indi, TMA bulguları geriledi.\n\n**Akılda kalsın**\n- **Hipertansif acil** = ciddi KB yüksekliği + **akut hedef organ hasarı** (ensefalopati, retinopati, böbrek, TMA, AKS, akciğer ödemi, diseksiyon, eklampsi).\n- **Hipertansif urgency** (hasar yok): oral tedavi, 24–48 saatte düşür; IV gerekmez.\n- Acilde: titre edilebilir IV ajan, ilk saatte OAB **en çok %25** düşüş (diseksiyon, eklampsi ve AKS özel hedefleri hariç).\n- **SL nifedipin kullanma**.\n\n*Kaynak: ESC/ESH 2018–2023; ESC 2019 hipertansif acil pozisyon makalesi.*","good"),
 "n8":E("Aşırı düşüş — iskemi","KB 2 saatte 120/70'e indi; hasta konfüzyon ve oligüri geliştirdi.\n\nHipertansif acilde hedef kontrollü ve kademeli düşüştür.","mid"),
 "n9":E("Komplikasyon","Hasta ani KB düşüşüyle iskemik inme geçirdi / taburculuk sonrası akut böbrek yetmezliğiyle döndü.\n\nHedef organ hasarı arayın; acilde kontrollü IV tedavi.","bad"),
}))
Qs+=[Q("c17q1","Hipertansif acil ile hipertansif urgency'yi ayıran temel özellik hangisidir?",["KB değerinin 200'ün üzerinde olması","Baş ağrısı","Akut hedef organ hasarının varlığı","Yaş","İlaç uyumsuzluğu"],2,"Ayrım KB değerine değil, akut hedef organ hasarına dayanır.","Kardiyoloji"),
 Q("c17q2","Hipertansif acilde (diseksiyon ve eklampsi dışı) ilk saatteki düşüş hedefi hangisidir?",["Ortalama arter basıncını en çok %25 düşürmek","Hemen 120/80'e indirmek","%50 düşürmek","Hiç düşürmemek","24 saat beklemek"],0,"İlk saatte OAB'de ≤%25 azalma, ardından 2–6 saatte 160/100–110.","Kardiyoloji"),
 Q("c17q3","Hipertansif acilde hangi tedaviden kaçınılmalıdır?",["Labetalol IV","Nikardipin infüzyonu","Dil altı kısa etkili nifedipin","Esmolol","Nitrogliserin (akciğer ödeminde)"],2,"SL nifedipin kontrolsüz ve ani düşüş yapar.","Kardiyoloji")]

# 18 FEBRİL KONVÜLZİYON
S.append(case("c18","Ateşle nöbet — 18 aylık kız","Pediatri",
 "18 aylık kız çocuk. İki gündür burun akıntısı; bugün ateşi 39,5 °C'ye çıkmış. Evde 2 dakika süren, tüm vücutta kasılma ve ardından uyku hali olmuş. Aşıları tam. İlk kez nöbet geçiriyor.",
 {"n1":N("Çocuk acil","Çocuk uyanık, annesini tanıyor, oyuncakla oynuyor. Ense sertliği, fontanel bombeliği, peteşi yok. Burun akıntısı ve hiperemik farenks.","Nb 148 · SS 30 · SpO₂ %98 · Ateş 39,2",[
   T("Kapiller glukoz",1,1,"96 mg/dL.","Nöbet sonrası rutin."),
   T("Lomber ponksiyon",-3,40,"Normal BOS. Çocuk ve aile gereksiz girişim yaşadı.","Basit febril konvülziyonda, meningeal bulgusu olmayan, aşıları tam ve iyi görünen çocukta rutin LP önerilmez."),
   T("Beyin BT",-3,30,"Normal. Gereksiz radyasyon.","Basit febril nöbette görüntüleme ve EEG gerekmez."),
   A("Basit febril konvülziyon: ateş nedenini değerlendir, antipiretikle konforu sağla, aileyi bilgilendir ve eğit (nöbette yan yatırma, 5 dakikayı geçerse ambulans/bukkal midazolam); iyi görünüyorsa taburcu",4,20,"n2","Doğru. 6 ay–5 yaş, jeneralize, <15 dakika, 24 saatte tek nöbet = basit febril konvülziyon."),
   A("Antiepileptik (valproat) başla",-4,10,"n9","Basit febril konvülziyonda profilaktik antiepileptik önerilmez; yararından çok zararı vardır."),
 ]),
 "n2":E("İyi sonuç","Aile eğitildi; ateş düşürücülerin nöbet tekrarını önlemediği, amaçlarının çocuğu rahatlatmak olduğu anlatıldı. Kontrolde çocuk iyiydi.\n\n**Akılda kalsın**\n- **Basit febril nöbet**: 6 ay–5 yaş, jeneralize, **<15 dakika**, 24 saatte tek.\n- **Komplike**: fokal, >15 dk veya 24 saatte tekrar → daha ayrıntılı değerlendirme.\n- LP: meningeal bulgu, **<12 ay ve aşısı eksik**, önceden antibiyotik kullanımı.\n- Rutin kan, BT, EEG gerekmez.\n- **Antipiretik tekrarı önlemez**; profilaktik antiepileptik verilmez.\n- 5 dakikayı aşan nöbet: **bukkal midazolam 0,3 mg/kg** (en çok 10 mg) veya rektal diazepam 0,5 mg/kg.\n\n*Kaynak: AAP 2011 basit febril nöbet kılavuzu.*","good"),
 "n9":E("Gereksiz tedavi","Çocukta valproata bağlı karaciğer enzim yüksekliği gelişti; nöbet tekrar riskinde anlamlı fark olmadı.\n\nBasit febril nöbet iyi huyludur; aile eğitimi esastır.","bad"),
}))
Qs+=[Q("c18q1","Hangisi basit febril konvülziyon tanımına uymaz?",["Jeneralize nöbet","3 dakika sürmesi","2 yaşında olması","Aynı gün içinde ikinci nöbet","Ateşle birlikte olması"],3,"24 saat içinde tekrarlama komplike febril nöbet özelliğidir.","Pediatri"),
 Q("c18q2","Basit febril konvülziyonda antipiretik kullanımıyla ilgili doğru ifade hangisidir?",["Nöbet tekrarını önler","Konfor içindir; tekrarı önlemez","Kontrendikedir","Yalnız rektal verilmelidir","Mutlaka dönüşümlü kullanılmalıdır"],1,"Antipiretikler febril nöbet tekrarını önlemez.","Pediatri"),
 Q("c18q3","5 dakikayı aşan nöbet geçiren 15 kg çocukta bukkal midazolam dozu yaklaşık ne kadardır?",["0,5 mg","1,5 mg","4,5 mg","15 mg","30 mg"],2,"Bukkal midazolam 0,3 mg/kg (en çok 10 mg) → 15 kg için 4,5 mg.","Pediatri")]

# 19 AORT DİSEKSİYONU
S.append(case("c19","Sırta vuran göğüs ağrısı — 63 yaşında erkek","Kardiyovasküler cerrahi",
 "63 yaşında erkek, kontrolsüz hipertansiyon. 30 dakika önce aniden başlayan, “yırtılır gibi”, sırta (kürek kemikleri arasına) vuran şiddetli göğüs ağrısı.",
 {"n1":N("Resüsitasyon alanı","Terli, huzursuz. Diyastolik üfürüm duyuluyor. Sol radial nabız zayıf.","KB sağ kol 182/98 · sol kol 138/80 · Nb 104 · SpO₂ %96",[
   T("12 derivasyonlu EKG",2,5,"Sol ventrikül hipertrofisi; ST elevasyonu yok.","Diseksiyon koroner ostiumu tutarsa (çoğunlukla sağ koroner) inferior STEMI taklit edebilir."),
   T("Yatak başı eko (POCUS)",2,5,"Aort kökü 4,6 cm, kökte flap şüphesi; az perikardiyal sıvı.","Tip A diseksiyonu ve tamponadı düşündürür."),
   T("BT anjiyografi (toraks-abdomen)",3,30,"**Stanford tip A diseksiyon**: çıkan aorttan başlayıp abdominal aorta uzanan flap.","ADD-RS yüksek riskte doğrudan BTA."),
   A("ASA 300 mg + tikagrelor + heparin — STEMI/AKS protokolü",-5,10,"n9","Diseksiyonda antitrombotikler ölümcül kanamaya yol açar. Yüksek riskli özellikler (yırtılır ağrı, nabız/KB farkı, yeni üfürüm) varken önce diseksiyon dışlanmalı."),
   A("Opioid analjezi; IV beta bloker (esmolol veya labetalol) ile önce nabız <60/dk, ardından gerekirse vazodilatörle sistolik KB 100–120 mmHg; acil kalp-damar cerrahisi",4,15,"n2","Doğru. Beta blokaj vazodilatörden önce gelir (refleks taşikardi aortik duvar stresini artırır)."),
   A("Önce nitroprussid ile KB'yi hızla düşür",-2,10,"n2","Beta blokaj olmadan vazodilatör refleks taşikardi yapar; sıralama: önce beta bloker."),
 ]),
 "n2":E("Acil cerrahi","Tip A diseksiyon tanısıyla hasta 90 dakikada ameliyata alındı; çıkan aort ve kök replasmanı yapıldı.\n\n**Akılda kalsın**\n- **Ani, yırtılır/bıçak gibi, sırta yayılan** ağrı; nabız/KB farkı; yeni AY üfürümü; nörolojik bulgu.\n- **ADD-RS** ile risk; yüksek riskte doğrudan **BTA**. D-dimer yalnız düşük riskte dışlamada yardımcı.\n- **Önce beta bloker** (nabız <60), sonra vazodilatör; sistolik **100–120 mmHg**; ağrı kontrolü.\n- **Antitrombotik verme.**\n- **Tip A → acil cerrahi**; komplikasyonsuz tip B → medikal/endovasküler.\n\n*Kaynak: ESC 2024 Periferik arter ve aort hastalıkları kılavuzu; ACC/AHA 2022 aort kılavuzu.*","good"),
 "n9":E("Ölümcül komplikasyon","Antitrombotik sonrası perikardiyal tamponad ve aort rüptürü gelişti; hasta kaybedildi.\n\nGöğüs ağrısında diseksiyon kırmızı bayrakları atlanmamalı.","bad"),
}))
Qs+=[Q("c19q1","Akut aort diseksiyonunda ilk ilaç tedavisi hedefi hangisidir?",["Nitroprussid ile hızlı KB düşüşü","Beta bloker ile nabız <60/dk, ardından sistolik 100–120 mmHg","Sıvı yüklemesi","Antiplatelet","Heparin infüzyonu"],1,"Önce beta blokaj (dP/dt'yi azaltır), sonra gerekirse vazodilatör.","Kardiyovasküler cerrahi"),
 Q("c19q2","Stanford tip A aort diseksiyonunun tedavisi hangisidir?",["Yalnız medikal tedavi","Acil cerrahi","Tromboliz","Elektif endovasküler tamir (aylar sonra)","Antikoagülasyon"],1,"Çıkan aortu tutan diseksiyon acil cerrahi gerektirir.","Kardiyovasküler cerrahi"),
 Q("c19q3","Aort diseksiyonunu düşündüren muayene bulgusu hangisidir?",["İki kol arasında >20 mmHg sistolik KB farkı","Bilateral wheezing","Sağ alt kadran hassasiyeti","Ense sertliği","Murphy bulgusu"],0,"Nabız defisiti ve kollar arası KB farkı diseksiyon için kırmızı bayraktır.","Kardiyovasküler cerrahi")]

# 20 PARASETAMOL İNTOKSİKASYONU
S.append(case("c20","İlaç alımı — 22 yaşında kadın","Toksikoloji",
 "22 yaşında kadın, yaklaşık 60 kg. Erkek arkadaşıyla tartıştıktan sonra 4 saat önce 30 adet parasetamol 500 mg (15 g) içtiğini söylüyor. Başka ilaç ve alkol almadığını belirtiyor. Bulantısı var, başka yakınması yok.",
 {"n1":N("Muayene odası","Bilinç açık, ajite değil. Karın muayenesi normal. Ağlıyor.","KB 118/72 · Nb 96 · SpO₂ %99",[
   T("Alınan doz hesabı",2,2,"15 g / 60 kg = **250 mg/kg**.","≥150 mg/kg (bazı kılavuzlarda ≥75 mg/kg tek doz eşik) potansiyel toksik doz."),
   T("4. saat serum parasetamol düzeyi",3,30,"**210 mg/L** (μg/mL). Nomogramda tedavi çizgisinin üzerinde.","Düzey alımdan **en erken 4 saat** sonra yorumlanır; 4 saatten önceki düzey nomograma uygulanmaz."),
   T("AST/ALT, INR, kreatinin, glukoz, kan gazı",1,40,"ALT 24, INR 1,0, kreatinin 0,7.","Bazal değerler; ilk saatlerde normal olması güvenlik göstergesi değildir."),
   T("Diğer ilaç düzeyleri (salisilat vb.)",1,40,"Salisilat negatif.","Kasıtlı alımlarda eşlik eden ilaç taraması önerilir."),
   A("N-asetilsistein (NAC) başla — örneğin 21 saatlik protokol: 150 mg/kg 1 saatte, 50 mg/kg 4 saatte, 100 mg/kg 16 saatte; psikiyatri konsültasyonu, gözetim",4,15,"n2","Doğru. Düzey tedavi çizgisinin üzerinde; NAC ilk 8 saatte başlanırsa karaciğer hasarı neredeyse tamamen önlenir."),
   A("Aktif kömür ver ve taburcu et; ilaç düzeyi önemli değil",-5,30,"n9","4 saat geçtiği için kömürün yararı sınırlı; toksik düzeyde NAC şarttır."),
   A("Karaciğer enzimleri normal — taburcu et",-5,10,"n9","Parasetamolde hepatotoksisite 24–72 saatte ortaya çıkar; erken enzimler normaldir."),
 ]),
 "n2":N("NAC'ın ilk saati","Hasta kaşıntı ve yüzde kızarıklık tarifliyor; hafif wheezing.","KB 112/70 · Nb 104 · SpO₂ %97",[
   A("Anafilaktoid reaksiyon: infüzyonu durdur, antihistaminik (± salbutamol), belirtiler geçince infüzyonu daha yavaş hızla yeniden başlat",3,20,"n3","Doğru. NAC reaksiyonu histamin aracılıdır, çoğunlukla ilk torbadadır; NAC kesin kontrendikasyon değildir."),
   A("NAC'a alerji var — tedaviyi tamamen kes",-4,10,"n9","NAC yaşam kurtarıcıdır; anafilaktoid reaksiyonda kısa ara ve yavaş yeniden başlama yeterlidir."),
 ]),
 "n3":E("İyi sonuç","NAC tamamlandı; 21. saatte ALT 30, INR 1,0, parasetamol saptanmadı. Psikiyatri değerlendirmesinden sonra güvenli taburculuk planlandı.\n\n**Akılda kalsın**\n- Doz hesabı (mg/kg) ve **alım zamanı** kritik.\n- Düzey **≥4. saatte**; nomograma göre NAC (zaman bilinmiyor, çoklu/yayılı alım veya >8 saat geçtiyse düzey beklenmeden NAC başlanır).\n- **NAC ilk 8 saatte** başlanırsa hepatotoksisite en aza iner.\n- Erken enzimler normaldir — güven verme.\n- NAC reaksiyonu: durdur, antihistaminik, yavaş yeniden başla.\n- Her kasıtlı alımda **psikiyatri** değerlendirmesi ve güvenlik planı.\n\n*Kaynak: UK MHRA/TOXBASE parasetamol önerileri; Rumack-Matthew nomogramı; ACMT 2023 uzlaşı.*","good"),
 "n9":E("Akut karaciğer yetmezliği","Hasta 3. günde sarılık, ensefalopati ve INR 6 ile getirildi; karaciğer nakli merkezine sevk edildi.\n\nParasetamol zehirlenmesinde zamanında NAC hayat kurtarır.","bad"),
}))
Qs+=[Q("c20q1","Parasetamol düzeyi nomograma göre değerlendirilirken en erken hangi saatte alınmalıdır?",["1. saat","2. saat","4. saat","12. saat","24. saat"],2,"4 saatten önce emilim tamamlanmadığından düzey nomograma uygulanmaz.","Toksikoloji"),
 Q("c20q2","NAC tedavisi en yüksek koruyuculuğu hangi süre içinde başlandığında sağlar?",["İlk 8 saat","İlk 24 saat","48 saat","72 saat","Süre önemli değil"],0,"İlk 8 saatte başlanan NAC hepatotoksisiteyi büyük oranda önler; geç başlandığında da yarar sağlar.","Toksikoloji"),
 Q("c20q3","NAC infüzyonu sırasında kaşıntı ve yüzde kızarıklık gelişirse ne yapılır?",["Tedavi tamamen kesilir","Adrenalin IM verilir ve NAC asla tekrar verilmez","İnfüzyon durdurulur, antihistaminik verilir, yavaşça yeniden başlanır","Doz iki katına çıkarılır","Hemodiyaliz yapılır"],2,"Anafilaktoid reaksiyon histamin aracılıdır; NAC yaşam kurtarıcı olduğundan yeniden başlanır.","Toksikoloji")]

P={"id":"ilk-nobet-2","title":"İlk Nöbet Vakaları — 2. Paket","desc":"Senkop, status epileptikus, CO zehirlenmesi, apandisit, menenjit, üst GİS kanama, hipertansif acil, febril konvülziyon, aort diseksiyonu, parasetamol zehirlenmesi.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 2. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 2. Paket","topic":"Temel acil","order":2,"req":[1],
     "desc":"İlk nöbet döneminin sık ve ölümcül 10 tablosu. Her vakada önce kendi kararınızı verin, sonra farklı yolları deneyin.",
     "intro":"- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."}}
build(P,sys.argv[1])
