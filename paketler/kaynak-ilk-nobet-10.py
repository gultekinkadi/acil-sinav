import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 91 SEREBRAL VENÖZ SİNÜS TROMBOZU
S.append(case("c91","Giderek artan baş ağrısı — 29 yaşında kadın","Nöroloji",
 "29 yaşında kadın, oral kontraseptif kullanıyor. 5 gündür giderek artan, yatınca ve öksürünce kötüleşen baş ağrısı; bulantı-kusma. Bugün sağ kolunda kasılma ile başlayan jeneralize nöbet geçirdi.",
 {"n1":N("Muayene","Postiktal, konfüzyon düzeliyor. Fundoskopide **bilateral papil ödemi**. Sağ kolda hafif güçsüzlük.","KB 132/82 · Nb 92 · Ateş 37,1",[
   T("Kontrastsız BT",2,20,"Sol parietal küçük hemorajik infarkt; superior sagital sinüste **hiperdens** görünüm (kordon işareti).","Arter sulama alanına uymayan hemorajik infarkt venöz trombozu düşündürür."),
   T("BT venografi / MR venografi",3,40,"**Superior sagital ve sol transvers sinüste trombüs** (kontrastlı BT'de boş delta işareti).","Tanı venografiyle konur."),
   T("D-dimer",0,40,"Yüksek.","Normal D-dimer SVT'yi dışlamaz."),
   A("**Antikoagülasyon** — DMAH (ör. enoksaparin 1 mg/kg 12 saatte bir) ya da anfraksiyone heparin; **hemorajik infarkt varlığında bile**; nöbet tedavisi (levetirasetam); kontraseptifi kes; nöroloji/inme ünitesi",4,20,"n2","Doğru. SVT'de kanamalı infarkt antikoagülasyon kontrendikasyonu değildir."),
   A("Beyinde kanama var — antikoagülan kontrendike, yalnız analjezi",-4,20,"n9","Kanama venöz tıkanıklığın sonucudur; antikoagülasyonsuz tromboz ilerler."),
   A("Migren — triptan ve taburcu",-5,10,"n9","Papil ödemi, nöbet ve fokal bulgulu baş ağrısı ikincil nedenlidir."),
 ]),
 "n2":E("Düzelme","Antikoagülasyonla 1 haftada baş ağrısı ve kol güçsüzlüğü geriledi; oral antikoagülana geçildi (3–12 ay), kontrasepsiyon yöntemi değiştirildi.\n\n**Akılda kalsın**\n- SVT: **genç kadın, OKS/gebelik/lohusalık, trombofili, enfeksiyon**.\n- Baş ağrısı (artan, pozisyonel), **papil ödemi**, nöbet, fokal defisit, bilinç değişikliği.\n- BT normal olabilir; tanı **BT/MR venografi**.\n- **Antikoagülasyon** (hemorajik infarktta da); nöbet ve KİBAS tedavisi.\n\n*Kaynak: ESO 2017 SVT kılavuzu; AHA 2024 bilimsel bildiri.*","good"),
 "n9":E("Kötüleşme","Tromboz ilerledi; bilinç bozuldu, yaygın venöz infarktlar gelişti.","bad"),
}))
Qs+=[Q("c91q1","Serebral venöz sinüs trombozunda hemorajik infarkt varlığında tedavi hangisidir?",["Antikoagülasyon kontrendikedir","Antikoagülasyon yine verilir (DMAH/heparin)","Yalnız aspirin","Tromboliz herkese","Steroid"],1,"Kanama venöz tıkanıklığın sonucudur.","Nöroloji"),
 Q("c91q2","SVT tanısında kullanılan görüntüleme hangisidir?",["Kontrastsız BT tek başına yeterli","BT veya MR venografi","Karotis Doppler","EEG","LP"],1,"Venöz sistem görüntülenmelidir.","Nöroloji"),
 Q("c91q3","SVT için risk faktörü hangisidir?",["Oral kontraseptif kullanımı","Düzenli egzersiz","Akdeniz diyeti","Erkek cinsiyet","İleri yaş tek başına"],0,"OKS, gebelik/lohusalık, trombofili, malignite, enfeksiyon.","Nöroloji")]

# 92 SPONTAN PNÖMOTORAKS (primer)
S.append(case("c92","Ani yan ağrısı — 21 yaşında erkek","Göğüs hastalıkları",
 "21 yaşında, uzun boylu, zayıf erkek; sigara içiyor. 6 saat önce dinlenirken sağ göğüste ani batıcı ağrı ve hafif nefes darlığı başlamış. Akciğer hastalığı yok.",
 {"n1":N("Muayene","Konuşabiliyor, rahat. Sağda solunum sesleri hafif azalmış.","KB 126/78 · Nb 92 · SS 18 · SpO₂ %97",[
   T("Akciğer grafisi",3,15,"**Sağ pnömotoraks**, hilus seviyesinde akciğer-göğüs duvarı mesafesi ≈3 cm (büyük); mediasten kayması yok.","BTS 2023: tedavi kararı boyuttan çok **semptom ve risk** ile verilir."),
   A("Primer spontan pnömotoraks, minimal semptom, stabil: **konservatif izlem** (gözlem, kontrol grafisi, uyarılar) ya da hasta tercihine göre iğne aspirasyonu/ambulatuvar cihaz; sigarayı bırakma danışmanlığı",4,20,"n2","Doğru. Semptomu az olan PSP'de konservatif yaklaşım, büyük pnömotoraksta bile güvenlidir (Brown ve ark., NEJM 2020)."),
   A("Hemen büyük çaplı göğüs tüpü (28 F)",-1,30,"n2","Gereksiz invazif; komplikasyon ve hastanede kalış artar. Gerekirse küçük çaplı kateter yeterlidir."),
   A("Analjezikle taburcu; yarın uçakla tatile gidebilir",-4,10,"n9","Pnömotoraks tam düzelmeden uçuş kontrendikedir; takip ve uyarılar şart."),
 ]),
 "n2":E("Kendiliğinden düzelme","4 saatlik gözlemde semptom artmadı; kontrol grafisinde ilerleme yoktu. Hasta uyarılarla taburcu edildi; 2 hafta sonra pnömotoraks rezorbe oldu.\n\n**Akılda kalsın**\n- **Primer** (sağlıklı akciğer, genç, uzun boylu, sigara) vs **sekonder** (KOAH vb. — daha agresif tedavi).\n- Stabil, minimal semptomlu PSP: **konservatif izlem** uygun; semptomatikse **iğne aspirasyonu** veya ambulatuvar cihaz; başarısızlıkta küçük çaplı tüp.\n- **Instabilite = tansiyon** → acil dekompresyon.\n- Tam düzelmeden **uçuş ve dalış yok**; sigarayı bırak.\n\n*Kaynak: BTS 2023 plevral hastalık kılavuzu.*","good"),
 "n9":E("Tansiyon pnömotoraks — uçakta","Hasta uçakta ani nefes darlığı geliştirdi; acil iniş yapıldı.","bad"),
}))
Qs+=[Q("c92q1","Minimal semptomlu, stabil primer spontan pnömotoraksta güncel yaklaşım hangisidir?",["Her zaman büyük çaplı göğüs tüpü","Konservatif izlem bir seçenektir","Acil torakotomi","Plevrodez","Tromboliz"],1,"BTS 2023 ve RKÇ verileri konservatif izlemi destekler.","Göğüs hastalıkları"),
 Q("c92q2","Sekonder spontan pnömotoraksın primerden farkı nedir?",["Daha iyi huyludur","Altta yatan akciğer hastalığı vardır; daha az tolere edilir, daha agresif tedavi","Yalnız gençlerde görülür","Tedavi gerektirmez","Travmatiktir"],1,"KOAH, kistik fibrozis vb.","Göğüs hastalıkları"),
 Q("c92q3","Pnömotoraks geçiren hastaya hangi uyarı verilmelidir?",["Tam düzelme gösterilmeden uçak yolculuğu ve dalıştan kaçınma","Egzersiz zorunlu","Sigara serbest","Yüksek irtifa yararlı","Hiçbiri"],0,"Basınç değişiklikleri pnömotoraksı büyütür.","Göğüs hastalıkları")]

# 93 TOPLUM KÖKENLİ PNÖMONİ
S.append(case("c93","Ateş ve öksürük — 72 yaşında erkek","Enfeksiyon / Göğüs",
 "72 yaşında erkek, diyabet. 3 gündür ateş, balgamlı öksürük, sağ yan ağrısı; bugün kızı biraz konfüze olduğunu söylüyor. Yaklaşık 70 kg.",
 {"n1":N("Muayene","Hafif konfüze (yer-zaman oryantasyonu bozuk). Sağ alt zonda bronşiyal solunum ve raller.","KB 98/58 · Nb 108 · SS 26 · SpO₂ %90 · Ateş 38,9",[
   T("Akciğer grafisi",2,15,"Sağ alt lob konsolidasyonu.","Tanı."),
   T("Üre, kreatinin, hemogram, CRP",1,30,"Üre 62 mg/dL (BUN 29; >7 mmol/L), lökosit 17.000, CRP 210.","CURB-65 hesaplanır."),
   T("CURB-65",2,2,"Konfüzyon (1) + üre >7 mmol/L (1) + SS ≥30 (0) + KB (sistolik <90 veya diyastolik ≤60) (1) + yaş ≥65 (1) = **4**.","3–5: ağır pnömoni → yatış, yoğun bakım değerlendirmesi."),
   A("Yatış; O₂ (hedef SpO₂ %94–98); **ilk 4 saatte** (sepsis bulgusunda 1 saatte) antibiyotik — ağır TKP: seftriakson (ya da amoksisilin-klavulanat) + makrolid (klaritromisin); kan ve balgam kültürü, idrar antijenleri; sıvı; sepsis ve yoğun bakım ölçütlerini değerlendir",4,20,"n2","Doğru. Ağır TKP'de beta-laktam + makrolid kombinasyonu."),
   A("Oral amoksisilin ile ayaktan tedavi",-5,10,"n9","CURB-65 = 4: ağır pnömoni; ayaktan tedavi ölümcül olabilir."),
 ]),
 "n2":E("İyileşme","Hasta 5 gün IV, ardından oral antibiyotikle iyileşti; 6 hafta sonra kontrol grafisi planlandı (malignite ekarte).\n\n**Akılda kalsın**\n- **CURB-65**: Konfüzyon, Üre >7 mmol/L, SS ≥30, KB düşük (s<90/d≤60), ≥65 yaş. 0–1 ayaktan, 2 yatış düşün, 3–5 ağır.\n- Ağır TKP: **beta-laktam + makrolid** (ya da yerel protokol); antibiyotik **4 saat içinde**, sepsiste 1 saatte.\n- O₂ hedefi %94–98 (hiperkapni riskinde %88–92).\n- Yoğun bakım ölçütleri (ATS/IDSA majör/minör).\n\n*Kaynak: BTS/NICE NG138; ATS/IDSA 2019 TKP kılavuzu.*","good"),
 "n9":E("Septik şok","Hasta ertesi gün septik şok ve solunum yetmezliğiyle döndü.","bad"),
}))
Qs+=[Q("c93q1","CURB-65 bileşenlerinden hangisi değildir?",["Konfüzyon","Üre >7 mmol/L","Solunum sayısı ≥30","Ateş >39 °C","Yaş ≥65"],3,"Ateş CURB-65'te yoktur.","Enfeksiyon / Göğüs"),
 Q("c93q2","CURB-65 skoru 3–5 olan hastada yaklaşım hangisidir?",["Ayaktan oral tedavi","Ağır pnömoni: yatış, yoğun bakım değerlendirmesi","Antibiyotiksiz izlem","Yalnız antipiretik","Ertesi gün kontrol"],1,"Mortalite riski yüksektir.","Enfeksiyon / Göğüs"),
 Q("c93q3","Hastaneye yatan ağır toplum kökenli pnömonide ampirik tedavi seçeneği hangisidir?",["Yalnız azitromisin","Beta-laktam (ör. seftriakson) + makrolid","Yalnız metronidazol","Vankomisin tek başına","Antiviral"],1,"Atipik etkenleri de kapsar.","Enfeksiyon / Göğüs")]

# 94 TONSİLLİT VE PERİTONSİLLER APSE
S.append(case("c94","Boğaz ağrısı ve ağız açamama — 24 yaşında erkek","KBB",
 "24 yaşında erkek. 5 gündür boğaz ağrısı; 2 gün önce başka bir yerde reçetesiz antibiyotik başlamış. Son 24 saatte sol tarafta artan ağrı, yutkunamama, ağzını tam açamama; sesi “ağzında sıcak patates varmış gibi”.",
 {"n1":N("Muayene","**Trismus** (2 parmak). Sol peritonsiller bölgede belirgin şişlik, **uvula sağa itilmiş**. Salya biriktiriyor ama solunum sıkıntısı yok, stridor yok.","Nb 108 · SpO₂ %98 · Ateş 38,7",[
   T("İntraoral USG",2,10,"Sol peritonsiller bölgede 2,4 cm sıvı koleksiyonu.","Apse ile selülit ayrımında yardımcı."),
   T("Boyun BT",0,40,"Peritonsiller apse; derin boyun yayılımı yok.","Derin boyun enfeksiyonu şüphesi ya da tanı belirsizse."),
   A("**İğne aspirasyonu veya insizyon-drenaj** (KBB/deneyimli hekim; karotis yakınlığına dikkat, iğneyi lateral değil medial-posteriora yönlendirme); ardından antibiyotik (ör. amoksisilin-klavulanat ya da penisilin + metronidazol); analjezi, sıvı; tek doz steroid düşünülebilir",4,20,"n2","Doğru. Peritonsiller apse drenaj gerektirir; antibiyotik tek başına yetmez."),
   A("Basit tonsillit — oral penisilin ve taburcu",-4,10,"n9","Trismus, tek taraflı şişlik ve uvula deviasyonu apseyi gösterir."),
 ]),
 "n2":E("Drenaj sonrası rahatlama","Aspirasyonla 6 mL pü boşaltıldı; hasta aynı gün yutabildi, oral antibiyotikle taburcu edildi.\n\n**Akılda kalsın**\n- Tonsillofarenjitte antibiyotik kararı: **Centor/McIsaac** (ateş, tonsil eksüdası, ön servikal LAP, öksürük yokluğu, yaş).\n- Peritonsiller apse: **trismus, sıcak patates sesi, tek taraflı şişlik, uvula deviasyonu**.\n- Tedavi: **drenaj** (aspirasyon/insizyon) + antibiyotik.\n- Kırmızı bayraklar: stridor, boyun şişliği, tortikollis → **derin boyun enfeksiyonu**, epiglotit, Lemierre.\n\n*Kaynak: ENT UK peritonsiller apse önerileri; IDSA 2012 farenjit kılavuzu.*","good"),
 "n9":E("Derin boyun enfeksiyonu","Apse parafarengeal alana yayıldı; hasta hava yolu tehlikesiyle geri döndü.","bad"),
}))
Qs+=[Q("c94q1","Peritonsiller apseyi tonsillitten ayıran bulgu hangisidir?",["Ateş","Boğaz ağrısı","Trismus ve uvula deviasyonu","Eksüda","Servikal LAP"],2,"Tek taraflı şişlik ve trismus apseyi düşündürür.","KBB"),
 Q("c94q2","Peritonsiller apsenin temel tedavisi hangisidir?",["Yalnız antibiyotik","Drenaj (iğne aspirasyonu veya insizyon) + antibiyotik","Tonsillektomi her olguda acil","Steroid tek başına","Gargara"],1,"Drenaj olmadan iyileşme gecikir.","KBB"),
 Q("c94q3","Hangisi Centor ölçütlerinden biri değildir?",["Ateş","Tonsil eksüdası","Öksürük yokluğu","Hassas ön servikal LAP","Burun akıntısı"],4,"Öksürük ve burun akıntısı viral nedeni düşündürür.","KBB")]

# 95 SİNÜZİT — ORBİTAL KOMPLİKASYON
S.append(case("c95","Göz çevresinde şişlik — 16 yaşında erkek","KBB / Göz",
 "16 yaşında erkek. 10 gündür burun tıkanıklığı ve sarı-yeşil akıntı; 2 gün önce biraz düzelip yeniden kötüleşmiş. Bugün sol göz çevresi şişmiş, kızarmış; gözünü hareket ettirince ağrıyor ve çift görüyor.",
 {"n1":N("Muayene","Sol periorbital ödem ve eritem, **proptozis**, göz hareketleri ağrılı ve kısıtlı, kemozis. Görme sağda 1,0, solda 0,7. RAPD yok.","Ateş 38,9 · Nb 104",[
   T("Kontrastlı orbita + sinüs BT",4,30,"Etmoid ve maksiller sinüzit; **sol subperiosteal apse** (medial), orbital selülit.","Orbital (septum arkası) tutulum: proptozis, ağrılı/kısıtlı göz hareketi, diplopi, görme azalması → BT."),
   A("**IV antibiyotik** (ör. seftriakson + vankomisin ± metronidazol); burun dekonjestanı; acil **KBB ve göz** konsültasyonu (apse drenajı); görme ve pupil izlemi",4,20,"n2","Doğru. Orbital selülit görme kaybı, kavernöz sinüs trombozu ve intrakraniyal yayılım yapabilir."),
   A("Preseptal selülit — oral amoksisilin-klavulanat ile ayaktan",-5,10,"n9","Proptozis, oftalmopleji ve görme azalması orbital (postseptal) tutulumdur."),
 ]),
 "n2":E("Drenaj ve IV tedavi","Endoskopik sinüs cerrahisiyle subperiosteal apse boşaltıldı; görme 1,0'e döndü.\n\n**Akılda kalsın**\n- Akut bakteriyel rinosinüzit: **>10 gün** süren ya da **iki kez kötüleşen** belirtiler, ağır başlangıç; çoğu viraldir.\n- Kırmızı bayraklar: **periorbital ödem, proptozis, ağrılı/kısıtlı göz hareketi, diplopi, görme azalması**, şiddetli baş ağrısı, nörolojik bulgu.\n- **Preseptal** (göz hareketleri normal) → oral; **orbital** → **BT + IV antibiyotik + KBB/göz**.\n\n*Kaynak: EPOS 2020; Chandler sınıflaması.*","good"),
 "n9":E("Kalıcı görme kaybı","Apse ilerledi; optik nöropati ve kavernöz sinüs trombozu gelişti.","bad"),
}))
Qs+=[Q("c95q1","Orbital (postseptal) selüliti preseptal selülitten ayıran bulgu hangisidir?",["Göz kapağında kızarıklık","Proptozis ve ağrılı/kısıtlı göz hareketleri","Ateş","Burun akıntısı","Kapakta ödem"],1,"Postseptal tutulumda göz hareketleri ve görme etkilenir.","KBB / Göz"),
 Q("c95q2","Orbital selülit şüphesinde ilk görüntüleme hangisidir?",["Direkt sinüs grafisi","Kontrastlı orbita-sinüs BT","Göz USG tek başına","Beyin MR zorunlu ilk","Görüntüleme gerekmez"],1,"Apse ve yayılım değerlendirilir.","KBB / Göz"),
 Q("c95q3","Akut bakteriyel rinosinüziti düşündüren seyir hangisidir?",["3 günlük burun akıntısı","10 günden uzun süren ya da düzelip yeniden kötüleşen belirtiler","Hapşırık","Kaşıntı","Mevsimsel tekrarlama"],1,"“Çift kötüleşme” ve uzamış seyir bakteriyel nedeni düşündürür.","KBB / Göz")]

# 96 AKUT OTİTİS MEDİA — MASTOİDİT
S.append(case("c96","Kulak arkasında şişlik — 3 yaşında kız","Pediatri / KBB",
 "3 yaşında kız. 6 gün önce sağ kulak ağrısı ve ateş başlamış; aile antibiyotik vermemiş. Bugün sağ kulak arkası şişmiş, kızarmış ve kulak öne doğru itilmiş görünüyor.",
 {"n1":N("Muayene","Sağ **retroaurikuler şişlik, kızarıklık ve hassasiyet**, kulak kepçesi öne-aşağı itilmiş. Otoskopide kızarık, bombeli zar. Ense sertliği yok, fasiyal sinir normal.","Ateş 39,2 · Nb 132",[
   T("Kontrastlı temporal kemik BT",3,40,"Sağ mastoid hücrelerde koalesans, **subperiosteal apse**; sigmoid sinüs açık.","Akut mastoidit komplikasyonu."),
   A("Akut mastoidit: **IV antibiyotik** (ör. seftriakson ± klindamisin/vankomisin), analjezi; acil **KBB** (miringotomi ± tüp, apse drenajı/mastoidektomi); intrakraniyal komplikasyon izlemi",4,20,"n2","Doğru."),
   A("Akut otitis media — oral amoksisilin ile ayaktan",-4,10,"n9","Retroaurikuler şişlik ve kulak kepçesinin öne itilmesi mastoidittir."),
 ]),
 "n2":E("Drenaj ve iyileşme","Miringotomi ve apse drenajı yapıldı; IV tedaviyle 5 günde iyileşti.\n\n**Akılda kalsın**\n- AOM tanısı: **bombeli zar** (+ akıntı, kızarıklık, ağrı).\n- Antibiyotik: <6 ay; 6–24 ay bilateral veya ağır; ağır belirti (ateş ≥39, şiddetli ağrı, >48 saat) → **amoksisilin 80–90 mg/kg/gün**; seçilmiş hastada izle-bekle; **analjezi her zaman**.\n- Kırmızı bayraklar: **retroaurikuler şişlik, kulak kepçesinin itilmesi** (mastoidit), fasiyal paralizi, baş ağrısı, ense sertliği, nörolojik bulgu.\n\n*Kaynak: AAP 2013 AOM kılavuzu.*","good"),
 "n9":E("İntrakraniyal komplikasyon","Çocuk 2 gün sonra sigmoid sinüs trombozu ve epidural apseyle getirildi.","bad"),
}))
Qs+=[Q("c96q1","Akut otitis media tanısında en önemli otoskopik bulgu hangisidir?",["Kulak zarında hafif kızarıklık","Bombeli kulak zarı","Buşon","Zarda retraksiyon","Normal zar"],1,"Bombeli zar AOM için en özgül bulgudur.","Pediatri / KBB"),
 Q("c96q2","AOM'de ilk tercih edilen antibiyotik ve dozu hangisidir?",["Siprofloksasin","Amoksisilin 80–90 mg/kg/gün","Azitromisin tek doz","Sefaleksin düşük doz","Metronidazol"],1,"Yüksek doz amoksisilin.","Pediatri / KBB"),
 Q("c96q3","Akut mastoiditin bulgusu hangisidir?",["Kulak kaşıntısı","Retroaurikuler şişlik ve kulak kepçesinin öne itilmesi","Kulak çınlaması","Dış kulak yolu ödemi tek başına","İşitme kaybı yok"],1,"Kırmızı bayrak — IV antibiyotik ve KBB.","Pediatri / KBB")]

# 97 OTİTİS EKSTERNA — NEKROTİZAN (MALİGN)
S.append(case("c97","İnatçı kulak ağrısı — 74 yaşında erkek","KBB / Enfeksiyon",
 "74 yaşında erkek, kötü kontrollü diyabet. 3 haftadır sağ kulakta akıntı ve geceleri uyutmayan şiddetli ağrı; iki kez antibiyotikli kulak damlası kullanmış, düzelmemiş. Dün sağ yüzünde kayma fark etmiş.",
 {"n1":N("Muayene","Sağ dış kulak yolunda ödem, akıntı ve kemik-kıkırdak bileşkesinde **granülasyon dokusu**. **Sağ periferik fasiyal paralizi**.","Ateş 37,4 · Glukoz 312",[
   T("ESH/CRP",1,30,"ESH 86, CRP 64.","Takipte de kullanılır."),
   T("Temporal kemik BT (± MR)",3,60,"Dış kulak yolu tabanında ve mastoidde **kemik erozyonu**.","Kafa tabanı osteomiyeliti."),
   T("Kulak akıntısı kültürü",2,10,"*Pseudomonas aeruginosa*.","En sık etken."),
   A("Nekrotizan (malign) otitis eksterna: yatış; **IV antipsödomonal antibiyotik** (ör. seftazidim veya piperasilin-tazobaktam; yerel duyarlılığa göre, uzun süreli); glukoz kontrolü; KBB (debridman, biyopsi — malignite dışlanmalı)",4,20,"n2","Doğru. Kafa tabanı osteomiyeliti haftalarca IV tedavi gerektirir."),
   A("Basit otitis eksterna — yeni bir kulak damlası ve analjezik",-5,10,"n9","Diyabetik yaşlıda inatçı ağrı + granülasyon + kraniyal sinir tutulumu nekrotizan otitis eksternadır."),
 ]),
 "n2":E("Uzun süreli tedavi","6 hafta IV + oral antibiyotikle ağrı ve akıntı geriledi; fasiyal paralizi kısmen düzeldi.\n\n**Akılda kalsın**\n- Basit OE: **topikal** damla (± kulak yolu temizliği), analjezi.\n- Nekrotizan OE: **yaşlı, diyabetik/immünsüprese**, gece kötüleşen şiddetli ağrı, **granülasyon** (kemik-kıkırdak bileşkesi), **kraniyal sinir paralizisi** (VII sık).\n- Etken çoğunlukla **Pseudomonas**; BT/MR, **uzun süreli IV antipsödomonal** tedavi, KBB.\n\n*Kaynak: Treviño González ve ark., derleme 2021; AAO-HNS 2014 OE kılavuzu.*","good"),
 "n9":E("Kafa tabanı osteomiyeliti ilerledi","Çoklu kraniyal sinir felci ve sigmoid sinüs trombozu gelişti.","bad"),
}))
Qs+=[Q("c97q1","Nekrotizan otitis eksternanın en sık etkeni hangisidir?",["Staphylococcus epidermidis","Pseudomonas aeruginosa","Candida","Streptococcus pneumoniae","Haemophilus influenzae"],1,"Kafa tabanı osteomiyeliti yapar.","KBB / Enfeksiyon"),
 Q("c97q2","Nekrotizan otitis eksternada en sık tutulan kraniyal sinir hangisidir?",["III","V","VII (fasiyal)","X","XII"],2,"Stilomastoid foramen yakınlığı.","KBB / Enfeksiyon"),
 Q("c97q3","Basit (komplike olmayan) otitis eksternanın tedavisi hangisidir?",["IV antibiyotik","Topikal antibiyotik damla ± kulak yolu temizliği, analjezi","Cerrahi","Steroid tablet","Antiviral"],1,"Sistemik antibiyotik genellikle gerekmez.","KBB / Enfeksiyon")]

# 98 AKUT SİSTİT (komplike olmayan)
S.append(case("c98","Yanarak idrar yapma — 26 yaşında kadın","Üroloji / Enfeksiyon",
 "26 yaşında kadın. 2 gündür idrar yaparken yanma, sık idrara çıkma ve suprapubik rahatsızlık. Ateş, yan ağrısı, vajinal akıntı yok. Son adeti 2 hafta önce.",
 {"n1":N("Muayene","Genel durumu iyi. Kostovertebral açı hassasiyeti yok.","Ateş 36,8 · Nb 82",[
   T("Gebelik testi",2,5,"Negatif.","Gebelikte tedavi seçimi ve izlem değişir."),
   T("İdrar strip",1,5,"Lökosit esteraz +, nitrit +.","Tipik öyküde tanı kliniktir; strip destekler."),
   T("İdrar kültürü + böbrek USG",-1,60,"—","Komplike olmayan ilk sistitte rutin kültür ve görüntüleme gerekmez."),
   A("Komplike olmayan sistit: **nitrofurantoin** (ör. 100 mg modifiye salınımlı, 12 saatte bir, 5 gün) ya da **fosfomisin 3 g tek doz** (veya pivmesilinam); bol sıvı, analjezi; ateş/yan ağrısı gelişirse başvuru uyarısı",4,10,"n2","Doğru. İlk basamak ajanlar direnç ve yan etki profiliyle seçilir."),
   A("Siprofloksasin 500 mg, 14 gün",-3,10,"n2","Florokinolonlar komplike olmayan sistitte ilk seçenek olarak önerilmez (yan etki, direnç); süre gereksiz uzun."),
 ]),
 "n2":E("İyileşme","Belirtiler 2 günde geçti.\n\n**Akılda kalsın**\n- Komplike olmayan sistit: gebe olmayan, sağlıklı kadın, **ateş/yan ağrısı yok**.\n- Tanı klinik; rutin kültür gerekmez (tekrarlayan, tedavi başarısızlığı, gebelik, erkek, komplike olgularda kültür).\n- İlk seçenek: **nitrofurantoin 5 gün**, **fosfomisin 3 g tek doz**, pivmesilinam; **florokinolon ilk seçenek değil**.\n- Gebelikte **asemptomatik bakteriüri de tedavi edilir**.\n- Ateş, yan ağrısı, kusma → **piyelonefrit**.\n\n*Kaynak: EAU 2024 Ürolojik Enfeksiyonlar Kılavuzu.*","good"),
 "n9":E("—","(Bu vakada ağır sonuç yok.)","mid"),
}))
# kötü son ulaşılabilir olsun
S[-1]["nodes"]["n1"]["opts"].append(A("Antibiyotik gerekmez; ateş ve yan ağrısı olsa bile bol su yeterli",-4,10,"n9","Belirti varken tedavisiz bırakmak ve uyarı vermemek piyelonefrite ilerlemeye yol açabilir."))
S[-1]["nodes"]["n9"]=E("Piyelonefrit","Hasta 3 gün sonra ateş, titreme ve yan ağrısıyla geri geldi; IV antibiyotik gerekti.","bad")
Qs+=[Q("c98q1","Komplike olmayan akut sistitte ilk seçenek tedavi hangisidir?",["Siprofloksasin 14 gün","Nitrofurantoin 5 gün veya fosfomisin 3 g tek doz","IV seftriakson","Amoksisilin 4 hafta","Antibiyotik gerekmez"],1,"EAU önerileri.","Üroloji / Enfeksiyon"),
 Q("c98q2","Hangi durumda sistitte idrar kültürü önerilir?",["Sağlıklı genç kadında ilk atak","Gebelik, tedavi başarısızlığı, tekrarlayan enfeksiyon, erkek hasta","Hiçbir zaman","Yalnız ateş varsa","Her hastada iki kez"],1,"Komplike/özel durumlarda kültür alınır.","Üroloji / Enfeksiyon"),
 Q("c98q3","Gebelikte asemptomatik bakteriüri için doğru ifade hangisidir?",["Tedavi edilmez","Taranır ve tedavi edilir","Yalnız 3. trimesterde önemlidir","Florokinolonla tedavi edilir","Doğumdan sonra tedavi edilir"],1,"Piyelonefrit ve erken doğum riskini azaltır.","Üroloji / Enfeksiyon")]

# 99 AKUT PİYELONEFRİT (gebe)
S.append(case("c99","Ateş ve yan ağrısı — 24 haftalık gebe","Kadın doğum / Enfeksiyon",
 "27 yaşında, 24 haftalık gebe. 2 gündür sık idrara çıkma, dün başlayan titremeyle yüksek ateş, sağ yan ağrısı ve kusma.",
 {"n1":N("Muayene","Sağ kostovertebral açı hassasiyeti belirgin. Uterus gebelik haftasıyla uyumlu, hassasiyet yok.","KB 102/60 · Nb 118 · SS 22 · Ateş 39,4",[
   T("İdrar strip + kültür, kan kültürü",2,10,"Lökosit +++, nitrit +; kültürler alındı.","Gebelikte piyelonefritte kültür şart."),
   T("Laktat, kreatinin, hemogram",1,30,"Laktat 2,1, kreatinin 0,8, lökosit 16.000.","Sepsis taraması."),
   T("Böbrek USG",2,20,"Sağda hafif hidronefroz (gebelikte fizyolojik olabilir), taş yok.","Obstrüksiyon/apse dışlanmalı."),
   T("Fetal kalp sesi / obstetrik değerlendirme",2,10,"Fetal kalp sesi 160/dk (maternal ateşe bağlı), kasılma yok.","Erken doğum riski izlenir."),
   A("Yatış; IV sıvı; **IV seftriakson** (gebelikte uygun); parasetamol; kadın doğum ile birlikte izlem; kültüre göre düzenle; tedavi sonrası bakteriüri taraması",4,20,"n2","Doğru. Gebelikte piyelonefrit yatış ve IV tedavi gerektirir (sepsis, ARDS, erken doğum riski)."),
   A("Oral siprofloksasin ile ayaktan tedavi",-5,10,"n9","Florokinolonlar gebelikte tercih edilmez; gebe piyelonefriti yatış gerektirir."),
   A("Oral nitrofurantoin",-4,10,"n9","Nitrofurantoin böbrek dokusunda yeterli düzeye ulaşmaz; piyelonefritte kullanılmaz."),
 ]),
 "n2":E("İyileşme","48 saatte ateş düştü; kültürde E. coli, seftriaksona duyarlı. Oral sefaleksinle toplam 14 güne tamamlandı; gebeliğin geri kalanında idrar kültürü takibi planlandı.\n\n**Akılda kalsın**\n- Piyelonefrit: **ateş, titreme, yan ağrısı, KVA hassasiyeti**, bulantı-kusma ± sistit belirtileri.\n- Gebelikte **yatış + IV beta-laktam** (seftriakson); **florokinolon ve nitrofurantoin yok**.\n- Kültür; obstrüksiyon/apse için **USG**; sepsis taraması.\n- Gebe olmayan, hafif olguda ayaktan oral tedavi (yerel direnç oranına göre) mümkündür.\n\n*Kaynak: EAU 2024; ACOG.*","good"),
 "n9":E("Ürosepsis","Hasta ertesi gün septik şok ve erken doğum eylemiyle getirildi.","bad"),
}))
Qs+=[Q("c99q1","Gebede akut piyelonefrit tedavisi için uygun ilk seçenek hangisidir?",["Oral siprofloksasin","IV seftriakson (yatırarak)","Nitrofurantoin","Doksisiklin","Gözlem"],1,"Gebelikte yatış ve IV beta-laktam.","Kadın doğum / Enfeksiyon"),
 Q("c99q2","Nitrofurantoin piyelonefritte neden kullanılmaz?",["Pahalı olduğu için","Böbrek dokusunda yeterli düzeye ulaşmadığı için","Nefrotoksik olduğu için","Yalnız IV formu olduğu için","Gebelikte kontrendike olduğu için (tek neden)"],1,"Yalnız idrarda yoğunlaşır.","Kadın doğum / Enfeksiyon"),
 Q("c99q3","Piyelonefritte böbrek USG'nin amacı nedir?",["Tanı koymak zorunlu","Obstrüksiyon veya apse gibi komplikasyonları dışlamak","Kültür yerine","Antibiyotik seçmek","Rutin değildir hiçbir zaman"],1,"Tıkalı enfekte sistem acil drenaj gerektirir.","Kadın doğum / Enfeksiyon")]

# 100 İSKEMİK İNME — ARKA DOLAŞIM (baziler)
S.append(case("c100","Ani baş dönmesi ve kusma — 61 yaşında erkek","Nöroloji",
 "61 yaşında erkek, hipertansiyon ve sigara. 1,5 saat önce ani başlayan şiddetli baş dönmesi, kusma, yürüyememe. Konuşması biraz peltek.",
 {"n1":N("Muayene","Uyanık. **Yön değiştiren nistagmus**, ayakta duramıyor (gövde ataksisi), hafif dizartri. Kafa itme (head impulse) testi **normal**, alternan örtme testinde **vertikal kayma (skew)**.","KB 182/98 · Nb 84 · Glukoz 138",[
   T("HINTS",3,3,"**Santral**: normal kafa itme testi + yön değiştiren nistagmus + skew deviasyonu.","Akut sürekli vertigoda HINTS, deneyimli elde ilk 48 saatte MR'dan daha duyarlıdır."),
   T("Kontrastsız BT",0,20,"Normal.","Arka çukurda iskemiyi göstermekte duyarsızdır; normal BT inmeyi dışlamaz."),
   T("BT anjiyografi",4,20,"**Baziler arterde tıkanıklık**.","Baziler oklüzyon hayatı tehdit eder."),
   A("Kod inme: BT + BTA; uygunsa **IV tromboliz** (4,5 saat içinde; KB <185/110'a indirilerek) ve **trombektomi** (baziler oklüzyonda 24 saate kadar kanıt var); nöroloji/girişimsel",4,20,"n2","Doğru. ATTENTION/BAOCHE (2022): baziler arter oklüzyonunda trombektomi işlevsel sonucu belirgin iyileştirir."),
   A("Periferik vertigo — antiemetik + antihistaminik, taburcu",-5,20,"n9","Gövde ataksisi, dizartri ve santral HINTS bulguları arka dolaşım inmesidir."),
 ]),
 "n2":E("Rekanalizasyon","Tromboliz + trombektomiyle baziler arter açıldı; 90. günde hasta bağımsız yürüyordu (mRS 1).\n\n**Akılda kalsın**\n- Arka dolaşım inmesi: **vertigo, kusma, gövde ataksisi**, dizartri, diplopi, bilinç değişikliği; sık atlanır.\n- **HINTS**: anormal kafa itme + tek yönlü nistagmus + skew yok → periferik; **normal kafa itme, yön değiştiren nistagmus, skew** → santral.\n- **BT arka çukurda duyarsız**; BTA/MR (DWI).\n- **Baziler oklüzyon**: tromboliz + **trombektomi** (24 saate kadar).\n\n*Kaynak: ESO-ESMINT 2023 arka dolaşım trombektomisi; ATTENTION & BAOCHE (NEJM 2022).*","good"),
 "n9":E("Baziler tıkanıklığın ilerlemesi","Hasta gece komaya girdi; “kilitli adam” sendromu gelişti.","bad"),
}))
Qs+=[Q("c100q1","Akut sürekli vertigoda santral nedeni düşündüren HINTS bulgusu hangisidir?",["Anormal kafa itme testi","Tek yönlü yatay nistagmus","Normal kafa itme testi + yön değiştiren nistagmus + skew deviasyonu","Pozisyonla kısa süreli vertigo","Kulak çınlaması"],2,"Bu üçlü santral (inme) lehinedir.","Nöroloji"),
 Q("c100q2","Arka çukur iskemisinde kontrastsız BT için doğru ifade hangisidir?",["Çok duyarlıdır","Duyarlılığı düşüktür; normal BT inmeyi dışlamaz","MR'dan üstündür","Tek başına yeterlidir","Gereksizdir"],1,"Kemik artefaktı ve erken iskemi nedeniyle.","Nöroloji"),
 Q("c100q3","Baziler arter oklüzyonunda güncel tedavi hangisidir?",["Yalnız aspirin","Uygun hastada tromboliz + endovasküler trombektomi","Yalnız gözlem","Steroid","Antihistaminik"],1,"2022 RKÇ'leri trombektominin yararını gösterdi.","Nöroloji")]

P={"id":"ilk-nobet-10","title":"İlk Nöbet Vakaları — 10. Paket","desc":"Serebral venöz sinüs trombozu, spontan pnömotoraks, pnömoni, peritonsiller apse, sinüzit (orbital komplikasyon), otitis media (mastoidit), nekrotizan otitis eksterna, sistit, gebelikte piyelonefrit, arka dolaşım inmesi.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 10. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 10. Paket","topic":"Acil tıp","order":10,"req":[1],"desc":"Sık başvuru nedenlerinin (enfeksiyonlar, baş dönmesi, pnömotoraks) atlanmaması gereken yüzleri.","intro":INTRO}}
build(P,sys.argv[1])
