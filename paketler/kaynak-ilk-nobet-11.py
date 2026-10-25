import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Önce **ilk değerlendirme** (muayene, monitör, damar yolu, oksijen) — gereksiz girişim puan kaybettirir.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 101 ATRİYAL FİBRİLASYON — preeksitasyonlu (WPW)
S.append(case("c101","Düzensiz, geniş QRS'li çarpıntı — 26 yaşında erkek","Kardiyoloji",
 "26 yaşında erkek. 1 saattir başlayan çarpıntı ve hafif baş dönmesi. Daha önce de kısa süreli çarpıntıları olmuş, hiç tetkik yaptırmamış. İlaç kullanmıyor.",
 {"n1":N("Monitör","Uyanık, konuşabiliyor, hafif terli. Akciğerler temiz. Monitörde **düzensiz, çok hızlı, QRS genişliği atımdan atıma değişen** taşikardi.","KB 118/74 · Nb 220–260 (düzensiz) · SS 20 · SpO₂ %97",[
   T("12 derivasyonlu EKG",3,5,"**Düzensiz** taşikardi, hız yer yer 280/dk; QRS'ler **farklı genişlik ve morfolojide** (bazıları dar, çoğu geniş, delta dalgası benzeri yavaş başlangıç). Polimorfik VT ile uyumlu değil: eksen sabit, düzensizlik AF'ye benziyor.","Düzensiz + geniş + değişken QRS + çok hızlı (>250) → **preeksitasyonlu AF (WPW)**."),
   T("Elektrolitler, TSH",0,40,"Normal.","Tedavi kararını değiştirmez."),
   A("**Preeksitasyonlu AF**: AV düğüm blokerlerinden kaçın; sedasyon altında **senkronize kardiyoversiyon** (stabil olduğu için elektif; alternatif: prokainamid/ibutilid — varsa); kardiyoloji, sonra ablasyon",4,15,"n2","Doğru. Stabil hastada da kardiyoversiyon güvenli ve etkilidir; prokainamid/ibutilid alternatiftir."),
   A("Hız kontrolü: diltiazem 0,25 mg/kg IV",-5,5,"n9","AV düğüm blokajı uyarıları aksesuar yola yönlendirir → VF."),
   A("Adenozin 6 mg hızlı IV puşe",-4,3,"n9","Adenozin preeksitasyonlu AF'de VF'ye neden olabilir."),
   A("Amiodaron 300 mg IV",-2,20,"n3","Kılavuzlar preeksitasyonlu AF'de amiodaronu önermez (AV düğüm etkisi, VF bildirimleri)."),
 ]),
 "n3":N("Amiodaron sırasında","İnfüzyonun 10. dakikasında hız 300/dk'ya çıktı, hasta solgun ve baş dönmesi arttı.","KB 86/50 · Nb 300 · SpO₂ %95",[
   A("Hemen **senkronize kardiyoversiyon** (sedasyonla)",2,5,"n4","Instabilite gelişti: elektrik."),
   A("Amiodaron infüzyonunu bitir, bekle",-4,20,"n9","Hız artıyor; VF'ye dönüşebilir."),
 ]),
 "n2":E("Sinüs ritmi","Kardiyoversiyonla sinüs ritmine döndü; EKG'de **kısa PR ve delta dalgası**. Kardiyolojiye yatırıldı, ertesi gün aksesuar yol ablasyonu yapıldı.\n\n**Akılda kalsın**\n- **Düzensiz + geniş/değişken QRS + çok hızlı** taşikardi = preeksitasyonlu AF'yi düşün.\n- **Adenozin, beta bloker, diltiazem/verapamil, digoksin ve amiodaron verme** (ABCD kuralı) — VF riski.\n- İnstabilse **senkronize kardiyoversiyon**; stabilse de kardiyoversiyon ya da **prokainamid/ibutilid**.\n- Kalıcı tedavi: **kateter ablasyonu**.\n\n*Kaynak: ESC 2019 SVT kılavuzu; ESC 2024 AF kılavuzu.*","good"),
 "n4":E("Geç ama düzeldi","Kardiyoversiyonla sinüs ritmi sağlandı; hasta ablasyona yönlendirildi. Amiodaron gereksiz risk ve gecikme yarattı.","mid"),
 "n9":E("Ventrikül fibrilasyonu","Hasta VF'ye girdi; defibrilasyonla döndürüldü.","bad"),
}))
Qs+=[Q("c101q1","Preeksitasyonlu AF'de hangi ilaçtan kaçınılmalıdır?",["Prokainamid","İbutilid","Diltiazem","Senkronize kardiyoversiyon için sedatif","Hiçbiri"],2,"AV düğüm blokerleri iletimi aksesuar yola kaydırır.","Kardiyoloji"),
 Q("c101q2","Hangi EKG özelliği preeksitasyonlu AF'yi düşündürür?",["Düzenli dar QRS 150/dk","Düzensiz, çok hızlı, genişliği değişen QRS","Testere dişi flutter dalgaları","Sinüs bradikardisi","Uzun QT"],1,"Hız sıklıkla >250/dk.","Kardiyoloji"),
 Q("c101q3","WPW'de kalıcı tedavi hangisidir?",["Ömür boyu digoksin","Kateter ablasyonu","Aspirin","Kalsiyum kanal blokeri","Pacemaker"],1,"Aksesuar yol ablasyonu küratiftir.","Kardiyoloji")]

# 102 LİTYUM ZEHİRLENMESİ (kronik)
S.append(case("c102","Titreme ve konfüzyon — 64 yaşında kadın","Toksikoloji",
 "64 yaşında kadın, bipolar bozukluk nedeniyle yıllardır lityum kullanıyor. 2 hafta önce hipertansiyon için ramipril + hidroklorotiyazid başlanmış. 4 gündür ishal, son 2 günde ellerde kaba titreme, dengesizlik ve konuşmada bozulma. Fazla ilaç almamış.",
 {"n1":N("Muayene","Konfüze, dizartrik. **Kaba tremor**, myoklonik sıçramalar, **hiperrefleksi**, ataksi. Mukozalar kuru.","KB 104/62 · Nb 96 · SS 18 · SpO₂ %97 · Ateş 37,2",[
   T("Serum lityum düzeyi",3,60,"**2,9 mmol/L** (tedavi aralığı 0,6–1,0).","Kronik zehirlenmede düzey, klinikten daha düşük görünebilir — tedavi kliniğe göre."),
   T("Kreatinin, elektrolit",2,40,"Kreatinin **2,1 mg/dL** (bazal 0,9), Na 146.","Akut böbrek hasarı lityum atılımını azaltır."),
   T("EKG",1,5,"Sinüs; QTc 470 ms, yaygın T düzleşmesi.","Kardiyotoksisite hafif."),
   A("Lityumu, ACE inhibitörünü, tiyazidi kes; **izotonik SF** ile volüm replasmanı; nefroloji — **hemodiyaliz** (bozulmuş böbrek fonksiyonu + nörolojik bulgular); aktif kömür verme",4,30,"n2","Doğru. EXTRIP: böbrek fonksiyonu bozukken düzey >4,0, bilinç bozukluğu, nöbet veya aritmide **önerilir**; konfüzyon, düzey >5,0 ya da uzun eliminasyon beklentisinde **önerilebilir**."),
   A("Aktif kömür 1 g/kg ve gözlem",-3,20,"n3","Aktif kömür lityumu bağlamaz."),
   A("Sıvıyla izle, diyaliz gereksiz — düzey 4'ün altında",-1,30,"n3","Kronik zehirlenmede nörolojik bulgu ve böbrek hasarı düzeyden daha önemlidir."),
 ]),
 "n3":N("6 saat sonra","Bilinç kötüleşti (GKS 11), bir kez jeneralize nöbet geçirdi. Tekrar lityum 2,7.","KB 100/60 · Nb 104 · SpO₂ %96",[
   A("Acil **hemodiyaliz** (nöbet ve bilinç bozukluğu)",2,60,"n4","Artık kesin endikasyon."),
   A("Yalnız antiepileptik ve sıvı",-4,30,"n9","Kalıcı nörotoksisite (SILENT) riski."),
 ]),
 "n2":E("Düzelme","İki seans hemodiyaliz sonrası lityum 0,8'e indi, rebound izlendi; bilinç 48 saatte düzeldi. Psikiyatri ile ilaç planı yeniden yapıldı.\n\n**Akılda kalsın**\n- Kronik lityum zehirlenmesi: **dehidratasyon, ACEi/ARB, tiyazid, NSAİİ** ile tetiklenir.\n- Bulgular: kaba tremor, ataksi, konfüzyon, hiperrefleksi, myoklonus, nöbet.\n- **Aktif kömür bağlamaz**; akut yavaş salınımlı alımda **tüm barsak irrigasyonu** düşünülür.\n- Tedavi: kes, **izotonik sıvı**, nefrotoksikleri durdur; **hemodiyaliz** (EXTRIP ölçütleri), rebound için düzey tekrarı.\n\n*Kaynak: EXTRIP 2015 lityum önerileri.*","good"),
 "n4":E("Geç düzelme","Diyaliz sonrası düzeldi; ancak taburculukta hafif ataksi sürüyordu.","mid"),
 "n9":E("Kalıcı nörolojik hasar","Hasta uzun süre yoğun bakımda kaldı; serebellar bulgular kalıcı oldu.","bad"),
}))
Qs+=[Q("c102q1","Lityum zehirlenmesinde hangisi etkisizdir?",["İzotonik sıvı","Hemodiyaliz","Aktif kömür","Nefrotoksik ilaçları kesmek","Tüm barsak irrigasyonu (akut SR alım)"],2,"Lityum aktif kömüre bağlanmaz.","Toksikoloji"),
 Q("c102q2","Hangi ilaç lityum düzeyini yükseltir?",["Hidroklorotiyazid","Parasetamol","Amoksisilin","Omeprazol","Levotiroksin"],0,"Tiyazid, ACEi/ARB, NSAİİ renal atılımı azaltır.","Toksikoloji"),
 Q("c102q3","Kronik lityum zehirlenmesinde tedavi kararını en çok ne belirler?",["Yalnız serum düzeyi","Nörolojik bulgular ve böbrek fonksiyonu","Kalp hızı","Ateş","Lökosit"],1,"Kronikte düzey klinikle orantısız düşük olabilir.","Toksikoloji")]

# 103 KLAVİKULA FRAKTÜRÜ
S.append(case("c103","Bisikletten düşme, omuz ağrısı — 19 yaşında erkek","Ortopedi",
 "19 yaşında erkek. Bisikletten omzunun üzerine düştü. Sağ köprücük kemiği üzerinde ağrı ve şişlik; kolunu kaldıramıyor. Başka yakınması yok.",
 {"n1":N("Muayene","Sağ klavikula orta 1/3'te deformite; **fragman ucu deriyi geriyor, deri soluk-beyaz (gerilmiş)**, açık yara yok. Distal nabızlar ve duyu normal. Solunum sesleri eşit.","KB 128/76 · Nb 92 · SS 16 · SpO₂ %98",[
   T("Klavikula grafisi (AP + 30° sefalik eğimli)",2,15,"Orta 1/3'te **tam deplase, 2 cm kısalmış** kırık; bir fragman yukarı-öne açılanmış.","Orta 1/3 kırıkları en sık tiptir."),
   T("Akciğer grafisi",1,15,"Pnömotoraks yok.","Yüksek enerjili travmada pnömotoraks ve nörovasküler yaralanma dışlanır."),
   A("Analjezi; kol askısı; deri gerilmesi (**tehdit altındaki deri**) olduğu için **acil ortopedi konsültasyonu** — açık kırığa dönmeden cerrahi değerlendirme",4,20,"n2","Doğru. Deride gerilme/beyazlaşma, açık kırık, nörovasküler hasar ve yüzen omuz acil ortopedi endikasyonudur."),
   A("Sekiz bandajı, analjezik, 2 hafta sonra poliklinik",-3,15,"n9","Sekiz bandajı askıya üstün değildir; asıl hata gerilmiş derinin kaçırılmasıdır."),
   A("Acilde kapalı redüksiyon dene",-2,20,"n9","Klavikula kapalı redüksiyonla tutmaz; deri hasarını artırabilir."),
 ]),
 "n2":E("Uygun tedavi","Ortopedi aynı gün plak-vida ile tespit yaptı; deri bütünlüğü korundu.\n\n**Akılda kalsın**\n- Klavikula kırıklarının çoğu **orta 1/3**; çoğu **kol askısı** ve analjeziyle iyileşir (sekiz bandajı üstün değil).\n- **Acil ortopedi**: açık kırık, **deride gerilme/beyazlaşma**, nörovasküler hasar, yüzen omuz, belirgin deplasman/kısalma (cerrahi değerlendirme).\n- Pnömotoraks ve subklavyen damar yaralanmasını unutma.\n\n*Kaynak: AAOS klavikula kırığı önerileri; Cochrane 2019 (askı vs sekiz bandajı).*","good"),
 "n9":E("Açık kırık","İki gün sonra fragman deriyi deldi; açık kırık ve enfeksiyon riskiyle acil ameliyat gerekti.","bad"),
}))
Qs+=[Q("c103q1","Klavikula kırığında acil ortopedi gerektiren bulgu hangisidir?",["Orta 1/3 non-deplase kırık","Deride gerilme ve beyazlaşma","Ağrı","Ekimoz","Hafif şişlik"],1,"Tehdit altındaki deri açık kırığa dönebilir.","Ortopedi"),
 Q("c103q2","Non-deplase orta 1/3 klavikula kırığında standart tedavi hangisidir?",["Acil plak","Kol askısı ve analjezi","Alçı","Traksiyon","Kapalı redüksiyon"],1,"Askı sekiz bandajı kadar etkili ve daha konforludur.","Ortopedi"),
 Q("c103q3","Klavikula kırığıyla birlikte hangisi aranmalıdır?",["Pnömotoraks ve nörovasküler yaralanma","Apandisit","Menisküs yırtığı","Böbrek taşı","Hepatit"],0,"Subklavyen damarlar ve brakiyal pleksus yakındır.","Ortopedi")]

# 104 AKREP SOKMASI (çocuk, sistemik)
S.append(case("c104","Akrep sokması — 7 yaşında erkek","Toksikoloji / Çocuk",
 "7 yaşında erkek, Şanlıurfa'dan. 1 saat önce bahçede sağ ayağından sarı renkli bir akrep sokmuş. Önce şiddetli yanma, ardından kusma, terleme ve huzursuzluk başlamış. Yaklaşık 22 kg.",
 {"n1":N("Muayene","Ajite, **aşırı terleme ve salya**, kusma. Sokma yerinde ağrı, belirgin şişlik yok. Bilateral bazal **raller**, ekstremiteler soğuk.","KB 148/98 · Nb 158 · SS 40 · SpO₂ %91 · Ateş 37,3",[
   T("Akciğer grafisi",2,15,"Bilateral perihiler **pulmoner ödem**.","Adrenerjik fırtına ve miyokardit → pulmoner ödem."),
   T("EKG + troponin",2,30,"Sinüs taşikardisi, yaygın ST-T değişiklikleri; troponin yüksek.","Toksik miyokardit."),
   T("Glukoz",1,5,"238 mg/dL.","Katekolamin deşarjı hiperglisemiye yol açar."),
   A("**Derece III sistemik zehirlenme**: O₂, monitör, yoğun bakım; **akrep antivenomu** (ürün ve UZEM 114 önerisine göre, IV); hipertansiyon/adrenerjik krizde **prazosin**; ağrı kontrolü; pulmoner ödemde destek (NIV)",4,20,"n2","Doğru. Sistemik bulgulu çocukta antivenom ve yoğun bakım; prazosin adrenerjik etkileri azaltır."),
   A("Sokma yerine buz, antihistaminik ve gözlem",-4,30,"n9","Sistemik ve kardiyopulmoner tutulum var; gecikme ölümcül olabilir."),
   A("Kalsiyum glukonat ve steroid",-2,20,"n9","Akrep zehirlenmesinde etkinliği gösterilmemiştir."),
 ]),
 "n2":E("Düzelme","Antivenom ve yoğun bakım desteğiyle 24 saatte pulmoner ödem geriledi; 3 gün sonra taburcu edildi.\n\n**Akılda kalsın**\n- Türkiye'de tehlikeli türler (ör. *Androctonus*, *Leiurus*) özellikle **Güneydoğu Anadolu**'da; ağır tablo **çocuklarda**.\n- **Derece I** yerel ağrı (analjezi, lokal anestezik), **II** sistemik bulgular (terleme, kusma, salya, ajitasyon), **III** kardiyovasküler/solunum/nörolojik (pulmoner ödem, şok, miyokardit).\n- Sistemik tabloda **antivenom** (UZEM 114 ile), yoğun bakım; adrenerjik krizde **prazosin**.\n- Ulusal Zehir Danışma Merkezi: **114**.\n\n*Kaynak: T.C. Sağlık Bakanlığı UZEM akrep sokması rehberi; Isbister & Bawaskar, NEJM 2014.*","good"),
 "n9":E("Kardiyojenik şok","Çocuk pulmoner ödem ve kardiyojenik şokla yoğun bakıma alındı; entübasyon gerekti.","bad"),
}))
Qs+=[Q("c104q1","Akrep sokmasında sistemik zehirlenme bulgusu hangisidir?",["Yalnız sokma yerinde ağrı","Terleme, salya, kusma, ajitasyon","Kaşıntı","Eritem","Lokal uyuşma"],1,"Otonom fırtına sistemik tutulumu gösterir.","Toksikoloji / Çocuk"),
 Q("c104q2","Akrep zehirlenmesinde ağır tablo en sık hangi grupta görülür?",["Gençler","Çocuklar","Kadınlar","Sporcular","Hepsinde eşit"],1,"Vücut ağırlığına göre zehir dozu yüksektir.","Toksikoloji / Çocuk"),
 Q("c104q3","Türkiye'de zehirlenmelerde danışılacak ulusal hat hangisidir?",["112","114","155","184","177"],1,"Ulusal Zehir Danışma Merkezi (UZEM) 114.","Toksikoloji / Çocuk")]

# 105 YABANCI CİSİM YUTMA — düğme pil
S.append(case("c105","Pil yuttu — 3 yaşında kız","Çocuk / Gastroenteroloji",
 "3 yaşında kız. Annesi 1 saat önce kumandanın düğme pilini ağzına aldığını, sonra pilin kaybolduğunu söylüyor. Çocuk bir kez öksürmüş, şimdi salya artışı ve yutkunurken huzursuzluk var. Yaklaşık 14 kg.",
 {"n1":N("Muayene","Uyanık, ağlıyor; hafif salya artışı. Solunum sıkıntısı yok, akciğerler temiz. Karın rahat.","Nb 128 · SS 26 · SpO₂ %98 · Ateş 36,8",[
   T("Boyun-göğüs-karın grafisi (AP + lateral)",3,15,"Üst özofagusta 20 mm yuvarlak yabancı cisim; AP'de **çift halka (halo) görünümü**, lateralde basamak — **düğme pil**.","Halo işareti pili bozuk paradan ayırır."),
   T("Hemogram",0,30,"Normal.","Kararı değiştirmez."),
   A("**Özofagusta düğme pil = acil**: oral alımı kes (yalnız bal/sükralfat), **acil endoskopi (ideal ≤2 saat)** için çocuk gastroenteroloji/cerrahi; 12 saatten kısa sürede ve ≥1 yaşta: endoskopiye kadar **bal 10 mL, 10 dakikada bir (en çok 6 doz)**",4,10,"n2","Doğru. Pil 2 saat içinde ciddi yanık yapabilir; bal, alkali hasarı azaltır."),
   A("Kusturma",-3,5,"n9","Aspirasyon ve ek özofagus hasarı riski."),
   A("Midede olabilir — 24 saat sonra kontrol grafisi",-5,10,"n9","Pil özofagusta; saatler içinde nekroz, perforasyon, aortoözofageal fistül."),
 ]),
 "n2":E("Zamanında çıkarıldı","Endoskopide pil başvurudan 90 dakika sonra çıkarıldı; mukozada yüzeyel yanık vardı, kontrolde darlık gelişmedi.\n\n**Akılda kalsın**\n- **Düğme pil özofagusta** = gerçek acil: **≤2 saatte endoskopi**.\n- Grafide **halo (çift halka)** ve lateralde basamak.\n- **≥1 yaş, <12 saat**: bal 10 mL her 10 dk (en çok 6 doz); hastanede sükralfat.\n- Kusturma yok; midedeki pil asemptomatikse çoğu kez izlenir (yaş ve pil boyutuna göre).\n- **Mıknatıs (birden fazla)** ve keskin cisimler de acil değerlendirme gerektirir.\n\n*Kaynak: NASPGHAN 2021; National Capital Poison Center düğme pil kılavuzu.*","good"),
 "n9":E("Özofagus yanığı","Pil 20 saat sonra çıkarıldı; derin nekroz, ardından özofagus darlığı gelişti.","bad"),
}))
Qs+=[Q("c105q1","Özofagusta düğme pil saptanan çocukta yaklaşım hangisidir?",["24 saat izlem","Acil endoskopik çıkarma (ideal ≤2 saat)","Kusturma","Laksatif","Ayaktan takip"],1,"Elektrik akımı hızla doku nekrozu yapar.","Çocuk / Gastroenteroloji"),
 Q("c105q2","Grafide düğme pili bozuk paradan ayıran bulgu hangisidir?",["Düz kenar","Çift halka (halo) görünümü","Daha küçük boyut","Radyolüsen olması","Yuvarlak olması"],1,"Lateralde basamak da görülür.","Çocuk / Gastroenteroloji"),
 Q("c105q3","Düğme pil yutan ≥1 yaş çocukta endoskopiye kadar önerilen hangisidir?",["Süt","Bal 10 mL her 10 dakikada (en çok 6 doz)","Sirke","Kusturucu","Su ile yıkama"],1,"İlk 12 saat içinde ve şüpheli perforasyon yoksa.","Çocuk / Gastroenteroloji")]

# 106 LOMBER BÖLGE TRAVMASI
S.append(case("c106","Merdivenden düşme, bel ve topuk ağrısı — 41 yaşında erkek","Travma / Omurga",
 "41 yaşında inşaat işçisi. Yaklaşık 4 metreden ayakları üzerine düştü. Bel ve her iki topukta ağrı. Ambulansta sırt tahtası ve boyunlukla getirildi.",
 {"n1":N("Birincil bakı","Hava yolu açık, solunum normal. L1 hizasında hassasiyet ve basamak hissi yok. Bilateral topuklarda şişlik, ekimoz. Alt ekstremite kuvvet 5/5, duyu normal, perianal duyu korunmuş.","KB 138/84 · Nb 96 · SS 18 · SpO₂ %98",[
   T("Tüm omurga BT",3,30,"**L1 patlama kırığı**, kanala %30 retropulsiyon; posterior ligaman kompleksi şüpheli. Başka seviyede kırık yok.","Ayakları üstüne düşmede omurga + kalkaneus birlikteliği; kırıkların ~%10'u ardışık olmayan seviyede."),
   T("Ayak bileği ve kalkaneus grafisi",2,15,"**Bilateral kalkaneus kırığı**.","Yüksekten düşmede birlikte aranır."),
   T("Yalnız lomber grafi",0,15,"L1'de yükseklik kaybı.","BT gerekli; grafide patlama kırığının ciddiyeti anlaşılmaz."),
   A("Omurga önlemleri (düz yatış, log-roll), analjezi; **omurga cerrahisi** (TLICS) ve ortopedi konsültasyonu; seri nörolojik muayene; tromboprofilaksi planı",4,20,"n2","Doğru. Patlama kırığında stabilite ve cerrahi kararı omurga ekibiyle."),
   A("Nörolojisi normal — korse ile ayakta mobilize et, taburcu",-5,10,"n9","Retropulsiyon ve olası ligaman hasarı varken mobilizasyon nörolojik hasar yapabilir."),
 ]),
 "n2":E("Uygun tedavi","Omurga cerrahisi posterior enstrümantasyon yaptı; kalkaneus kırıkları ortopediyle izlendi. Nörolojik defisit gelişmedi.\n\n**Akılda kalsın**\n- Yüksekten ayak üstü düşme: **kalkaneus + torakolomber kırık** birlikteliği.\n- Bir omurga kırığı varsa **tüm omurga görüntülenmeli** (ardışık olmayan kırıklar).\n- Patlama kırığı: **BT**, retropulsiyon ve posterior ligaman kompleksi (MR) değerlendirilir; **TLICS/AOSpine** ile karar.\n- Seri nörolojik ve perianal duyu/anal tonus muayenesi.\n\n*Kaynak: ATLS 10. baskı; AOSpine torakolomber sınıflaması.*","good"),
 "n9":E("Nörolojik kötüleşme","Mobilizasyon sırasında bacaklarda güçsüzlük gelişti; acil dekompresyon gerekti.","bad"),
}))
Qs+=[Q("c106q1","Yüksekten ayak üstü düşen hastada kalkaneus kırığına sık eşlik eden yaralanma hangisidir?",["Klavikula kırığı","Torakolomber omurga kırığı","Kafatası kırığı","Kosta kırığı","Radius kırığı"],1,"Aksiyel yük omurgaya iletilir.","Travma / Omurga"),
 Q("c106q2","Bir seviyede omurga kırığı saptandığında ne yapılmalıdır?",["Yalnız o bölge izlenir","Tüm omurga görüntülenir","MR gereksizdir","Hemen mobilize edilir","Taburcu edilir"],1,"Ardışık olmayan kırık oranı yüksektir.","Travma / Omurga"),
 Q("c106q3","Torakolomber patlama kırığının ciddiyetini değerlendirmek için en uygun ilk tetkik hangisidir?",["Direkt grafi","BT","USG","Sintigrafi","EMG"],1,"Retropulsiyon ve kanal daralması BT ile değerlendirilir.","Travma / Omurga")]

# 107 İNTRAPARANKİMAL KANAMA (antikoagülan)
S.append(case("c107","Ani sol güçsüzlük ve kusma — 76 yaşında erkek","Nöroloji",
 "76 yaşında erkek. AF nedeniyle apiksaban 5 mg günde iki kez kullanıyor; son dozu 3 saat önce. 1 saat önce ani sol kol-bacak güçsüzlüğü, baş ağrısı ve kusma başladı.",
 {"n1":N("Muayene","Uykuya meyilli (GKS 13), sol hemiparezi, sağa bakış tercihi.","KB 204/112 · Nb 92 (düzensiz) · SS 18 · SpO₂ %96 · Kapiller glukoz 132",[
   T("Kontrastsız beyin BT",3,15,"Sağ putaminal **intraparankimal hematom ≈25 mL**, ventriküle açılım yok, hafif kitle etkisi.","Tanı ve hacim (ABC/2)."),
   T("Kanama paneli, hemogram, kreatinin",1,40,"Trombosit 210.000; kreatinin 1,1; INR 1,2 (apiksaban INR'yi güvenilir göstermez).","Anti-Xa düzeyi varsa yararlı."),
   A("**Apiksaban geri çevirme**: andeksanet alfa ya da (yoksa) **4 faktörlü PCC 50 IU/kg**; **KB düşürme** — hedef sistolik ≈140 mmHg (130–150; 1 saat içinde, ani düşüşten kaçın) titre edilebilir IV ajanla; nöroşirürji; yatak başı 30°; nöbet/glukoz/ateş kontrolü; inme ünitesi/yoğun bakım",4,20,"n2","Doğru. Antikoagülasyonun hızla geri çevrilmesi ve erken KB kontrolü hematom büyümesini azaltır."),
   A("Hedef sistolik <110 mmHg — agresif düşür",-3,20,"n3","Çok agresif düşüş (sistolik <130) yarar sağlamaz, böbrek ve nörolojik zarar artabilir."),
   A("TDP 4 ünite ve K vitamini",-3,40,"n3","TDP ve K vitamini faktör Xa inhibitörünü geri çevirmez."),
   A("Trombolitik — iskemik inme olabilir",-5,10,"n9","BT'de kanama var; tromboliz kontrendike."),
 ]),
 "n3":N("Kontrol","Bir saat sonra GKS 11; kontrol BT'de hematom 34 mL.","KB 168/96 · Nb 96",[
   A("Andeksanet/4F-PCC ver, hedef sistolik ≈140; nöroşirürji",2,20,"n4","Geç ama doğru yöne dönüş."),
   A("İzle",-3,30,"n9","Hematom büyümesi sürüyor."),
 ]),
 "n2":E("Stabil","Hematom 6 saatlik kontrolde büyümedi; hasta inme ünitesinde izlendi, rehabilitasyona yönlendirildi.\n\n**Akılda kalsın**\n- Antikoagülan ilişkili İPK'da **hızlı geri çevirme**: faktör Xa inhibitörü → **andeksanet** ya da **4F-PCC (≈50 IU/kg)**; dabigatran → **idarusizumab**; varfarin → **4F-PCC + IV K vitamini**.\n- KB: sistolik ≈**140** hedefi (130–150), ani ve aşırı düşüşten kaçın.\n- Hematom hacmi (ABC/2), ventrikül açılımı, GKS, yaş → prognoz (ICH skoru).\n\n*Kaynak: AHA/ASA 2022 spontan İPK kılavuzu; ESO 2025.*","good"),
 "n4":E("Geç kontrol","Hematom büyüdü ama ilerlemedi; hasta orta derecede defisitle rehabilitasyona gitti.","mid"),
 "n9":E("Hematom büyümesi","Hematom 60 mL'ye ulaştı, herniasyon gelişti.","bad"),
}))
Qs+=[Q("c107q1","Apiksaban kullanan hastada intraserebral kanamada geri çevirme seçeneği hangisidir?",["Vitamin K","Protamin","Andeksanet alfa veya 4F-PCC","İdarusizumab","TDP tek başına"],2,"İdarusizumab dabigatran içindir.","Nöroloji"),
 Q("c107q2","Akut spontan İPK'da önerilen sistolik KB hedefi yaklaşık nedir?",["<110","≈140 (130–150)","<180","<200","Düşürülmez"],1,"Sistolik <130'a düşürmekten kaçınılır.","Nöroloji"),
 Q("c107q3","Varfarin ilişkili İPK'da tedavi hangisidir?",["4F-PCC + IV K vitamini","Yalnız TDP","Andeksanet","İdarusizumab","Traneksamik asit tek başına"],0,"PCC TDP'den hızlı ve hacim yükü azdır.","Nöroloji")]

# 108 PARMAK TRAVMASI — mallet parmak
S.append(case("c108","Topa çarpan parmak — 32 yaşında kadın","Ortopedi / El",
 "32 yaşında kadın. Voleybol oynarken top sağ orta parmağının ucuna çarptı. Parmak ucu “düşük” duruyor, düzeltemiyor.",
 {"n1":N("Muayene","Sağ 3. parmak DİF eklemi ≈30° fleksiyonda; **aktif ekstansiyon yok**, pasif tam düzeliyor. Tırnak ve deri sağlam. Nörovasküler muayene normal.","KB 118/72 · Nb 76 · SpO₂ %99",[
   T("Parmak grafisi (AP + lateral)",2,15,"Distal falanks dorsal tabanında **küçük avulsiyon parçası** (eklem yüzeyinin <1/3'ü); volar subluksasyon yok.","Büyük parça (>1/3) ya da subluksasyonda el cerrahisi."),
   A("**DİF ekleminde ekstansiyonda atel** (stack/dorsal atel), **6–8 hafta kesintisiz**; atel çıkarılırken bile parmak ucu düşürülmemeli; el cerrahisi polikliniği",4,10,"n2","Doğru. Kemik parçası küçük ve eklem uyumlu: konservatif."),
   A("Bilek-el ateli, PİF ve DİF fleksiyonda 3 hafta",-3,10,"n9","Fleksiyonda tespit tendonun kaynamasını engeller; kalıcı düşük parmak."),
   A("Sargı ve buz, gerekirse kontrol",-3,5,"n9","Tedavisiz kalırsa kalıcı deformite (kuğu boynu)."),
 ]),
 "n2":E("İyileşme","8 hafta kesintisiz atel sonrası aktif ekstansiyon geri geldi; hafif 5° ekstansiyon kaybı kaldı.\n\n**Akılda kalsın**\n- Mallet parmak: **terminal ekstansör tendon** kopması/avulsiyonu; DİF'te aktif ekstansiyon kaybı.\n- **Grafi** çek: kemik parçası >1/3 eklem yüzeyi veya **volar subluksasyon** → el cerrahisi.\n- Tedavi: yalnız DİF'i **ekstansiyonda** tutan atel, **6–8 hafta kesintisiz** (+2–4 hafta gece).\n- Tedavi edilmezse **kuğu boynu deformitesi**.\n\n*Kaynak: Cochrane 2004/2021 mallet parmak derlemesi; BSSH önerileri.*","good"),
 "n9":E("Kalıcı deformite","Parmak ucu düşük kaldı; aylar sonra kuğu boynu deformitesi gelişti.","bad"),
}))
Qs+=[Q("c108q1","Mallet parmakta atel nasıl uygulanır?",["DİF fleksiyonda","DİF ekstansiyonda, 6–8 hafta kesintisiz","Tüm el fleksiyonda","Yalnız gece","Atel gerekmez"],1,"Kesintiye uğrarsa süre baştan başlar.","Ortopedi / El"),
 Q("c108q2","Mallet parmakta el cerrahisine yönlendirme gerektiren bulgu hangisidir?",["Küçük avulsiyon parçası","Eklem yüzeyinin >1/3'ü ve volar subluksasyon","Ağrı","Şişlik","Ekimoz"],1,"Eklem uyumsuzluğu cerrahi gerektirir.","Ortopedi / El"),
 Q("c108q3","Tedavi edilmeyen mallet parmakta gelişebilecek deformite hangisidir?",["Boutonnière","Kuğu boynu","Dupuytren","Tetik parmak","Ulnar deviasyon"],1,"PİF hiperekstansiyonu + DİF fleksiyonu.","Ortopedi / El")]

# 109 NON-STEMI — çok yüksek risk
S.append(case("c109","Geçmeyen göğüs ağrısı — 67 yaşında kadın","Kardiyoloji",
 "67 yaşında kadın, diyabet ve hipertansiyon. 3 saattir göğüste sıkışma; ambulansta 300 mg aspirin ve dil altı nitrat almış, ağrı geçmemiş.",
 {"n1":N("Muayene","Terli, ağrılı (7/10). Akciğerler temiz, üfürüm yok.","KB 142/84 · Nb 98 · SS 20 · SpO₂ %96",[
   T("12 derivasyonlu EKG",3,5,"**V3–V6, I, aVL'de 2 mm yatay ST çökmesi**; ST elevasyonu yok (aVR'de 1 mm elevasyon).","Yaygın ST çökmesi + aVR elevasyonu: yaygın subendokardiyal iskemi."),
   T("Yüksek duyarlıklı troponin (0. saat)",2,60,"Belirgin yüksek (>5× üst sınır).","ESC 0/1 saat algoritması: yüksek ilk değer NSTEMI'yi destekler."),
   T("Yatak başı eko",1,10,"Anterolateral hipokinezi; EF ≈%45; perikardiyal sıvı yok.","Mekanik komplikasyon yok."),
   A("NSTE-AKS **çok yüksek risk** (tedaviye dirençli süren ağrı + dinamik ST değişiklikleri): **acil invaziv strateji (<2 saat)** — kardiyoloji/kateter laboratuvarı; heparin (ör. anfraksiyone heparin 70–100 Ü/kg IV); analjezi, nitrat infüzyonu; monitör",4,15,"n2","Doğru. ESC 2023: hemodinamik instabilite, dirençli ağrı, ciddi aritmi, mekanik komplikasyon, akut KY, tekrarlayan dinamik ST değişikliği → <2 saatte anjiyografi."),
   A("Fibrinolitik (tenekteplaz)",-5,10,"n9","NSTE-AKS'de fibrinoliz endike değildir ve zararlıdır."),
   A("Troponin yükselmiş — koroner yoğun bakımda izle, 72 saat içinde anjiyo",-2,30,"n3","Süren ağrı ve dinamik değişiklik varken anjiyografiyi geciktirmek uygun değil."),
 ]),
 "n3":N("Gözlemde","Bir saat sonra ağrı arttı, monitörde kısa VT salvoları.","KB 108/66 · Nb 112",[
   A("Acil anjiyografi",2,15,"n4","Artık gecikmeden."),
   A("Amiodaron ve izlem",-3,20,"n9","Aritmi iskeminin sonucu; reperfüzyon gerekli."),
 ]),
 "n2":E("Revaskülarizasyon","Anjiyografide sol ana koroner + proksimal LAD kritik darlık; aynı seansta PKG yapıldı, ağrı geçti.\n\n**Akılda kalsın**\n- NSTE-AKS'de risk: **çok yüksek** (<2 saat), **yüksek** (<24 saat), değilse yatışta seçici invaziv.\n- Yaygın ST çökmesi + **aVR elevasyonu**: sol ana/çok damar iskemisi düşündürür.\n- **Fibrinoliz NSTE-AKS'de yok.**\n- Erken invaziv planlanıyorsa P2Y12 ön yüklemesi rutin önerilmez (ESC 2023).\n\n*Kaynak: ESC 2023 Akut Koroner Sendromlar Kılavuzu.*","good"),
 "n4":E("Geç revaskülarizasyon","PKG yapıldı ama hasta VT ve kalp yetmezliği nedeniyle yoğun bakımda uzun kaldı.","mid"),
 "n9":E("Komplikasyon","Hasta kardiyak arrest geçirdi; geri döndürüldü ancak ağır sol ventrikül disfonksiyonu kaldı.","bad"),
}))
Qs+=[Q("c109q1","NSTE-AKS'de <2 saatte invaziv strateji gerektiren durum hangisidir?",["Ağrısı geçmiş, troponin normal","Tedaviye dirençli süren göğüs ağrısı","Yalnız diyabet","Yaş >65","Hiperlipidemi"],1,"Çok yüksek risk ölçütüdür.","Kardiyoloji"),
 Q("c109q2","NSTEMI'de hangisi uygun değildir?",["Aspirin","Antikoagülan","Fibrinolitik tedavi","Koroner anjiyografi","Analjezi"],2,"Fibrinoliz yalnız STEMI'de.","Kardiyoloji"),
 Q("c109q3","Yaygın ST çökmesi ile birlikte aVR'de ST elevasyonu neyi düşündürür?",["Perikardit","Sol ana koroner/çok damar iskemisi","Erken repolarizasyon","Hipokalemi","Pulmoner emboli"],1,"Yaygın subendokardiyal iskemi paterni.","Kardiyoloji")]

# 110 SOL DAL BLOĞU + göğüs ağrısı (Sgarbossa)
S.append(case("c110","Göğüs ağrısı ve dal bloğu — 71 yaşında erkek","Kardiyoloji",
 "71 yaşında erkek. 1 saattir başlayan, sol kola yayılan baskı tarzı göğüs ağrısı, terleme. Bilinen kalp yetmezliği ve sol dal bloğu var (eski EKG'si yanında).",
 {"n1":N("Muayene","Terli, ağrılı. Bazallerde hafif raller.","KB 108/64 · Nb 102 · SS 22 · SpO₂ %94",[
   T("12 derivasyonlu EKG",3,5,"Sol dal bloğu; **V5–V6'da QRS ile aynı yönde (konkordan) 2 mm ST elevasyonu**; V2'de QRS'e zıt yönde 7 mm ST elevasyonu (S dalgası 25 mm; oran 0,28).","**Sgarbossa**: konkordan ST elevasyonu ≥1 mm → akut oklüzyon. Modifiye Smith: diskordan STE/S ≥0,25."),
   T("Eski EKG ile karşılaştır",1,2,"Eskisinde V5–V6'da konkordan elevasyon yok.","Yeni değişiklik."),
   T("Troponin",0,60,"Sonuç 1 saatte.","Reperfüzyon kararı için beklenmez."),
   A("**STEMI eşdeğeri** (LBBB + iskemik semptom + Sgarbossa pozitif): primer PKG için kateter laboratuvarını aktive et; aspirin, heparin; P2Y12 kardiyolojiyle",4,10,"n2","Doğru. ESC 2023: LBBB ve süren iskemik semptomu olan hasta STEMI gibi yönetilir."),
   A("Dal bloğu eski, EKG değerlendirilemez — troponin bekle",-4,60,"n9","Sgarbossa ölçütleri LBBB'de akut oklüzyonu gösterebilir; bekleme miyokard kaybıdır."),
 ]),
 "n2":E("Primer PKG","Sirkumfleks arter tam tıkalı bulundu; stent sonrası ağrı geçti.\n\n**Akılda kalsın**\n- LBBB'de akut oklüzyon: **Sgarbossa** — konkordan STE ≥1 mm (en güçlü), V1–V3'te konkordan ST çökmesi ≥1 mm, **modifiye Smith**: diskordan STE/S oranı ≥0,25.\n- Süren iskemik semptom + LBBB (yeni veya eski) → **STEMI gibi yönet** (primer PKG).\n- Pacemaker ritminde de benzer ölçütler kullanılır.\n\n*Kaynak: ESC 2023 AKS kılavuzu; Smith ve ark., Ann Emerg Med 2012.*","good"),
 "n9":E("Geç tanı","Troponin pozitif gelince anjiyografi yapıldı; büyük infarkt ve kalp yetmezliği gelişti.","bad"),
}))
Qs+=[Q("c110q1","LBBB'de akut MI için en özgül Sgarbossa ölçütü hangisidir?",["Diskordan ST çökmesi","Konkordan ST elevasyonu ≥1 mm","Geniş QRS","T inversiyonu V5-V6","Sol aks"],1,"QRS ile aynı yönde ST elevasyonu.","Kardiyoloji"),
 Q("c110q2","Modifiye Smith-Sgarbossa ölçütünde diskordan ST elevasyonu/S dalgası oranı eşiği nedir?",["≥0,10","≥0,25","≥0,50","≥1","≥2"],1,"Orantısal ölçüt duyarlılığı artırır.","Kardiyoloji"),
 Q("c110q3","Süren iskemik göğüs ağrısı ve LBBB olan hasta nasıl yönetilir?",["Troponin beklenir","STEMI gibi (primer PKG)","Taburcu","Yalnız nitrat","Stres testi"],1,"ESC 2023 önerisi.","Kardiyoloji")]

P={"id":"ilk-nobet-11","title":"İlk Nöbet Vakaları — 11. Paket (vaka 101–110)","desc":"Preeksitasyonlu AF, kronik lityum zehirlenmesi, klavikula kırığı, akrep sokması, düğme pil yutma, lomber patlama kırığı, antikoagülan ilişkili intraparankimal kanama, mallet parmak, çok yüksek riskli NSTEMI, sol dal bloğunda akut MI.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 11. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 11. Paket","topic":"Temel acil","order":11,"req":[1],"desc":"Kardiyolojiden toksikolojiye ve el travmasına 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
