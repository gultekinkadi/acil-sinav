import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 21 AKUT AKCİĞER ÖDEMİ (SCAPE)
S.append(case("c21","Gece başlayan nefes darlığı — 72 yaşında kadın","Kardiyoloji",
 "72 yaşında kadın, hipertansiyon ve diyabet. Gece uykudan nefes darlığıyla uyanmış, oturarak nefes almaya çalışıyor; pembe köpüklü balgam.",
 {"n1":N("Resüsitasyon alanı","Oturur pozisyonda, konuşamıyor, terli. Her iki akciğerde apekse kadar raller.","KB 214/118 · Nb 118 · SS 34 · SpO₂ %81 (oda havası)",[
   T("Akciğer USG (POCUS)",2,5,"Her iki hemitoraksta yaygın **B çizgileri**; VCI geniş.","Akciğer ödemini dakikalar içinde destekler."),
   T("EKG + troponin",1,30,"Sinüs taşikardisi, sol ventrikül hipertrofisi; akut ST elevasyonu yok.","Tetikleyici AKS dışlanmalı."),
   T("Akciğer grafisi",1,20,"Bilateral perihiler infiltrasyon, Kerley B çizgileri.","Tedaviyi geciktirmemeli."),
   A("Oturt; noninvaziv ventilasyon (CPAP 5–10 cmH₂O ya da BiPAP); yüksek doz nitrat (dil altı nitrogliserin tekrarlayan dozlar → IV nitrogliserin infüzyonu, hızla titre); furosemid IV (ör. 40 mg ya da evdeki dozun 1–2,5 katı)",4,10,"n2","Doğru. Hipertansif akut kalp yetmezliğinde (SCAPE) asıl tedavi ard yükü azaltmak: yüksek doz nitrat + NIV."),
   A("Yalnız furosemid 40 mg IV ver ve etkisini bekle",-2,30,"n3","Diüretik tek başına yavaş etkilidir; bu hastalar çoğunlukla hipervolemik değil, sıvı akciğere yeniden dağılmıştır."),
   A("Morfin 5 mg IV ile dispneyi rahatlat",-3,10,"n3","Morfin solunum depresyonu, kusma/aspirasyon ve artmış entübasyon ihtiyacıyla ilişkilidir; rutin önerilmez."),
 ]),
 "n3":N("20 dakika sonra","Hasta yorgun, uykuya meyilli.","KB 200/110 · SpO₂ %78 · SS 38",[
   A("Hemen NIV + yüksek doz nitrat; NIV başarısız/bilinç kötüleşirse entübasyon",2,15,"n2","Doğru ama gecikmeli."),
   A("Bir doz daha furosemid",-3,20,"n9","Hipoksi derinleşiyor; ard yük azaltılmadan diüretik yetersiz kalır."),
 ]),
 "n2":E("Hızlı düzelme","NIV ve nitrat infüzyonuyla 45 dakikada SpO₂ %95, KB 150/88; hasta konuşabiliyor. Koroner yoğun bakıma alındı.\n\n**Akılda kalsın**\n- **SCAPE** (ani, hipertansif akciğer ödemi): ard yük azaltma + NIV.\n- **Yüksek doz nitrat** (SL tekrar + IV infüzyon hızla artırılır); KB düşükse (<110) nitrat verme.\n- **CPAP/BiPAP** entübasyonu azaltır.\n- Furosemid IV — yardımcı.\n- **Morfin rutin değil**.\n- Tetikleyiciyi ara: AKS, aritmi, ilaç/tuz uyumsuzluğu, böbrek arter stenozu.\n\n*Kaynak: ESC 2021 (2023 güncelleme) Kalp Yetmezliği Kılavuzu.*","good"),
 "n9":E("Entübasyon","Hasta solunum yetmezliğine girip entübe edildi; yoğun bakımda uzun kaldı.\n\nAkut akciğer ödeminde erken NIV ve yüksek doz nitrat entübasyonu önler.","bad"),
}))
Qs+=[Q("c21q1","Hipertansif akut akciğer ödeminde (SCAPE) en etkili ilk ilaç tedavisi hangisidir?",["Morfin","Yüksek doz nitrogliserin","Digoksin","Dobutamin","Beta bloker IV"],1,"Ard yükü hızla azaltan yüksek doz nitrat, NIV ile birlikte temel tedavidir.","Kardiyoloji"),
 Q("c21q2","Akut akciğer ödeminde noninvaziv ventilasyonun temel yararı hangisidir?",["Diürezi artırır","Entübasyon ihtiyacını azaltır","KB'yi yükseltir","Aritmiyi önler","Antikoagülan etkisi vardır"],1,"CPAP/BiPAP solunum işini ve ön/ard yükü azaltır; entübasyonu azaltır.","Kardiyoloji"),
 Q("c21q3","Hangi durumda akut kalp yetmezliğinde nitrat verilmez?",["KB 190/110","Sistolik KB <90–110 mmHg","Raller","Ortopne","Diyabet"],1,"Hipotansiyonda nitrat kontrendikedir.","Kardiyoloji")]

# 22 TESTİS TORSİYONU
S.append(case("c22","Ani skrotal ağrı — 15 yaşında erkek","Üroloji",
 "15 yaşında erkek. 2 saat önce uykudan ani, şiddetli sol skrotal ağrıyla uyanmış; bulantı ve bir kez kusma. Travma yok, idrar yakınması yok.",
 {"n1":N("Muayene","Sol testis yukarıda ve yatay duruşlu, çok hassas. **Sol kremaster refleksi yok.** Skrotumda hafif ödem.","KB 128/74 · Nb 104 · Ateş 36,7",[
   T("TWIST skoru",1,2,"Testis şişliği (2) + sert testis (2) + kremaster refleksi yok (1) + bulantı/kusma (1) + yüksek yerleşimli testis (1) = **7** (yüksek risk).","TWIST ≥5 yüksek risk: görüntüleme beklemeden cerrahi."),
   T("Renkli Doppler USG",0,40,"Sol testiste akım yok. 40 dakika geçti.","Klinik şüphe yüksekse USG cerrahiyi geciktirmemeli."),
   T("Tam idrar",0,20,"Normal.","Epididimitte piyüri olabilir; normal idrar torsiyonu destekler."),
   A("Hemen üroloji — acil skrotal eksplorasyon; analjezi, aç bırak. Ameliyathane gecikecekse manuel detorsiyon dene (“kitabı açar gibi”, içten dışa)",4,15,"n2","Doğru. Testisi kurtarma oranı ilk 6 saatte çok yüksek, sonrasında hızla düşer."),
   A("Epididimit — antibiyotik ve analjezik ile taburcu",-5,20,"n9","Ani başlangıç, kusma, yüksek yerleşimli testis ve kremaster refleksi kaybı torsiyon lehinedir."),
 ]),
 "n2":E("Testis kurtarıldı","4. saatte ameliyata alındı; 720° torsiyon, detorsiyon sonrası testis renk aldı, bilateral orşiopeksi yapıldı.\n\n**Akılda kalsın**\n- Ani skrotal ağrı = **aksi kanıtlanana kadar torsiyon**.\n- Kremaster refleksi kaybı, yüksek/yatay testis, kusma.\n- **Zaman testistir**: ilk 6 saatte kurtarma >%90.\n- Şüphe yüksekse **USG beklemeden eksplorasyon**; manuel detorsiyon köprü olabilir.\n- Karşı testise de orşiopeksi.\n\n*Kaynak: EAU 2024 Pediatrik Üroloji Kılavuzu.*","good"),
 "n9":E("Testis kaybı","Hasta 24 saat sonra artan ağrıyla döndü; nekrotik testis için orşiektomi yapıldı.\n\nAni başlayan skrotal ağrıda torsiyon dışlanmadan taburculuk yapılmaz.","bad"),
}))
Qs+=[Q("c22q1","Testis torsiyonunu en çok düşündüren muayene bulgusu hangisidir?",["Prehn bulgusu pozitif","Kremaster refleksinin olmaması","Piyüri","Ateş","Mavi nokta bulgusu"],1,"Kremaster refleksi kaybı torsiyon için duyarlı bir bulgudur.","Üroloji"),
 Q("c22q2","Testis torsiyonunda kurtarma oranı hangi sürede en yüksektir?",["İlk 6 saat","12–24 saat","24–48 saat","72 saat","Süre önemsiz"],0,"İlk 6 saatte kurtarma >%90; 24 saatten sonra <%10.","Üroloji"),
 Q("c22q3","Klinik olarak yüksek olasılıklı torsiyonda doğru yaklaşım hangisidir?",["Doppler USG sonucunu beklemek","Antibiyotik başlayıp izlemek","Acil cerrahi eksplorasyon","Sintigrafi","24 saat sonra kontrol"],2,"Görüntüleme cerrahiyi geciktirmemelidir.","Üroloji")]

# 23 EKTOPİK GEBELİK
S.append(case("c23","Karın ağrısı ve bayılma — 28 yaşında kadın","Kadın doğum",
 "28 yaşında kadın. Son adeti 7 hafta önce. Bugün ani başlayan sol alt kadran ağrısı ve tuvalette bayılma. Hafif vajinal kanama var. Daha önce pelvik enfeksiyon geçirmiş.",
 {"n1":N("Resüsitasyon alanı","Soluk, terli. Karın yaygın hassas, defans. Omuz ağrısı tarifliyor.","KB 82/50 · Nb 128 · SS 22 · SpO₂ %98",[
   T("İdrarda/serumda β-hCG",2,5,"**Pozitif**.","Doğurganlık çağındaki her kadında karın ağrısı/senkopta gebelik testi."),
   T("POCUS (FAST)",3,5,"**Morison poşunda ve pelviste serbest sıvı**; uterus içinde gebelik kesesi yok.","Pozitif gebelik + şok + serbest sıvı = rüptüre ektopik kabul edilir."),
   T("Transvajinal USG (radyoloji)",-2,40,"Sol adneksiyel kitle, yaygın hemoperitoneum. 40 dakika kaybedildi.","Hemodinamik bozuklukta resmi görüntüleme cerrahiyi geciktirmemeli."),
   A("İki geniş damar yolu, kan grubu/çapraz karşılaştırma, masif transfüzyon protokolü (eritrosit:TDP:trombosit dengeli); acil kadın doğum — ameliyathane",4,15,"n2","Doğru. Hemodinamik instabilitede tedavi cerrahidir."),
   A("Metotreksat başla, β-hCG takibi",-5,20,"n9","Metotreksat yalnız hemodinamik olarak stabil, rüptüre olmamış seçilmiş olgularda uygundur."),
 ]),
 "n2":N("Ameliyathaneye giderken","Kan grubu **0 Rh negatif**.","KB 96/58 · Nb 112",[
   A("Anti-D immünglobulin uygula (Rh negatif, cerrahi tedavi)",2,5,"n3","Doğru. Rh negatif ektopik gebelikte cerrahi tedavi sonrası anti-D önerilir."),
   A("Rh durumu önemli değil",-1,5,"n3","Rh izoimmünizasyonu sonraki gebelikleri etkiler."),
 ]),
 "n3":E("Salpenjektomi","Laparoskopide rüptüre sol tubal ektopik; 1,5 L hemoperitoneum. Salpenjektomi yapıldı, hasta stabil.\n\n**Akılda kalsın**\n- Doğurganlık çağında karın ağrısı/senkop/vajinal kanama → **β-hCG**.\n- β-hCG pozitif + uterus içi gebelik yok + serbest sıvı + şok = **rüptüre ektopik**.\n- **POCUS** dakikalar içinde yönlendirir; instabilitede **doğrudan ameliyathane**.\n- Metotreksat yalnız stabil, rüptüre olmayan seçilmiş hastada.\n- Rh negatifse **anti-D**.\n\n*Kaynak: ACOG 2018 tubal ektopik gebelik; NICE NG126 (2023).*","good"),
 "n9":E("Hemorajik şok","Hasta hipovolemik arrest geçirdi; acil laparotomiye geç alındı.\n\nRüptüre ektopik cerrahi bir acildir.","bad"),
}))
Qs+=[Q("c23q1","β-hCG pozitif, hipotansif ve FAST'ta serbest sıvısı olan kadında ilk yaklaşım hangisidir?",["Metotreksat","48 saat β-hCG takibi","Resüsitasyon + acil cerrahi","Transvajinal USG için radyolojiye sevk","Analjezik ve gözlem"],2,"Hemodinamik instabilitede rüptüre ektopik kabul edilip cerrahiye alınır.","Kadın doğum"),
 Q("c23q2","Ektopik gebelikte metotreksat için uygun olmayan durum hangisidir?",["Hemodinamik stabilite","Rüptür bulguları ve hemoperitoneum","β-hCG <5000","Kardiyak aktivite yok","Takibe uyumlu hasta"],1,"Rüptür ve instabilite metotreksat kontrendikasyonudur.","Kadın doğum"),
 Q("c23q3","Rh negatif ektopik gebelikte cerrahi sonrası ne yapılmalıdır?",["Hiçbir şey","Anti-D immünglobulin","IVIG","Rh pozitif kan transfüzyonu","Kortikosteroid"],1,"İzoimmünizasyonu önlemek için anti-D önerilir.","Kadın doğum")]

# 24 YABANCI CİSİM ASPİRASYONU (ÇOCUK)
S.append(case("c24","Fıstık yerken öksürük — 2 yaşında erkek","Pediatri",
 "2 yaşında erkek çocuk. Annesi, 3 saat önce kardeşleriyle fıstık yerken aniden boğulur gibi öksürmeye başladığını, morardığını, sonra öksürüğün azaldığını anlatıyor. Şimdi ara ara öksürüyor.",
 {"n1":N("Çocuk acil","Çocuk ağlıyor, konuşabiliyor (kelimeler), hava giriş-çıkışı var. **Sağda solunum sesleri azalmış**, sağda wheezing.","Nb 132 · SS 34 · SpO₂ %95 · Ateş 36,8",[
   T("Akciğer grafisi (inspiryum + ekspiryum ya da lateral dekübit)",2,20,"Ekspiryumda **sağ akciğerde hava hapsi** (hiperinflasyon), mediasten sola itilmiş. Opak cisim görülmüyor.","Fıstık radyolusenttir; normal grafi aspirasyonu dışlamaz."),
   T("Kör parmakla ağız içi tarama",-3,1,"Cisim yok; çocuk öğürdü, morardı.","Kör parmak taraması cismi daha derine itebilir; yapılmaz."),
   A("Çocuk öksürebiliyor ve stabil: sakin tut, annesinin kucağında oturt, O₂ hazır; çocuk göğüs cerrahisi/KBB — rijit bronkoskopi",4,20,"n2","Doğru. Etkili öksürük varken müdahale etme, ajite etme; tanı ve tedavi bronkoskopidir."),
   A("Bronşiolit — salbutamol nebül ve taburcu",-5,20,"n9","Ani boğulma öyküsü + tek taraflı bulgu = aspirasyon kabul edilir."),
 ]),
 "n2":N("Bronkoskopi beklenirken","Çocuk aniden morarıyor, sessizleşiyor; öksüremiyor, ağlayamıyor.","SpO₂ %78 · Nb 160",[
   A("Etkisiz öksürük, bilinç açık: 5 sırt vuruşu + 5 karın baskısı (1 yaş üstü); bilinç kaybolursa CPR'a başla, her solunumda ağza bak; hava yolu ekibi",3,2,"n3","Doğru. 1 yaş altında karın baskısı yerine göğüs baskısı."),
   A("Hemen kör parmakla cismi çıkarmaya çalış",-4,2,"n9","Kör parmak taraması cismi ilerletir."),
 ]),
 "n3":E("Rijit bronkoskopi","Manevralarla cisim yer değiştirip çocuk yeniden öksürmeye başladı; acil rijit bronkoskopide sağ ana bronştan fıstık parçası çıkarıldı.\n\n**Akılda kalsın**\n- Ani boğulma/öksürük öyküsü = **aspirasyon** (grafi normal olabilir).\n- **Etkili öksürük**: öksürmeyi teşvik et, müdahale etme, sakin tut.\n- **Etkisiz öksürük, bilinç açık**: 5 sırt vuruşu + 5 karın (≥1 yaş) / göğüs (<1 yaş) baskısı.\n- Bilinç kaybı: CPR; **kör parmak taraması yok**.\n- Tanı/tedavi: **rijit bronkoskopi**.\n\n*Kaynak: ERC 2021 Pediatrik Yaşam Desteği.*","good"),
 "n9":E("Gecikmiş tanı / arrest","Aspirasyon atlandı; çocuk günler sonra tekrarlayan pnömoniyle geldi ya da tam tıkanma ile hipoksik arrest gelişti.\n\nYabancı cisim öyküsü her zaman ciddiye alınır.","bad"),
}))
Qs+=[Q("c24q1","Etkisiz öksürüğü olan, bilinci açık 3 yaşındaki çocukta ilk yaklaşım hangisidir?",["Kör parmakla ağız taraması","5 sırt vuruşu + 5 karın baskısı","Hemen CPR","Ters çevirip sallamak","Su içirmek"],1,"≥1 yaş: 5 sırt vuruşu, ardından 5 karın baskısı; <1 yaş: göğüs baskısı.","Pediatri"),
 Q("c24q2","Fıstık aspirasyonunda akciğer grafisi için doğru ifade hangisidir?",["Cisim her zaman görünür","Normal grafi aspirasyonu dışlar","Ekspiryum grafisinde hava hapsi görülebilir; normal grafi dışlamaz","BT zorunludur","Grafi kontrendikedir"],2,"Organik cisimler radyolusenttir; dolaylı bulgular (hava hapsi, atelektazi) aranır.","Pediatri"),
 Q("c24q3","1 yaş altı bebekte etkisiz öksürükle seyreden yabancı cisim aspirasyonunda hangi uygulama yapılmaz?",["Sırt vuruşu","Göğüs baskısı","Karın baskısı (Heimlich)","Bilinç kaybında CPR","Ağızda görünür cismin alınması"],2,"Bebeklerde karın baskısı iç organ yaralanması riski nedeniyle önerilmez.","Pediatri")]

# 25 AKUT PANKREATİT
S.append(case("c25","Sırta vuran karın ağrısı — 45 yaşında erkek","Gastroenteroloji",
 "45 yaşında erkek, düzenli alkol kullanıyor. Dün akşamdan beri epigastriumda başlayıp sırta yayılan, öne eğilince azalan şiddetli ağrı ve kusma. Yaklaşık 75 kg.",
 {"n1":N("Muayene","Epigastrik hassasiyet, defans yok. Bağırsak sesleri azalmış.","KB 122/74 · Nb 112 · SS 20 · SpO₂ %96 · Ateş 37,6",[
   T("Lipaz",2,30,"**Normalin 9 katı**.","Tipik ağrı + lipaz/amilaz ≥3 kat → tanı. BT gerekmez."),
   T("Hemogram, üre, kreatinin, kalsiyum, trigliserid, KCFT",1,40,"Hct 48, BUN 26, kreatinin 1,1, Ca 8,6, trigliserid 180, ALT 52, bilirubin normal.","Yükselen BUN/Hct ağır seyir habercisi; trigliserid ve kalsiyum etiyoloji."),
   T("Abdominal USG",2,20,"Safra kesesinde taş yok; pankreas ödemli.","Her pankreatitte safra taşı için USG."),
   T("Kontrastlı abdominal BT (hemen)",-2,40,"Ödematöz pankreatit. Tanı zaten kesindi.","Erken BT tanı belirsizse istenir; nekroz/komplikasyon değerlendirmesi 72 saatten sonra."),
   A("Hedefe yönelik ılımlı sıvı (Ringer laktat; hipovolemide 10 mL/kg bolus, sonra ≈1,5 mL/kg/saat; idrar, Hct, BUN ile yeniden değerlendir); opioid dahil yeterli analjezi; antiemetik; tolere ederse erken oral beslenme",4,15,"n2","Doğru. WATERFALL: agresif sıvı yararlı değil, sıvı yüklenmesini artırır."),
   A("Agresif sıvı: 20 mL/kg bolus + 3 mL/kg/saat; profilaktik imipenem başla",-3,15,"n3","Agresif sıvı sıvı yüklenmesine yol açar; profilaktik antibiyotik önerilmez."),
 ]),
 "n3":N("12. saat","Hasta takipneik, bazallerde raller.","SpO₂ %89 · SS 30",[
   A("Sıvıyı azalt, O₂, yeniden değerlendir; antibiyotiği kes (enfeksiyon kanıtı yok)",1,10,"n2","Doğru — geç fark edildi."),
   A("Sıvıyı sürdür",-3,30,"n9","Sıvı yüklenmesi ARDS'yi kötüleştirir."),
 ]),
 "n2":E("Hafif pankreatit — iyileşme","Ağrı 48 saatte geriledi, ikinci gün oral beslenmeye geçildi. Alkol bırakma danışmanlığı verildi.\n\n**Akılda kalsın**\n- Tanı: 3 kriterin 2'si — tipik ağrı, lipaz/amilaz ≥3 kat, görüntüleme.\n- **USG ile safra taşı** her hastada.\n- **Ilımlı, hedefe yönelik sıvı** (Ringer laktat); agresif sıvıdan kaçın.\n- Yeterli analjezi (opioid uygun).\n- **Erken oral beslenme**; uzun süre aç bırakma yok.\n- **Profilaktik antibiyotik yok**; enfekte nekroz şüphesinde.\n- BT: tanı belirsizse ya da 72 saatten sonra komplikasyon için.\n\n*Kaynak: ACG 2024 akut pankreatit kılavuzu; WATERFALL (NEJM 2022).*","good"),
 "n9":E("Solunum yetmezliği","Aşırı sıvı ile ARDS gelişti; hasta yoğun bakımda entübe edildi.\n\nPankreatitte sıvı tedavisi hedefe yönelik ve ölçülü olmalı.","bad"),
}))
Qs+=[Q("c25q1","Akut pankreatitte önerilen sıvı stratejisi hangisidir?",["Herkese 20 mL/kg bolus + 3 mL/kg/saat","Hedefe yönelik ılımlı sıvı (Ringer laktat)","Sıvı kısıtlaması","Yalnız %5 dekstroz","Albümin"],1,"WATERFALL'da agresif sıvı yararlı değil, sıvı yüklenmesini artırdı.","Gastroenteroloji"),
 Q("c25q2","Akut pankreatitte profilaktik antibiyotikle ilgili doğru ifade hangisidir?",["Tüm hastalara verilir","Nekrotizan pankreatitte rutin verilir","Önerilmez; yalnız kanıtlanmış/şüpheli enfeksiyonda","Yalnız alkolik pankreatitte verilir","İlk 72 saatte zorunludur"],2,"Profilaktik antibiyotik, nekrotizan olgularda bile, önerilmez.","Gastroenteroloji"),
 Q("c25q3","Tipik ağrı ve lipaz 5 kat yüksek olan hastada erken kontrastlı BT için doğru ifade hangisidir?",["Tanı için zorunlu","Tanı kesinse gerekmez; komplikasyon için 72 saatten sonra","Mutlaka ilk saatte çekilir","Antibiyotik kararı için şart","Hiçbir zaman gerekmez"],1,"Tanı klinik + laboratuvarla konmuşsa erken BT gereksizdir.","Gastroenteroloji")]

# 26 HİPONATREMİ (ağır, semptomatik)
S.append(case("c26","Konfüzyon ve nöbet — 76 yaşında kadın","Nefroloji / Metabolik",
 "76 yaşında kadın. Hipertansiyon için 3 aydır hidroklorotiyazid kullanıyor; sıcak günlerde bol su içiyor. İki gündür bulantı ve dengesizlik, bugün konfüze. Acilde 1 dakika süren jeneralize nöbet geçirdi.",
 {"n1":N("Resüsitasyon alanı","Postiktal, GKS 12. Ödem yok, mukozalar nemli.","KB 142/80 · Nb 92 · SpO₂ %97 · Glukoz 110",[
   T("Na, K, osmolalite",3,10,"**Na 112 mmol/L**, K 3,1, serum osmolalitesi 236 mOsm/kg.","Hipotonik ağır hiponatremi; nöbet = ağır semptom."),
   T("İdrar osmolalitesi ve idrar Na",1,30,"İdrar osm 380, idrar Na 48.","Tiyazid ve SIADH'de benzer; tedaviyi geciktirmez."),
   A("Ağır semptomatik hiponatremi: %3 NaCl 150 mL (veya 100 mL) 20 dakikada IV bolus; 20 dakika sonra Na kontrol; gerekirse tekrarla (en çok 2–3 kez) — hedef ilk saatte 4–6 mmol/L artış; tiyazidi kes",4,20,"n2","Doğru. Beyin ödemini durdurmak için hızlı ama sınırlı artış yeterlidir."),
   A("%0,9 NaCl 1000 mL hızlı infüzyon",-2,60,"n3","İzotonik serum ağır semptomatik hiponatremide yetersiz, SIADH benzeri durumlarda Na'yı düşürebilir."),
   A("Sıvı kısıtla ve sabahı bekle",-4,240,"n9","Nöbet geçiren hastada acil hipertonik tedavi gerekir."),
 ]),
 "n3":N("1 saat sonra","Hasta yeniden nöbet geçiriyor.","Na 111",[
   A("%3 NaCl 150 mL 20 dakikada bolus",2,20,"n2","Doğru — gecikmeli."),
 ]),
 "n2":N("İlk 6 saat","İki bolus sonrası Na 117; nöbet yok, bilinç düzeliyor. Hasta çok idrar yapıyor (tiyazid kesildi, su diürezi).","Na (6. saat) 119 · idrar çıkışı 400 mL/saat",[
   A("Aşırı düzeltme riski: 24 saatlik artışı ≤8–10 mmol/L ile sınırla (yüksek risk hastada ≤8); 2–4 saatte bir Na; gerekirse desmopressin + %5 dekstroz ile düzeltmeyi frenle",4,20,"n4","Doğru. Hipokalemi, yaşlılık, malnütrisyon ozmotik demiyelinizasyon riskini artırır; potasyum da Na'yı yükseltir."),
   A("Na hâlâ düşük — hipertonik infüzyonu sürdür",-4,60,"n9","Na 24 saatte 12 mmol/L'yi aştı; ozmotik demiyelinizasyon riski."),
 ]),
 "n4":E("Güvenli düzeltme","24. saatte Na 120 (+8). Hasta nörolojik sekelsiz düzeldi; tiyazid kalıcı olarak kesildi.\n\n**Akılda kalsın**\n- Ağır semptom (nöbet, koma, kusma, solunum sıkıntısı) → **%3 NaCl 150 mL (veya 100 mL) 20 dakikada**, Na'ya göre 2–3 kez.\n- Hedef: ilk saatlerde **+4–6 mmol/L** (semptomları durdurmaya yeter).\n- Sınır: **24 saatte ≤10 mmol/L** (yüksek riskte ≤8).\n- Su diürezi + K replasmanı aşırı düzeltmeye yol açar → sık Na, gerekirse **desmopressin**.\n- Neden: tiyazid, SIADH, polidipsi, hipovolemi, adrenal yetmezlik, hipotiroidi.\n\n*Kaynak: Avrupa (ESE/ESICM/ERA-EDTA) 2014 hiponatremi kılavuzu; ABD uzman paneli 2013.*","good"),
 "n9":E("Komplikasyon","Ya tedavisiz beyin ödemiyle herniasyon ya da aşırı hızlı düzeltmeyle günler sonra ozmotik demiyelinizasyon (dizartri, disfaji, kuadriparezi) gelişti.\n\nAğır hiponatremide hem hızlı başla hem de frenle.","bad"),
}))
Qs+=[Q("c26q1","Nöbet geçiren ağır hiponatremik hastada ilk tedavi hangisidir?",["%0,9 NaCl 1 L","Sıvı kısıtlaması","%3 NaCl 150 mL 20 dakikada bolus","Tolvaptan","Furosemid"],2,"Ağır semptomda hipertonik bolus, gerekirse tekrar.","Nefroloji / Metabolik"),
 Q("c26q2","Kronik hiponatreminin düzeltilmesinde 24 saatlik üst sınır (genel) hangisidir?",["4 mmol/L","10 mmol/L (yüksek riskte 8)","15 mmol/L","20 mmol/L","Sınır yoktur"],1,"Aşırı hızlı düzeltme ozmotik demiyelinizasyona yol açar.","Nefroloji / Metabolik"),
 Q("c26q3","Hangisi ozmotik demiyelinizasyon için risk faktörü değildir?",["Hipokalemi","Alkolizm","Malnütrisyon","Na 112 mmol/L","Genç ve sağlıklı olmak"],4,"Hipokalemi, alkol, malnütrisyon, karaciğer hastalığı ve Na ≤105 riski artırır.","Nefroloji / Metabolik")]

# 27 SVT
S.append(case("c27","Çarpıntı — 31 yaşında kadın","Kardiyoloji",
 "31 yaşında kadın. 40 dakika önce aniden başlayan hızlı çarpıntı; daha önce de benzer ataklar olmuş, kendiliğinden geçmiş. Astımı yok. Göğüs ağrısı ve bayılma yok.",
 {"n1":N("Muayene odası","Anksiyöz, konuşabiliyor. Boyun venlerinde hızlı pulsasyon.","KB 118/74 · Nb 192 (düzenli) · SpO₂ %98",[
   T("12 derivasyonlu EKG",2,5,"**Dar QRS, düzenli taşikardi 192/dk**, P dalgası seçilmiyor (AVNRT ile uyumlu).","Düzenli dar QRS taşikardi; stabil."),
   A("Modifiye Valsalva (oturur pozisyonda 15 saniye 40 mmHg zorlama → hemen sırtüstü yatırıp bacakları 15 saniye 45° kaldır)",3,5,"n2","Doğru. REVERT çalışmasında modifiye Valsalva ile başarı ≈%43 (standart Valsalva ≈%17)."),
   A("Hemen senkronize kardiyoversiyon",-2,20,"n4","Stabil hastada önce vagal manevra ve adenozin denenir; sedasyon gereksiz risk."),
   A("Karotis masajı (her iki tarafa birlikte)",-4,5,"n9","Bilateral karotis masajı asla yapılmaz; yaşlıda ve üfürümde tek taraflı bile risklidir."),
 ]),
 "n2":N("Manevra sonrası","Taşikardi sürüyor.","Nb 190 · KB 116/72",[
   A("Adenozin 6 mg hızlı IV (antekübital, üç yollu musluktan 20 mL SF ile hızlı yıkama; kolu kaldır); yanıt yoksa 12 mg (gerekirse bir kez daha 12 mg). Hastayı geçici göğüs sıkışması/“kötü his” konusunda uyar; monitörde kaydet",4,10,"n3","Doğru. Adenozinin yarılanma ömrü saniyelerdir; hızlı itme ve yıkama şart."),
   A("Adenozini yavaş infüzyonla 5 dakikada ver",-2,10,"n4","Yavaş verilen adenozin kalbe ulaşmadan yıkılır; etkisiz."),
   A("Verapamil 5 mg IV, 2 dakikada (adenozin kontrendike ise alternatif)",1,15,"n3","Kabul edilebilir alternatif; ilk seçenek adenozindir. Düşük EF ve hipotansiyonda kaçın."),
 ]),
 "n4":N("Yeniden değerlendirme","Hasta stabil, taşikardi sürüyor.","Nb 188",[
   A("Adenozin 6 → 12 mg hızlı IV bolus + yıkama",2,10,"n3","Doğru."),
 ]),
 "n3":E("Sinüs ritmi","Adenozin 12 mg sonrası kısa asistoli ardından sinüs ritmi 82/dk. EKG'de preeksitasyon yok. Ablasyon değerlendirmesi için kardiyolojiye yönlendirildi.\n\n**Akılda kalsın**\n- **Instabilite** (şok, senkop, iskemi, kalp yetmezliği) → **senkronize kardiyoversiyon**.\n- Stabil düzenli dar QRS: **modifiye Valsalva** → **adenozin 6 → 12 mg** hızlı IV + yıkama.\n- Alternatif: verapamil/diltiazem (EF korunmuş, KB normal).\n- Adenozin ciddi astımda dikkat; **dipiridamol, karbamazepin, kalp nakli** → doz azalt.\n- Ritim kaydı önemlidir; tekrarlayan SVT'de **ablasyon** küratif.\n\n*Kaynak: ESC 2019 SVT Kılavuzu; REVERT (Lancet 2015).*","good"),
 "n9":E("Komplikasyon","Bilateral karotis masajı sonrası hasta senkop geçirdi; uzamış asistoli.\n\nVagal manevra olarak modifiye Valsalva güvenli ve etkilidir.","bad"),
}))
Qs+=[Q("c27q1","Stabil düzenli dar QRS taşikardide modifiye Valsalva manevrasının farkı nedir?",["Karotis masajı ile birlikte yapılır","Zorlamadan hemen sonra sırtüstü yatırıp bacakları kaldırmak","Buzlu suya yüz batırma","Gözlere bası","Öksürtme"],1,"Zorlama sonrası pasif bacak kaldırma vagal yanıtı artırır.","Kardiyoloji"),
 Q("c27q2","Erişkin SVT'de adenozinin başlangıç dozu hangisidir?",["1 mg","3 mg","6 mg hızlı IV bolus","12 mg infüzyon","0,1 mg/kg"],2,"6 mg hızlı bolus + yıkama; yanıt yoksa 12 mg.","Kardiyoloji"),
 Q("c27q3","SVT'li hipotansif ve bilinci bulanık hastada ilk tedavi hangisidir?",["Adenozin","Verapamil","Senkronize kardiyoversiyon","Amiodaron infüzyonu","Vagal manevra"],2,"Hemodinamik instabilitede senkronize elektriksel kardiyoversiyon.","Kardiyoloji")]

# 28 NEKROTİZAN FASİİT
S.append(case("c28","Bacakta şiddetli ağrı — 54 yaşında erkek","Enfeksiyon / Cerrahi",
 "54 yaşında erkek, kötü kontrollü diyabet. 2 gün önce bahçede uyluğunu çizmiş. Dünden beri sağ uylukta hızla artan, görünümüne göre çok şiddetli ağrı; bugün titreme ve halsizlik.",
 {"n1":N("Resüsitasyon alanı","Sağ uylukta sınırları belirsiz eritem, gergin ödem, mor-gri renk değişikliği ve büller; palpasyonda **krepitasyon**. Ağrı muayeneyle orantısız şiddetli; eritemin dışında da hassasiyet var.","KB 86/50 · Nb 126 · SS 24 · Ateş 39,0",[
   T("Laboratuvar (LRINEC bileşenleri), laktat, kan kültürü",2,30,"CRP 280, lökosit 24.000, Na 131, kreatinin 1,9, glukoz 380, Hb 11 → LRINEC 9. Laktat 4,2.","LRINEC yüksekse destekler, ama **düşük skor nekrotizan fasiiti dışlamaz**."),
   T("BT (cerrahi kararından önce)",-2,60,"Fasya boyunca gaz. 1 saat kaybedildi.","Klinik tanı açıksa görüntüleme cerrahiyi geciktirmemeli."),
   A("Sepsis resüsitasyonu + geniş spektrumlu antibiyotik (ör. meropenem veya piperasilin-tazobaktam + vankomisin/linezolid + **klindamisin**); acil cerrahi konsültasyon — debridman",4,15,"n2","Doğru. Erken cerrahi debridman mortaliteyi belirleyen en önemli faktördür; klindamisin toksin üretimini baskılar."),
   A("Selülit — IV sefazolin, servis yatışı, ertesi gün değerlendirme",-5,60,"n9","Orantısız ağrı, krepitasyon, bül ve şok nekrotizan enfeksiyonun kırmızı bayraklarıdır."),
 ]),
 "n2":E("Acil debridman","2 saat içinde ameliyathaneye alındı; geniş debridman, 24 saat sonra ikinci bakış. Kültürde polimikrobiyal üreme. Hasta 3 haftada iyileşti.\n\n**Akılda kalsın**\n- Kırmızı bayraklar: **muayeneyle orantısız ağrı**, eritem dışı hassasiyet, hızlı yayılım, bül, nekroz, **krepitasyon**, sistemik toksisite.\n- **LRINEC dışlama aracı değildir**.\n- Tedavi: **erken cerrahi debridman** (tekrarlı), geniş spektrum + **klindamisin**, sepsis resüsitasyonu.\n- Görüntüleme cerrahiyi geciktirmez.\n\n*Kaynak: IDSA 2014 deri ve yumuşak doku enfeksiyonları; WSES/SIS-E 2022.*","good"),
 "n9":E("Septik şok — amputasyon","Ertesi sabah enfeksiyon gövdeye yayıldı; kalça dezartikülasyonu gerekti, hasta yoğun bakımda çoklu organ yetmezliğine girdi.\n\nNekrotizan fasiitte zaman doku ve yaşamdır.","bad"),
}))
Qs+=[Q("c28q1","Nekrotizan fasiitin en erken ve önemli klinik ipucu hangisidir?",["Yüksek ateş","Muayene bulgularıyla orantısız şiddetli ağrı","Lenfanjit","Kaşıntı","Bölgesel lenfadenopati"],1,"Erken dönemde deri bulguları silik olabilir; orantısız ağrı en önemli ipucudur.","Enfeksiyon / Cerrahi"),
 Q("c28q2","Nekrotizan fasiit tedavisine klindamisin eklenmesinin amacı nedir?",["Böbrek koruması","Toksin üretimini baskılamak","Anaerop dışı Gram negatif kapsama","Antipiretik etki","Ağrı kontrolü"],1,"Klindamisin protein sentezini inhibe ederek streptokok/klostridyal toksin üretimini azaltır.","Enfeksiyon / Cerrahi"),
 Q("c28q3","LRINEC skoru düşük (≤5) olan ama klinik şüphe yüksek hastada ne yapılır?",["Nekrotizan fasiit dışlanmıştır","Selülit tedavisi ve taburculuk","Cerrahi değerlendirme yine yapılır","48 saat beklenir","Yalnız MR çekilir"],2,"LRINEC'in duyarlılığı düşüktür; klinik şüphe cerrahi eksplorasyon gerektirir.","Enfeksiyon / Cerrahi")]

# 29 EPİGLOTİT (erişkin)
S.append(case("c29","Boğaz ağrısı ve salya akıtma — 45 yaşında erkek","KBB / Hava yolu",
 "45 yaşında erkek. Dün başlayan ve hızla artan boğaz ağrısı, yutkunamıyor, sesi boğuk (“ağzında patates varmış gibi”). Bugün tükürüğünü yutamadığı için salya akıyor.",
 {"n1":N("Triaj","Öne eğilerek oturuyor (tripod), salya akıyor. Ağız içi muayenede farenks neredeyse normal görünüyor. Hafif inspiratuvar stridor.","Nb 118 · SS 24 · SpO₂ %95 · Ateş 38,9",[
   T("Yatak başı nazofaringolaringoskopi (KBB, oturur pozisyonda)",3,15,"**Ödemli, kızarık epiglot** ve ariepiglottik plikalar; hava yolu yaklaşık %50 daralmış.","Stabil erişkinde tanı, hava yolu ekibi hazırken esnek endoskopi ile konur."),
   T("Dil basacağıyla zorlayarak boğaz muayenesi, hastayı sırtüstü yatır",-4,2,"Hasta ajite oldu, stridor arttı, SpO₂ %88.","Sırtüstü pozisyon ve ajitasyon tam tıkanmayı tetikleyebilir."),
   T("Lateral boyun grafisi (radyolojiye gönder)",-2,30,"Başparmak bulgusu. Hasta gözetimsiz kaldı.","Hava yolu riski olan hasta gözetimsiz radyolojiye gönderilmez."),
   A("Hastayı rahat ettiği oturur pozisyonda bırak, ajite etme, O₂; zor hava yolu ekibi (anestezi + KBB) ve cerrahi hava yolu hazırlığı; IV seftriakson (± vankomisin); deksametazon düşünülebilir",4,10,"n2","Doğru. Erişkin epiglotitte hava yolu kaybı aniden olabilir; plan A, B, C (krikotirotomi) hazır olmalı."),
   A("Boğaz ağrısı — oral antibiyotik ve analjezikle taburcu",-5,10,"n9","Salya akıtma, boğuk ses, stridor ve muayeneyle orantısız odinofaji epiglotit kırmızı bayraklarıdır."),
 ]),
 "n2":N("Stridor artıyor","Hasta yorgunlaşıyor.","SpO₂ %90 · SS 30",[
   A("Ameliyathanede, hasta oturur pozisyonda ve spontan solurken uyanık fiberoptik entübasyon; KBB krikotirotomi/trakeotomi için hazır",4,20,"n3","Doğru. Uyanık teknik spontan solunumu korur; paralitik ile hızlı ardışık entübasyon başarısız olursa “entübe edilemiyor, oksijenlenemiyor” tablosu gelişebilir."),
   A("Acilde nöromüsküler blokerle hızlı ardışık entübasyon",-2,10,"n3","Riskli: ödemli epiglotte görüntü kötü; başarısızlıkta acil krikotirotomi gerekti."),
 ]),
 "n3":E("Hava yolu güvende","Fiberoptik entübasyon başarılı; 48 saat sonra ödem geriledi, ekstübe edildi. Kan kültüründe *H. influenzae* üredi.\n\n**Akılda kalsın**\n- Erişkin epiglotit: **orantısız odinofaji, salya, boğuk ses, tripod**, stridor; farenks normal görünebilir.\n- **Oturur pozisyon, ajite etme**, sırtüstü yatırma, dil basacağı ile zorlama yok.\n- Hava yolu ekibi + **cerrahi hava yolu hazır**; stabil hastada esnek endoskopiyle tanı.\n- Gerekirse ameliyathanede **uyanık fiberoptik** entübasyon.\n- IV seftriakson (± vankomisin).\n\n*Kaynak: Difficult Airway Society; Tintinalli Emergency Medicine (9. baskı).*","good"),
 "n9":E("Tam hava yolu tıkanıklığı","Hasta evde/serviste tam hava yolu tıkanıklığıyla arrest oldu.\n\nEpiglotit atlanırsa ölümcüldür.","bad"),
}))
Qs+=[Q("c29q1","Epiglotit şüphesinde hangisi yapılmamalıdır?",["Hastayı oturur pozisyonda tutmak","Dil basacağı ile zorlayarak boğaz muayenesi ve sırtüstü yatırmak","Zor hava yolu ekibini çağırmak","IV antibiyotik","O₂ vermek"],1,"Ajitasyon ve sırtüstü pozisyon tam tıkanmayı tetikleyebilir.","KBB / Hava yolu"),
 Q("c29q2","Epiglotitte lateral boyun grafisindeki klasik bulgu hangisidir?",["Çan kulesi","Başparmak bulgusu","Yelken işareti","Halo işareti","Kuş gagası"],1,"Ödemli epiglot başparmak bulgusu verir; çan kulesi krup bulgusudur.","KBB / Hava yolu"),
 Q("c29q3","Epiglotitli erişkinde entübasyon gerektiğinde tercih edilen yöntem hangisidir?",["Acilde paralitikle hızlı ardışık entübasyon","Ameliyathanede uyanık fiberoptik entübasyon, cerrahi hava yolu hazırken","Kör nazal entübasyon","Laringeal maske","Bekle-gör"],1,"Spontan solunumu koruyan uyanık teknik, cerrahi hava yolu yedeğiyle tercih edilir.","KBB / Hava yolu")]

# 30 AKUT ÜRİNER RETANSİYON
S.append(case("c30","İdrar yapamama — 72 yaşında erkek","Üroloji",
 "72 yaşında erkek, prostat büyümesi biliniyor. 2 gündür grip için “soğuk algınlığı ilacı” (antihistaminik + psödoefedrin) kullanıyor. 10 saattir idrar yapamıyor, alt karın ağrısı dayanılmaz.",
 {"n1":N("Muayene odası","Suprapubik bölgede ele gelen, hassas, dolgun mesane.","KB 162/90 · Nb 98 · Ateş 36,8",[
   T("Yatak başı mesane USG",2,5,"Mesane hacmi **≈1100 mL**.","Tanıyı doğrular."),
   T("Kreatinin, elektrolit",1,30,"Kreatinin 1,6 (bazal 1,0).","Obstrüktif akut böbrek hasarı."),
   A("Üretral kateter (gerekirse koude uçlu); mesaneyi tamamen boşalt (kademeli boşaltma/klemp gerekmez); idrar tetkiki",4,10,"n2","Doğru. Hızlı tam boşaltmanın hematüri/hipotansiyon riskini artırdığına dair güçlü kanıt yoktur."),
   A("Furosemid 40 mg IV ver",-5,10,"n9","Tıkanıklıkta diüretik mesane gerginliğini artırır."),
   A("Kateter takılamazsa zorla, defalarca dene",-2,20,"n2","Zorlama üretral travma ve yalancı yol oluşturur; 1–2 denemeden sonra üroloji (suprapubik kateter)."),
 ]),
 "n2":N("Kateter sonrası","Hasta rahatladı; 1150 mL idrar boşaldı. Sonraki 2 saatte saatte 300 mL idrar çıkıyor.","KB 138/80 · Nb 84",[
   A("Postobstrüktif diürez izlemi (saatlik idrar, elektrolit, gerekirse sıvı); antikolinerjik/sempatomimetik ilaçları kes; alfa bloker (tamsulosin 0,4 mg) başla; 2–3 gün sonra kateter çekme denemesi (TWOC); üroloji takibi",4,15,"n3","Doğru. Alfa bloker kateter çekme başarısını artırır."),
   A("Kateteri hemen çıkar ve taburcu et",-3,10,"n8","Tetikleyici ve prostat obstrüksiyonu sürerken retansiyon büyük olasılıkla tekrarlar."),
 ]),
 "n3":E("Başarılı kateter çekme","3. gün kateter çekildi; hasta tamsulosinle spontan işedi, kreatinin 1,1'e indi.\n\n**Akılda kalsın**\n- Erkekte en sık neden **BPH**; tetikleyiciler: **antikolinerjik**, sempatomimetik, opioid, alkol, kabızlık, enfeksiyon.\n- **Mesane USG** ile doğrula; kateterle **tamamen boşalt**.\n- **Postobstrüktif diürez** (>200 mL/saat) için izle.\n- **Alfa bloker** başla, 2–3 gün sonra kateter çekme denemesi.\n- Kadın veya genç erkekte retansiyon → nörolojik neden (kauda equina) ara.\n\n*Kaynak: EAU 2024 erkekte alt üriner sistem semptomları kılavuzu.*","good"),
 "n8":E("Tekrarlayan retansiyon","Hasta aynı gece yeniden retansiyonla geldi.\n\nTetikleyiciyi durdurmadan ve alfa bloker başlamadan kateter çekme başarısız olur.","mid"),
 "n9":E("Komplikasyon","Ağrı arttı, mesane aşırı gerildi; hasta vazovagal senkop geçirdi ve böbrek fonksiyonu kötüleşti.\n\nAkut retansiyonun tedavisi drenajdır.","bad"),
}))
Qs+=[Q("c30q1","Akut üriner retansiyonda kateter sonrası kateter çekme başarısını artıran ilaç hangisidir?",["Furosemid","Tamsulosin (alfa bloker)","Oksibutinin","Psödoefedrin","Finasterid tek başına"],1,"Alfa blokerler TWOC başarısını artırır.","Üroloji"),
 Q("c30q2","Hangi ilaç grubu akut üriner retansiyonu tetikleyebilir?",["Alfa blokerler","Antikolinerjikler (ör. birinci kuşak antihistaminikler)","PPİ","Statinler","ACE inhibitörleri"],1,"Antikolinerjikler detrüsör kasılmasını, sempatomimetikler mesane boynunu etkiler.","Üroloji"),
 Q("c30q3","Postobstrüktif diürez için hangi eşik önemlidir?",["İdrar çıkışı >50 mL/saat","İdrar çıkışı >200 mL/saat (2 saat süreyle) ya da >3 L/24 saat","Anüri","Hematüri","Ateş"],1,"Belirgin postobstrüktif diürezde sıvı-elektrolit izlemi gerekir.","Üroloji")]

P={"id":"ilk-nobet-3","title":"İlk Nöbet Vakaları — 3. Paket","desc":"Akut akciğer ödemi, testis torsiyonu, ektopik gebelik, çocukta yabancı cisim aspirasyonu, akut pankreatit, hiponatremi, SVT, nekrotizan fasiit, epiglotit, akut üriner retansiyon.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 3. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 3. Paket","topic":"Temel acil","order":3,"req":[1],"desc":"Hava yolu, ürolojik ve jinekolojik acillerden metabolik krizlere 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
