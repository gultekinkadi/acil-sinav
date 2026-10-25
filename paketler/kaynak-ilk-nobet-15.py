import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Önce **ilk değerlendirme** (muayene, monitör, damar yolu, oksijen) — gereksiz girişim puan kaybettirir.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 141 PNÖMONİ — düşük riskli, ayaktan
S.append(case("c141","Ateş ve balgamlı öksürük — 34 yaşında kadın","Enfeksiyon / Göğüs",
 "34 yaşında kadın, sağlıklı, ilaç alerjisi yok. 3 gündür ateş, sarı balgamlı öksürük, sağ yan ağrısı. Yemek yiyebiliyor, sıvı alabiliyor. Gebe değil.",
 {"n1":N("Muayene","Genel durumu iyi, oryante. Sağ alt zonda raller.","KB 122/76 · Nb 96 · SS 20 · SpO₂ %97 · Ateş 38,4",[
   T("Akciğer grafisi",2,15,"Sağ alt lobda sınırlı konsolidasyon; efüzyon yok.","Tanı."),
   T("CURB-65 / CRB-65",2,2,"Konfüzyon yok, SS <30, KB normal, yaş <65 (üre bakılmadan CRB-65 = **0**).","Düşük risk: ayaktan tedavi uygun."),
   T("Toraks BT",-2,30,"Sağ alt lob pnömonisi.","Komplike olmayan pnömonide gereksiz."),
   A("**Düşük şiddetli TKP**: ayaktan **amoksisilin 500 mg (ya da 1 g) günde 3 kez, 5 gün**; parasetamol, sıvı; **güvenlik ağı** (nefes darlığı, konfüzyon, düzelmeme → 48–72 saatte kontrol)",4,10,"n2","Doğru. NICE NG138: düşük şiddette 5 gün amoksisilin."),
   A("Moksifloksasin IV ve yatış",-3,30,"n9","Gereksiz yatış ve geniş spektrum; direnç ve yan etki."),
   A("Viral olabilir — antibiyotiksiz taburcu",-2,5,"n9","Radyolojik konsolidasyon + klinik → bakteriyel pnömoni tedavi edilir."),
 ]),
 "n2":E("Ayaktan iyileşme","Hasta 3. günde ateşsizleşti; 5 günlük tedaviyle iyileşti.\n\n**Akılda kalsın**\n- **CRB-65 / CURB-65 = 0–1**: düşük risk → **ayaktan tedavi** (sosyal durum, oral alım, komorbidite de göz önünde).\n- Düşük şiddette **amoksisilin, 5 gün**; penisilin alerjisinde doksisiklin/klaritromisin.\n- Gereksiz BT, yatış ve geniş spektrumdan kaçın.\n- **Güvenlik ağı**: kötüleşme belirtileri ve 48–72 saatte yeniden değerlendirme.\n\n*Kaynak: NICE NG138 (2019, güncelleme 2025); BTS TKP kılavuzu.*","good"),
 "n9":E("Uygunsuz tedavi","Hasta ya gereksiz yere 4 gün yattı (C. difficile ishali gelişti) ya da antibiyotiksiz kalıp 3 gün sonra kötüleşerek döndü.","bad"),
}))
Qs+=[Q("c141q1","CRB-65 = 0 olan sağlıklı erişkinde TKP tedavisi hangisidir?",["IV seftriakson + yatış","Ayaktan amoksisilin 5 gün","Moksifloksasin IV","Antibiyotiksiz izlem","Vankomisin"],1,"NICE NG138.","Enfeksiyon / Göğüs"),
 Q("c141q2","Düşük şiddetli TKP'de önerilen antibiyotik süresi nedir?",["3 gün","5 gün","14 gün","21 gün","6 hafta"],1,"Klinik yanıt varsa 5 gün yeterli.","Enfeksiyon / Göğüs"),
 Q("c141q3","Penisilin alerjisinde düşük şiddetli TKP için alternatif hangisidir?",["Doksisiklin veya klaritromisin","Amoksisilin-klavulanat","Sefaleksin","Nitrofurantoin","Metronidazol"],0,"NICE önerisi.","Enfeksiyon / Göğüs")]

# 142 DİYABETİK KETOASİDOZ — öglisemik (SGLT2i)
S.append(case("c142","Bulantı, karın ağrısı, kan şekeri “normal” — 56 yaşında erkek","Endokrin",
 "56 yaşında erkek, tip 2 diyabet; metformin + **empagliflozin**. 3 gün önce laparoskopik kolesistektomi; o günden beri az yiyor. Bulantı, kusma, karın ağrısı ve hızlı solunum. “Şekerim 190, normal” diyor.",
 {"n1":N("Muayene","Halsiz, **derin-hızlı solunum**, mukozalar kuru. Karın yumuşak, ameliyat yerleri temiz.","KB 104/66 · Nb 112 · SS 28 · SpO₂ %98 · Kapiller glukoz 192",[
   T("Venöz kan gazı",3,10,"**pH 7,11, HCO₃ 8**, anyon açığı 26.","Yüksek anyon açıklı metabolik asidoz."),
   T("Kapiller/serum keton (β-hidroksibütirat)",3,10,"**5,8 mmol/L**.","Normal glukozda ketoasidoz → **öglisemik DKA**."),
   T("Laktat, lipaz, karın BT",-1,60,"Laktat 1,4; lipaz normal; BT'de cerrahi komplikasyon yok.","Ameliyat sonrası komplikasyon dışlanır ama tanı keton ve kan gazıyla konur."),
   A("**SGLT2 inhibitörü ilişkili öglisemik DKA**: empagliflozini kes; izotonik sıvı; **sabit doz IV insülin 0,1 Ü/kg/saat** + **en baştan %5–10 dekstroz** (glukoz düşmesin); K izlemi/replasmanı (K <3,5 ise insülinden önce); keton ve kan gazıyla takip; endokrinoloji, yoğun bakım/yakın izlem",4,20,"n2","Doğru. Glukoz normal diye insülin kesilmez; dekstrozla birlikte verilir."),
   A("Glukoz 192 — DKA olamaz; antiemetik ve sıvı, taburcu",-5,10,"n9","Öglisemik DKA kaçırıldı."),
   A("İnsülin infüzyonu, dekstroz yok",-2,20,"n3","Glukoz hızla düşer, hipoglisemi; insülin erken kesilmek zorunda kalınır, asidoz düzelmez."),
 ]),
 "n3":N("2 saat sonra","Glukoz 68 mg/dL, pH 7,14.","KB 110/70 · Nb 100",[
   A("İnsülini sürdür, **%10 dekstroz** ekle",2,10,"n4","Doğru düzeltme."),
   A("İnsülini kes",-4,10,"n9","Ketoasidoz derinleşir."),
 ]),
 "n2":E("Düzelme","18 saatte keton <0,6, pH 7,33; hasta oral beslenmeye geçti, SC insüline geçildi. SGLT2 inhibitörü kalıcı kesildi.\n\n**Akılda kalsın**\n- **Öglisemik DKA**: glukoz <250 mg/dL ama **keton ↑ + asidoz**; SGLT2 inhibitörü, açlık, cerrahi, gebelik, alkol.\n- Tanı: **kan gazı + keton** (glukoz değil).\n- Tedavi: sıvı, **sabit doz insülin + baştan dekstroz**, K; SGLT2i kes.\n- Ameliyat öncesi SGLT2i **3 gün önce** (ertugliflozin 4 gün) kesilmeli.\n\n*Kaynak: JBDS 2023 DKA kılavuzu; ADA 2024 hiperglisemik krizler uzlaşı raporu.*","good"),
 "n4":E("Gecikmeli düzelme","Dekstroz eklendikten sonra asidoz düzeldi; hasta bir gün fazla yoğun bakımda kaldı.","mid"),
 "n9":E("Ağır asidoz","Hasta 12 saat sonra pH 6,9 ile döndü; yoğun bakımda entübe edildi.","bad"),
}))
Qs+=[Q("c142q1","Öglisemik DKA'nın en sık ilaç nedeni hangisidir?",["Metformin","SGLT2 inhibitörleri","DPP-4 inhibitörleri","Sülfonilüre","GLP-1 agonisti"],1,"Empagliflozin, dapagliflozin vb.","Endokrin"),
 Q("c142q2","Öglisemik DKA tedavisinde farklı olan nedir?",["İnsülin verilmez","İnsülinle birlikte en baştan dekstroz verilir","Bikarbonat zorunlu","Sıvı kısıtlanır","Potasyum verilmez"],1,"Glukoz düşmeden keton temizlenir.","Endokrin"),
 Q("c142q3","DKA tanısında en belirleyici testler hangileridir?",["Yalnız glukoz","Kan gazı ve keton","HbA1c","Lipaz","Troponin"],1,"Glukoz normal olabilir.","Endokrin")]

# 143 HİPERNATREMİ
S.append(case("c143","Bakımevinden gelen uykulu hasta — 88 yaşında kadın","Metabolik / Geriatri",
 "88 yaşında kadın, ileri demans, bakımevinde yaşıyor. 5 gündür ateş ve az sıvı alımı; bugün uyandırmakta zorlanmışlar. Yaklaşık 50 kg.",
 {"n1":N("Muayene","GKS 11, mukozalar çok kuru, deri turgoru azalmış. Sağ bazalde raller.","KB 86/50 · Nb 118 · SS 24 · SpO₂ %93 · Ateş 38,3 · Kapiller glukoz 168",[
   T("Na, K, üre, kreatinin, osmolalite",3,40,"**Na 166**, K 3,6, üre 128, kreatinin 2,0; serum osm 352.","Hipovolemik hipernatremi; >48 saat → kronik."),
   T("Akciğer grafisi, kültürler",2,30,"Sağ alt lob pnömonisi.","Altta yatan neden (sıklıkla enfeksiyon + su alamama)."),
   A("Önce **şok/hipovolemi**: **izotonik kristaloid** bolusları (KB ve perfüzyon düzelene kadar); sonra **hipotonik sıvı** (%5 dekstroz ya da %0,45 NaCl / enteral su) ile serbest su açığını kapat — **24 saatte ≤10–12 mmol/L** düşüş; 4–6 saatte bir Na; **pnömoni tedavisi** (sepsis bulgusunda 1 saatte antibiyotik)",4,20,"n2","Doğru. Su açığı ≈ 0,45 × 50 × (166/140 − 1) ≈ 4 L; 48 saate yayılır."),
   A("Hemen 4 L %5 dekstroz, 6 saatte",-4,20,"n9","Kronik hipernatremide hızlı düzeltme serebral ödem riski; ayrıca şok önce izotonikle düzeltilmeli."),
   A("Na çok yüksek — SF verme, yalnız oral su",-3,20,"n9","Hipotansif, bilinç bozuk hasta oral alamaz; perfüzyon önceliklidir."),
 ]),
 "n2":E("Düzelme","İlk 24 saatte Na 166 → 156, 72 saatte 144; bilinç başlangıç düzeyine döndü, pnömoni tedavi edildi.\n\n**Akılda kalsın**\n- Yaşlı/demanslı hastada hipernatremi = **su alamama** (+ ateş, enfeksiyon, diürez).\n- Önce **perfüzyon (izotonik)**, sonra **serbest su**.\n- **Serbest su açığı** = TBW × (Na/140 − 1); TBW: yaşlı kadında ≈0,45 × kg.\n- Kronik hipernatremide **≈10–12 mmol/L/24 saat** sınırı (akutta daha hızlı olabilir).\n- Altta yatan nedeni tedavi et.\n\n*Kaynak: Adrogué & Madias, NEJM 2000; ESE 2014 / sodyum bozuklukları derlemeleri.*","good"),
 "n9":E("Komplikasyon","Hızlı/uygunsuz düzeltme sonrası nöbet ve bilinç kötüleşmesi gelişti ya da şok derinleşti.","bad"),
}))
Qs+=[Q("c143q1","Hipovolemik ve hipotansif hipernatremik hastada ilk sıvı hangisidir?",["%5 dekstroz","İzotonik kristaloid","%3 NaCl","Albümin zorunlu","Sıvı verilmez"],1,"Önce perfüzyon.","Metabolik / Geriatri"),
 Q("c143q2","Kronik hipernatremide düzeltme hızı yaklaşık ne olmalıdır?",["24 saatte ≤10–12 mmol/L","1 saatte 10 mmol/L","24 saatte 30 mmol/L","Hız önemsiz","Hemen normale"],0,"Serebral ödem riski.","Metabolik / Geriatri"),
 Q("c143q3","Serbest su açığı formülü hangisidir?",["TBW × (Na/140 − 1)","Kilo × 0,1","(Na − 140) × 2","TBW × Na","Kilo/Na"],0,"TBW cinsiyet ve yaşa göre.","Metabolik / Geriatri")]

# 144 SVT — süt çocuğu
S.append(case("c144","Hızlı soluyan, emmeyen bebek — 2 aylık erkek","Çocuk / Kardiyoloji",
 "2 aylık erkek bebek. Annesi 6 saattir emmediğini, huzursuz ve terli olduğunu söylüyor. Ateş yok. Yaklaşık 5 kg.",
 {"n1":N("Muayene","Huzursuz, soluk ama tepki veriyor. Kapiller dolum 2 sn, nabızlar iyi. Karaciğer kot altında 2 cm.","Nb 290 (düzenli) · SS 56 · SpO₂ %96 · Ateş 36,9",[
   T("12 derivasyonlu EKG",3,5,"**Dar QRS, düzenli taşikardi 290/dk**, P dalgası görülmüyor, hız değişkenliği yok.","Bebekte >220/dk dar QRS → SVT (sinüs taşikardisi değil)."),
   A("**Stabil SVT (bebek)**: vagal manevra — **yüze buzlu su torbası** 10–15 sn (göze bası yok); yanıt yoksa **adenozin 0,1 mg/kg (0,5 mg) hızlı IV bolus + hızlı SF yıkama** (proksimal damar), ikinci doz 0,2 mg/kg (en çok 12 mg); defibrilatör pedleri hazır",4,10,"n2","Doğru. Stabil SVT'de vagal → adenozin."),
   A("Ateş ve sepsis sanılarak 20 mL/kg sıvı bolusu ve antibiyotik",-2,20,"n3","Sinüs taşikardisi bu hızda ve sabit olmaz; tanı EKG'de."),
   A("Verapamil 0,1 mg/kg IV",-5,5,"n9","Bebeklerde verapamil ağır hipotansiyon ve arreste yol açar — kontrendike."),
 ]),
 "n3":N("Kötüleşme","Bebek letarjik, kapiller dolum 4 sn, nabızlar zayıf.","Nb 290 · SpO₂ %92",[
   A("**Senkronize kardiyoversiyon 0,5–1 J/kg** (yanıtsızsa 2 J/kg); sedasyon geciktirmeyecekse",2,5,"n4","Instabil SVT."),
   A("Bir sıvı bolusu daha",-3,10,"n9","Ritim düzeltilmedikçe kalp yetmezliği ilerler."),
 ]),
 "n2":E("Sinüs ritmi","Buzlu su başarısız oldu; adenozin 0,5 mg ile SVT sonlandı. EKG'de preeksitasyon yoktu; çocuk kardiyolojisi tedavi planladı.\n\n**Akılda kalsın**\n- Bebekte dar QRS **>220/dk** (çocukta >180) ve **sabit hız** → SVT.\n- Bebekler bulgu vermez: **emmeme, huzursuzluk, terleme**; saatler sonra kalp yetmezliği.\n- Stabil: **buzlu su (dalış refleksi)** → **adenozin 0,1 mg/kg** (≤6 mg) → **0,2 mg/kg** (≤12 mg).\n- Instabil: **senkronize kardiyoversiyon 0,5–1 → 2 J/kg**.\n- **<1 yaşta verapamil yok**.\n\n*Kaynak: ERC 2021 pediatrik yaşam desteği; AHA PALS 2020.*","good"),
 "n4":E("Geç kardiyoversiyon","Kardiyoversiyonla sinüs ritmi sağlandı; bebek kalp yetmezliği nedeniyle 2 gün yoğun bakımda kaldı.","mid"),
 "n9":E("Arrest","Bebek bradikardi ve arreste girdi; resüsitasyonla döndürüldü.","bad"),
}))
Qs+=[Q("c144q1","Bebekte SVT'de adenozin ilk dozu nedir?",["0,01 mg/kg","0,1 mg/kg (en çok 6 mg)","1 mg/kg","6 mg sabit","0,5 mg/kg"],1,"İkinci doz 0,2 mg/kg (≤12 mg).","Çocuk / Kardiyoloji"),
 Q("c144q2","Bebeklerde kontrendike olan antiaritmik hangisidir?",["Adenozin","Verapamil","Amiodaron","Senkronize kardiyoversiyon","Buzlu su"],1,"Ağır hipotansiyon/arrest riski.","Çocuk / Kardiyoloji"),
 Q("c144q3","Bebekte vagal manevra olarak hangisi uygulanır?",["Göz küresine bası","Yüze buzlu su torbası","Karotis masajı","Valsalva","Rektal uyarı"],1,"Dalış refleksi; göze bası yapılmaz.","Çocuk / Kardiyoloji")]

# 145 ZONA — oftalmik
S.append(case("c145","Alında döküntü ve göz ağrısı — 71 yaşında erkek","Enfeksiyon / Göz",
 "71 yaşında erkek. 4 gündür sol alında yanma; 2 gündür sol alın ve saçlı deride kümeler hâlinde su dolu kabarcıklar. Bugün sol gözde kızarıklık ve batma. Bağışıklık baskılayıcı ilaç kullanmıyor.",
 {"n1":N("Muayene","Sol V1 dermatomunda orta hattı geçmeyen **grup veziküller**, **burun ucunda vezikül (Hutchinson bulgusu)**. Sol gözde konjonktival hiperemi; görme 0,7. Ateş yok, genel durum iyi.","KB 138/84 · Nb 82 · SpO₂ %98 · Ateş 36,9",[
   T("Floresein ile göz muayenesi",2,10,"Korneada **dendritiform (psödodendrit)** boyanma.","Göz tutulumu var."),
   A("**Herpes zoster oftalmikus**: **oral valasiklovir 1 g günde 3 kez, 7 gün** (ya da asiklovir 800 mg günde 5 kez); **aynı gün göz hekimi** (yarık lamba, keratit/üveit); analjezi; **topikal steroidi göz hekimi kararı olmadan verme**",4,10,"n2","Doğru. Hutchinson bulgusu göz tutulumu riskini artırır; erken antiviral ve oftalmoloji."),
   A("Topikal steroidli göz damlası + asiklovir krem",-4,10,"n9","Göz hekimi değerlendirmesi olmadan steroid ve topikal antiviral tek başına uygun değil."),
   A("Analjezik, döküntü 72 saati geçti — antiviral gereksiz",-3,5,"n9","Göz tutulumunda ve yeni lezyon çıkarken 72 saatten sonra da antiviral verilir."),
 ]),
 "n2":E("Görme korundu","Göz hekimi keratit ve hafif ön üveit saptayarak tedaviyi düzenledi; görme 0,9'a yükseldi.\n\n**Akılda kalsın**\n- **Hutchinson bulgusu** (burun ucu-yanı: nazosiliyer sinir) → göz tutulumu riski yüksek.\n- HZO: **oral antiviral** (valasiklovir 1 g × 3 / asiklovir 800 mg × 5, 7 gün) ideal **72 saat içinde**, göz tutulumunda sonra da; **aynı gün göz hekimi**.\n- **İmmünsüpresyon, yaygın/dissemine zona, görmeyi tehdit eden tablo, SSS tutulumu** → **IV asiklovir**.\n- Topikal steroid yalnız göz hekimince.\n\n*Kaynak: AAO; CDC zona klinik özeti; Am Fam Physician 2011 (HZO).*","good"),
 "n9":E("Görme kaybı","Tedavi gecikti; stromal keratit ve sekonder glokom gelişti, görme kalıcı olarak azaldı.","bad"),
}))
Qs+=[Q("c145q1","Hutchinson bulgusu neyi gösterir?",["Kulak tutulumu","Nazosiliyer sinir tutulumu — göz tutulumu riski","Sistemik yayılım","Bakteriyel süperenfeksiyon","Postherpetik nevralji"],1,"Burun ucunda vezikül.","Enfeksiyon / Göz"),
 Q("c145q2","Bağışıklığı normal HZO hastasında antiviral tedavi hangisidir?",["Oral valasiklovir 1 g günde 3 kez, 7 gün","Topikal asiklovir tek başına","Oseltamivir","IV gansiklovir","Antiviral gerekmez"],0,"Göz hekimi ile birlikte.","Enfeksiyon / Göz"),
 Q("c145q3","Zonada IV asiklovir endikasyonu hangisidir?",["Tek dermatom, sağlıklı genç","İmmünsüpresyon veya dissemine zona","Hafif kaşıntı","Postherpetik ağrı","72 saati geçmiş tek lezyon"],1,"Görmeyi tehdit eden ve SSS tutulumu da.","Enfeksiyon / Göz")]

# 146 GİS PERFORASYONU — peptik ülser
S.append(case("c146","Ani başlayan şiddetli karın ağrısı — 49 yaşında erkek","Genel cerrahi",
 "49 yaşında erkek. Bel ağrısı için 2 haftadır yüksek doz ibuprofen kullanıyor, sigara içiyor. 3 saat önce epigastriumda **bıçak saplanır tarzda ani** ağrı başladı, tüm karına yayıldı.",
 {"n1":N("Muayene","Hareketsiz yatıyor, dizleri karnına çekik. Karın **tahta gibi sert** (yaygın defans), rebound; karaciğer matitesi silinmiş.","KB 104/66 · Nb 118 · SS 24 · SpO₂ %97 · Ateş 37,6",[
   T("Ayakta akciğer grafisi",2,15,"**Sağ diyafram altında serbest hava**.","Duyarlılığı ≈%70–80; negatifse BT."),
   T("Kontrastlı abdominal BT",2,30,"Serbest hava ve sıvı; duodenum bulbus ön duvarında defekt.","Tanı ve lokalizasyon."),
   T("Lipaz, hemogram, laktat",1,30,"Lipaz hafif yüksek; lökosit 16.000; laktat 2,4.","Perforasyonda lipaz hafif artabilir — pankreatitle karıştırma."),
   A("**Perfore peptik ülser**: aç bırak, **NG dekompresyon**, IV sıvı, analjezi; **IV PPI**; **geniş spektrumlu antibiyotik** (ör. piperasilin-tazobaktam ya da seftriakson + metronidazol); **acil genel cerrahi** (onarım/omentopeksi)",4,15,"n2","Doğru. Erken cerrahi kaynak kontrolü mortaliteyi azaltır."),
   A("Akut pankreatit — sıvı, analjezi, servise yatış",-4,20,"n9","Lipazdaki hafif artış perforasyonda da görülür; serbest hava var."),
   A("NSAİİ ile analjezi, antasit ve gözlem",-5,10,"n9","Peritonit bulguları ve NSAİİ öyküsü — perforasyon dışlanmalı."),
 ]),
 "n2":E("Cerrahi onarım","Laparoskopik primer onarım ve omentopeksi yapıldı; H. pylori testi pozitif, eradikasyon tedavisi verildi.\n\n**Akılda kalsın**\n- Ani “bıçak saplanır” epigastrik ağrı + **tahta karın** → **perforasyon**.\n- Risk: **NSAİİ, sigara, H. pylori**, steroid, yaşlılık.\n- **Ayakta akciğer grafisi** (serbest hava) → negatif ama şüphe sürerse **BT**.\n- Aç bırak, **NG**, sıvı, **IV PPI**, **antibiyotik**, **acil cerrahi**.\n\n*Kaynak: WSES 2020 perfore peptik ülser kılavuzu.*","good"),
 "n9":E("Septik şok","Tanı gecikti; hasta peritonit ve septik şokla yoğun bakıma alındı.","bad"),
}))
Qs+=[Q("c146q1","Perfore peptik ülser şüphesinde ilk görüntüleme hangisidir?",["Ayakta akciğer grafisi (serbest hava)","MR","Endoskopi","Baryumlu grafi","Sintigrafi"],0,"Negatifse BT.","Genel cerrahi"),
 Q("c146q2","Peptik perforasyonda hangisi kontrendikedir?",["NG dekompresyon","Endoskopi (tanı için)","IV PPI","Antibiyotik","Cerrahi konsültasyon"],1,"Hava insüflasyonu perforasyonu büyütür.","Genel cerrahi"),
 Q("c146q3","Peptik ülser perforasyonu için risk faktörü hangisidir?",["NSAİİ kullanımı","Düşük tuzlu diyet","Statin","Metformin","D vitamini"],0,"Sigara ve H. pylori de.","Genel cerrahi")]

# 147 AKUT ARTER — diz çıkığı sonrası popliteal arter yaralanması
S.append(case("c147","Motosiklet kazası, diz yaralanması — 28 yaşında erkek","Travma / Vasküler",
 "28 yaşında erkek. Motosikletten düşüp sağ dizini çarpmış. Olay yerinde dizi “yerinden çıkmış”, paramedik çekişle düzeltmiş. Dizde şişlik ve ağrı.",
 {"n1":N("Muayene","Sağ diz belirgin şiş, **çok yönlü instabilite**. Sağ ayak sıcak; dorsalis pedis ve posterior tibial nabızlar **zayıf ama alınıyor**. Peroneal sinir alanında hafif uyuşma.","KB 132/80 · Nb 98 · SS 18 · SpO₂ %98",[
   T("Ayak bileği-kol indeksi (ABI)",3,10,"Sağ **ABI 0,72**; sol 1,1.","**ABI <0,9** → arter yaralanması → BT anjiyografi."),
   T("Diz grafisi",1,15,"Eklem redükte; tibial platoda küçük avulsiyon parçası.","Kendiliğinden redükte olmuş çıkık sık gözden kaçar."),
   A("**Redükte diz çıkığı + ABI <0,9**: **BT anjiyografi**, **vasküler cerrahi** ve ortopedi acil; uzun bacak ateli; seri nörovasküler muayene; kompartman sendromu izlemi",4,20,"n2","Doğru. Nabzın alınması popliteal arter yaralanmasını dışlamaz."),
   A("Nabızlar var — diz ateli, ertesi gün ortopedi polikliniği",-5,10,"n9","İntimal yırtık saatler içinde tromboza ilerler; 6–8 saati geçen iskemide amputasyon riski."),
 ]),
 "n2":E("Ekstremite kurtarıldı","BTA'da popliteal arterde intimal yırtık ve kısmi tromboz saptandı; vasküler cerrahi bypass yaptı, profilaktik fasyotomi uygulandı.\n\n**Akılda kalsın**\n- **Diz çıkığı** (çoğu kendiliğinden redükte) → **popliteal arter yaralanması** riski yüksek.\n- **Nabızlar alınıyor diye dışlama**: **ABI** ölç; **<0,9 → BT anjiyografi**; **kesin bulgular** (nabızsızlık, aktif kanama, büyüyen hematom, üfürüm/thrill) → doğrudan ameliyathane.\n- Akut ekstremite iskemisi: **6 P** (ağrı, solukluk, nabızsızlık, parestezi, paralizi, soğukluk); duyu/motor kaybı = acil revaskülarizasyon.\n- Reperfüzyon sonrası **kompartman sendromu**.\n\n*Kaynak: EAST 2012 ekstremite vasküler yaralanma kılavuzu; ESVS 2020 akut ekstremite iskemisi.*","good"),
 "n9":E("Amputasyon","Ertesi sabah ayak soğuk ve nabızsızdı; geç revaskülarizasyona rağmen diz altı amputasyon gerekti.","bad"),
}))
Qs+=[Q("c147q1","Diz çıkığı sonrası nabızları alınan hastada arter yaralanmasını taramak için ne yapılır?",["Hiçbir şey","ABI ölçümü; <0,9 ise BT anjiyografi","Yalnız grafi","D-dimer","EMG"],1,"Nabız varlığı yaralanmayı dışlamaz.","Travma / Vasküler"),
 Q("c147q2","Arter yaralanmasının 'kesin bulgusu' hangisidir?",["Nabızsızlık veya aktif pulsatil kanama","Hafif şişlik","Ekimoz","Ağrı","Uyuşma tek başına"],0,"Doğrudan cerrahi.","Travma / Vasküler"),
 Q("c147q3","Revaskülarizasyon sonrası izlenmesi gereken komplikasyon hangisidir?",["Kompartman sendromu","Pnömotoraks","Hipoglisemi","Menenjit","Pankreatit"],0,"Reperfüzyon ödemi.","Travma / Vasküler")]

# 148 VENTRİKÜLER FİBRİLASYON — tanıklı arrest
S.append(case("c148","Acil bekleme salonunda yığılma — 59 yaşında erkek","Resüsitasyon",
 "59 yaşında erkek. Göğüs ağrısı nedeniyle triajda beklerken yığıldı. Hemşire yanıtsız ve solunumu olmadığını, nabız alınamadığını bildirdi; hasta resüsitasyon odasına alındı, KPR başladı.",
 {"n1":N("Arrest","Yanıtsız, solunum yok, nabız yok. Pedler takıldı: **ventrikül fibrilasyonu**.","Monitör: kaba VF",[
   A("**Hemen defibrilasyon** (bifazik 150–200 J veya cihaz önerisi), şoktan hemen sonra **2 dakika KPR** (göğüs basısına ara vermeden); ritim kontrolü",4,2,"n2","Doğru. Şoklanabilir ritimde en önemli girişim erken defibrilasyon."),
   A("Önce entübasyon, sonra şok",-4,5,"n9","Defibrilasyonu geciktirir; ileri hava yolu bekleyebilir."),
   A("Önce adrenalin 1 mg IV, sonra şok",-3,3,"n9","Şoklanabilir ritimde adrenalin 3. şoktan sonra verilir."),
 ]),
 "n2":N("3. şoktan sonra","Üç şok ve 6 dakika KPR sonrası VF sürüyor. Damar yolu açıldı.","Monitör: VF",[
   A("**Adrenalin 1 mg IV** + **amiodaron 300 mg IV**; KPR'ye ara vermeden devam; geri döndürülebilir nedenler (4H/4T); EtCO₂ izlemi",4,2,"n3","Doğru. ERC: 3. şoktan sonra adrenalin ve amiodaron."),
   A("Amiodaron 150 mg ve lidokain birlikte",-1,2,"n3","İlk amiodaron dozu 300 mg'dır."),
   A("Şoklar işe yaramadı — KPR'yi sonlandır",-5,1,"n9","Refrakter VF'de resüsitasyon sürer."),
 ]),
 "n3":N("Refrakter VF","5. şoktan sonra hâlâ VF. EtCO₂ 22 mmHg. Göğüs ağrısı ile gelmişti.","Monitör: VF",[
   A("**Amiodaron 150 mg** (5. şoktan sonra); **ped yerini değiştir (ön-arka)**, gerekiyorsa çift ardışık defibrilasyon (kurumda varsa); adrenalin 3–5 dakikada bir; koroner oklüzyon olasılığı için kardiyoloji (ROSC sonrası acil anjiyo)",4,3,"n4","Doğru. DOSE-VF: vektör değişikliği ve DSED refrakter VF'de sağkalımı artırdı."),
   A("Aynı pedlerle aynı enerjide sürdür, başka bir şey yapma",-1,3,"n5","Refrakter VF'de seçenekler kullanılmalı."),
 ]),
 "n4":E("ROSC","Ön-arka ped pozisyonuyla 6. şoktan sonra ROSC sağlandı; EKG'de anterior STEMI; acil anjiyografide LAD açıldı. Hedefli sıcaklık yönetimi ile iyi nörolojik sonuçla taburcu oldu.\n\n**Akılda kalsın**\n- VF/nabızsız VT: **erken defibrilasyon + kesintisiz KPR**.\n- **Adrenalin 1 mg** ve **amiodaron 300 mg** **3. şoktan sonra**; adrenalin 3–5 dk'da bir; amiodaron **150 mg 5. şoktan sonra**.\n- Refrakter VF: **ped vektörü değişikliği (ön-arka)**, **çift ardışık defibrilasyon** (DOSE-VF), 4H/4T, olası koroner oklüzyon.\n- ROSC sonrası: STEMI varsa **acil anjiyo**, ateşten kaçınma, normoksi/normokapni.\n\n*Kaynak: ERC 2021 erişkin ileri yaşam desteği; DOSE-VF (NEJM 2022).*","good"),
 "n5":E("Geç ROSC","Uzamış resüsitasyon sonrası ROSC sağlandı; ancak hipoksik beyin hasarı gelişti.","mid"),
 "n9":E("Ölüm","Resüsitasyon başarısız oldu.","bad"),
}))
Qs+=[Q("c148q1","VF'de adrenalin ilk ne zaman verilir (ERC 2021)?",["Hemen, şoktan önce","3. şoktan sonra","İlk şoktan sonra","Hiç verilmez","ROSC sonrası"],1,"Sonra 3–5 dakikada bir.","Resüsitasyon"),
 Q("c148q2","Refrakter VF'de amiodaron dozları nedir?",["300 mg (3. şok sonrası), 150 mg (5. şok sonrası)","150 mg tek","1 g bolus","50 mg","5 mg/kg infüzyon"],0,"ERC 2021.","Resüsitasyon"),
 Q("c148q3","Refrakter VF'de sağkalımı artırdığı gösterilen yöntem hangisidir?",["Ped vektörü değişikliği / çift ardışık defibrilasyon","Yüksek doz adrenalin","Kalsiyum","Bikarbonat rutin","Atropin"],0,"DOSE-VF çalışması.","Resüsitasyon")]

# 149 HİPOKALSEMİ — tiroidektomi sonrası
S.append(case("c149","Ağız çevresinde uyuşma ve kramp — 45 yaşında kadın","Endokrin",
 "45 yaşında kadın. 2 gün önce total tiroidektomi olmuş, dün taburcu edilmiş. Bu sabahtan beri ağız çevresi ve parmak uçlarında uyuşma, ellerde kramp.",
 {"n1":N("Muayene","Anksiyöz. **Chvostek bulgusu pozitif**; KB manşonu şişirilince **Trousseau** (karpopedal spazm). Stridor yok. Boyun yarası temiz, hematom yok.","KB 128/80 · Nb 92 · SS 18 · SpO₂ %99",[
   T("Serum kalsiyum, albümin, Mg, fosfor, PTH",3,40,"**Düzeltilmiş Ca 6,6 mg/dL** (iyonize 0,78 mmol/L), **Mg 1,4**, P yüksek, PTH düşük.","Postoperatif hipoparatiroidi; hipomagnezemi eşlik ediyor."),
   T("EKG",2,5,"**QTc 520 ms**.","Aritmi riski."),
   A("**Semptomatik akut hipokalsemi**: **%10 kalsiyum glukonat 10–20 mL**, 50–100 mL %5 dekstrozda **10 dakikada IV** (EKG monitörde), ardından kalsiyum infüzyonu; **Mg replasmanı** (magnezyum sülfat 2 g IV); oral kalsiyum + **kalsitriol**; endokrin/cerrahi",4,15,"n2","Doğru. Hipomagnezemi düzeltilmezse hipokalsemi dirençli kalır."),
   A("Yalnız oral kalsiyum ile taburcu",-3,10,"n9","QT uzaması ve tetani — IV tedavi gerekir."),
   A("Kalsiyumu bikarbonatlı sıvıyla aynı hattan hızlı bolus",-3,5,"n9","Kalsiyum bikarbonatla çöker; hızlı bolus aritmi yapabilir."),
 ]),
 "n2":E("Düzelme","IV kalsiyum ve Mg sonrası semptomlar geçti, QTc 450'ye indi; kalsitriol ve oral kalsiyumla taburcu edildi.\n\n**Akılda kalsın**\n- Tiroidektomi/paratiroidektomi sonrası: **hipoparatiroidi** (ve “aç kemik” sendromu).\n- Bulgular: perioral uyuşma, parestezi, **Chvostek/Trousseau**, tetani, laringospazm, nöbet, **uzun QT**.\n- Tedavi: **%10 kalsiyum glukonat 10–20 mL / 10 dk** (EKG), sonra infüzyon; **Mg düzelt**; **kalsitriol** + oral kalsiyum.\n- Kalsiyumu bikarbonat/fosfatla karıştırma; digoksin kullananda dikkat.\n\n*Kaynak: Society for Endocrinology acil hipokalsemi kılavuzu (2016).*","good"),
 "n9":E("Komplikasyon","Hasta evde laringospazm ve nöbetle döndü / aritmi gelişti.","bad"),
}))
Qs+=[Q("c149q1","Semptomatik akut hipokalsemide ilk tedavi hangisidir?",["Oral kalsiyum","%10 kalsiyum glukonat 10–20 mL, 10 dakikada IV","Bisfosfonat","Furosemid","Kalsitonin"],1,"Sonra infüzyon.","Endokrin"),
 Q("c149q2","Hipokalseminin düzelmemesine yol açan eşlik eden bozukluk hangisidir?",["Hipomagnezemi","Hiperkalemi","Hiperglisemi","Hipernatremi","Hipofosfatemi"],0,"Mg PTH salınımı ve etkisi için gereklidir.","Endokrin"),
 Q("c149q3","Hipokalsemide EKG bulgusu hangisidir?",["QT uzaması","Kısa QT","Delta dalgası","Sivri T","U dalgası tek başına"],0,"Aritmi riski.","Endokrin")]

# 150 AKUT PANKREATİT — biliyer + kolanjit
S.append(case("c150","Karın ağrısı, sarılık ve ateş — 62 yaşında kadın","Gastroenteroloji / Cerrahi",
 "62 yaşında kadın. Bilinen safra taşı. Dün başlayan sırta vuran epigastrik ağrı, kusma; bugün ateş, titreme ve gözlerde sararma.",
 {"n1":N("Muayene","Sklera ikterik; epigastrium ve sağ üst kadranda hassasiyet, defans yok. Hafif konfüze.","KB 96/58 · Nb 116 · SS 22 · SpO₂ %95 · Ateş 39,0",[
   T("Lipaz, KCFT, bilirubin, hemogram, laktat",3,40,"Lipaz 2.400 U/L (>3×); total bilirubin **4,8**, ALT 320, ALP 410; lökosit 18.000; laktat 2,6.","Pankreatit + kolestaz + sistemik enflamasyon."),
   T("Abdominal USG",2,20,"Safra kesesinde taşlar, **koledok 11 mm**, distalde taş şüphesi.","Biliyer etiyoloji."),
   T("Kontrastlı abdominal BT (hemen)",-1,40,"Ödematöz pankreatit; nekroz değerlendirmesi için erken.","Tanı kesinse erken BT gerekmez; 72 saatten sonra komplikasyon için."),
   A("**Biliyer pankreatit + akut kolanjit (Charcot üçlüsü + konfüzyon/hipotansiyon)**: kan kültürü ve **hemen antibiyotik** (ör. piperasilin-tazobaktam); **hedefe yönelik ılımlı sıvı** (hipovolemide 10 mL/kg bolus, sonra ≈1,5 mL/kg/saat; aşırı yüklemeden kaçın); analjezi (opioid uygun); **acil ERCP (24 saat içinde)** — gastroenteroloji; erken oral beslenme hedefi",4,20,"n2","Doğru. Kolanjit eşlik eden biliyer pankreatitte erken ERCP; kolanjitsiz olguda rutin erken ERCP önerilmez."),
   A("Agresif sıvı (20 mL/kg bolus + 3 mL/kg/saat), antibiyotik yok, pankreatit izlemi",-3,20,"n3","WATERFALL: agresif sıvı yarar sağlamadı, sıvı yüklenmesini artırdı; kolanjit tedavisiz kaldı."),
   A("Profilaktik karbapenem ile 72 saat izle, ERCP'yi elektif planla",-3,30,"n3","Kolanjit varken ERCP ertelenmemeli."),
 ]),
 "n3":N("12 saat sonra","Hipotansiyon derinleşti, bilirubin 7,2; solunum sıkıntısı arttı.","KB 82/48 · Nb 128 · SpO₂ %91",[
   A("Antibiyotik (yoksa başla), vazopresör, **acil ERCP**",2,20,"n4","Kaynak kontrolü."),
   A("Sıvıya devam",-4,30,"n9","Septik şok ve sıvı yüklenmesi."),
 ]),
 "n2":E("Düzelme","ERCP'de koledok taşı çıkarıldı, sfinkterotomi yapıldı; ateş 24 saatte düştü. Aynı yatışta kolesistektomi planlandı.\n\n**Akılda kalsın**\n- Akut pankreatit: **3 ölçütten 2'si** (tipik ağrı, lipaz/amilaz ≥3×, görüntüleme).\n- **Biliyer pankreatit + kolanjit** → **antibiyotik + ERCP ≤24 saat**; kolanjit/obstrüksiyon yoksa rutin erken ERCP yok.\n- Sıvı: **ılımlı, hedefe yönelik** (WATERFALL 2022); aşırı sıvıdan kaçın.\n- Profilaktik antibiyotik **önerilmez** (enfekte nekroz/kolanjit yoksa); **erken oral beslenme**.\n- Biliyer pankreatitte **aynı yatışta kolesistektomi**.\n\n*Kaynak: ACG 2024 akut pankreatit kılavuzu; Tokyo 2018 kolanjit; WATERFALL (NEJM 2022).*","good"),
 "n4":E("Geç ERCP","ERCP ile drenaj sağlandı; hasta septik şok nedeniyle 4 gün yoğun bakımda kaldı.","mid"),
 "n9":E("Septik şok","Hasta çoklu organ yetmezliğine ilerledi.","bad"),
}))
Qs+=[Q("c150q1","Biliyer pankreatite kolanjit eşlik ediyorsa ERCP zamanlaması nedir?",["Elektif, 6 hafta sonra","Acil/erken (≤24 saat)","Hiç yapılmaz","Yalnız taburculuktan sonra","Kolesistektomiden sonra"],1,"Kolanjitsiz olguda rutin erken ERCP önerilmez.","Gastroenteroloji / Cerrahi"),
 Q("c150q2","Akut pankreatitte güncel sıvı yaklaşımı hangisidir?",["Agresif (20 mL/kg bolus + 3 mL/kg/saat) herkese","Hedefe yönelik ılımlı sıvı","Sıvı kısıtlaması","Yalnız kolloid","Sıvı gerekmez"],1,"WATERFALL çalışması.","Gastroenteroloji / Cerrahi"),
 Q("c150q3","Akut pankreatitte profilaktik antibiyotik ne zaman önerilir?",["Her hastada","Rutin önerilmez; enfeksiyon (kolanjit, enfekte nekroz) varsa","Lipaz >1000 ise","Ateş 37,5 ise","Alkolik pankreatitte"],1,"ACG 2024.","Gastroenteroloji / Cerrahi")]

P={"id":"ilk-nobet-15","title":"İlk Nöbet Vakaları — 15. Paket (vaka 141–150)","desc":"Düşük riskli pnömoni, SGLT2 ilişkili öglisemik DKA, hipernatremi, süt çocuğunda SVT, herpes zoster oftalmikus, perfore peptik ülser, diz çıkığı sonrası popliteal arter yaralanması, refrakter VF, tiroidektomi sonrası hipokalsemi, kolanjitli biliyer pankreatit.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 15. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 15. Paket","topic":"Temel acil","order":15,"req":[2],"desc":"Metabolik, enfeksiyon, cerrahi ve resüsitasyon acillerinden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
