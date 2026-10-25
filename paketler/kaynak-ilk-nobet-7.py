import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 61 BOTULİZM
S.append(case("c61","Çift görme ve yutma güçlüğü — 46 yaşında kadın","Nöroloji / Toksikoloji",
 "46 yaşında kadın. İki gün önce evde konserve edilmiş fasulye yemiş. Dün çift görme ve göz kapaklarında düşüklük, bugün konuşma ve yutmada güçlük başlamış. Eşi de bulantı tarifliyor.",
 {"n1":N("Muayene","Bilinç tamamen açık. Bilateral pitoz, oftalmopleji, **dilate ve ışığa yavaş yanıtlı pupiller**, dizartri, disfaji. Kollarda proksimal güçsüzlük başlıyor (**inen, simetrik flask paralizi**). Duyu normal, ateş yok.","KB 128/78 · Nb 96 · SS 22 · SpO₂ %96",[
   T("Zorlu vital kapasite (FVC) / negatif inspiratuvar kuvvet",3,10,"**FVC 22 mL/kg**, NIF −28 cmH₂O.","Solunum yetmezliği sinsi gelişir; FVC <20 mL/kg veya NIF >−30 cmH₂O entübasyon ölçütleri arasında."),
   T("BT ve LP",0,60,"Normal.","İnme, Guillain-Barré (BOS'ta protein ↑, çıkan paralizi, duyu tutulumu) ayırıcı tanısı."),
   A("Klinik botulizm: **halk sağlığına hemen bildir ve antitoksin iste** (doğrulamayı bekleme); seri FVC/NIF ile yoğun bakım izlemi; aspirasyon önlemleri; eşini de değerlendir; şüpheli gıdayı sakla",4,20,"n2","Doğru. Antitoksin yalnız dolaşımdaki toksini nötralize eder; ne kadar erken o kadar etkili."),
   A("Myastenia gravis düşün — piridostigmin başla, poliklinikte izlem",-5,20,"n9","İnen simetrik paralizi + kraniyal sinir tutulumu + gıda öyküsü botulizmdir; ayaktan izlem solunum yetmezliği riski taşır."),
 ]),
 "n2":N("6 saat sonra","Disfaji arttı, hasta sekresyonlarını yutamıyor.","FVC 16 mL/kg · SpO₂ %93",[
   A("Elektif entübasyon ve mekanik ventilasyon; antitoksin uygulandı; aminoglikozid gibi nöromüsküler blokajı artıran ilaçlardan kaçın",4,20,"n3","Doğru. Antitoksin ilerlemeyi durdurur ama mevcut paraliziyi geri çevirmez; iyileşme haftalar sürer."),
   A("SpO₂ normal — entübasyonu bekle",-4,60,"n9","Nöromüsküler solunum yetmezliğinde SpO₂ geç düşer; FVC ve sekresyon kontrolü belirleyicidir."),
 ]),
 "n3":E("Uzun ama başarılı iyileşme","Hasta 4 hafta mekanik ventilasyonda kaldı ve tam iyileşti. Eşinde hafif tablo gelişti, antitoksin aldı.\n\n**Akılda kalsın**\n- **İnen, simetrik flask paralizi**; önce kraniyal sinirler (diplopi, pitoz, dizartri, disfaji); bilinç açık, ateş yok, duyu normal.\n- Kaynaklar: ev konservesi, yara, bebek (bal), iyatrojenik.\n- **Antitoksin erken** (doğrulama beklenmez) + bildirim.\n- **FVC/NIF** ile izle; SpO₂'ye güvenme.\n- Aminoglikozid ve Mg'den kaçın.\n\n*Kaynak: CDC 2021 botulizm klinik kılavuzu.*","good"),
 "n9":E("Solunum arresti","Hasta gece solunum yetmezliğiyle arrest oldu.","bad"),
}))
Qs+=[Q("c61q1","Botulizmin tipik paralizi paterni hangisidir?",["Çıkan, duyu kayıplı","İnen, simetrik, flask, kraniyal sinirlerle başlayan","Tek taraflı hemipleji","Spastik parapleji","Proksimalde yorgunlukla artan, sabah iyi"],1,"Guillain-Barré genellikle çıkan paralizi yapar.","Nöroloji / Toksikoloji"),
 Q("c61q2","Botulizm antitoksini için doğru ifade hangisidir?",["Laboratuvar doğrulaması beklenmeli","Klinik şüphede erken verilmeli; mevcut paraliziyi geri çevirmez, ilerlemeyi durdurur","Yalnız bebeklerde kullanılır","Paraliziyi hemen düzeltir","Gereksizdir"],1,"Erken antitoksin mekanik ventilasyon süresini kısaltır.","Nöroloji / Toksikoloji"),
 Q("c61q3","Nöromüsküler solunum yetmezliğini izlemede en uygun ölçüm hangisidir?",["SpO₂","FVC ve negatif inspiratuvar kuvvet","Kan şekeri","Nabız","Ateş"],1,"SpO₂ geç düşer.","Nöroloji / Toksikoloji")]

# 62 REFEEDING SENDROMU
S.append(case("c62","Beslenme başladıktan sonra kötüleşme — 70 yaşında erkek","Metabolik",
 "70 yaşında erkek, alkol kullanım bozukluğu. Yalnız yaşıyor, 10 günden beri neredeyse hiç yemek yememiş; bitkin halde bulundu (BMI 16). Dün servise yatırıldı, %10 dekstroz infüzyonu ve tam oral diyet başlandı. Bugün konfüze, nefes darlığı ve bacaklarda ödem var. Acil konsültasyon istendi.",
 {"n1":N("Konsültasyon","Konfüze, taşipneik, bilateral bazal raller, alt ekstremitelerde ödem. Kas güçsüzlüğü.","KB 104/62 · Nb 118 · SS 26 · SpO₂ %91",[
   T("Fosfor, K, Mg, glukoz",4,30,"**P 0,9 mg/dL**, **K 2,8**, **Mg 1,1**, glukoz 210.","Yeniden beslenme sendromu: hücre içine kayma ile hipofosfatemi, hipokalemi, hipomagnezemi; sıvı-tuz retansiyonu."),
   T("EKG",1,5,"Sinüs taşikardisi, uzun QT, U dalgaları.","Elektrolit bozukluklarına bağlı aritmi riski."),
   A("Beslenme ve dekstrozu yavaşlat (yüksek riskte ≈10 kcal/kg/gün, kademeli artış); **IV fosfat**, K ve Mg replasmanı; **tiamin** (beslenmeden önce ve ilk günlerde) ve multivitamin; sıvı/tuz kısıtla, kalp yetmezliği tedavisi; monitör ve günlük elektrolit",4,20,"n2","Doğru. Refeeding sendromu ölümcül aritmi ve kalp yetmezliği yapabilir."),
   A("Hipoglisemi olmasın diye dekstroz hızını artır",-4,20,"n9","Daha fazla karbonhidrat insülin salınımı ve hücre içine fosfat kaymasını artırır."),
 ]),
 "n2":E("Düzelme","48 saatte P 2,8, K 4,0, Mg 1,9; konfüzyon ve ödem geriledi. Beslenme 7 günde kademeli artırıldı.\n\n**Akılda kalsın**\n- Risk: BMI <16, 10 günden fazla az/hiç beslenme, son 3–6 ayda >%15 kilo kaybı, başlangıçta düşük K/P/Mg, alkol, kemoterapi.\n- Belirti: **hipofosfatemi** (ana bulgu), hipokalemi, hipomagnezemi, tiamin eksikliği, sıvı retansiyonu → aritmi, kalp yetmezliği, solunum yetmezliği, konfüzyon.\n- Önlem: **yavaş başla** (10 kcal/kg/gün), **tiamin önce**, elektrolitleri yerine koy ve izle.\n\n*Kaynak: NICE CG32 (2017 güncelleme); ASPEN 2020 uzlaşısı.*","good"),
 "n9":E("Aritmi","Hasta ventriküler aritmi ve solunum yetmezliği geliştirdi; yoğun bakıma alındı.","bad"),
}))
Qs+=[Q("c62q1","Yeniden beslenme sendromunun en karakteristik elektrolit bozukluğu hangisidir?",["Hipernatremi","Hipofosfatemi","Hiperkalemi","Hiperkalsemi","Hiperfosfatemi"],1,"İnsülin aracılı hücre içi fosfat kayması.","Metabolik"),
 Q("c62q2","Yüksek riskli hastada beslenmeye başlarken önerilen enerji miktarı hangisidir?",["10 kcal/kg/gün ile başlayıp kademeli artırmak","Hemen 35 kcal/kg/gün","Hiç beslememek","Yalnız %20 dekstroz","Yalnız protein"],0,"NICE: yüksek riskte en çok 10 kcal/kg/gün, aşırı yüksekte 5.","Metabolik"),
 Q("c62q3","Yeniden beslenmeden önce verilmesi gereken vitamin hangisidir?",["B12","Tiamin","D vitamini","K vitamini","A vitamini"],1,"Karbonhidrat yükü tiamin tüketimini artırır.","Metabolik")]

# 63 MYASTENİK KRİZ
S.append(case("c63","Güçsüzlük ve nefes darlığı — 41 yaşında kadın","Nöroloji",
 "41 yaşında kadın, myastenia gravis; piridostigmin kullanıyor. 3 gün önce idrar yolu enfeksiyonu için siprofloksasin başlanmış. Son 24 saatte konuşması burundan gelir gibi olmuş, yutarken boğuluyor, nefesi yetmiyor.",
 {"n1":N("Muayene","Pitoz, burundan konuşma, zayıf öksürük; boyun fleksörleri güçsüz. Cümle ortasında nefes alıyor. Pupiller normal, fasikülasyon yok, sekresyon artışı yok.","KB 128/80 · Nb 104 · SS 28 · SpO₂ %95",[
   T("FVC ve NIF",3,10,"**FVC 15 mL/kg**, NIF −18 cmH₂O.","Entübasyon ölçütleri: FVC <15–20 mL/kg, NIF >−20/−30 cmH₂O, artan solunum işi, bulbar yetmezlik."),
   T("Tek nefeste 1'den 20'ye sayma",1,1,"10'a kadar sayabiliyor.","Yatak başı kaba solunum rezervi göstergesi."),
   A("Myastenik kriz: yoğun bakım; **elektif entübasyon** (nondepolarizan blokerler düşük dozda, süksinilkoline yanıt öngörülemez); piridostigmini ventilasyon sırasında beklet; **IVIG (2 g/kg, 2–5 günde) veya plazmaferez**; siprofloksasini kes (MG'yi kötüleştirir), uygun antibiyotiğe geç",4,20,"n2","Doğru. Tetikleyiciler: enfeksiyon, ameliyat, ilaçlar (florokinolon, aminoglikozid, Mg, beta bloker)."),
   A("Piridostigmin dozunu iki katına çıkar ve izle",-3,30,"n3","Kolinerjik krize yol açabilir ve kriz tedavisi gecikir; solunum rezervi zaten kritik."),
 ]),
 "n3":N("1 saat sonra","Sekresyonlar arttı, solunum sıkıntısı derinleşti.","SpO₂ %89 · FVC 11 mL/kg",[
   A("Entübasyon + IVIG/plazmaferez; antikolinesterazı kes",2,20,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Krizden çıkış","Plazmaferez sonrası 8. günde ekstübe edildi; steroid ve immünsupresif planlandı.\n\n**Akılda kalsın**\n- Myastenik kriz: solunum kaslarının tutulumu; **bulbar bulgular** ve zayıf öksürük alarmdır.\n- **FVC/NIF ile izle**; SpO₂ geç düşer.\n- Tedavi: hava yolu/ventilasyon, **IVIG veya plazmaferez**, tetikleyiciyi kaldır.\n- MG'yi kötüleştiren ilaçlar: **florokinolon, aminoglikozid, makrolid, Mg, beta bloker, nöromüsküler blokerler**.\n- Kolinerjik kriz (aşırı piridostigmin): sekresyon artışı, fasikülasyon, miyozis, bradikardi.\n\n*Kaynak: MGFA 2020 uluslararası uzlaşı kılavuzu.*","good"),
 "n9":E("Solunum arresti","Hasta solunum arrestiyle acil entübe edildi; aspirasyon pnömonisi gelişti.","bad"),
}))
S[-1]["nodes"]["n3"]["opts"].append(A("Piridostigmini yeniden artır",-4,20,"n9","Kolinerjik kriz tabloyu ağırlaştırır."))
Qs+=[Q("c63q1","Myastenik krizde kısa vadeli immünomodülatör tedavi hangisidir?",["Yüksek doz piridostigmin","IVIG veya plazmaferez","Siprofloksasin","Beta bloker","Morfin"],1,"IVIG 2 g/kg veya plazmaferez.","Nöroloji"),
 Q("c63q2","Hangisi myasteni gravisi kötüleştirebilir?",["Seftriakson","Siprofloksasin","Parasetamol","Omeprazol","Heparin"],1,"Florokinolonlar, aminoglikozidler, makrolidler, Mg ve beta blokerler.","Nöroloji"),
 Q("c63q3","Myastenik krizde entübasyon kararında en yararlı ölçüm hangisidir?",["SpO₂","FVC (<15–20 mL/kg) ve NIF","Nabız","Ateş","Kan şekeri"],1,"Solunum rezervi ölçülerek karar verilir.","Nöroloji")]

# 64 GEBEDE KARDİYAK ARREST (amniyotik sıvı embolisi)
S.append(case("c64","Eylemde kollaps — 32 haftalık gebe","Kadın doğum / Resüsitasyon",
 "29 yaşında, 32 haftalık gebe. Erken doğum eylemiyle geldi; doğumhaneye taşınırken acilde ani nefes darlığı, siyanoz ve ardından bilinç kaybı gelişti. Nabız alınamıyor.",
 {"n1":N("0. dakika — arrest","Yanıtsız, solunum yok, nabız yok. Fundus göbeğin üzerinde.","Monitör: NEA",[
   A("Yüksek kaliteli KPR (standart el yeri); **manuel sol uterus yer değiştirme**; erken hava yolu (zor hava yolu ve aspirasyon riski); diyafram üstü damar yolu; adrenalin; kadın doğum ve neonatoloji ekibini çağır — **resüsitatif histerotomi** hazırlığı",4,2,"n2","Doğru. Uterus aortokaval basıyla KPR etkinliğini düşürür; ≥20 hafta gebelikte sol yer değiştirme şart."),
   A("Standart KPR; gebeliğe özel bir şey yapma",-3,4,"n2","Aortokaval bası nedeniyle KPR etkisiz kalır; perimortem sezaryen hazırlığı gecikti."),
 ]),
 "n2":N("4. dakika","KPR sürüyor, spontan dolaşım yok.","",[
   A("**Resüsitatif histerotomi (perimortem sezaryen)** — arrestin 4. dakikasında başla, bebeği 5. dakikada çıkar; KPR'yi kesintisiz sürdür; masif transfüzyon ve AFE için DİK yönetimi",4,5,"n3","Doğru. Uterusun boşaltılması anne resüsitasyonunu kolaylaştırır; amaç öncelikle annenin sağkalımıdır."),
   A("Ameliyathaneye transfer et, orada sezaryen yap",-4,15,"n9","Transfer KPR kalitesini bozar ve zaman kaybettirir; işlem resüsitasyon yerinde yapılır."),
 ]),
 "n3":E("Dolaşım döndü","Histerotomiden 2 dakika sonra spontan dolaşım döndü. Bebek neonatoloji ekibine teslim edildi. Annede DİK gelişti; fibrinojen ve kan ürünleriyle yönetildi. AFE tanısı klinik olarak kondu.\n\n**Akılda kalsın**\n- ≥20 hafta gebelikte arrest: **manuel sol uterus yer değiştirme**, standart KPR, erken hava yolu, diyafram üstü damar yolu.\n- **4. dakikada ROSC yoksa resüsitatif histerotomi**; doğum 5. dakikada.\n- İşlem **olay yerinde**, transfer yok.\n- AFE: ani hipoksi + kollaps + DİK; erken fibrinojen.\n\n*Kaynak: ERC 2021 özel durumlar (gebelik); AHA 2015 gebelikte arrest bilimsel bildirisi.*","good"),
 "n9":E("Anne ve bebek kaybı","Transfer ve gecikme nedeniyle anne ve bebek kaybedildi.","bad"),
}))
Qs+=[Q("c64q1","Gebede arrestte resüsitatif histerotomi ne zaman düşünülmelidir?",["30. dakikada","ROSC yoksa 4. dakikada başlayıp 5. dakikada doğum","Yalnız fetüs canlıysa","Ameliyathanede","Hiçbir zaman"],1,"Annenin resüsitasyonunu kolaylaştırmak için.","Kadın doğum / Resüsitasyon"),
 Q("c64q2","Gebelikte KPR sırasında uterus için doğru uygulama hangisidir?",["Sağa itmek","Manuel sol uterus yer değiştirme","Bacakları kaldırmak","Trendelenburg","Uteri sıkıştırmak"],1,"Aortokaval basıyı giderir.","Kadın doğum / Resüsitasyon"),
 Q("c64q3","Gebede arrestte damar yolu nereden açılmalıdır?",["Femoral ven","Diyaframın üstünden (kol/boyun)","Ayak sırtı","Tercih önemsiz","Yalnız IO tibia"],1,"Uterus inferior vena kavaya bası yapar.","Kadın doğum / Resüsitasyon")]

# 65 TOKSİK ŞOK SENDROMU
S.append(case("c65","Ateş, döküntü ve hipotansiyon — 21 yaşında kadın","Enfeksiyon",
 "21 yaşında kadın. Adet döneminin 3. günü; tampon kullanıyor. Dün yüksek ateş, kusma, ishal ve kas ağrısı başlamış; bugün baş dönmesi ve vücudunda kızarıklık var.",
 {"n1":N("Resüsitasyon alanı","Yaygın, güneş yanığı gibi **diffüz makülopapüler eritrodermi**, konjunktival hiperemi, çilek dili. Konfüze.","KB 74/40 · Nb 136 · SS 26 · Ateş 39,8",[
   T("Pelvik muayene",3,5,"Vajende **2 gündür takılı unutulmuş tampon**.","Kaynak kontrolü."),
   T("Laboratuvar",1,40,"Kreatinin 2,2, trombosit 85.000, CK 1800, AST/ALT yüksek.","Çoklu organ tutulumu (TSS tanı ölçütü)."),
   A("Tamponu çıkar (kaynak kontrolü); kültür; agresif sıvı + norepinefrin; IV **klindamisin** (toksin baskılama) + **vankomisin** (MRSA) ± beta-laktam; ağır olguda IVIG düşün; yoğun bakım",4,15,"n2","Doğru. TSS'de kaynak kontrolü + antitoksin etkili antibiyotik."),
   A("Viral döküntü ve gastroenterit — sıvı ve antiemetik",-5,30,"n9","Ateş + eritroderma + şok + çoklu organ tutulumu TSS'dir."),
 ]),
 "n2":E("Toksik şoktan çıkış","48 saatte vazopresör kesildi; 10. günde avuç içi ve ayak tabanlarında soyulma başladı.\n\n**Akılda kalsın**\n- Stafilokokal TSS: **ateş + diffüz eritrodermi + hipotansiyon + ≥3 organ tutulumu**; 1–2 hafta sonra **deskuamasyon**.\n- Kaynak: tampon, nazal tampon, cerrahi yara, yanık; streptokokal TSS'de yumuşak doku enfeksiyonu.\n- **Kaynağı çıkar**, sıvı/vazopresör, **klindamisin + vankomisin** (± beta-laktam), ağır olguda IVIG.\n\n*Kaynak: CDC TSS vaka tanımı; IDSA 2014.*","good"),
 "n9":E("Refrakter şok","Kaynak saatlerce yerinde kaldı; hasta çoklu organ yetmezliğine girdi.","bad"),
}))
Qs+=[Q("c65q1","Toksik şok sendromunda klindamisin eklenmesinin nedeni nedir?",["Böbrek koruması","Toksin üretimini baskılamak","Gram negatif kapsama","Antipiretik","Antiinflamatuvar değil"],1,"Protein sentezi inhibisyonu ile toksin üretimini azaltır.","Enfeksiyon"),
 Q("c65q2","Tampona bağlı TSS'de ilk ve en önemli girişimlerden biri hangisidir?",["Antihistaminik","Tamponun çıkarılması","Steroid","Kültür sonucunu beklemek","Antipiretik"],1,"Kaynak kontrolü esastır.","Enfeksiyon"),
 Q("c65q3","Stafilokokal TSS'nin geç bulgusu hangisidir?",["Avuç içi ve ayak tabanında deskuamasyon","Ense sertliği","Sarılık","Hemoptizi","Hematüri"],0,"1–2 hafta sonra görülür.","Enfeksiyon")]

# 66 PRES
S.append(case("c66","Baş ağrısı, görme kaybı ve nöbet — 33 yaşında kadın","Nöroloji",
 "33 yaşında kadın, 6 ay önce böbrek nakli olmuş; takrolimus kullanıyor. 2 gündür şiddetli baş ağrısı, bulanık görme; acilde jeneralize nöbet geçirdi.",
 {"n1":N("Postiktal dönem","Konfüze; **görme alanında kortikal körlük** (ışığı seçiyor, nesneleri göremiyor). Fokal motor bulgu yok.","KB 196/118 · Nb 98 · Ateş 37,0 · Glukoz 104",[
   T("Kontrastsız BT",1,25,"Kanama yok; oksipital beyaz cevherde hafif hipodansite.","BT normal olabilir."),
   T("Beyin MR (FLAIR)",3,60,"**Bilateral parieto-oksipital subkortikal vazojenik ödem**.","PRES ile uyumlu."),
   T("Takrolimus düzeyi, Mg",1,60,"Takrolimus yüksek, Mg 1,3.","Kalsinörin inhibitörü toksisitesi ve hipomagnezemi PRES riskini artırır."),
   A("Nöbet için benzodiazepin (gerekirse levetirasetam); **KB'yi kontrollü düşür** (IV labetalol/nikardipin; ilk saatlerde OAB'de ≈%20–25 azalma); Mg replasmanı; nefroloji ile takrolimusun dozunu azalt/değiştir",4,20,"n2","Doğru. PRES çoğunlukla nedeni düzeltilince geri dönüşlüdür."),
   A("Görme bozukluğu ve nöbet — tromboliz için inme koduna al",-4,20,"n9","Bilateral posterior vazojenik ödem ve hipertansiyon PRES'i düşündürür; tromboliz kanama riski taşır."),
 ]),
 "n2":E("Geri dönüş","KB kontrolü ve takrolimus düzenlemesiyle görme 48 saatte düzeldi; 2 hafta sonra MR'da ödem gerilemişti.\n\n**Akılda kalsın**\n- PRES: **baş ağrısı, görme bozukluğu (kortikal körlük), nöbet, ensefalopati** + çoğunlukla ağır hipertansiyon.\n- Nedenler: hipertansif acil, **eklampsi**, böbrek yetmezliği, **kalsinörin inhibitörleri**, kemoterapi, otoimmün hastalık.\n- **MR (FLAIR)**: bilateral parieto-oksipital vazojenik ödem.\n- Tedavi: **kontrollü KB düşüşü**, nöbet tedavisi, tetikleyiciyi kaldır, Mg.\n\n*Kaynak: Fugate & Rabinstein, Lancet Neurol 2015.*","good"),
 "n9":E("Komplikasyon","Gereksiz tromboliz sonrası oksipital kanama gelişti.","bad"),
}))
Qs+=[Q("c66q1","PRES'in tipik MR bulgusu hangisidir?",["Tek taraflı MCA infarktı","Bilateral parieto-oksipital vazojenik ödem","Subaraknoid kanama","Halka tarzı kontrastlanan lezyon","Hipokampal atrofi"],1,"Posterior beyaz cevherde FLAIR hiperintensitesi.","Nöroloji"),
 Q("c66q2","Hangi ilaç PRES ile ilişkilidir?",["Takrolimus","Parasetamol","Omeprazol","Amoksisilin","Metformin"],0,"Kalsinörin inhibitörleri (takrolimus, siklosporin).","Nöroloji"),
 Q("c66q3","PRES tedavisinin temeli hangisidir?",["Tromboliz","Kontrollü KB düşüşü + tetikleyiciyi kaldırmak + nöbet kontrolü","Antikoagülan","Yüksek doz steroid","Lomber ponksiyon"],1,"Çoğu olgu geri dönüşlüdür.","Nöroloji")]

# 67 PREEKLAMPSİ / EKLAMPSİ
S.append(case("c67","Baş ağrısı ve nöbet — 35 haftalık gebe","Kadın doğum",
 "24 yaşında, ilk gebeliği, 35 haftalık. 1 gündür şiddetli baş ağrısı, gözlerinin önünde ışık çakmaları, sağ üst kadran ağrısı. Acilde bekleme salonunda jeneralize nöbet geçirdi.",
 {"n1":N("Nöbet sırası","Jeneralize tonik-klonik nöbet sürüyor (2. dakika). Yüz ve ellerde ödem.","KB 178/116 · Nb 112 · SpO₂ %92",[
   T("İdrarda protein, trombosit, KCFT, kreatinin",1,30,"Protein +++, trombosit 92.000, AST 180, ALT 210, LDH 720.","HELLP bulguları da var."),
   A("Hasta sol yana, hava yolu ve O₂; **magnezyum sülfat 4–6 g IV, 15–20 dakikada**, ardından 1–2 g/saat infüzyon; ağır KB (≥160/110) için 30–60 dakika içinde antihipertansif (IV labetalol, IV hidralazin veya oral hızlı salınımlı nifedipin); kadın doğum — stabilizasyondan sonra doğum planı",4,10,"n2","Doğru. Eklampside ilk seçenek MgSO₄'tür (hem tedavi hem nöbet önleme)."),
   A("Diazepam ve fenitoin ile nöbeti kontrol et, magnezyum gerekmez",-3,20,"n2","Eklampside MgSO₄ nöbet tekrarını benzodiazepin ve fenitoinden daha iyi önler."),
 ]),
 "n2":N("Magnezyum infüzyonunun 6. saati","Nöbet tekrarlamadı. Hemşire, hastanın uykulu olduğunu ve diz reflekslerinin alınmadığını bildiriyor.","SS 9 · SpO₂ %90 · İdrar 15 mL/saat",[
   A("Magnezyum toksisitesi: infüzyonu durdur, **kalsiyum glukonat 1 g (%10, 10 mL) IV 10 dakikada**; solunum desteği; serum Mg; böbrek fonksiyonu",4,10,"n3","Doğru. Refleks kaybı, solunum depresyonu ve oligüri Mg toksisitesinin uyarı işaretleridir."),
   A("İnfüzyon hızını artır (nöbet tekrarlamasın)",-5,10,"n9","Mg toksisitesi solunum ve kardiyak arreste yol açar."),
 ]),
 "n3":E("Anne ve bebek iyi","Kalsiyum sonrası solunum düzeldi; Mg dozu böbrek fonksiyonuna göre ayarlandı. Hasta stabilize edildikten sonra sezaryenle doğurtuldu; bebek sağlıklı.\n\n**Akılda kalsın**\n- Preeklampsi: >20 hafta, **KB ≥140/90 + proteinüri veya organ tutulumu**; ağır özellikler: KB ≥160/110, baş ağrısı, görme bozukluğu, SÜK ağrısı, trombositopeni, karaciğer/böbrek bozukluğu, akciğer ödemi.\n- Eklampsi: **MgSO₄ 4–6 g yükleme, 1–2 g/saat** (24 saat).\n- Ağır KB → **30–60 dakikada** labetalol/hidralazin/nifedipin.\n- Mg toksisitesi: refleks kaybı, solunum depresyonu → **kalsiyum glukonat 1 g IV**.\n- Kesin tedavi **doğum**; postpartum 6 haftaya kadar görülebilir.\n\n*Kaynak: ACOG 2020 (No. 222) gestasyonel hipertansiyon ve preeklampsi.*","good"),
 "n9":E("Solunum arresti","Mg toksisitesine bağlı solunum ve kardiyak arrest gelişti.","bad"),
}))
Qs+=[Q("c67q1","Eklampside nöbet tedavisi ve tekrarını önlemede ilk seçenek hangisidir?",["Fenitoin","Diazepam","Magnezyum sülfat","Levetirasetam","Valproat"],2,"MgSO₄ 4–6 g yükleme, ardından 1–2 g/saat.","Kadın doğum"),
 Q("c67q2","Magnezyum toksisitesinin antidotu hangisidir?",["Nalokson","Kalsiyum glukonat","Flumazenil","Atropin","Protamin"],1,"Kalsiyum glukonat 1 g IV.","Kadın doğum"),
 Q("c67q3","Preeklampside ağır hipertansiyon eşiği hangisidir (tedavi 30–60 dakikada)?",["≥140/90","≥150/95","≥160/110","≥180/120","≥200/120"],2,"≥160/110 mmHg ağır hipertansiyondur.","Kadın doğum")]

# 68 METHEMOGLOBİNEMİ
S.append(case("c68","Oksijene yanıt vermeyen siyanoz — 24 yaşında erkek","Toksikoloji",
 "24 yaşında erkek. Bir partide “popper” (amil/izobütil nitrit) şişesinden içine çekmek yerine yanlışlıkla bir yudum içmiş. 30 dakika sonra baş ağrısı, baş dönmesi ve nefes darlığı başlamış; dudakları mor.",
 {"n1":N("Resüsitasyon alanı","Belirgin siyanoz; solunum sesleri normal. Rezervuarlı maskeyle O₂ verilmesine rağmen siyanoz düzelmiyor.","KB 118/70 · Nb 118 · SS 24 · **SpO₂ %85 (O₂'ye rağmen sabit)**",[
   T("Arteriyel kan gazı + CO-oksimetri",4,10,"**pO₂ 410 mmHg** (normal), **MetHb %34**; kan **çikolata kahvesi** renkte.","Satürasyon aralığı: normal pO₂ ama düşük SpO₂ → dishemoglobinemi."),
   T("G6PD öyküsü",1,2,"Bilinen G6PD eksikliği yok.","Metilen mavisi G6PD eksikliğinde etkisiz/hemolitik olabilir."),
   A("**Metilen mavisi 1–2 mg/kg IV 5 dakikada** (gerekirse 1 saat sonra tekrar); O₂; G6PD eksikliği veya yanıtsızlıkta askorbik asit/kan değişimi/HBO düşün",4,10,"n2","Doğru. Semptomatik veya MetHb >%20–30 olgularda metilen mavisi."),
   A("SpO₂ düşük — entübe et",-3,15,"n9","Sorun ventilasyon değil, oksijen taşıma; entübasyon MetHb'yi düzeltmez."),
 ]),
 "n2":E("Hızlı düzelme","Metilen mavisi sonrası 30 dakikada siyanoz kayboldu, MetHb %4. 6 saat izlendi.\n\n**Akılda kalsın**\n- **O₂'ye yanıt vermeyen siyanoz**, SpO₂ ≈ %85'te sabit, **normal pO₂** → methemoglobinemi.\n- Kan çikolata kahvesi; tanı **CO-oksimetri**.\n- Nedenler: **nitritler (popper), dapson, lokal anestezikler (benzokain, prilokain)**, nitratlı kuyu suyu (bebek).\n- Tedavi: **metilen mavisi 1–2 mg/kg IV**; G6PD eksikliğinde ve serotonerjik ilaç kullananlarda dikkat (serotonin sendromu).\n\n*Kaynak: Goldfrank's Toxicologic Emergencies.*","good"),
 "n9":E("Ağır hipoksi","MetHb %50'ye çıktı; hasta nöbet ve aritmi geliştirdi.","bad"),
}))
Qs+=[Q("c68q1","Methemoglobinemide tipik bulgu hangisidir?",["Düşük pO₂ + düşük SpO₂","Normal pO₂ + O₂'ye yanıtsız düşük SpO₂ (≈%85)","Yüksek SpO₂","Hipertermi","Bradipne"],1,"Satürasyon aralığı (saturation gap).","Toksikoloji"),
 Q("c68q2","Methemoglobineminin antidotu ve dozu hangisidir?",["Hidroksokobalamin 5 g","Metilen mavisi 1–2 mg/kg IV","Nalokson 0,4 mg","N-asetilsistein","Fizostigmin"],1,"Metilen mavisi NADPH-MetHb redüktaz yolunu hızlandırır.","Toksikoloji"),
 Q("c68q3","Metilen mavisinin kontrendike olduğu durum hangisidir?",["G6PD eksikliği","Hipertansiyon","Diyabet","Astım","Gebelik dışı her durum"],0,"G6PD eksikliğinde etkisiz ve hemolitik olabilir; serotonerjik ilaç kullananlarda da dikkat.","Toksikoloji")]

# 69 SICAK ÇARPMASI
S.append(case("c69","Koşu sırasında yığılma — 22 yaşında erkek","Çevresel aciller",
 "22 yaşında erkek, sıcak ve nemli bir günde yarı maratonun 18. kilometresinde konfüze olup yere yığılmış. Sağlık ekibi acile getirdi.",
 {"n1":N("Acil girişi","Ajite, anlamsız konuşuyor; deri sıcak, terli. Nöbet yok.","KB 96/54 · Nb 152 · SS 30 · **Rektal ısı 41,8 °C** · Glukoz 88",[
   T("Laboratuvar (Na, CK, böbrek, KCFT, koagülasyon)",1,40,"Na 134, CK 3200, kreatinin 1,7, AST 240, INR 1,4.","Rabdomiyoliz, AKI, karaciğer hasarı, DİK riski."),
   A("**Hemen soğuk suya daldırma** (buzlu su küveti; yoksa ıslatma + güçlü fan + buz paketleri); hedef 30 dakika içinde **<39 °C** (≈38,5–39'da dur); rektal ısı izlemi; IV sıvı; ajitasyon/titreme için benzodiazepin",4,15,"n2","Doğru. Sağkalımı belirleyen hipertermi süresidir: “önce soğut, sonra taşı”."),
   A("Parasetamol IV ve serin odada izlem",-5,30,"n9","Sıcak çarpmasında antipiretikler etkisizdir (set noktası değişmemiştir); hızlı aktif soğutma gerekir."),
 ]),
 "n2":E("Hızlı soğutma","Buzlu su küvetinde 15 dakikada rektal ısı 38,9 °C'ye indi; bilinç düzeldi. Rabdomiyoliz için sıvıyla izlendi, kreatinin normale döndü.\n\n**Akılda kalsın**\n- Sıcak çarpması: **≥40 °C + SSS disfonksiyonu** (konfüzyon, nöbet, koma).\n- **Egzersizle ilişkili**: genç, sporcu, asker; terleme olabilir.\n- **Soğuk suya daldırma en hızlı yöntem** (>0,15 °C/dk); hedef **30 dakikada <39 °C**.\n- **Antipiretik yok**.\n- Komplikasyonlar: rabdomiyoliz, AKI, karaciğer hasarı, DİK, hiponatremi (aşırı su).\n\n*Kaynak: Wilderness Medical Society 2019; ACSM 2023 egzersizle ilişkili sıcak çarpması.*","good"),
 "n9":E("Çoklu organ yetmezliği","Ateş 2 saat yüksek kaldı; DİK, karaciğer ve böbrek yetmezliği gelişti.","bad"),
}))
Qs+=[Q("c69q1","Egzersizle ilişkili sıcak çarpmasında en etkili soğutma yöntemi hangisidir?",["Parasetamol IV","Soğuk/buzlu suya daldırma","Serin odada bekleme","Yalnız soğuk IV sıvı","Antihistaminik"],1,"En hızlı soğutma hızını sağlar.","Çevresel aciller"),
 Q("c69q2","Sıcak çarpmasını sıcak bitkinliğinden ayıran temel özellik hangisidir?",["Terleme","SSS disfonksiyonu (konfüzyon, nöbet, koma)","Bulantı","Kas krampı","Taşikardi"],1,"Merkezi sinir sistemi tutulumu sıcak çarpmasını tanımlar.","Çevresel aciller"),
 Q("c69q3","Sıcak çarpmasında soğutma hedefi hangisidir?",["24 saatte normale","30 dakika içinde <39 °C","2 saatte 40 °C","Yalnız 41 °C altına","Soğutma gerekmez"],1,"Hipertermi süresi prognozu belirler; 38,5–39 °C'de soğutma durdurulur.","Çevresel aciller")]

# 70 YAĞ EMBOLİSİ SENDROMU
S.append(case("c70","Kırık sonrası hipoksi ve konfüzyon — 22 yaşında erkek","Ortopedi / Yoğun bakım",
 "22 yaşında erkek; 36 saat önce trafik kazasında sağ femur cisim kırığı oldu, ateliyle cerrahi bekliyor. Bugün nefes darlığı, huzursuzluk ve konfüzyon başladı.",
 {"n1":N("Servis konsültasyonu","Konfüze, taşipneik. **Aksilla, konjunktiva ve göğüs üst kısmında peteşiler**. Akciğerlerde ince raller.","KB 118/70 · Nb 124 · SS 30 · SpO₂ %86 · Ateş 38,4",[
   T("Akciğer grafisi",2,15,"Bilateral yaygın infiltrasyon (“kar fırtınası”).","ARDS benzeri tablo."),
   T("Kan gazı, trombosit, hemoglobin",1,20,"pO₂ 54, trombosit 98.000, Hb düşüyor.","Gurd ölçütleri: solunum yetmezliği, serebral bulgular, peteşi (majör) + minör ölçütler."),
   T("BT pulmoner anjiyografi",1,40,"Trombüs yok.","PE ayırıcı tanısı."),
   A("Yağ embolisi sendromu: destek tedavisi — O₂ (gerekirse NIV/entübasyon, akciğer koruyucu ventilasyon), sıvı dengesi, yoğun bakım; ortopedi ile **erken kırık stabilizasyonu**",4,20,"n2","Doğru. Özgül tedavi yok; destek ve erken fiksasyon esastır."),
   A("Pnömoni — yalnız antibiyotik ve servis izlemi",-4,20,"n9","Uzun kemik kırığı + hipoksi + nörolojik bulgu + peteşi triadı yağ embolisidir."),
 ]),
 "n2":E("Destekle iyileşme","Hasta 3 gün NIV ile desteklendi; stabil olunca intramedüller çivileme yapıldı. Nörolojik bulgular haftada geriledi.\n\n**Akılda kalsın**\n- Uzun kemik (özellikle femur) veya pelvis kırığından **24–72 saat sonra**.\n- Triad: **hipoksemi + nörolojik bulgular + peteşi** (aksilla, konjunktiva, üst gövde).\n- Tanı klinik (Gurd ölçütleri); PE dışlanır.\n- Tedavi **destekleyici**; önleme: **erken kırık stabilizasyonu**.\n\n*Kaynak: Kosova ve ark., Orthopedics 2015; Tintinalli.*","good"),
 "n9":E("Solunum yetmezliği","Hasta ağır ARDS ile entübe edildi; yoğun bakımda uzun kaldı.","bad"),
}))
Qs+=[Q("c70q1","Yağ embolisi sendromunun klasik triadı hangisidir?",["Ateş, sarılık, ağrı","Hipoksemi, nörolojik bulgular, peteşi","Hipotansiyon, JVD, kalp seslerinde azalma","Hematüri, böğür ağrısı, kitle","Öksürük, hemoptizi, kilo kaybı"],1,"Peteşiler sıklıkla aksilla ve konjunktivadadır.","Ortopedi / Yoğun bakım"),
 Q("c70q2","Yağ embolisi sendromu çoğunlukla ne zaman ortaya çıkar?",["İlk 1 saat","Kırıktan 24–72 saat sonra","2 hafta sonra","1 ay sonra","Yalnız ameliyat sırasında"],1,"Tipik latent dönem 24–72 saattir.","Ortopedi / Yoğun bakım"),
 Q("c70q3","Yağ embolisi sendromunu önlemede en etkili yaklaşım hangisidir?",["Profilaktik steroid (rutin)","Erken kırık stabilizasyonu","Heparin","Antibiyotik","Uzun süre traksiyon"],1,"Erken fiksasyon riski azaltır.","Ortopedi / Yoğun bakım")]

P={"id":"ilk-nobet-7","title":"İlk Nöbet Vakaları — 7. Paket","desc":"Botulizm, refeeding sendromu, myastenik kriz, gebede arrest (amniyotik sıvı embolisi), toksik şok sendromu, PRES, eklampsi, methemoglobinemi, sıcak çarpması, yağ embolisi.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 7. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 7. Paket","topic":"Acil tıp","order":7,"req":[2],"desc":"Nörolojik, obstetrik, toksikolojik ve çevresel acillerden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
