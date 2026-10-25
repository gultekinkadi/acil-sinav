import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Önce **ilk değerlendirme** (muayene, monitör, damar yolu, oksijen) — gereksiz girişim puan kaybettirir.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 131 MİGREN
S.append(case("c131","Tanıdık baş ağrısı, geçmiyor — 31 yaşında kadın","Nöroloji",
 "31 yaşında kadın. Yıllardır migren tanısı var; atakları bu kez de aynı tarzda: sol zonklayıcı ağrı, bulantı, ışık-ses hassasiyeti. 30 saattir sürüyor; evde iki kez triptan ve ibuprofen almış, kusmuş. Gebe değil.",
 {"n1":N("Muayene","Karanlık köşeyi tercih ediyor. Ateş yok, ense sertliği yok, **nörolojik muayene ve fundus normal**.","KB 128/80 · Nb 92 · SS 16 · SpO₂ %99 · Ateş 36,7",[
   T("Kırmızı bayrak sorgusu (SNOOP)",2,3,"Ani başlangıç yok, alışıldık atak paterni, ateş/immünsüpresyon yok, yeni nörolojik bulgu yok, 50 yaş altı, gebelik/lohusalık yok.","Kırmızı bayrak yoksa görüntüleme gerekmez."),
   T("Beyin BT",-2,30,"Normal.","Tipik migrende gereksiz radyasyon ve zaman kaybı."),
   A("Hidrasyon; **metoklopramid 10 mg IV** (ya da proklorperazin) + **NSAİİ** (ör. ketorolak 15–30 mg IV / deksketoprofen); tekrarlamayı azaltmak için **deksametazon 10 mg IV**; **opioid verme**",4,20,"n2","Doğru. AHS 2016 acil servis önerileri."),
   A("Morfin 5 mg IV",-3,10,"n9","Opioidler migrende daha az etkili, tekrar başvuru ve medikasyon aşırı kullanımı baş ağrısı riski."),
   A("Üçüncü triptan dozu",-2,10,"n9","24 saatte doz sınırı aşılır; zaten yanıtsız."),
 ]),
 "n2":E("Düzelme","Bir saat içinde ağrı 2/10'a indi; bulantı geçti. Profilaksi için nöroloji polikliniğine yönlendirildi.\n\n**Akılda kalsın**\n- Önce **kırmızı bayraklar** (SNOOP4): sistemik bulgu, nörolojik bulgu, ani başlangıç, >50 yaş, patern değişikliği, pozisyonel, Valsalva ile tetiklenme, papil ödemi, gebelik.\n- Acil tedavi: **dopamin antagonisti (metoklopramid/proklorperazin) + NSAİİ**, sıvı; **deksametazon** tekrarı azaltır.\n- **Opioid ve butalbitalden kaçın**.\n- Status migrenozus (>72 saat) ve sık atakta profilaksi.\n\n*Kaynak: American Headache Society 2016 acil servis migren kılavuzu.*","good"),
 "n9":E("Tekrar başvuru","Ağrı kısmen geçti; hasta ertesi gün yine başvurdu.","bad"),
}))
Qs+=[Q("c131q1","Acil serviste migren atağında birinci basamak IV tedavi hangisidir?",["Morfin","Metoklopramid/proklorperazin + NSAİİ","Diazepam","Fenitoin","Antibiyotik"],1,"AHS 2016.","Nöroloji"),
 Q("c131q2","Migrende tekrar başvuruyu azaltan ilaç hangisidir?",["Deksametazon","Morfin","Kodein","Parasetamol","Kafein"],0,"Tek doz 10 mg IV.","Nöroloji"),
 Q("c131q3","Hangisi baş ağrısında kırmızı bayrak değildir?",["Ani başlangıçlı en şiddetli ağrı","Yeni nörolojik bulgu","Yıllardır aynı paternde tekrarlayan ağrı","Ateş ve ense sertliği","50 yaşından sonra yeni başlangıç"],2,"Alışıldık paterni destekler.","Nöroloji")]

# 132 FASİYAL PARALİZİ — Bell
S.append(case("c132","Yüzünün bir tarafı kaydı — 45 yaşında erkek","Nöroloji / KBB",
 "45 yaşında erkek. Dün akşam kulak arkasında hafif ağrı; bu sabah aynada ağzının sağa kaydığını, sol gözünü kapatamadığını fark etmiş. Başka yakınması yok.",
 {"n1":N("Muayene","Sol yüzün **alın dahil** tüm yarısında güçsüzlük (kaş kaldıramıyor, göz tam kapanmıyor, Bell fenomeni +). Kulak kepçesi ve dış kulak yolunda **vezikül yok**, kulak zarı normal. Diğer kraniyal sinirler ve ekstremiteler normal.","KB 132/84 · Nb 76 · SpO₂ %99 · Ateş 36,6",[
   T("Alın tutulumunun değerlendirilmesi",2,2,"Alın tutulmuş → **periferik** (alt motor nöron) paralizi.","Merkezi (inme) paralizide alın korunur (bilateral kortikal innervasyon)."),
   T("Beyin BT",-2,30,"Normal.","Tipik izole periferik paralizide görüntüleme gerekmez."),
   A("**Bell paralizisi**: ilk 72 saatte **prednizolon** (ör. 50 mg/gün 10 gün ya da 60 mg/gün 5 gün + azaltma); **göz koruması** (gündüz suni gözyaşı, gece jel ve göz bandı); 3 haftada iyileşme yoksa nöroloji/KBB",4,10,"n2","Doğru. Steroid erken verildiğinde tam iyileşme oranını artırır."),
   A("Yalnız asiklovir",-2,10,"n9","Antiviral tek başına etkisiz; steroid eksik."),
   A("İnme protokolü — tromboliz için nöroloji",-3,20,"n9","Alın tutulmuş, izole periferik paralizi; inme değil."),
 ]),
 "n2":E("İyileşme","Steroid ve göz bakımıyla 6 haftada tam iyileşti.\n\n**Akılda kalsın**\n- **Alın tutulumu = periferik**; alın korunuyorsa merkezi neden (inme) düşün.\n- **Ramsay Hunt** (kulakta vezikül, ağrı, işitme kaybı/vertigo) → **steroid + antiviral**.\n- Bell: **72 saat içinde prednizolon**; antiviral tek başına önerilmez (ağır olguda eklenebilir).\n- **Kornea koruması** şart.\n- Bilateral, tekrarlayan, ilerleyici paralizi veya diğer kraniyal sinir bulgusunda ileri tetkik.\n\n*Kaynak: AAO-HNS 2013 Bell paralizisi kılavuzu; Cochrane 2016.*","good"),
 "n9":E("Kötü sonuç","Steroid verilmedi; göz korunmadı. Kornea abrazyonu gelişti ve iyileşme eksik kaldı (sinkinezi).","bad"),
}))
Qs+=[Q("c132q1","Periferik fasiyal paraliziyi merkezi paraliziden ayıran bulgu hangisidir?",["Ağız köşesinde düşme","Alın tutulumu","Nazolabial silinme","Disfaji","Dizartri"],1,"Merkezi lezyonda alın korunur.","Nöroloji / KBB"),
 Q("c132q2","Bell paralizisinde ilk 72 saatte önerilen tedavi hangisidir?",["Yalnız asiklovir","Oral kortikosteroid","Antibiyotik","Aspirin","Fizik tedavi tek başına"],1,"Prednizolon.","Nöroloji / KBB"),
 Q("c132q3","Kulakta veziküller ve fasiyal paralizi hangi tanıyı düşündürür?",["Bell","Ramsay Hunt sendromu","Otitis eksterna","Menière","Kolesteatom"],1,"VZV reaktivasyonu: steroid + antiviral.","Nöroloji / KBB")]

# 133 SUBARAKNOİD KANAMA — >6 saat, BT negatif
S.append(case("c133","Ani başlayan en şiddetli baş ağrısı — 44 yaşında kadın","Nöroloji",
 "44 yaşında kadın. Dün gece 23:00'te spor salonunda ağırlık kaldırırken ani başlayan, “hayatının en şiddetli” baş ağrısı; 1 kez kustu. Sabah 08:00'de acile geldi. Bilinç açık.",
 {"n1":N("Muayene","GKS 15, hafif ense sertliği, fokal nörolojik bulgu yok.","KB 158/92 · Nb 84 · SS 16 · SpO₂ %98 · Ateş 36,9",[
   T("Ottawa SAK kuralı",1,2,"Ani en şiddetli ağrı, eforla başlangıç, ense sertliği → **SAK dışlanamaz**.","Duyarlılığı yüksek bir karar kuralı."),
   T("Kontrastsız beyin BT",3,20,"**Normal** (başlangıçtan ≈9 saat sonra).","İlk 6 saatte yapılan modern BT çok duyarlıdır; 6 saatten sonra duyarlılık düşer."),
   A("BT >6 saatte normal: **lomber ponksiyon** (başlangıçtan ≥12 saat sonra; ksantokromi, eritrosit sayısı) ya da **BT anjiyografi**",4,30,"n2","Doğru. 6 saatten sonra BT negatifliği SAK'ı dışlamaz."),
   A("BT normal — migren tedavisi ve taburcu",-5,10,"n9","Uyarıcı (sentinel) kanama kaçırıldı."),
 ]),
 "n2":N("LP / BTA","Saat 11:00'de LP: 4 tüpte de eritrosit ≈2.000/mm³ (azalmıyor), **ksantokromi pozitif**. BTA: **sol posterior komünikan arter anevrizması (6 mm)**.","KB 162/94 · Nb 80",[
   A("Anevrizmal SAK: nöroşirürji/girişimsel nöroradyoloji (anevrizmanın erken güvenceye alınması); **nimodipin 60 mg oral 4 saatte bir** (21 gün); sistolik KB **<160** (titre edilebilir ajan); analjezi, antiemetik, nöbet ve hidrosefali izlemi; antikoagülan/antiagregan yok",4,20,"n3","Doğru."),
   A("Nimodipin 2 mg/saat IV yüksek doz ve KB'yi 110'a düşür",-2,15,"n4","Agresif hipotansiyon serebral perfüzyonu bozar."),
 ]),
 "n3":E("Anevrizma güvencede","Ertesi gün anevrizma endovasküler olarak sarıldı (coil); vazospazm gelişmedi, hasta nörolojik defisitsiz taburcu oldu.\n\n**Akılda kalsın**\n- Ani, en şiddetli baş ağrısı (thunderclap): **SAK dışlanana kadar SAK**.\n- **BT ≤6 saat** ve normal → SAK büyük ölçüde dışlanır (deneyimli yorum). **>6 saat** → **LP (≥12 saat, ksantokromi)** ya da **BTA**.\n- Tedavi: anevrizmayı **erken güvenceye al**, **nimodipin 60 mg/4 saat**, KB sistolik <160, yeniden kanama/hidrosefali/nöbet/hiponatremi izlemi.\n\n*Kaynak: AHA/ASA 2023 aSAK kılavuzu; Perry ve ark., BMJ 2011 ve JAMA 2013.*","good"),
 "n4":E("İskemik komplikasyon","Hipotansiyon sonrası sol hemiparezi gelişti; anevrizma sarıldı, kısmi defisitle taburcu oldu.","mid"),
 "n9":E("Yeniden kanama","Hasta 2 gün sonra koma ile geldi; anevrizma yeniden kanamıştı.","bad"),
}))
Qs+=[Q("c133q1","Başlangıçtan 9 saat sonra çekilen BT'si normal olan thunderclap baş ağrısında sonraki adım hangisidir?",["Taburcu","LP (≥12 saat) veya BT anjiyografi","EEG","MR yalnız 1 hafta sonra","Triptan"],1,"6 saatten sonra BT duyarlılığı azalır.","Nöroloji"),
 Q("c133q2","Anevrizmal SAK'ta vazospazm/iskemiyi azaltan ilaç ve dozu hangisidir?",["Nimodipin 60 mg oral 4 saatte bir","Nifedipin 10 mg","Amlodipin 10 mg","Verapamil 5 mg IV","Diltiazem infüzyonu"],0,"21 gün.","Nöroloji"),
 Q("c133q3","LP'de SAK lehine bulgu hangisidir?",["Tüplerde azalan eritrosit","Ksantokromi","Düşük protein","Lenfositoz","Düşük açılış basıncı"],1,"Hemoglobin yıkımı; ≥12 saatte belirgin.","Nöroloji")]

# 134 HİPONATREMİ — aşırı düzeltme riski
S.append(case("c134","Kusma ve halsizlik — 73 yaşında kadın","Metabolik",
 "73 yaşında kadın. Hipertansiyon için hidroklorotiyazid kullanıyor. 4 gündür kusma-ishal, ağızdan az alım. Bugün halsiz, biraz dalgın. Nöbet yok. Yaklaşık 60 kg.",
 {"n1":N("Muayene","Uykuya meyilli ama oryante, bulantılı. Mukozalar kuru, ortostatik KB düşüşü.","KB 98/58 · Nb 104 · SS 16 · SpO₂ %97 · Kapiller glukoz 104",[
   T("Na, K, osmolalite; idrar Na ve osmolalite",3,40,"**Na 116**, K 3,1; serum osm 244. İdrar Na 18, idrar osm 480.","Hipovolemik hipotonik hiponatremi (tiyazid + GİS kaybı); kronik (>48 saat)."),
   A("**Orta derecede semptomlu kronik hiponatremi**: tiyazidi kes; hipovolemiyi **izotonik SF** ile dikkatli düzelt + K replasmanı (K da Na'yı yükseltir); **24 saatte en çok 8–10 mmol/L** artış hedefi (ODS riski: hipokalemi, yaşlı); **2–4 saatte bir Na**, idrar çıkışı izlemi",4,20,"n2","Doğru."),
   A("%3 NaCl 150 mL bolus × 3",-3,20,"n3","Ağır semptom (nöbet, koma) yok; tekrarlayan hipertonik bolus aşırı düzeltmeye yol açar."),
   A("Hızlıca 3 L SF",-2,30,"n3","Volüm düzelince ADH baskılanır, su diürezi başlar → hızlı düzelme."),
 ]),
 "n2":N("6 saat sonra","1,5 L SF sonrası idrar çıkışı **400 mL/saat**, dilüe idrar (osm 90). Na **116 → 124** (6 saatte +8).","KB 122/70 · Nb 84",[
   A("**Aşırı düzeltme riski**: düzeltmeyi durdur — **desmopressin 2 mcg IV** (6–8 saatte bir) ve gerekirse **%5 dekstroz** ile Na'yı hedefe çek; saatlik Na izlemi",4,10,"n4","Doğru. Su diürezi saatler içinde limiti aşacaktı."),
   A("SF'ye devam et, sabah Na bak",-4,60,"n9","Gece boyunca Na 136'ya çıkar (+20/24 saat) → ozmotik demiyelinizasyon riski."),
 ]),
 "n3":N("Aşırı düzeltme","Na 4 saatte 116'dan 128'e çıktı (+12).","KB 118/72",[
   A("Desmopressin 2 mcg IV + %5 dekstroz ile Na'yı yeniden düşür (relowering)",2,20,"n5","Kurtarıcı adım."),
   A("İzle",-4,30,"n9","ODS riski."),
 ]),
 "n4":E("Güvenli düzelme","24 saatte Na 124'e, 48 saatte 131'e çıktı; nörolojik komplikasyon olmadı.\n\n**Akılda kalsın**\n- Kronik hiponatremide limit: **24 saatte ≤10 mmol/L** (yüksek ODS riskinde **≤8**): alkolizm, malnütrisyon, **hipokalemi**, siroz, Na ≤105.\n- **Hipovolemi düzelince ADH kapanır → su diürezi → hızlı Na artışı**: idrar çıkışı >100 mL/saat ise alarm.\n- Önlem/kurtarma: **desmopressin** (clamp) ± **%5 dekstroz**.\n- Ağır semptomda (nöbet, koma): **%3 NaCl 150 mL** (20 dk), 4–6 mmol/L artışa kadar tekrar.\n\n*Kaynak: ESE/ESICM/ERA-EDTA 2014 hiponatremi kılavuzu; ABD uzman paneli 2013.*","good"),
 "n5":E("Sınırda kurtarma","Na yeniden düşürüldü; hasta yakından izlendi, nörolojik bulgu gelişmedi.","mid"),
 "n9":E("Ozmotik demiyelinizasyon","Bir hafta sonra dizartri, disfaji ve kuadriparezi gelişti (ozmotik demiyelinizasyon sendromu).","bad"),
}))
Qs+=[Q("c134q1","Kronik hiponatremide 24 saatlik düzeltme sınırı yaklaşık nedir?",["≤10 mmol/L (yüksek riskte ≤8)","≤20 mmol/L","≤30 mmol/L","Sınır yok","≤2 mmol/L"],0,"ODS'yi önlemek için.","Metabolik"),
 Q("c134q2","Hipovolemik hiponatremide volüm replasmanından sonra hızlı Na artışının nedeni nedir?",["ADH baskılanması ve su diürezi","Aldosteron artışı","Hiperglisemi","Böbrek yetmezliği","Hipotiroidi"],0,"İdrar çıkışı artar, idrar dilüe olur.","Metabolik"),
 Q("c134q3","Aşırı hızlı Na düzelmesinde kullanılan ilaç hangisidir?",["Desmopressin","Tolvaptan","Furosemid","Fludrokortizon","Hidroklorotiyazid"],0,"%5 dekstrozla birlikte.","Metabolik")]

# 135 AKUT APANDİSİT — gebe
S.append(case("c135","Gebede karın ağrısı — 29 yaşında kadın, 22 haftalık","Genel cerrahi / Kadın doğum",
 "29 yaşında, 22 haftalık gebe. 18 saattir göbek çevresinde başlayıp sağ yana yerleşen ağrı, iştahsızlık, bir kez kusma. Vajinal kanama ya da sıvı gelmesi yok.",
 {"n1":N("Muayene","Sağ alt-orta kadranda (göbeğin biraz altında, lateralde) hassasiyet ve istemsiz defans. Uterus gebelik haftasıyla uyumlu, hassas değil.","KB 112/68 · Nb 108 · SS 18 · SpO₂ %98 · Ateş 38,0",[
   T("Fetal kalp sesi / obstetrik değerlendirme",2,10,"FKS 148/dk, kasılma yok.","Gebelikte cerrahi aciller kadın doğumla birlikte."),
   T("Graded kompresyon USG",2,30,"Apendiks net görüntülenemedi; serbest sıvı yok.","İlk tercih; sıklıkla tanısız."),
   T("Kontrastsız MR (abdomen)",3,60,"**Apendiks 10 mm, duvar kalın, periapendiküler ödem** — akut apandisit.","USG tanısızsa MR; gadolinyum kullanılmaz."),
   T("Lökosit ve CRP",1,30,"Lökosit 15.800, CRP 64.","Gebelikte lökosit fizyolojik olarak yüksek olabilir — tek başına tanı koydurmaz."),
   A("**Gebede akut apandisit**: genel cerrahi + kadın doğum; aç bırak, IV sıvı, analjezi (parasetamol/opioid; NSAİİ'den kaçın), **sol lateral eğik pozisyon**; preoperatif antibiyotik; **laparoskopik apendektomi gecikmeden**; fetal izlem",4,20,"n2","Doğru. Gecikme perforasyonu, perforasyon da fetal kaybı belirgin artırır."),
   A("Gebelikte cerrahiden kaçın — antibiyotikle izle",-4,30,"n9","Gebelikte konservatif tedavinin başarısızlık ve perforasyon riski yüksektir; standart cerrahidir."),
   A("Radyasyon nedeniyle görüntüleme yapma, 24 saat gözlem",-4,30,"n9","Gecikme perforasyona yol açar; MR güvenlidir, gerekirse düşük doz BT bile kabul edilebilir."),
 ]),
 "n2":E("Ameliyat","Laparoskopik apendektomi yapıldı (perforasyonsuz); gebelik sorunsuz sürdü.\n\n**Akılda kalsın**\n- Gebelikte apendiks **yukarı-laterale** yer değiştirir; ağrı yeri değişebilir.\n- Görüntüleme: **USG → (tanısızsa) kontrastsız MR**; MR yoksa BT bekletilmez.\n- Lökositoz gebelikte normal olabilir.\n- **Gecikmeden cerrahi** (laparoskopi güvenli); perforasyonda fetal kayıp belirgin artar.\n- Sol lateral eğik pozisyon (aortokaval bası), NSAİİ'den kaçın.\n\n*Kaynak: WSES 2020 akut apandisit kılavuzu; ACOG 2017 gebelikte görüntüleme.*","good"),
 "n9":E("Perforasyon","Apendiks perfore oldu; peritonit ve erken doğum eylemi gelişti.","bad"),
}))
Qs+=[Q("c135q1","Gebede apandisit şüphesinde USG tanısızsa tercih edilen görüntüleme hangisidir?",["Kontrastlı BT","Kontrastsız MR","Direkt grafi","Sintigrafi","PET"],1,"Gadolinyum kullanılmaz.","Genel cerrahi / Kadın doğum"),
 Q("c135q2","Gebede akut apandisitte standart tedavi hangisidir?",["Yalnız antibiyotik","Gecikmeden apendektomi (laparoskopik olabilir)","Doğuma kadar izlem","Steroid","Tokoliz tek başına"],1,"Perforasyon fetal kaybı artırır.","Genel cerrahi / Kadın doğum"),
 Q("c135q3","Gebelikte apendiksin konumu nasıl değişir?",["Aşağı ve medial","Yukarı ve lateral","Değişmez","Sola kayar","Pelvise iner"],1,"Büyüyen uterus nedeniyle.","Genel cerrahi / Kadın doğum")]

# 136 SERVİKAL TRAVMA — yaşlıda odontoid
S.append(case("c136","Düşme sonrası boyun ağrısı — 83 yaşında kadın","Travma / Omurga",
 "83 yaşında kadın. Evde ayakta dururken geriye düşüp başını kapı çerçevesine çarptı. Boyun arkasında ağrı. AF nedeniyle apiksaban kullanıyor. Bilinç kaybı yok.",
 {"n1":N("Muayene","GKS 15. Alında ekimoz. Üst servikal orta hat hassasiyeti. Nörolojik defisit yok. Boyun hareketiyle ağrı.","KB 148/82 · Nb 88 (düzensiz) · SS 16 · SpO₂ %96",[
   T("Kanada Servikal Omurga Kuralı",2,2,"**Yaş ≥65 → yüksek risk** → görüntüleme gerekli (aktif rotasyon testine geçilmez).","NEXUS'ta da orta hat hassasiyeti pozitif."),
   T("Servikal BT",3,20,"**Tip II odontoid kırığı**, hafif posterior deplasman; kanal geniş.","Yaşlıda en sık servikal kırık."),
   T("Beyin BT",2,15,"Kanama yok.","Antikoagülanlı hastada kafa travmasında BT gerekli."),
   A("Servikal **boyunluk** (sert) + omurga önlemleri; **omurga cerrahisi/nöroşirürji**; analjezi (yaşlıda dikkatli, deliryum önlemi); antikoagülasyon planını ekip ile; düşme nedenini (senkop?) araştır",4,15,"n2","Doğru."),
   A("Düşük enerjili travma — klinik olarak temizle, boyunluğu çıkar",-5,10,"n9","CCR'de 65 yaş ve üzeri yüksek risk; klinik temizleme yapılmaz."),
 ]),
 "n2":E("Uygun tedavi","Omurga cerrahisi ile tartışılıp sert boyunlukla izlem kararı alındı; düşme değerlendirmesinde ortostatik hipotansiyon saptandı.\n\n**Akılda kalsın**\n- **Kanada C-omurga kuralı**: yüksek risk = **yaş ≥65**, tehlikeli mekanizma, ekstremitelerde parestezi → görüntüle.\n- **NEXUS**: orta hat hassasiyeti, fokal defisit, bilinç değişikliği, intoksikasyon, dikkat dağıtıcı yaralanma.\n- Yaşlıda **düşük enerjili düşme** bile **odontoid (C2)** kırığı yapar; görüntüleme **BT**.\n- Antikoagülanlıda **beyin BT** ve düşmenin nedeni.\n\n*Kaynak: Stiell ve ark., JAMA 2001/NEJM 2003; ATLS 10.*","good"),
 "n9":E("Nörolojik hasar","Boyunluk çıkarıldıktan sonra kırık deplase oldu; hasta kuadriparezi geliştirdi.","bad"),
}))
Qs+=[Q("c136q1","Kanada servikal omurga kuralında yüksek risk faktörü hangisidir?",["Yaş ≥65","Yaş <16","Kadın cinsiyet","Gece başvurusu","Orta hat hassasiyeti olmaması"],0,"Tehlikeli mekanizma ve parestezi de yüksek risktir.","Travma / Omurga"),
 Q("c136q2","Yaşlılarda en sık görülen servikal kırık hangisidir?",["C7 spinöz","Odontoid (C2)","C5 kompresyon","Atlas posterior arkı","T1"],1,"Düşük enerjili düşmede bile.","Travma / Omurga"),
 Q("c136q3","Görüntüleme gereken erişkin servikal travmada tercih edilen tetkik hangisidir?",["Direkt grafi","BT","USG","Fleksiyon-ekstansiyon grafisi","Sintigrafi"],1,"Duyarlılık yüksektir.","Travma / Omurga")]

# 137 İLEUS — adezyona bağlı ince barsak obstrüksiyonu
S.append(case("c137","Kusma ve karın şişliği — 58 yaşında erkek","Genel cerrahi",
 "58 yaşında erkek. 5 yıl önce kolon ameliyatı. 1 gündür kramp tarzı karın ağrısı, safralı kusma, gaz-gaita çıkaramıyor.",
 {"n1":N("Muayene","Karın distandü, timpanik; yaygın hafif hassasiyet, **defans/rebound yok**. Barsak sesleri metalik. Fıtık yok. Mukozalar kuru.","KB 118/70 · Nb 104 · SS 18 · SpO₂ %97 · Ateş 37,2",[
   T("Laktat, elektrolit, böbrek fonksiyonu",2,30,"Laktat 1,6; K 3,2; kreatinin 1,4.","Hipokalemi ve prerenal AKI."),
   T("Kontrastlı abdominal BT",3,40,"Dilate ince barsak anslarında **geçiş noktası** (adezyon); **iskemi bulgusu yok** (duvar kontrastlanması normal, serbest sıvı az, kapalı ans yok).","Strangülasyon bulgusu yok."),
   T("Direkt karın grafisi",1,15,"Dilate ince barsak, hava-sıvı seviyeleri.","BT daha bilgilendiricidir."),
   A("**Komplike olmayan adezyon ileusu**: aç bırak, **nazogastrik dekompresyon**, IV sıvı, **K replasmanı**, analjezi-antiemetik; genel cerrahi; **suda çözünür kontrast (gastrografin) testi**; strangülasyon belirtileri (ateş, taşikardi, peritonit, laktat ↑) için seri muayene",4,20,"n2","Doğru. Çoğu konservatif düzelir; kontrast testi tanısal ve tedavi edicidir."),
   A("Metoklopramid ve lavman, taburcu",-4,10,"n9","Mekanik obstrüksiyonda prokinetik kontrendike; hasta dehidrate."),
 ]),
 "n2":E("Konservatif düzelme","Gastrografin 24 saatte kolona geçti; gaz-gaita çıkışı başladı, hasta 3. günde beslenmeye geçti.\n\n**Akılda kalsın**\n- İnce barsak obstrüksiyonunun en sık nedeni **adezyon**, sonra **fıtık** (fıtık deliklerini mutlaka muayene et).\n- **BT**: geçiş noktası, **kapalı ans, iskemi** (azalmış duvar kontrastlanması, mezenter ödem, pnömatozis).\n- Strangülasyon (ateş, taşikardi, peritonit, lökositoz, laktat) → **acil cerrahi**.\n- Komplike değilse NG, sıvı, elektrolit, **suda çözünür kontrast** testi.\n\n*Kaynak: Bologna (WSES) 2017 adezyon ileusu kılavuzu.*","good"),
 "n9":E("Strangülasyon","Hasta 2 gün sonra peritonit ve şokla döndü; nekrotik barsak rezeksiyonu gerekti.","bad"),
}))
Qs+=[Q("c137q1","İnce barsak obstrüksiyonunun en sık nedeni hangisidir?",["Tümör","Adezyon","Volvulus","Safra taşı","Yabancı cisim"],1,"Geçirilmiş cerrahi öyküsü.","Genel cerrahi"),
 Q("c137q2","Adezyon ileusunda strangülasyonu düşündüren bulgu hangisidir?",["Ateş, taşikardi, peritonit, laktat artışı","Gaz çıkışı","Hafif distansiyon","Kusma","Hipokalemi"],0,"Acil cerrahi endikasyonu.","Genel cerrahi"),
 Q("c137q3","Komplike olmayan adezyon ileusunda tanısal ve tedavi edici test hangisidir?",["Baryum lavmanı","Suda çözünür (gastrografin) kontrast testi","Kolonoskopi","Laparotomi","Sintigrafi"],1,"24 saatte kolona geçerse konservatif başarı olasılığı yüksek.","Genel cerrahi")]

# 138 AORT ANEVRİZMASI — rüptür
S.append(case("c138","“Böbrek taşı” ve bayılma — 72 yaşında erkek","Vasküler cerrahi",
 "72 yaşında erkek, sigara içiyor. 2 saattir sol yan ve bel ağrısı; tuvalette bayılmış. Daha önce böbrek taşı geçirmemiş.",
 {"n1":N("Muayene","Solgun, terli, bilinç açık. Göbek üstünde **pulsatil kitle**; karın hafif hassas. Femoral nabızlar zayıf.","KB 84/52 · Nb 118 · SS 22 · SpO₂ %96",[
   T("Yatak başı aort USG (POCUS)",3,5,"**İnfrarenal aort çapı 7,2 cm**, retroperitoneal hematom şüphesi; batın içi serbest sıvı yok.","Yaşlı + yan ağrısı + hipotansiyon/senkop + AAA = rüptür kabul et."),
   T("Kan grubu, çapraz karşılaştırma, hemogram",2,10,"Hb 9,8.","Masif transfüzyon hazırlığı."),
   T("BT anjiyografi",-2,30,"Rüptüre AAA, retroperitoneal hematom; hasta BT'de KB 62/40.","Instabil hastada BT gecikme yaratır; stabilse EVAR planlaması için yapılır."),
   A("**Rüptüre AAA**: **vasküler cerrahiyi hemen çağır** (ameliyathane/EVAR); iki geniş damar yolu, **masif transfüzyon protokolü**; **permisif hipotansiyon** (bilinç açıksa sistolik 70–90); aşırı kristaloidden kaçın; traneksamik asit kurum protokolüne göre",4,10,"n2","Doğru. Tedavi cerrahi; resüsitasyon cerrahiyi geciktirmemeli."),
   A("Renal kolik: NSAİİ, 2 L SF ve kontrastsız BT",-5,30,"n9","Yaşlıda “ilk böbrek taşı” AAA rüptürü olabilir; agresif sıvı kanamayı artırır."),
 ]),
 "n2":E("Cerrahi","Hasta 25 dakikada ameliyathaneye alındı; açık onarım yapıldı, yoğun bakımdan sonra taburcu edildi.\n\n**Akılda kalsın**\n- Klasik üçlü: **ağrı (karın/bel/yan) + hipotansiyon + pulsatil kitle** — çoğu zaman eksik.\n- **>50 yaşta “ilk böbrek taşı”** ve senkop → **POCUS ile aortaya bak**.\n- **Permisif hipotansiyon** (bilinç ve perfüzyon korunarak), **erken kan ürünleri**, **vasküler cerrahi**.\n- Instabil → doğrudan ameliyathane; stabil → BTA (EVAR uygunluğu).\n\n*Kaynak: ESVS 2024 AAA kılavuzu; SVS 2018.*","good"),
 "n9":E("Ölüm","Hasta BT çıkışında arrest oldu; ameliyathaneye ulaşamadı.","bad"),
}))
Qs+=[Q("c138q1","Rüptüre AAA şüphesinde instabil hastada yaklaşım hangisidir?",["Önce BT anjiyo","Vasküler cerrahi ve doğrudan ameliyathane","Agresif kristaloid","Gözlem","Endoskopi"],1,"Zaman en önemli faktör.","Vasküler cerrahi"),
 Q("c138q2","Rüptüre AAA'da resüsitasyon hedefi nedir?",["Sistolik 140 üstü","Permisif hipotansiyon (bilinç korunurken sistolik ≈70–90)","Yalnız kristaloid","Vazopresör ilk tercih","Diüretik"],1,"Pıhtıyı bozmamak için.","Vasküler cerrahi"),
 Q("c138q3","Hangi tablo AAA rüptürünü taklit edebilir?",["Renal kolik","Migren","Konjunktivit","Faranjit","Selülit"],0,"Yaşlıda ilk kez böbrek taşı tanısına dikkat.","Vasküler cerrahi")]

# 139 TİTREME — febril nötropeni
S.append(case("c139","Titreme ve ateş — 47 yaşında kadın, kemoterapi alıyor","Onkoloji / Enfeksiyon",
 "47 yaşında kadın, meme kanseri; son kemoterapisini 9 gün önce almış. 2 saat önce **titreme** ile başlayan ateş (38,8). Port kateteri var. Öksürük ya da idrar yakınması yok.",
 {"n1":N("Muayene","Halsiz, titriyor. Port giriş yeri temiz. Ağız içinde mukozit. Akciğer ve karın muayenesi normal. (Rektal muayene yapılmaz.)","KB 94/58 · Nb 122 · SS 22 · SpO₂ %96 · Ateş 38,9",[
   T("Hemogram",2,30,"**Mutlak nötrofil sayısı 200/mm³**.","Febril nötropeni: ANS <500 + ateş ≥38,3 (ya da ≥38,0 bir saat)."),
   T("Kan kültürü (port + periferik), idrar kültürü, laktat, akciğer grafisi",2,15,"Laktat 2,8; grafi normal.","Kültür antibiyotiği geciktirmemeli."),
   T("MASCC skoru",1,5,"Hipotansiyon, şiddetli semptom → **<21: yüksek risk**.","Ayaktan tedaviye uygun değil."),
   A("**Yüksek riskli febril nötropeni + sepsis**: **60 dakika içinde** antipsödomonal beta-laktam — **piperasilin-tazobaktam 4,5 g IV** (ya da sefepim/meropenem — yerel direnç); 30 mL/kg kristaloid; kateter enfeksiyonu/şokta **vankomisin** ekle; onkoloji, yatış (izolasyon)",4,15,"n2","Doğru. Her saatlik gecikme mortaliteyi artırır."),
   A("Ateşi parasetamolle düşür, hemogram sonucunu bekle, sonra karar ver",-4,60,"n9","Febril nötropenide antibiyotik hemogram beklenmeden başlanır."),
   A("Oral amoksisilin-klavulanat + siprofloksasin ile ayaktan",-4,10,"n9","Düşük riskli (MASCC ≥21) ve stabil hastalar içindir."),
 ]),
 "n2":E("Düzelme","Antibiyotik 35. dakikada başlandı; kan kültüründe *E. coli* üredi. Hasta 48 saatte ateşsizleşti, nötrofil 5. günde yükseldi.\n\n**Akılda kalsın**\n- Kemoterapi alan hastada **titreme/ateş = febril nötropeni varsay**.\n- **Kapıdan antibiyotiğe ≤60 dakika**; kültürleri hızla al ama bekleme.\n- Ampirik: **antipsödomonal beta-laktam** (piperasilin-tazobaktam, sefepim, meropenem); hemodinamik instabilite, kateter enfeksiyonu, deri-yumuşak doku, MRSA kolonizasyonu → **vankomisin** ekle.\n- **Rektal muayene/tuşe ve rektal ısı ölçümü yok**.\n- **MASCC ≥21** düşük risk → seçilmiş hastada oral/ayaktan.\n\n*Kaynak: ESMO 2016; IDSA/ASCO 2018 febril nötropeni kılavuzları.*","good"),
 "n9":E("Septik şok","Hasta 3 saat sonra septik şoka girdi; yoğun bakıma alındı.","bad"),
}))
Qs+=[Q("c139q1","Febril nötropenide antibiyotik başlama hedef süresi nedir?",["24 saat","6 saat","≤60 dakika","Kültür sonucu gelince","Ateş 3 gün sürerse"],2,"Gecikme mortaliteyi artırır.","Onkoloji / Enfeksiyon"),
 Q("c139q2","Febril nötropenide ampirik tedavi seçeneği hangisidir?",["Piperasilin-tazobaktam","Amoksisilin tek başına","Azitromisin","Klindamisin","Nitrofurantoin"],0,"Antipsödomonal beta-laktam.","Onkoloji / Enfeksiyon"),
 Q("c139q3","Nötropenik hastada hangisinden kaçınılır?",["Kan kültürü","Rektal muayene/ısı ölçümü","Akciğer grafisi","İdrar kültürü","Laktat"],1,"Bakteriyemi ve doku hasarı riski.","Onkoloji / Enfeksiyon")]

# 140 VENTRİKÜLER TAŞİKARDİ — stabil monomorfik
S.append(case("c140","Çarpıntı ve göğüste baskı — 66 yaşında erkek","Kardiyoloji",
 "66 yaşında erkek. 3 yıl önce anterior MI geçirmiş. 40 dakikadır çarpıntı ve hafif göğüs baskısı. Bayılma yok.",
 {"n1":N("Muayene","Bilinç açık, konuşuyor, hafif terli. Akciğerler temiz, periferik dolaşım iyi.","KB 124/78 · Nb 168 (düzenli) · SS 20 · SpO₂ %96",[
   T("12 derivasyonlu EKG",3,5,"**Düzenli geniş QRS taşikardisi** 168/dk, QRS 160 ms, **AV disosiyasyon** (arada P dalgaları), **füzyon atımları**, prekordiyal konkordans.","Geçirilmiş MI + geniş QRS taşikardi → **VT kabul et**."),
   T("K, Mg, troponin",1,40,"K 3,6, Mg 1,7.","Elektrolitler düzeltilir."),
   A("**Stabil monomorfik VT**: defibrilatör pedleri takılı; **amiodaron 300 mg IV, 10–20 dakikada** (ya da prokainamid — varsa) **veya** sedasyon altında **senkronize kardiyoversiyon**; K ve Mg replasmanı; kardiyoloji",4,15,"n2","Doğru. ERC 2021: stabil geniş QRS taşikardide amiodaron ya da elektif kardiyoversiyon."),
   A("SVT + aberasyon olabilir — verapamil 5 mg IV",-5,5,"n9","VT'de verapamil kardiyovasküler kollapsa yol açar."),
   A("Stabil — gözlem, kendiliğinden geçebilir",-3,30,"n3","Süren VT hemodinamik bozulmaya dönebilir."),
 ]),
 "n3":N("Bozulma","Hasta konfüzyon geliştirdi, KB 78/50.","KB 78/50 · Nb 172",[
   A("Senkronize kardiyoversiyon (sedasyonla)",2,5,"n4","Instabil VT."),
   A("Amiodaron infüzyonuna başla ve bekle",-3,20,"n9","Instabil hastada elektrik önceliklidir."),
 ]),
 "n2":E("Sinüs ritmi","Amiodaron sonrası VT sonlanmadı; sedasyonla 120 J senkronize kardiyoversiyonla sinüs ritmi sağlandı. Kardiyolojiye yatırıldı; ICD planlandı.\n\n**Akılda kalsın**\n- **Geniş QRS taşikardi = aksi kanıtlanana kadar VT**, özellikle **yapısal kalp hastalığı/MI öyküsünde**.\n- VT ipuçları: **AV disosiyasyon, füzyon/yakalama atımları**, prekordiyal konkordans, çok geniş QRS.\n- Instabil → **senkronize kardiyoversiyon**; stabil → **amiodaron 300 mg (10–20 dk)** veya prokainamid / elektif kardiyoversiyon.\n- **Verapamil/diltiazem verme**.\n\n*Kaynak: ERC 2021; ESC 2022 ventriküler aritmi kılavuzu.*","good"),
 "n4":E("Geç kardiyoversiyon","Kardiyoversiyonla düzeldi; ancak hipoperfüzyon döneminde akut böbrek hasarı gelişti.","mid"),
 "n9":E("Kollaps","Hasta nabızsız VT'ye girdi; defibrilasyonla döndürüldü.","bad"),
}))
Qs+=[Q("c140q1","Geniş QRS taşikardide VT lehine bulgu hangisidir?",["AV disosiyasyon ve füzyon atımları","Düzensiz ritim","Delta dalgası","Hız 110/dk","Genç yaş"],0,"Yakalama atımları da VT lehinedir.","Kardiyoloji"),
 Q("c140q2","Stabil monomorfik VT'de ilaç seçeneği ve dozu (ERC) hangisidir?",["Verapamil 5 mg","Amiodaron 300 mg IV 10–20 dakikada","Adenozin 12 mg","Digoksin 0,5 mg","Metoprolol 5 mg"],1,"Alternatif: elektif senkronize kardiyoversiyon.","Kardiyoloji"),
 Q("c140q3","Instabil VT'de (nabızlı) ilk tedavi hangisidir?",["Senkronize kardiyoversiyon","Defibrilasyon (senkronsuz) her zaman","Amiodaron infüzyonu","Lidokain","Gözlem"],0,"Nabızsızsa defibrilasyon.","Kardiyoloji")]

P={"id":"ilk-nobet-14","title":"İlk Nöbet Vakaları — 14. Paket (vaka 131–140)","desc":"Migren atağı, Bell paralizisi, BT negatif subaraknoid kanama, hiponatremide aşırı düzeltme, gebede apandisit, yaşlıda odontoid kırığı, adezyon ileusu, rüptüre aort anevrizması, febril nötropeni, stabil ventriküler taşikardi.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 14. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 14. Paket","topic":"Temel acil","order":14,"req":[2],"desc":"Nöroloji, cerrahi ve ritim acillerinden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
