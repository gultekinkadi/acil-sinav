import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 51 WERNICKE ENSEFALOPATİSİ
S.append(case("c51","Konfüzyon ve dengesizlik — 52 yaşında erkek","Nöroloji / Toksikoloji",
 "52 yaşında erkek, uzun süredir günde yarım şişe rakı içiyor, son haftalarda pek yemek yememiş. Ailesi 2 gündür konfüze olduğunu, yürürken düştüğünü ve “çift gördüğünü” söylüyor.",
 {"n1":N("Muayene","Dezoryante. **Horizontal nistagmus**, sağ lateral rektus zaafı. Geniş tabanlı, ataksik yürüyüş. Fokal motor bulgu yok.","KB 112/70 · Nb 104 · Ateş 36,4 · Kapiller glukoz 62 mg/dL",[
   T("Beyin BT",1,30,"Akut kanama yok; hafif atrofi.","Travma/kanama dışlanmalı (düşme öyküsü); Wernicke tanısı kliniktir."),
   T("Mg, K, P",2,40,"Mg 1,2 (düşük), K 3,2, P 1,9.","Hipomagnezemi tiamin etkinliğini azaltır; birlikte düzeltilir."),
   A("**Yüksek doz IV tiamin** (ör. 500 mg IV, günde 3 kez, 2–3 gün; ardından 250 mg/gün) — glukozdan önce ya da birlikte; ardından dekstroz; Mg ve K replasmanı; alkol yoksunluğu izlemi",4,15,"n2","Doğru. Wernicke kliniktir: triadın (konfüzyon, oftalmopleji, ataksi) tümü olmasa da tedavi edilir."),
   A("Hipoglisemi için önce %20 dekstroz ver, tiamini sonraya bırak",-3,10,"n3","Tiamin eksikliğinde tek başına glukoz Wernicke'yi ağırlaştırabilir; birlikte veya önce tiamin verilir (hipoglisemi tedavisini de geciktirme)."),
   A("Oral tiamin 100 mg/gün ile taburcu",-4,10,"n9","Alkol kullanımında oral emilim yetersizdir; Wernicke'de yüksek doz parenteral gerekir."),
 ]),
 "n3":N("30 dakika sonra","Konfüzyon artıyor.","Glukoz 140",[
   A("Yüksek doz IV tiamin + Mg replasmanı",2,10,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Düzelme","48 saatte oftalmopleji düzeldi, konfüzyon azaldı; ataksi haftalar içinde geriledi. Alkol bırakma programına yönlendirildi.\n\n**Akılda kalsın**\n- Triad: **konfüzyon + oftalmopleji/nistagmus + ataksi** (hastaların azında tamamı vardır).\n- Risk: alkol, malnütrisyon, hiperemezis, bariatrik cerrahi, kanser, uzun süre kusma.\n- **Yüksek doz parenteral tiamin** (500 mg IV × 3/gün), **glukozdan önce/birlikte**; Mg'yi düzelt.\n- Tedavi edilmezse **Korsakoff** (kalıcı amnezi).\n\n*Kaynak: EFNS 2010 Wernicke kılavuzu; RCP önerileri.*","good"),
 "n9":E("Korsakoff sendromu","Hasta kalıcı anterograd amnezi ve konfabulasyonla kaldı.","bad"),
}))
Qs+=[Q("c51q1","Wernicke ensefalopatisinin klasik triadı hangisidir?",["Ateş, baş ağrısı, ense sertliği","Konfüzyon, oftalmopleji/nistagmus, ataksi","Tremor, rijidite, bradikinezi","Afazi, hemipleji, göz deviasyonu","Nöbet, hiponatremi, kusma"],1,"Triadın tamamı hastaların azında görülür; tek bulgu bile tedavi için yeterli olabilir.","Nöroloji / Toksikoloji"),
 Q("c51q2","Alkolik hipoglisemik hastada tiamin ve glukoz sırası için doğru ifade hangisidir?",["Önce glukoz, tiamin ertesi gün","Tiamin glukozdan önce veya birlikte verilir; hipoglisemi tedavisi geciktirilmez","Yalnız tiamin","Yalnız glukoz","Hiçbiri"],1,"Glukoz metabolizması tiamin tüketir.","Nöroloji / Toksikoloji"),
 Q("c51q3","Wernicke tedavisinde tiaminin etkinliği için hangi elektrolit de düzeltilmelidir?",["Sodyum","Magnezyum","Kalsiyum","Klor","Bikarbonat"],1,"Magnezyum tiamine bağımlı enzimlerin kofaktörüdür.","Nöroloji / Toksikoloji")]

# 52 HİPERKALSEMİ (malignite)
S.append(case("c52","Halsizlik ve konfüzyon — 66 yaşında kadın","Onkoloji / Metabolik",
 "66 yaşında kadın, kemik metastazlı meme kanseri. 1 haftadır çok su içiyor, sık idrara çıkıyor, kabız; son 2 gündür uykulu ve konfüze. Yaklaşık 65 kg.",
 {"n1":N("Muayene","Uykuya meyilli ama uyandırılabiliyor. Mukozalar kuru.","KB 102/62 · Nb 108 · SpO₂ %97",[
   T("Kalsiyum, albümin, böbrek fonksiyonu",3,40,"**Total Ca 15,4 mg/dL** (albümin 3,6 → düzeltilmiş ≈15,7), kreatinin 1,8 (bazal 0,9), fosfor 3,2.","Ca >14 ağır hiperkalsemi; poliüri → dehidratasyon → AKI kısır döngüsü."),
   T("EKG",1,5,"**Kısa QT**, sinüs taşikardisi.","Hiperkalsemide QT kısalır; aritmi riski."),
   A("Agresif IV SF (ör. 200–300 mL/saat; idrar 100–150 mL/saat hedefi); **kalsitonin** 4 Ü/kg SC/IM (12 saatte bir) hızlı etki için; **zoledronik asit 4 mg IV 15 dakikada** (böbrek fonksiyonuna göre); tiyazid ve kalsiyum içeren ilaçları kes",4,15,"n2","Doğru. Sıvı + kalsitonin (saatler) + bifosfonat (2–4 gün) kombinasyonu."),
   A("Önce furosemid 80 mg IV ile kalsiyumu at",-4,10,"n9","Hipovolemik hastada furosemid dehidratasyonu ve böbrek hasarını artırır; yalnız sıvı yüklemesi sonrası hipervolemide düşünülür."),
   A("Oral sıvı öner, onkoloji poliklinik randevusu",-5,10,"n9","Konfüzyonlu ağır hiperkalsemi acildir."),
 ]),
 "n2":E("Kalsiyum düştü","48 saatte Ca 11,2'ye, kreatinin 1,1'e indi; konfüzyon düzeldi. Denosumab ve onkolojik tedavi planlandı.\n\n**Akılda kalsın**\n- Belirtiler: “taşlar, kemikler, karın ağrısı, psikiyatrik bulgular” — poliüri, polidipsi, kabızlık, konfüzyon; **kısa QT**.\n- Albümine göre düzelt (ya da iyonize Ca).\n- Tedavi: **IV SF** (önce hacim), **kalsitonin** (hızlı, kısa süreli), **zoledronik asit** (2–4 günde); böbrek yetmezliğinde **denosumab**; dirençli/çok ağır olguda diyaliz.\n- Furosemid yalnız hacim yerine konduktan sonra, hipervolemide.\n- Malignitede PTHrP, kemik metastazı; ayaktan en sık neden **primer hiperparatiroidi**.\n\n*Kaynak: Endocrine Society 2023 malignite hiperkalsemisi kılavuzu.*","good"),
 "n9":E("Akut böbrek yetmezliği","Hasta dehidratasyonun derinleşmesiyle oligürik böbrek yetmezliği ve komaya girdi.","bad"),
}))
Qs+=[Q("c52q1","Ağır hiperkalsemide ilk tedavi adımı hangisidir?",["Furosemid","IV izotonik sıvı","Kalsiyum kanal blokeri","Tiyazid","Oral fosfat"],1,"Hastalar hipovolemiktir; önce hacim yerine konur.","Onkoloji / Metabolik"),
 Q("c52q2","Hiperkalsemide en hızlı etki eden (saatler içinde) ilaç hangisidir?",["Zoledronik asit","Kalsitonin","Denosumab","Prednizolon","Sinakalset"],1,"Kalsitonin saatler içinde etki eder ama taşifilaksi gelişir; bifosfonat 2–4 günde.","Onkoloji / Metabolik"),
 Q("c52q3","Hiperkalsemide EKG'de hangi bulgu görülür?",["Uzun QT","Kısa QT","Sivri T","Delta dalgası","Osborn dalgası"],1,"QT kısalması tipiktir.","Onkoloji / Metabolik")]

# 53 TANSİYON PNÖMOTORAKS (travma)
S.append(case("c53","Motosiklet kazası — 27 yaşında erkek","Travma",
 "27 yaşında erkek, motosiklet kazası. Ambulansla getirildi; sol göğsünde ağrı ve giderek artan nefes darlığı var. Yolda SpO₂ düşmüş.",
 {"n1":N("Travma alanı — birincil bakı","Hava yolu açık, konuşuyor ama zorlanıyor. **Sol hemitoraksta solunum sesi yok**, hiperrezonans. Boyun venleri dolgun. Trakea hafif sağa deviye.","KB 78/50 · Nb 138 · SS 36 · SpO₂ %82 (rezervuarlı maskeyle)",[
   T("Akciğer grafisi",-4,10,"Sol tansiyon pnömotoraks. 10 dakika kaybedildi; hasta arrest eşiğinde.","Tansiyon pnömotoraks klinik tanıdır; grafi beklenmez."),
   T("eFAST (akciğer)",1,2,"Solda **akciğer kayması yok**, barkod işareti.","Saniyeler içinde destekler."),
   A("**Hemen dekompresyon**: sol 4.–5. interkostal aralık, ön-orta aksiller çizgide **parmak torakostomi** (eğitimliyse) ya da uzun (≥8 cm) kanülle iğne dekompresyonu (alternatif: 2. İKA midklaviküler); ardından göğüs tüpü",4,5,"n2","Doğru. Tansiyon pnömotoraksta görüntüleme beklenmez; erişkinde 4./5. İKA önerilir (2. İKA'da göğüs duvarı daha kalın, başarısızlık fazla)."),
   A("Entübe et, pozitif basınçla ventile et, sonra bak",-5,10,"n9","Pozitif basınç tansiyonu hızla derinleştirir; dekompresyon önce gelir."),
 ]),
 "n2":N("Dekompresyon sonrası","Hava çıkışıyla birlikte KB 112/70, SpO₂ %94.","Nb 112",[
   A("Sol göğüs tüpü (5. İKA, orta aksiller çizgi, güvenli üçgen); kontrol grafisi; ikincil bakı ve eFAST'a devam",3,15,"n3","Doğru. İğne dekompresyonu geçici; tüp torakostomi kesin tedavidir."),
   A("Düzeldi — göğüs tüpüne gerek yok, izle",-3,30,"n9","İğne kanülü tıkanabilir/yerinden çıkabilir; tansiyon tekrarlar."),
 ]),
 "n3":E("Stabil","Göğüs tüpüyle akciğer ekspanse oldu; ikincil bakıda başka hayatı tehdit eden yaralanma yoktu.\n\n**Akılda kalsın**\n- Tansiyon pnömotoraks **klinik tanıdır**: solunum sıkıntısı, tek taraflı solunum sesi kaybı, hipotansiyon, JVD; trakea deviasyonu geç bulgu.\n- **Görüntüleme bekleme**: erişkinde **4.–5. İKA ön/orta aksiller çizgi** (parmak torakostomi veya uzun iğne).\n- Ardından **göğüs tüpü**.\n- Pozitif basınçlı ventilasyon tansiyonu ağırlaştırır.\n\n*Kaynak: ATLS 10. baskı; ERC 2021 travmatik arrest.*","good"),
 "n9":E("Travmatik arrest","Hasta nabızsız elektriksel aktiviteye girdi; bilateral torakostomiyle dolaşım ancak döndü.","bad"),
}))
Qs+=[Q("c53q1","Tansiyon pnömotoraksta tanı için hangisi doğrudur?",["Akciğer grafisi zorunludur","BT gerekir","Klinik tanıdır; görüntüleme beklenmez","Kan gazı gerekir","Bronkoskopi gerekir"],2,"Hemodinamik bozulmada hemen dekompresyon yapılır.","Travma"),
 Q("c53q2","ATLS 10'a göre erişkinde iğne dekompresyonu için önerilen yer hangisidir?",["2. İKA, midklaviküler","4.–5. İKA, ön-orta aksiller çizgi","7. İKA, skapular çizgi","Subksifoid","Supraklaviküler"],1,"Göğüs duvarı burada daha incedir; başarı daha yüksektir.","Travma"),
 Q("c53q3","İğne dekompresyonu sonrası kesin tedavi hangisidir?",["Gözlem","Göğüs tüpü (tüp torakostomi)","Oksijen tek başına","Plevrodez","Entübasyon"],1,"İğne geçici bir köprüdür.","Travma")]

# 54 SIADH (küçük hücreli akciğer kanseri)
S.append(case("c54","Bulantı ve dengesizlik — 64 yaşında erkek","Nefroloji / Onkoloji",
 "64 yaşında erkek, 40 paket-yıl sigara. 3 haftadır öksürük, kilo kaybı; son 1 haftadır bulantı, iştahsızlık, dengesizlik. İlaç kullanmıyor.",
 {"n1":N("Muayene","Uyanık, oryante; hafif dikkat dağınıklığı. Ödem yok, mukozalar nemli, ortostatik değişiklik yok (övolemik).","KB 132/78 · Nb 84 · SpO₂ %95",[
   T("Na, serum osm, glukoz",2,20,"**Na 121**, serum osm 254, glukoz 98.","Hipotonik hiponatremi."),
   T("İdrar osm ve idrar Na",3,30,"**İdrar osm 520 mOsm/kg**, **idrar Na 62 mmol/L**.","Övolemik + idrar osm >100 + idrar Na >30 → SIADH (tiroid, adrenal, ilaç dışlanmalı)."),
   T("TSH, sabah kortizolü",1,60,"Normal.","SIADH dışlama tanısıdır."),
   T("Akciğer grafisi",2,20,"Sağ hiler kitle, mediasten genişliği.","Küçük hücreli akciğer kanseri SIADH'nin önemli nedeni."),
   A("Orta şiddette semptom: sıvı kısıtlaması (≈800–1000 mL/gün); bulantı/konfüzyon artarsa tek doz %3 NaCl 150 mL; 24 saatte ≤8–10 mmol/L artış; nedeni araştır (göğüs BT, onkoloji); sıvı kısıtlaması yetmezse üre/tolvaptan",4,20,"n2","Doğru. SIADH'de izotonik serum Na'yı düşürebilir."),
   A("2 L %0,9 NaCl ver",-4,240,"n9","SIADH'de böbrek suyu tutar, tuzu atar: izotonik serum sonrası Na düşebilir."),
 ]),
 "n2":E("Kontrollü düzelme","Sıvı kısıtlamasıyla Na 48 saatte 128'e yükseldi; BT ve biyopsiyle küçük hücreli akciğer kanseri tanısı kondu.\n\n**Akılda kalsın**\n- SIADH ölçütleri: hipotonik hiponatremi, **övolemi**, **idrar osm >100**, **idrar Na >30**, normal tiroid/adrenal, diüretik yok.\n- Nedenler: **akciğer (küçük hücreli kanser, pnömoni)**, SSS (kanama, menenjit), ilaçlar (SSRI, karbamazepin, siklofosfamid), ağrı/bulantı, ameliyat sonrası.\n- Tedavi: **sıvı kısıtlaması**, üre veya tolvaptan; semptom ağırsa hipertonik.\n- **İzotonik serum SIADH'de Na'yı düşürebilir**.\n\n*Kaynak: Avrupa 2014 hiponatremi kılavuzu.*","good"),
 "n9":E("Kötüleşen hiponatremi","Na 116'ya düştü, hasta nöbet geçirdi.","bad"),
}))
Qs+=[Q("c54q1","SIADH için hangisi beklenen bulgudur?",["İdrar osm <100","Hipovolemi","İdrar Na >30 mmol/L ve idrar osm >100","Hiperkalemi","Serum osm >300"],2,"Övolemik, konsantre idrar ve yüksek idrar Na.","Nefroloji / Onkoloji"),
 Q("c54q2","SIADH'nin temel tedavisi hangisidir?",["%0,9 NaCl","Sıvı kısıtlaması","Hipotonik sıvı","Furosemid tek başına","Desmopressin"],1,"Ağır semptom yoksa ilk tedavi sıvı kısıtlamasıdır.","Nefroloji / Onkoloji"),
 Q("c54q3","SIADH yapan malignite hangisidir?",["Bazal hücreli karsinom","Küçük hücreli akciğer kanseri","Tiroid papiller kanseri","Prostat adenokarsinomu (tipik değil)","Lipom"],1,"Ektopik ADH üretimi.","Nefroloji / Onkoloji")]

# 55 MENİNGOKOKSEMİ
S.append(case("c55","Ateş ve döküntü — 17 yaşında erkek","Enfeksiyon / Pediatri",
 "17 yaşında erkek, lise öğrencisi. Sabah grip benzeri yakınmalarla başlayan ateş; öğleden sonra bacaklarında ağrı, soğuk el-ayak ve hızla yayılan mor lekeler.",
 {"n1":N("Resüsitasyon alanı","Bilinç açık ama huzursuz. Bacaklarda ve gövdede **basmakla solmayan peteşi ve purpura**, bazıları birleşmiş. Ekstremiteler soğuk, kapiller dolum 5 sn. Ense sertliği yok.","KB 78/40 · Nb 146 · SS 30 · SpO₂ %94 · Ateş 39,8",[
   T("Bardak testi (döküntüye cam bardakla bastırma)",1,1,"Lezyonlar **solmuyor**.","Ateş + solmayan döküntü = meningokoksemi kabul edilir."),
   T("Lomber ponksiyon",-4,30,"Yapıldı; hasta kötüleşti, ponksiyon yerinde kanama.","Şok, koagülopati ve purpurada LP ertelenir; tedaviyi geciktirmez."),
   A("**Hemen seftriakson 2 g IV** (ya da IM/IO — damar yolu beklenmez); 20 mL/kg kristaloid bolus ve yeniden değerlendir; erken vazopresör (norepinefrin/adrenalin); kan kültürü (antibiyotiği geciktirmeden), PCR; yoğun bakım; halk sağlığına bildirim ve temaslı profilaksisi",4,10,"n2","Doğru. Meningokoksemide dakikalar önemlidir; antibiyotik ilk dakikalarda."),
   A("Viral döküntü olabilir — ateş düşürücü ve gözlem",-5,60,"n9","Ateşli hastada solmayan purpura ve şok meningokoksemidir."),
 ]),
 "n2":E("Yoğun bakımda sağkalım","Antibiyotik 10. dakikada verildi; 4 L sıvı ve norepinefrinle şok kontrol altına alındı. Kanda *N. meningitidis* serogrup B üredi. Parmak uçlarında küçük nekrozlar dışında sekelsiz iyileşti.\n\n**Akılda kalsın**\n- **Ateş + basmakla solmayan döküntü** = aksi kanıtlanana kadar meningokoksemi.\n- Erken bulgular: **bacak ağrısı, soğuk ekstremiteler, anormal deri rengi** (döküntüden önce).\n- **İlk dakikalarda seftriakson** (IV/IM/IO); hastane öncesinde benzilpenisilin.\n- Şokta sıvı + erken vazopresör; **LP'yi ertele**.\n- Bildirim ve **temaslı kemoprofilaksisi**; aşılama.\n\n*Kaynak: NICE NG240 (2024) bakteriyel menenjit ve meningokok hastalığı.*","good"),
 "n9":E("Purpura fulminans","Tedavi gecikti; purpura fulminans, çoklu organ yetmezliği gelişti, iki alt ekstremitede amputasyon gerekti.","bad"),
}))
Qs+=[Q("c55q1","Ateşli ve basmakla solmayan purpurik döküntüsü olan hastada ilk yapılacak nedir?",["LP","Beyin BT","Hemen parenteral seftriakson","Kan kültürü sonucunu beklemek","Antihistaminik"],2,"Antibiyotik hiçbir tetkik için geciktirilmez.","Enfeksiyon / Pediatri"),
 Q("c55q2","Meningokoksemide döküntüden önce görülebilen erken bulgular hangileridir?",["Bacak ağrısı, soğuk ekstremiteler, anormal deri rengi","Ense sertliği ve fotofobi","Kaşıntı","Konjunktivit","Lenfadenopati"],0,"Bu erken bulgular sepsisin habercisidir.","Enfeksiyon / Pediatri"),
 Q("c55q3","Şoktaki meningokoksemi hastasında LP için doğru ifade hangisidir?",["Hemen yapılmalıdır","Şok, koagülopati ve purpura nedeniyle ertelenir","Antibiyotikten önce zorunludur","BT sonrası mutlaka yapılır","Tedaviyi belirler"],1,"Hasta stabil olduğunda gerekirse yapılır.","Enfeksiyon / Pediatri")]

# 56 ADRENAL KRİZ (bilinen Addison)
S.append(case("c56","Kusma ve halsizlik — 38 yaşında kadın","Endokrin",
 "38 yaşında kadın, Addison hastalığı; günde hidrokortizon 20 mg + fludrokortizon kullanıyor. 2 gündür gastroenterit; kusmadığı zamanlarda ilaçlarını almaya çalışmış ama tutamamış. Bugün ayağa kalkamıyor.",
 {"n1":N("Resüsitasyon alanı","Letarjik, deri bronz renkli, mukozalar kuru. Yaygın karın ağrısı.","KB 76/42 · Nb 124 · Ateş 37,9 · Kapiller glukoz 58",[
   T("Na, K, kortizol, ACTH (tedaviden önce örnek)",1,10,"Na 124, **K 6,0**, kreatinin 1,6. (Kortizol/ACTH sonuçları sonra gelecek.)","Primer adrenal yetmezlikte hiponatremi + hiperkalemi + hipoglisemi. Örnek alınır ama tedavi beklemez."),
   A("**Hidrokortizon 100 mg IV/IM hemen**, ardından 200 mg/24 saat (50 mg 6 saatte bir ya da infüzyon); 1 L %0,9 NaCl ilk saatte, sonra ihtiyaca göre; hipoglisemi için dekstroz; tetikleyiciyi tedavi et",4,10,"n2","Doğru. Adrenal krizde hidrokortizon dakikalar içinde verilmeli; yüksek dozda mineralokortikoid etkisi de vardır."),
   A("Kortizol sonucunu bekle, sonra steroid başla",-5,120,"n9","Adrenal kriz tanısı bilinen hastada tetkik beklemek ölümcüldür."),
   A("Gastroenterit — antiemetik + sıvı, hidrokortizon dozunu evde iki katına çıkar",-4,30,"n9","Kusan ve hipotansif hasta oral ilaç alamaz; parenteral hidrokortizon şarttır."),
 ]),
 "n2":E("Krizden çıkış","1 saat içinde KB 110/68, glukoz 102; 48 saat sonra oral doza geçildi. “Hasta gün kuralları” ve **acil hidrokortizon enjeksiyon kiti** eğitimi verildi.\n\n**Akılda kalsın**\n- Adrenal kriz: **hipotansiyon/şok**, kusma, karın ağrısı, bilinç değişikliği; hiponatremi, **hiperkalemi** (primer), hipoglisemi.\n- **Hidrokortizon 100 mg IV/IM hemen**, sonra 200 mg/24 saat; **SF 1 L/saat** ilk saatte.\n- Tetkik için örnek al ama **tedaviyi bekletme**.\n- Hasta gün kuralları: ateş/hastalıkta doz 2–3 kat; kusmada **IM hidrokortizon** ve acile başvuru.\n\n*Kaynak: Endocrine Society 2016; Society for Endocrinology adrenal kriz rehberi 2020.*","good"),
 "n9":E("Refrakter şok","Hasta 2 saat sonra refrakter şok ve arrest geliştirdi.","bad"),
}))
Qs+=[Q("c56q1","Adrenal krizde ilk tedavi dozu hangisidir?",["Deksametazon 0,5 mg","Hidrokortizon 100 mg IV/IM","Prednizolon 5 mg PO","Fludrokortizon 0,1 mg","Metilprednizolon 1 g"],1,"Hidrokortizon 100 mg bolus, ardından 200 mg/24 saat.","Endokrin"),
 Q("c56q2","Primer adrenal yetmezlikte tipik elektrolit bulgusu hangisidir?",["Hipernatremi + hipokalemi","Hiponatremi + hiperkalemi","Hiperkalsemi","Hipofosfatemi","Hipomagnezemi"],1,"Mineralokortikoid eksikliği hiperkalemi yapar; sekonder yetmezlikte hiperkalemi yoktur.","Endokrin"),
 Q("c56q3","Addison hastası kusma nedeniyle ilacını alamıyorsa ne önerilir?",["Dozu atlamak","IM hidrokortizon enjeksiyonu ve acile başvuru","Yalnız fludrokortizon","Bol su","Ertesi gün iki doz"],1,"Hastalar acil enjeksiyon kitiyle eğitilmelidir.","Endokrin")]

# 57 MASİF PULMONER EMBOLİ — ARREST
S.append(case("c57","Acil serviste ani kollaps — 52 yaşında erkek","Resüsitasyon",
 "52 yaşında erkek, 10 gün önce kalça protezi ameliyatı olmuş, tromboprofilaksiyi bırakmış. Ani nefes darlığıyla geldi; triajda konuşurken aniden bilincini kaybetti.",
 {"n1":N("Kollaps — 0. dakika","Yanıtsız, solunum yok. Monitörde dar QRS'li ritim 110/dk, **nabız yok** (NEA).","",[
   A("Yüksek kaliteli KPR (göğüs basısı, minimum kesinti), adrenalin 1 mg 3–5 dakikada bir, hava yolu; nabız kontrollerinde POCUS",4,5,"n2","Doğru. NEA'da geri döndürülebilir nedenler (4H-4T) aranır."),
   A("Defibrilasyon",-3,2,"n2","NEA şoklanabilir ritim değildir."),
 ]),
 "n2":N("4. dakika","KPR sürüyor. Nabız kontrolünde POCUS: **sağ ventrikül belirgin dilate**, sol ventrikül küçük; perikardiyal sıvı yok. Bacakta şişlik var.","",[
   A("Pulmoner emboli olasılığı çok yüksek: **KPR sırasında trombolitik** (ör. alteplaz 50 mg IV bolus — kurum protokolüne göre); trombolizden sonra **KPR'ye en az 60–90 dakika** devam; ECPR/cerrahi embolektomi seçeneklerini değerlendir",4,10,"n3","Doğru. Arrest nedeni PE olduğu düşünülüyorsa tromboliz önerilir; etkisi için uzun KPR gerekir."),
   A("Rutin KPR'ye devam, 20 dakika sonra sonlandır",-4,20,"n9","Tedavi edilebilir neden atlandı; trombolizden sonra bile 60–90 dakika KPR gerekebilir."),
 ]),
 "n3":E("Spontan dolaşımın dönüşü","Trombolizden 18 dakika sonra spontan dolaşım döndü. Yoğun bakımda heparin infüzyonu başlandı; hasta nörolojik olarak iyi taburcu oldu.\n\n**Akılda kalsın**\n- Arrestte **4H-4T**; **POCUS** (KPR kesintisini uzatmadan) dilate sağ ventrikül gösterebilir.\n- PE'ye bağlı arrest düşünülüyorsa **trombolitik** ver ve **60–90 dakika KPR** sürdür.\n- Seçenekler: cerrahi embolektomi, kateter tedavisi, **ECPR**.\n- Risk: yakın cerrahi, immobilizasyon, kanser, östrojen, önceki VTE.\n\n*Kaynak: ERC 2021 özel durumlar; ESC 2019 PE kılavuzu.*","good"),
 "n9":E("Ölüm","Resüsitasyon 20. dakikada sonlandırıldı; otopside masif PE saptandı.","bad"),
}))
Qs+=[Q("c57q1","PE'ye bağlı olduğu düşünülen kardiyak arrestte trombolitik sonrası KPR ne kadar sürdürülmelidir?",["5 dakika","10 dakika","En az 60–90 dakika","Trombolitik verilmez","1 saatten fazla asla"],2,"ERC 2021: trombolitik verildiyse en az 60–90 dakika KPR düşünülmeli.","Resüsitasyon"),
 Q("c57q2","NEA ile arrest olan hastada KPR sırasındaki POCUS'ta dilate sağ ventrikül neyi düşündürür?",["Hipovolemi","Pulmoner emboli","Hipoglisemi","Hiperkalemi","Tansiyon pnömotoraks (her zaman)"],1,"Akut sağ ventrikül yükü masif PE'yi düşündürür (ama özgül değildir — uzamış arrestte de olabilir).","Resüsitasyon"),
 Q("c57q3","Nabızsız elektriksel aktivitede hangisi uygun değildir?",["KPR","Adrenalin","Defibrilasyon","Geri döndürülebilir neden araştırması","Hava yolu yönetimi"],2,"NEA ve asistoli şoklanamayan ritimlerdir.","Resüsitasyon")]

# 58 MEZENTER İSKEMİ
S.append(case("c58","Şiddetli karın ağrısı — 78 yaşında erkek","Genel cerrahi / Damar",
 "78 yaşında erkek, AF, antikoagülan kullanmıyor. 3 saat önce ani başlayan, çok şiddetli, göbek çevresinde karın ağrısı; bir kez ishal. Kıvranıyor.",
 {"n1":N("Muayene","Karın yumuşak, hafif yaygın hassasiyet; defans ve rebound yok. **Ağrı muayeneyle orantısız şiddetli.**","KB 138/84 · Nb 118 (düzensiz) · Ateş 37,2",[
   T("Laktat ve lökosit",1,15,"Laktat 3,4, lökosit 18.000.","Laktat erken dönemde normal olabilir; normal laktat dışlamaz."),
   T("BT anjiyografi (bifazik)",4,30,"**Süperior mezenter arterde embolik tıkanıklık**, ince bağırsak duvarında kontrastlanma azalması.","Akut mezenter iskemi şüphesinde ilk görüntüleme; böbrek fonksiyonu beklenmez."),
   T("Direkt grafi",-1,15,"Normal.","Erken mezenter iskemide normaldir; yanıltıcı."),
   A("Sıvı resüsitasyonu, **anfraksiyone heparin**, geniş spektrumlu antibiyotik, analjezi; acil genel cerrahi + damar cerrahisi/girişimsel radyoloji — revaskülarizasyon (embolektomi/endovasküler) ± laparotomi",4,20,"n2","Doğru. Zaman bağırsaktır: hızlı revaskülarizasyon ve canlı olmayan bağırsağın rezeksiyonu."),
   A("Muayene yumuşak — kabızlık, lavman ve taburcu",-5,20,"n9","Yaşlı, AF'li hastada orantısız karın ağrısı mezenter iskemidir."),
 ]),
 "n2":E("Revaskülarizasyon","Endovasküler aspirasyon trombektomisi + laparotomide 40 cm ileum rezeksiyonu; ikinci bakışta kalan bağırsak canlıydı. Antikoagülasyon başlandı.\n\n**Akılda kalsın**\n- **Muayeneyle orantısız şiddetli karın ağrısı** + yaşlı + AF/aterosklerotik hastalık = akut mezenter iskemi.\n- Laktat ve direkt grafi **erken dönemde normal** olabilir.\n- **Bifazik BT anjiyografi** hemen; kontrast nefropatisi kaygısı tanıyı geciktirmemeli.\n- Heparin, sıvı, antibiyotik; **acil revaskülarizasyon** + gerekirse rezeksiyon ve ikinci bakış.\n\n*Kaynak: ESVS 2017 mezenter arter hastalığı; WSES 2022.*","good"),
 "n9":E("Bağırsak nekrozu","Hasta 12 saat sonra peritonit ve septik şokla döndü; yaygın ince bağırsak nekrozu, ameliyatta kaybedildi.","bad"),
}))
Qs+=[Q("c58q1","Akut mezenter iskeminin en önemli klinik ipucu hangisidir?",["Ateş","Muayeneyle orantısız şiddetli karın ağrısı","Sarılık","Melena","Konstipasyon"],1,"Erken dönemde peritoneal bulgu yoktur.","Genel cerrahi / Damar"),
 Q("c58q2","Akut mezenter iskemi şüphesinde ilk görüntüleme hangisidir?",["Direkt grafi","USG","Bifazik BT anjiyografi","MR","Kolonoskopi"],2,"Yüksek doğruluklu ve hızlıdır.","Genel cerrahi / Damar"),
 Q("c58q3","Normal laktat düzeyi için doğru ifade hangisidir?",["Mezenter iskemiyi dışlar","Erken dönemde normal olabilir; dışlamaz","Her zaman yüksektir","Tanı koydurur","Prognozla ilişkisizdir"],1,"Laktat geç yükselir.","Genel cerrahi / Damar")]

# 59 YANGIN — CO + SİYANÜR
S.append(case("c59","Ev yangınından çıkarılan hasta — 45 yaşında erkek","Toksikoloji / Yanık",
 "45 yaşında erkek, kapalı bir odada çıkan ev yangınından itfaiye tarafından bilinci kapalı çıkarıldı. Burun deliklerinde ve ağızda is var.",
 {"n1":N("Resüsitasyon alanı","GKS 8. Yüzde yüzeysel yanıklar, kaş-burun kılları yanık, sesi kısık. Hafif stridor.","KB 84/48 · Nb 124 · SS 26 · SpO₂ %98 (rezervuarlı maskeyle)",[
   T("Kan gazı + CO-oksimetri + laktat",3,10,"COHb %18, **laktat 11 mmol/L**, pH 7,12.","Kapalı alan yangınında **laktat ≥8–10** siyanür zehirlenmesini düşündürür (CO tek başına bu derecede laktat yapmaz)."),
   T("Laringoskopi (hava yolu değerlendirmesi)",2,5,"Supraglottik ödem, is.","İnhalasyon yaralanması: erken hava yolu kontrolü."),
   A("Erken entübasyon (inhalasyon hasarı, stridor, GKS 8) + %100 O₂; **hidroksokobalamin 5 g IV 15 dakikada** (gerekirse 5 g daha); sıvı resüsitasyonu; HBO'yu daha sonra değerlendir",4,15,"n2","Doğru. Hidroksokobalamin siyanürü bağlar (siyanokobalamin), güvenlidir; idrar ve deriyi kırmızıya boyar."),
   A("Yalnız %100 O₂ — CO zehirlenmesi, hidroksokobalamin gereksiz",-3,20,"n3","Yüksek laktat ve hipotansiyon siyanürü düşündürür; O₂ tek başına yetersiz."),
   A("Entübasyonu ertele, önce yanık pansumanı",-4,30,"n9","Hava yolu ödemi hızla artar; geç entübasyon imkânsız hale gelebilir."),
 ]),
 "n3":N("30 dakika sonra","Hipotansiyon derinleşti, laktat 13.","KB 70/40",[
   A("Entübasyon + hidroksokobalamin 5 g IV",2,15,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Stabilizasyon","Hidroksokobalamin sonrası KB 108/64, laktat 6 saatte 3'e indi. Yanık merkezine transfer edildi.\n\n**Akılda kalsın**\n- Kapalı alan yangını: **CO + siyanür + inhalasyon hasarı**.\n- SpO₂ yanıltıcı; COHb ve **laktat** ölç (laktat ≥8–10 siyanür lehine).\n- İnhalasyon bulguları (yüz yanığı, is, ses kısıklığı, stridor) → **erken entübasyon**.\n- **Hidroksokobalamin 5 g IV** (çocuk 70 mg/kg), %100 O₂.\n- Nitrit tedavisi methemoglobinemi yapar; CO zehirlenmesinde oksijen taşıma kapasitesini daha da azaltır.\n\n*Kaynak: ABA; Goldfrank's.*","good"),
 "n9":E("Hava yolu kaybı","Ödem ilerledi; entübasyon başarısız oldu, acil cerrahi hava yolu gerekti.","bad"),
}))
Qs+=[Q("c59q1","Kapalı alan yangınından çıkarılan hastada siyanür zehirlenmesini düşündüren laboratuvar bulgusu hangisidir?",["Hiperkalemi","Belirgin laktat yüksekliği (≥8–10 mmol/L)","Hiperglisemi","Hipernatremi","Trombositopeni"],1,"Siyanür hücresel solunumu bloke eder; ağır laktik asidoz.","Toksikoloji / Yanık"),
 Q("c59q2","Duman inhalasyonunda siyanür zehirlenmesinin tercih edilen antidotu hangisidir?",["Amil nitrit","Hidroksokobalamin 5 g IV","Metilen mavisi","N-asetilsistein","Fizostigmin"],1,"Methemoglobinemi yapmadığı için yangın hastasında tercih edilir.","Toksikoloji / Yanık"),
 Q("c59q3","İnhalasyon yaralanmasında erken entübasyon endikasyonu hangisidir?",["Hafif öksürük","Stridor, ses kısıklığı, derin yüz yanığı, GKS ≤8","El yanığı","SpO₂ %99","Ateş"],1,"Hava yolu ödemi hızla ilerler.","Toksikoloji / Yanık")]

# 60 ABDOMİNAL KOMPARTMAN SENDROMU
S.append(case("c60","Gergin karın ve azalan idrar — 46 yaşında erkek","Yoğun bakım / Cerrahi",
 "46 yaşında erkek, ağır akut pankreatit nedeniyle 18 saattir acil yoğun bakım alanında izleniyor; 9 L sıvı verilmiş. Entübe. Son 4 saatte idrar çıkışı azalıyor, ventilatör basınçları yükseliyor.",
 {"n1":N("18. saat","Karın belirgin distandü ve gergin.","KB 92/56 · Nb 128 · Tepe hava yolu basıncı 42 cmH₂O · İdrar 10 mL/saat",[
   T("Mesane içi basınç ölçümü",3,10,"**İntraabdominal basınç 26 mmHg**.","İAB >20 mmHg + yeni organ disfonksiyonu = abdominal kompartman sendromu (ACS)."),
   T("Kreatinin, laktat",1,30,"Kreatinin 2,4 (bazal 1,0), laktat 4,8.","Organ disfonksiyonu."),
   A("Tıbbi önlemler (sedasyon/analjezi, gerekirse nöromüsküler blok, nazogastrik/rektal dekompresyon, pozitif sıvı dengesini durdur, asit varsa perkütan drenaj) + genel cerrahi — yanıt yoksa **dekompresif laparotomi**",4,20,"n2","Doğru. ACS'de yanıtsız hastada dekompresif laparotomi hayat kurtarır."),
   A("Oligüri için 2 L daha sıvı yükle",-5,60,"n9","Daha fazla sıvı intraabdominal basıncı artırır; böbrek, akciğer ve bağırsak perfüzyonu kötüleşir."),
 ]),
 "n2":E("Dekompresyon","Tıbbi önlemlere rağmen İAB 25'te kaldı; dekompresif laparotomi yapıldı (geçici karın kapatma). İdrar çıkışı arttı, hava yolu basınçları düştü.\n\n**Akılda kalsın**\n- Risk: masif sıvı resüsitasyonu, pankreatit, travma, yanık, ileus.\n- **Mesane basıncı** ile İAB ölç: **>12 hipertansiyon**, **>20 + yeni organ disfonksiyonu = ACS**.\n- Bulgular: gergin karın, oligüri, artan hava yolu basınçları, hipotansiyon.\n- Tıbbi önlemler + **dekompresif laparotomi**; **aşırı sıvıdan kaçın**.\n\n*Kaynak: WSACS 2013 uzlaşı ve kılavuzu.*","good"),
 "n9":E("Çoklu organ yetmezliği","Ek sıvı sonrası İAB 34'e çıktı; anüri, hipoksemi ve bağırsak iskemisi gelişti.","bad"),
}))
Qs+=[Q("c60q1","Abdominal kompartman sendromunun tanımı hangisidir?",["İAB >12 mmHg","İAB >20 mmHg + yeni organ disfonksiyonu","Karında asit","İleus","Lökositoz"],1,"WSACS tanımı.","Yoğun bakım / Cerrahi"),
 Q("c60q2","İntraabdominal basınç en sık nasıl ölçülür?",["Santral venöz basınç","Mesane içi basınç","Mide pH","Rektal ısı","Arteriyel kateter"],1,"Mesane basıncı standart dolaylı ölçümdür.","Yoğun bakım / Cerrahi"),
 Q("c60q3","Tıbbi önlemlere yanıtsız abdominal kompartman sendromunda tedavi hangisidir?",["Ek sıvı","Diüretik tek başına","Dekompresif laparotomi","Gözlem","Antibiyotik"],2,"Cerrahi dekompresyon organ perfüzyonunu düzeltir.","Yoğun bakım / Cerrahi")]

P={"id":"ilk-nobet-6","title":"İlk Nöbet Vakaları — 6. Paket","desc":"Wernicke, hiperkalsemi, tansiyon pnömotoraks, SIADH, meningokoksemi, adrenal kriz, masif PE'ye bağlı arrest, mezenter iskemi, yangında CO + siyanür, abdominal kompartman sendromu.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 6. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 6. Paket","topic":"Acil tıp","order":6,"req":[2],"desc":"Metabolik, endokrin, travma ve resüsitasyon acillerinden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
