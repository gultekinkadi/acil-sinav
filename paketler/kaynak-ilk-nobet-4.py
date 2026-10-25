import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 31 DİGOKSİN İNTOKSİKASYONU (kronik)
S.append(case("c31","Bulantı ve sarı görme — 82 yaşında kadın","Toksikoloji",
 "82 yaşında kadın, yaklaşık 55 kg. Kalp yetmezliği ve AF için yıllardır digoksin 0,25 mg/gün kullanıyor. 1 hafta önce idrar yolu enfeksiyonu için klaritromisin başlanmış. 3 gündür bulantı, iştahsızlık, halsizlik; “her şeyi sarımsı” görüyor.",
 {"n1":N("Monitörlü alan","Bilinç açık, hafif konfüze. Dehidrate.","KB 98/58 · Nb 38 · SpO₂ %95",[
   T("12 derivasyonlu EKG",2,5,"Yavaş, düzenli **kavşak ritmi 38/dk** (AF'li hastada düzenli ritim = AV blok), ST'de “kepçe” çökmesi, ventriküler ekstrasistoller.","AF'de yavaş ve düzenli ritim digoksin toksisitesini düşündürür."),
   T("Digoksin düzeyi, K, kreatinin, Mg",3,40,"Digoksin **4,2 ng/mL** · **K 6,1** · kreatinin 2,1 (bazal 1,0) · Mg 1,7.","Böbrek hasarı + makrolid (P-gp inhibisyonu) → digoksin birikimi. Hiperkalemi toksisite ağırlığını gösterir."),
   A("Digoksin ve klaritromisini kes; monitör; **digoksine özgü antikor (Fab)**: kronik zehirlenmede flakon sayısı ≈ düzey (ng/mL) × kg / 100 → 4,2 × 55 / 100 ≈ 2,3 → 3 flakon (ya da kurum protokolüne göre 1–2 flakonla başla); hiperkalemi Fab ile düzelir; atropin köprü",4,20,"n2","Doğru. Fab endikasyonları: yaşamı tehdit eden aritmi/bradikardi, K >5–5,5, son organ hasarı, yüksek düzey."),
   A("Hiperkalemi için önce kalsiyum + insülin-glukoz, digoksini sürdür",-3,20,"n3","Digoksini sürdürmek toksisiteyi artırır; asıl tedavi Fab. (Kalsiyumun güvenliği tartışmalı; Fab varken ilk seçenek değil.)"),
   A("Bradikardi için transkutan pace ve elektriksel kardiyoversiyon hazırlığı, digoksine devam",-4,20,"n9","Digoksin toksisitesinde elektriksel girişimler ventriküler aritmileri tetikleyebilir; neden tedavi edilmeli."),
 ]),
 "n3":N("1 saat sonra","Ventriküler bigemine ritim, hız 36.","KB 84/50 · K 5,8",[
   A("Digoksini kes, Fab antikor ver",2,20,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Fab sonrası düzelme","Fab sonrası 60 dakikada hız 72'ye çıktı, K 4,6'ya düştü. Hasta 3 gün izlendi; digoksin dozu böbrek fonksiyonuna göre yeniden düzenlendi, makrolid değiştirildi.\n\n**Akılda kalsın**\n- Kronik digoksin zehirlenmesi: **yaşlı, böbrek yetmezliği, ilaç etkileşimi** (makrolid, amiodaron, verapamil), dehidratasyon.\n- Bulgular: bulantı, konfüzyon, **sarı-yeşil görme**, bradikardi/AV blok, **AF'de düzenli yavaş ritim**, ventriküler ektopi, çift yönlü VT.\n- **Hiperkalemi** = ağır toksisite (akut alımda K >5–5,5 Fab endikasyonu).\n- Tedavi: digoksini kes, **digoksin Fab**; elektriksel kardiyoversiyondan kaçın.\n- Fab sonrası serum digoksin düzeyi yorumlanamaz.\n\n*Kaynak: Lapostolle F. ve ark.; Goldfrank's Toxicologic Emergencies (11. baskı).*","good"),
 "n9":E("Ventriküler fibrilasyon","Hasta VF'ye girdi; uzun resüsitasyon gerekti.\n\nDigoksin toksisitesinde nedene yönelik tedavi Fab'dır.","bad"),
}))
Qs+=[Q("c31q1","Uzun süredir AF'si olan hastada ritmin düzenli ve yavaşlaması neyi düşündürür?",["Spontan sinüs ritmine dönüş","Digoksin toksisitesi (AV blok + kavşak ritmi)","Hipertiroidi","Hipokalsemi","Normal bulgu"],1,"AF'de düzenli yavaş ritim tam AV blok + kavşak/ventriküler kaçışı gösterir; digoksin toksisitesinde tipiktir.","Toksikoloji"),
 Q("c31q2","Kronik digoksin zehirlenmesinde Fab flakon sayısı formülü hangisidir?",["Düzey × kg / 100","Düzey × 10","kg / 10","Alınan mg × 2","Düzey / kg"],0,"Kronik: flakon ≈ serum düzeyi (ng/mL) × kg / 100.","Toksikoloji"),
 Q("c31q3","Digoksinle ilaç etkileşimi yaparak düzeyini artıran ilaç hangisidir?",["Parasetamol","Klaritromisin","Furosemid tek başına azaltır","Metformin","Omeprazol (anlamlı değil)"],1,"Makrolidler, amiodaron, verapamil, kinidin digoksin düzeyini artırır.","Toksikoloji")]

# 32 TCA İNTOKSİKASYONU
S.append(case("c32","Bilinç bulanıklığı — 26 yaşında kadın","Toksikoloji",
 "26 yaşında kadın. Arkadaşı, depresyon tedavisi gören hastanın yaklaşık 2 saat önce amitriptilin kutusunun tamamını (25 mg × 30) ve alkol aldığını, giderek uykuya daldığını söylüyor. Yaklaşık 60 kg.",
 {"n1":N("Resüsitasyon alanı","GKS 10, pupiller midriyatik, deri kuru-sıcak, mesane dolu (antikolinerjik bulgular).","KB 88/52 · Nb 128 · SS 14 · SpO₂ %94 · Ateş 37,8",[
   T("12 derivasyonlu EKG",3,5,"Sinüs taşikardisi, **QRS 138 ms**, **aVR'de terminal R dalgası 4 mm**, QTc uzun.","QRS >100 ms nöbet, >160 ms ventriküler aritmi riskini artırır; aVR'de R >3 mm toksisite göstergesi."),
   T("Kan gazı",1,10,"pH 7,32, pCO₂ 44.","Asidoz sodyum kanal blokajını artırır."),
   A("Sodyum bikarbonat 1–2 mEq/kg IV bolus (%8,4); QRS daralana kadar tekrar, ardından infüzyon (hedef pH 7,45–7,55); hava yolunu koru (gerekirse entübasyon + hiperventilasyon); hipotansiyonda sıvı, gerekirse norepinefrin",4,15,"n2","Doğru. Bikarbonat (sodyum yükü + alkalinizasyon) TCA'nın sodyum kanal blokajını aşar."),
   A("Flumazenil ver (benzodiazepin de almış olabilir)",-5,5,"n9","Flumazenil TCA zehirlenmesinde nöbeti tetikler; kontrendikedir."),
   A("Fizostigmin ile antikolinerjik bulguları geri çevir",-4,5,"n9","TCA'da fizostigmin asistoli ve nöbetle ilişkilidir; kontrendike."),
 ]),
 "n2":N("Bikarbonattan sonra","QRS 110 ms'ye daraldı. Hasta jeneralize nöbet geçirmeye başladı.","KB 96/60 · Nb 120",[
   A("Benzodiazepin (ör. diazepam 10 mg IV ya da midazolam); bikarbonatı tekrarla (nöbet asidozu artırır); fenitoin verme",3,5,"n3","Doğru. TCA nöbetinde ilk seçenek benzodiazepin; fenitoin sodyum kanal blokajını artırabilir."),
   A("Fenitoin yükle",-3,15,"n9","Fenitoin TCA kardiyotoksisitesinde önerilmez."),
 ]),
 "n3":E("Yoğun bakımda iyileşme","Entübe edilip bikarbonat infüzyonu ile izlendi; 24 saatte QRS normale döndü, hasta ekstübe edildi. Psikiyatri değerlendirmesi yapıldı.\n\n**Akılda kalsın**\n- TCA: **antikolinerjik bulgular + nöbet + hipotansiyon + geniş QRS**.\n- EKG: **QRS >100 ms**, aVR'de **R >3 mm**, sağ eksen.\n- **Sodyum bikarbonat 1–2 mEq/kg** bolus, QRS daralana kadar; hedef pH 7,45–7,55.\n- Nöbette **benzodiazepin**; fenitoin, flumazenil, fizostigmin, sınıf IA/IC antiaritmik yok.\n- Hava yolu güvenliyse ve ilk 1–2 saatteyse aktif kömür düşünülebilir.\n\n*Kaynak: Goldfrank's Toxicologic Emergencies; EXTRIP/AACT önerileri.*","good"),
 "n9":E("Ventriküler aritmi / arrest","Hasta geniş QRS'li taşikardiye, ardından arreste girdi.\n\nTCA zehirlenmesinde bikarbonat hayat kurtarır; flumazenil, fizostigmin ve fenitoinden kaçınılır.","bad"),
}))
Qs+=[Q("c32q1","TCA zehirlenmesinde QRS genişliğinde ilk tedavi hangisidir?",["Amiodaron","Sodyum bikarbonat 1–2 mEq/kg IV","Lidokain tek başına","Kalsiyum glukonat","Fizostigmin"],1,"Hipertonik sodyum ve alkalinizasyon sodyum kanal blokajını aşar.","Toksikoloji"),
 Q("c32q2","TCA zehirlenmesinde kontrendike olan ilaç hangisidir?",["Diazepam","Norepinefrin","Flumazenil","Sodyum bikarbonat","Aktif kömür (uygun hastada)"],2,"Flumazenil nöbet eşiğini düşürür.","Toksikoloji"),
 Q("c32q3","TCA zehirlenmesinde EKG'de toksisiteyi gösteren bulgu hangisidir?",["aVR'de R dalgası >3 mm","Sivri T","Delta dalgası","U dalgası","Osborn dalgası"],0,"aVR'de terminal R >3 mm ve QRS >100 ms.","Toksikoloji")]

# 33 ÇOCUKTA DEHİDRATASYON
S.append(case("c33","İshal ve kusma — 18 aylık erkek","Pediatri",
 "18 aylık erkek, 11 kg (1 hafta önce 11,8 kg). 2 gündür sulu ishal (günde 8–10) ve kusma. Son 8 saatte 1 bez ıslatmış. Ateş 38 °C.",
 {"n1":N("Çocuk acil","Huzursuz ama uyanık; gözler çökük, mukozalar kuru, ağlarken az gözyaşı, deri turgoru hafif azalmış, kapiller dolum 2 sn. Ekstremiteler sıcak.","Nb 148 · SS 32 · KB 92/58",[
   T("Dehidratasyon derecesi",2,2,"Kilo kaybı ≈ %7 → **orta dehidratasyon**.","Klinik dehidratasyon skalası; hafif <%5, orta %5–10, ağır >%10 (şok)."),
   T("Kapiller glukoz",1,1,"72 mg/dL.","Uzamış açlıkta hipoglisemi olabilir."),
   T("Rutin elektrolit ve gaita kültürü",0,60,"Na 138, K 3,6, HCO₃ 18.","Orta dehidratasyonda ORS ile tedavi edilen çocukta rutin laboratuvar gerekmez."),
   A("Oral rehidratasyon: ORS 75 mL/kg (≈800 mL) 4 saatte, sık ve küçük yudumlarla (5 dakikada bir 5–10 mL); kusma varsa ondansetron 0,15 mg/kg PO (≈2 mg); emzirme/beslenmeyi sürdür",4,30,"n2","Doğru. Orta dehidratasyonda ilk seçenek ORS; ondansetron kusmayı ve IV ihtiyacını azaltır."),
   A("IV hipotonik (%0,45) sıvı yükle, aç bırak",-2,30,"n2","Orta dehidratasyonda ORS IV kadar etkilidir; IV gerekiyorsa izotonik sıvı kullanılır. Aç bırakmak gereksiz."),
   A("Loperamid + meyve suyu/kola öner, taburcu",-5,10,"n9","Loperamid küçük çocukta kontrendike (ileus, SSS depresyonu); şekerli içecekler ishali artırır."),
 ]),
 "n2":N("4 saat sonra","Çocuk 750 mL ORS içti, 2 kez idrar yaptı, oyun oynuyor. İshal sürüyor.","Nb 118",[
   A("Taburculuk: her ishal sonrası 10 mL/kg ORS, normal beslenme; uyarı bulguları (az idrar, uyuşukluk, kanlı ishal, inatçı kusma) anlatıldı; çinko (10–20 mg/gün, 10–14 gün)",3,15,"n3","Doğru."),
   A("İshal geçene kadar yatır",-1,30,"n3","Rehidrate ve oral alan çocuk ayaktan izlenebilir."),
 ]),
 "n3":E("Başarılı oral rehidratasyon","Kontrolde çocuk 11,6 kg, iyi görünüyor.\n\n**Akılda kalsın**\n- Dehidratasyon derecesini **klinik bulgularla** belirle (kapiller dolum, turgor, solunum paterni en değerli).\n- Hafif–orta: **ORS 50–100 mL/kg, 4 saatte**; sık ve küçük yudumlar.\n- Kusmada **ondansetron 0,15 mg/kg**.\n- Ağır/şok: **20 mL/kg izotonik bolus**, yeniden değerlendir.\n- **Beslenmeyi kesme**; loperamid ve şekerli içecek yok; çinko (DSÖ).\n\n*Kaynak: ESPGHAN/ESPID 2014; DSÖ ishal yönetimi.*","good"),
 "n9":E("Ağır dehidratasyon","Çocuk 24 saat sonra letarjik, şokta getirildi; ayrıca loperamide bağlı abdominal distansiyon vardı.\n\nÇocukta ishalde ORS esastır; antidiyareik verilmez.","bad"),
}))
Qs+=[Q("c33q1","Orta dehidratasyonlu çocukta ilk seçenek tedavi hangisidir?",["IV %0,45 NaCl","ORS 50–100 mL/kg, 4 saatte","Meyve suyu","Loperamid","Açlık"],1,"Oral rehidratasyon IV kadar etkili ve daha güvenlidir.","Pediatri"),
 Q("c33q2","Gastroenteritte kusan çocukta ORS toleransını artıran ilaç hangisidir?",["Metoklopramid","Ondansetron 0,15 mg/kg","Prometazin","Loperamid","Domperidon"],1,"Tek doz ondansetron kusmayı ve IV ihtiyacını azaltır.","Pediatri"),
 Q("c33q3","Şok bulguları olan dehidrate çocukta ilk IV sıvı bolusu hangisidir?",["5 mL/kg %5 dekstroz","20 mL/kg izotonik kristaloid","40 mL/kg %0,45 NaCl","10 mL/kg albümin","Sıvı verilmez"],1,"Ağır dehidratasyonda 20 mL/kg izotonik bolus, ardından yeniden değerlendirme.","Pediatri")]

# 34 OMUZ ÇIKIĞI (ANTERİOR)
S.append(case("c34","Omuz ağrısı — 25 yaşında erkek","Ortopedi",
 "25 yaşında erkek. Basketbolda kolu dışa dönük ve yukarıdayken düşmüş. Sağ omzunu hareket ettiremiyor, kolunu diğer eliyle tutuyor. İlk kez oluyor.",
 {"n1":N("Muayene","Sağ omuzda deltoid konturu kaybolmuş (“apolet” görünümü), humerus başı önde ele geliyor. Kol hafif abdüksiyon ve dış rotasyonda.","KB 132/80 · Nb 96",[
   T("Nörovasküler muayene (aksiller sinir)",2,2,"Deltoid üzerindeki “apolet” bölgesinde duyu **normal**; radial nabız normal.","Aksiller sinir hasarı en sık eşlik eden sinir yaralanmasıdır; redüksiyon öncesi ve sonrası belgele."),
   T("Omuz grafisi (AP + skapular Y/aksiller)",2,15,"**Anterior glenohumeral çıkık**; eşlik eden kırık yok.","İlk çıkık, yüksek enerji ve yaşlı hastada redüksiyon öncesi grafi önerilir."),
   A("Analjezi (± prosedürel sedasyon/intraartiküler lidokain); atravmatik redüksiyon tekniği — dış rotasyon, Cunningham veya FARES ya da skapular manipülasyon",4,20,"n2","Doğru. Kuvvet uygulamayan teknikler çoğunlukla sedasyon gerektirmeden başarılıdır."),
   A("Analjezi vermeden, ayakla koltuk altına bastırıp sert çekiş (Hipokrat), kırık grafisi gerekmez",-3,10,"n2","Analjezisiz zorlu çekiş ağrılı ve komplikasyon (sinir/damar, kırık) riski yüksektir; grafi atlanırsa eşlik eden kırık gözden kaçabilir."),
 ]),
 "n2":N("Redüksiyon sonrası","“Klonk” sesiyle omuz yerine oturdu; hasta rahatladı.","Nb 84",[
   A("Redüksiyon sonrası nörovasküler muayene ve kontrol grafisi; kol askısı (konfor için kısa süre), erken fizyoterapi ve ortopedi kontrolü",3,15,"n3","Doğru."),
   A("Muayene/grafi gerekmez, 6 hafta sıkı askı",-2,10,"n3","Redüksiyon sonrası kontrol ve muayene atlanmamalı; uzun immobilizasyon nüksü azaltmaz, sertlik yapar."),
 ]),
 "n3":E("Başarılı redüksiyon","Kontrol grafisinde eklem yerinde; aksiller sinir fonksiyonu normal. Genç ve ilk çıkık olduğu için nüks riski anlatıldı; ortopedi kontrolü planlandı.\n\n**Akılda kalsın**\n- Anterior çıkık en sık; **aksiller sinir** (deltoid üstü duyu) muayenesi redüksiyon öncesi ve sonrası.\n- İlk çıkıkta grafi; **atravmatik teknikler** (dış rotasyon, Cunningham, FARES, skapular manipülasyon).\n- Yeterli analjezi; intraartiküler lidokain bir seçenektir.\n- **>40 yaşta rotator manşet yırtığı**, genç hastada **nüks** riski yüksek.\n- Posterior çıkık: nöbet/elektrik çarpması sonrası, kol iç rotasyonda kilitli — kolayca atlanır.\n\n*Kaynak: Roberts & Hedges' Clinical Procedures (7. baskı).*","good"),
 "n9":E("Komplikasyon","(Bu sonuç yolunda: zorlu manevra sonrası humerus boyun kırığı / sinir hasarı.)","bad"),
}))
# n9 ulaşılabilir olmalı — kötü yol ekle
S[-1]["nodes"]["n1"]["opts"].append(A("Grafi çekmeden, sedasyonsuz ve kuvvetli kaldıraç (Kocher) manevrası",-4,10,"n9","Kaldıraç manevraları humerus kırığı ve damar-sinir yaralanmasıyla ilişkilidir."))
S[-1]["nodes"]["n9"]["text"]="Kuvvetli kaldıraç manevrası sonrası humerus cerrahi boyun kırığı gelişti; hasta acil ameliyata alındı.\n\nRedüksiyonda kuvvet değil, gevşeme ve atravmatik teknik esastır."
S[-1]["order"]=list(S[-1]["nodes"].keys())
Qs+=[Q("c34q1","Anterior omuz çıkığında redüksiyon öncesi mutlaka değerlendirilmesi gereken sinir hangisidir?",["Radial sinir","Aksiller sinir","Ulnar sinir","Median sinir","Torasik uzun sinir"],1,"Deltoid üstü (apolet bölgesi) duyu kaybı aksiller sinir hasarını gösterir.","Ortopedi"),
 Q("c34q2","Hangisi kuvvet uygulamayan (atravmatik) bir redüksiyon tekniğidir?",["Hipokrat","Kocher kaldıracı","Cunningham tekniği","Sert traksiyon-kontratraksiyon","Hiçbiri"],2,"Cunningham, dış rotasyon, FARES ve skapular manipülasyon atravmatik tekniklerdir.","Ortopedi"),
 Q("c34q3","Nöbet veya elektrik çarpması sonrası kolun iç rotasyonda kilitli olduğu omuz çıkığı hangisidir?",["Anterior","Posterior","İnferior (luxatio erecta)","Superior","Akromiyoklaviküler"],1,"Posterior çıkık sıklıkla atlanır; aksiller veya skapular Y grafisi gerekir.","Ortopedi")]

# 35 DİSTAL RADİUS KIRIĞI (COLLES)
S.append(case("c35","Bilekte ağrı ve şekil bozukluğu — 68 yaşında kadın","Ortopedi",
 "68 yaşında kadın. Buzlu kaldırımda düşerken sol elini yere koymuş. Bilekte ağrı ve “çatal sırtı” şekil bozukluğu var.",
 {"n1":N("Muayene","Distal radiusta dorsale açılanma ve şişlik. Parmaklar sıcak, kapiller dolum normal.","KB 148/86 · Nb 90",[
   T("Median sinir muayenesi",2,2,"İlk üç parmak volar yüzde hafif uyuşma; tenar güç normal.","Distal radius kırığında akut karpal tünel sendromu gelişebilir — redüksiyon öncesi ve sonrası belgele."),
   T("El bileği grafisi (AP + lateral)",2,15,"Ekstraartiküler distal radius kırığı, **dorsal açılanma 25°**, radial kısalma 4 mm; ulna stiloid kırığı.","Kabul edilebilirlik ölçütleri: volar tilt ≈ nötr (dorsal açılanma <10°), radial boy kaybı <3–5 mm, radial inklinasyon korunmuş, eklem içi basamak <2 mm."),
   A("Analjezi + hematom bloğu (ya da Bier bloğu); kapalı redüksiyon (traksiyon, volar fleksiyon/ulnar deviasyon); sugar-tong/dorsal atel; redüksiyon sonrası grafi ve nörovasküler muayene",4,30,"n2","Doğru. Kabul edilemez açılanmada redüksiyon gerekir."),
   A("Redüksiyon yapmadan alçıya al, 6 hafta sonra kontrol",-3,15,"n8","Dorsal açılanma 25° kabul edilemez; malunion ve fonksiyon kaybı."),
 ]),
 "n2":N("Redüksiyon sonrası","Kontrol grafisi: dorsal açılanma 5°, radial boy korunmuş. Hasta ateli tolere ediyor.","",[
   A("Kolu kalp seviyesinde/hafif yüksek tut, parmak egzersizleri; 1 hafta içinde kırık kliniği/ortopedi (yer değiştirme kontrolü); uyarılar (artan ağrı, uyuşma, parmak rengi); kemik sağlığı (osteoporoz) değerlendirmesine yönlendir",3,15,"n3","Doğru. Düşük enerjili kırık yaşlı kadında frajilite kırığıdır."),
   A("Sıkı dairesel alçı, kontrol gerekmez",-3,10,"n9","Akut dönemde dairesel alçı kompartman/sinir basısı riski taşır; ilk haftalarda yer değiştirme sık."),
 ]),
 "n3":E("İyi sonuç","1. hafta grafisinde redüksiyon korunmuştu; 6 haftada alçı çıkarıldı. DXA'da osteoporoz saptandı, tedavi başlandı.\n\n**Akılda kalsın**\n- Colles: dorsale açılanmış distal radius kırığı (“çatal sırtı”).\n- **Median sinir** muayenesi; akut karpal tünel cerrahi acil olabilir.\n- Kabul edilemez dizilimde **hematom/Bier bloğu ile kapalı redüksiyon**, atel.\n- Akut dönemde **dairesel alçı yok**; 1 hafta içinde kontrol.\n- Yaşlıda **frajilite kırığı** → osteoporoz değerlendirmesi.\n\n*Kaynak: AAOS 2020 distal radius kırığı kılavuzu; BOAST 2017.*","good"),
 "n8":E("Malunion","6 haftada kırık açılanmış olarak kaynadı; kavrama gücü ve rotasyon kısıtlı, korektif osteotomi planlandı.","mid"),
 "n9":E("Alçı altında bası","İki gün sonra şiddetli ağrı ve parmaklarda uyuşmayla döndü; alçı açıldı, akut karpal tünel sendromu için cerrahi gevşetme gerekti.","bad"),
}))
Qs+=[Q("c35q1","Distal radius kırığında redüksiyon öncesi ve sonrası özellikle değerlendirilmesi gereken sinir hangisidir?",["Ulnar","Median","Radial","Aksiller","Muskulokutanöz"],1,"Akut karpal tünel sendromu (median sinir) önemli bir komplikasyondur.","Ortopedi"),
 Q("c35q2","Distal radius kırığında hangi bulgu kabul edilemez dizilimi gösterir?",["Volar tilt nötr","Dorsal açılanma 25°","Radial boy kaybı 1 mm","Eklem içi basamak 0 mm","Radial inklinasyon 22°"],1,"Dorsal açılanma >10° (bazı kaynaklarda >15–20°) genellikle kabul edilemez.","Ortopedi"),
 Q("c35q3","68 yaşında düşük enerjili düşmeyle distal radius kırığı olan kadında ek olarak ne planlanmalıdır?",["Rutin el BT","Osteoporoz değerlendirmesi","Antikoagülan","Profilaktik antibiyotik","Psikiyatri konsültasyonu"],1,"Frajilite kırıkları osteoporoz değerlendirmesi ve tedavi gerektirir.","Ortopedi")]

# 36 AKUT AÇI KAPANMASI GLOKOMU
S.append(case("c36","Kırmızı göz ve baş ağrısı — 62 yaşında kadın","Göz",
 "62 yaşında kadın, hipermetrop. Akşam karanlık sinema salonunda sağ gözünde şiddetli ağrı, baş ağrısı, bulantı-kusma başlamış; ışıkların çevresinde halkalar görüyor, görmesi bulanık.",
 {"n1":N("Muayene","Sağ göz kırmızı (silier enjeksiyon), kornea buğulu, **pupil orta dilate ve ışığa yanıtsız**. Palpasyonda göz taş gibi sert. Sağ görme keskinliği el hareketi düzeyinde.","KB 168/94 · Nb 92",[
   T("Göz içi basıncı (tonometri)",3,5,"Sağ **58 mmHg**, sol 16 mmHg.","Normal 10–21 mmHg."),
   T("Beyin BT (migren/kanama için)",-2,40,"Normal. 40 dakika kaybedildi.","Kırmızı göz + dilate sabit pupil + sert göz → glokom; BT tedaviyi geciktirmemeli."),
   A("GİB düşürücü tedavi: topikal timolol %0,5 + apraklonidin/brimonidin + (birkaç dakika arayla) pilokarpin %1–2; asetazolamid 500 mg IV/PO; analjezi + antiemetik; dirençli ise mannitol IV; acil göz konsültasyonu (lazer iridotomi)",4,20,"n2","Doğru. Amaç GİB'i hızla düşürüp optik siniri korumak; kesin tedavi lazer periferik iridotomi."),
   A("Migren — triptan ve antiemetik, karanlık odada dinlendir",-5,30,"n9","Karanlık ortam pupili dilate ederek açı kapanmasını artırır; görme kaybı riski."),
   A("Pupili büyütüp fundusa bak (tropikamid)",-5,10,"n9","Midriyatikler açı kapanmasını kötüleştirir."),
 ]),
 "n2":E("Görme korundu","1 saatte GİB 30 mmHg'ye, 3 saatte 18 mmHg'ye indi. Ertesi gün iki göze lazer periferik iridotomi yapıldı (diğer göz de risk altında).\n\n**Akılda kalsın**\n- Kırmızı göz + şiddetli ağrı/baş ağrısı + bulantı-kusma + halolar + **orta dilate sabit pupil** + sert göz = **akut açı kapanması**.\n- Karanlık ortam, antikolinerjik/sempatomimetik ilaçlar, midriyatikler tetikler.\n- Tedavi: **timolol + alfa agonist + pilokarpin + asetazolamid** (± mannitol); acil göz.\n- Kesin tedavi **lazer iridotomi** (karşı göze de profilaktik).\n- Migren veya gastroenteritle karıştırılabilir.\n\n*Kaynak: AAO Preferred Practice Pattern 2020 (birincil açı kapanması).*","good"),
 "n9":E("Kalıcı görme kaybı","Basınç saatlerce yüksek kaldı; optik sinir hasarı ile sağ gözde kalıcı görme kaybı gelişti.","bad"),
}))
Qs+=[Q("c36q1","Akut açı kapanması glokomunda pupil nasıldır?",["Miyotik, ışığa yanıtlı","Orta dilate, ışığa yanıtsız","Normal","Anizokori yok, iki taraf miyotik","Marcus Gunn"],1,"Orta dilate, sabit pupil tipiktir.","Göz"),
 Q("c36q2","Akut açı kapanmasında kontrendike olan ilaç hangisidir?",["Timolol","Asetazolamid","Pilokarpin","Tropikamid (midriyatik)","Apraklonidin"],3,"Midriyatikler açıyı daha da kapatır.","Göz"),
 Q("c36q3","Akut açı kapanması glokomunun kesin tedavisi hangisidir?",["Topikal steroid","Lazer periferik iridotomi","Oral antibiyotik","Kontakt lens","Yapay gözyaşı"],1,"Lazer iridotomi hümör akışı için yeni yol açar; karşı göze de profilaktik uygulanır.","Göz")]

# 37 SEPTİK ARTRİT
S.append(case("c37","Şiş, sıcak diz — 70 yaşında erkek","Ortopedi / Enfeksiyon",
 "70 yaşında erkek, diyabet ve gut öyküsü. 2 gündür sağ dizde artan ağrı, şişlik; yürüyemiyor. Dün titremesi olmuş. 2 hafta önce dize başka bir merkezde steroid enjeksiyonu yapılmış.",
 {"n1":N("Muayene","Sağ diz sıcak, kızarık, belirgin efüzyon; pasif hareket çok ağrılı.","KB 128/76 · Nb 108 · Ateş 38,6",[
   T("Eklem aspirasyonu (antibiyotikten önce): hücre sayımı, Gram boyama, kültür, kristal",4,20,"Bulanık sıvı; **lökosit 82.000/mm³ (%92 PNL)**; Gram pozitif koklar; **ürat kristalleri de var**.","Sinovyal lökosit >50.000 septik artriti düşündürür; **kristal varlığı enfeksiyonu dışlamaz**."),
   T("Kan kültürü, CRP, lökosit",1,30,"CRP 210, lökosit 15.400.","Kan kültürü %30–50 pozitif."),
   T("Diz grafisi",0,20,"Efüzyon; kemik tutulumu yok.","Başlangıçta normal olabilir; bazal olarak yararlı."),
   A("Aspirasyondan sonra IV ampirik antibiyotik (ör. vankomisin + seftriakson; risk faktörlerine göre); ortopedi — acil eklem drenajı/lavaj; analjezi",4,15,"n2","Doğru. Septik artrit eklem kıkırdağını günler içinde yıkar; drenaj ve antibiyotik birlikte."),
   A("Kristal görüldü — gut atağı: NSAİİ + kolşisin, taburcu",-5,15,"n9","Gut ve septik artrit birlikte olabilir; yüksek hücre sayısı + Gram boyamada bakteri septik artrittir."),
   A("İntraartiküler steroid enjeksiyonu yap",-5,10,"n9","Enfekte ekleme steroid enfeksiyonu ağırlaştırır."),
 ]),
 "n2":E("Drenaj ve antibiyotik","Artroskopik lavaj yapıldı; kültürde MSSA üredi, sefazoline geçildi. 6 haftalık antibiyotikle iyileşti.\n\n**Akılda kalsın**\n- Akut monoartrit = **aksi kanıtlanana kadar septik artrit**.\n- **Antibiyotikten önce eklem aspirasyonu** (Gram, kültür, hücre, kristal).\n- Sinovyal lökosit >50.000 (özellikle >100.000) güçlü destek; **kristal enfeksiyonu dışlamaz**.\n- IV ampirik antibiyotik + **acil drenaj**.\n- Risk: ileri yaş, diyabet, RA, protez, yakın zamanda eklem girişimi, IV ilaç kullanımı.\n\n*Kaynak: BSR/BOA septik artrit kılavuzu; EULAR.*","good"),
 "n9":E("Eklem yıkımı / sepsis","Hasta 3 gün sonra sepsis ve eklem kıkırdağı yıkımıyla döndü; kalıcı fonksiyon kaybı.\n\nSeptik artritte zaman kıkırdaktır.","bad"),
}))
Qs+=[Q("c37q1","Akut monoartritte antibiyotikten önce yapılması gereken işlem hangisidir?",["MR","Eklem aspirasyonu (Gram, kültür, hücre, kristal)","Kemik sintigrafisi","Ürik asit düzeyi","Romatoid faktör"],1,"Tanı ve hedefe yönelik tedavi için aspirasyon antibiyotikten önce yapılır (ama geciktirilmez).","Ortopedi / Enfeksiyon"),
 Q("c37q2","Sinovyal sıvıda ürat kristali görülmesi ile ilgili doğru ifade hangisidir?",["Septik artriti dışlar","Septik artrit ile birlikte bulunabilir","Antibiyotik gereksizdir","Yalnız psödogutta görülür","Kültür gerekmez"],1,"Kristal artropatisi ve enfeksiyon birlikte olabilir.","Ortopedi / Enfeksiyon"),
 Q("c37q3","Septik artritte antibiyotikle birlikte gereken temel tedavi hangisidir?",["İntraartiküler steroid","Eklem drenajı/lavajı","Uzun süre immobilizasyon tek başına","Soğuk uygulama","Kolşisin"],1,"Pürülan sıvının drenajı (iğne, artroskopi veya açık) kıkırdağı korur.","Ortopedi / Enfeksiyon")]

# 38 EPİDURAL HEMATOM
S.append(case("c38","Kafa travması — 19 yaşında erkek","Beyin cerrahisi / Travma",
 "19 yaşında erkek. Kasksız bisiklet kazasında sol şakağını çarpmış, kısa süre bilinç kaybı olmuş. Arkadaşları acile getirdi; yolda uyanık ve konuşuyormuş.",
 {"n1":N("Acil girişi","Uyanık, oryante, baş ağrısı ve bulantısı var. Sol temporalde şişlik. Nörolojik muayene normal.","GKS 15 · KB 132/78 · Nb 76 · SpO₂ %98",[
   T("Kraniyal BT (Kanada BT kuralı)",3,20,"**Sol temporalde 2,1 cm kalınlıkta bikonveks (lens şeklinde) hiperdens epidural hematom**, temporal kemikte lineer kırık; 4 mm orta hat kayması.","Kanada BT kuralı: bilinç kaybı + kafatası kırığı şüphesi, kusma, ≥65 yaş, tehlikeli mekanizma vb. → BT."),
   A("GKS 15, nörolojisi normal — 4 saat gözlem, sonra taburcu",-5,120,"n3","“Lusid interval”: epidural hematomlu hastalar başlangıçta iyi görünebilir. Bilinç kaybı ve temporal travma BT endikasyonudur."),
   A("BT çek; hematom görülürse acil beyin cerrahisi",4,20,"n2","Doğru."),
 ]),
 "n3":N("2 saat sonra — gözlem alanı","Hasta uykuya meyilli, kusuyor. Sol pupil dilate, sağ kolda güçsüzlük.","GKS 9 · KB 168/88 · Nb 54",[
   A("Acil BT + beyin cerrahisi; hava yolu (entübasyon), başı 30° kaldır, hiperozmolar tedavi (mannitol 1 g/kg veya %3 NaCl) köprü olarak; hipotansiyon/hipoksiden kaçın",2,20,"n2","Doğru — herniasyon bulguları. Cushing yanıtı (hipertansiyon + bradikardi) kafa içi basınç artışını gösterir."),
   A("Analjezik ve antiemetik, sabaha kadar gözlem",-5,60,"n9","Herniasyon bulguları; dakikalar içinde ölümcül olabilir."),
 ]),
 "n2":E("Acil kraniyotomi","Hematom boşaltıldı; orta meningeal arter kanaması kontrol edildi. Hasta 1 hafta sonra nörolojik sekelsiz taburcu oldu.\n\n**Akılda kalsın**\n- Epidural hematom: temporal travma, **orta meningeal arter**, BT'de **bikonveks**, kemik kırığı.\n- **Lusid interval**: uyanık hastada ani kötüleşme.\n- Kafa travmasında **Kanada BT kuralı** / NICE ölçütleri ile BT kararı.\n- Herniasyon: anizokori, kontralateral hemiparezi, Cushing yanıtı → **acil cerrahi**; hiperozmolar tedavi ve kısa süreli hiperventilasyon yalnız köprü.\n- Hipoksi (SpO₂ <%90) ve hipotansiyon (sistolik <110 erişkin) sekonder hasarı artırır.\n\n*Kaynak: Brain Trauma Foundation 2016; NICE NG232 (2023).*","good"),
 "n9":E("Herniasyon","Hasta transtentoryal herniasyonla kaybedildi.\n\nKafa travmasında bilinç kaybı ve temporal darbe varsa BT ile değerlendirilmeli.","bad"),
}))
Qs+=[Q("c38q1","Epidural hematomun BT görünümü nasıldır?",["Hilal şeklinde","Bikonveks (lens şeklinde)","Sulkuslarda hiperdensite","Bazal sisternlerde kan","İntraparankimal"],1,"Epidural hematom sütür hatlarını aşmaz, bikonvekstir; subdural hilal şeklindedir.","Beyin cerrahisi / Travma"),
 Q("c38q2","Epidural hematomda en sık kanama kaynağı hangisidir?",["Köprü venler","Orta meningeal arter","Baziler arter","Sinüs sagittalis superior","Koroid pleksus"],1,"Temporal kemik kırığı ile orta meningeal arter yaralanması klasiktir.","Beyin cerrahisi / Travma"),
 Q("c38q3","Cushing yanıtı hangi bulgulardan oluşur?",["Hipotansiyon + taşikardi","Hipertansiyon + bradikardi + düzensiz solunum","Ateş + taşikardi","Hipotermi + hipotansiyon","Taşipne + hipotansiyon"],1,"Artmış kafa içi basıncının geç bulgusudur.","Beyin cerrahisi / Travma")]

# 39 TORSADES DE POINTES
S.append(case("c39","Tekrarlayan bayılma — 58 yaşında kadın","Kardiyoloji",
 "58 yaşında kadın. Pnömoni için levofloksasin, bulantı için ondansetron kullanıyor; kalp yetmezliği nedeniyle furosemid alıyor. Bugün iki kez kısa süreli bayılmış.",
 {"n1":N("Monitörlü alan","Uyanık. Monitörde birkaç saniyelik, QRS'leri eksen etrafında dönen polimorfik VT atakları kendiliğinden sonlanıyor.","KB 112/70 · Nb 58 · SpO₂ %96",[
   T("12 derivasyonlu EKG (atak arası)",3,5,"Sinüs bradikardisi, **QTc 590 ms**, belirgin U dalgaları.","Uzun QT + polimorfik VT = **torsades de pointes**."),
   T("K, Mg, Ca",2,20,"**K 2,9**, **Mg 1,4**, Ca normal.","Hipokalemi ve hipomagnezemi QT'yi uzatır."),
   A("**Magnezyum sülfat 2 g IV** (1–2 dakikada; stabilse 10–15 dakikada); K'yı 4,5–5 mmol/L'ye yükselt; QT uzatan ilaçları (levofloksasin, ondansetron) kes; defibrilatör pedleri takılı",4,15,"n2","Doğru. Magnezyum, Mg düzeyi normal olsa bile ilk tedavidir."),
   A("Amiodaron 300 mg IV",-5,10,"n9","Amiodaron QT'yi uzatır; torsades'ı kötüleştirir."),
 ]),
 "n2":N("Magnezyumdan sonra","Ataklar seyreldi ama 2 kez daha tekrarladı; bradikardik dönemlerden sonra başlıyor.","Nb 52",[
   A("Kalp hızını artır: geçici transvenöz overdrive pace (hız 90–110) ya da izoprenalin infüzyonu (köprü); gerekirse magnezyum tekrarı",3,20,"n3","Doğru. Bradikardi ve duraklamalar torsades'ı tetikler; hızı artırmak QT'yi kısaltır."),
   A("Beta bloker ver",-3,10,"n9","Edinsel uzun QT'de bradikardi torsades'ı tetikler; beta bloker (konjenital uzun QT dışında) kötüleştirir."),
 ]),
 "n3":E("Kontrol altında","Overdrive pace ve elektrolit düzeltilmesiyle atak kalmadı; 48 saatte QTc 470 ms'ye indi. İlaç listesi düzenlendi.\n\n**Akılda kalsın**\n- Torsades = **uzun QT + polimorfik VT**; çoğu kendiliğinden durur ama VF'ye dönebilir.\n- **Nabızsız/instabil → asenkron defibrilasyon**.\n- **Magnezyum sülfat 2 g IV**; K'yı 4,5–5'e çıkar.\n- QT uzatan ilaçları kes (makrolid, florokinolon, ondansetron, haloperidol, metadon, sınıf IA/III).\n- Hızı artır: **overdrive pace** veya izoprenalin. **Amiodaron yok.**\n\n*Kaynak: ESC 2022 Ventriküler aritmiler ve ani kardiyak ölüm kılavuzu.*","good"),
 "n9":E("Ventriküler fibrilasyon","Torsades VF'ye dönüştü; defibrilasyon ve uzun resüsitasyon gerekti.\n\nTorsades'da QT'yi uzatan ilaçlardan kaçınılır.","bad"),
}))
Qs+=[Q("c39q1","Torsades de pointes'in ilk ilaç tedavisi hangisidir?",["Amiodaron","Magnezyum sülfat 2 g IV","Prokainamid","Sotalol","Adenozin"],1,"Mg, serum düzeyi normal olsa bile ilk tedavidir.","Kardiyoloji"),
 Q("c39q2","Edinsel uzun QT'ye bağlı tekrarlayan torsades'da hangisi yararlıdır?",["Beta bloker","Kalp hızını artırmak (overdrive pace/izoprenalin)","Amiodaron","Haloperidol","Hipokalemiyi sürdürmek"],1,"Hız artışı QT'yi kısaltır, duraklama bağımlı torsades'ı önler.","Kardiyoloji"),
 Q("c39q3","Hangisi QT uzatan ilaç değildir?",["Levofloksasin","Ondansetron","Haloperidol","Klaritromisin","Parasetamol"],4,"Parasetamol QT'yi uzatmaz.","Kardiyoloji")]

# 40 KOMPARTMAN SENDROMU
S.append(case("c40","Alçı altında artan ağrı — 24 yaşında erkek","Ortopedi",
 "24 yaşında erkek. Dün motosiklet kazasında sağ tibia cisim kırığı; uzun bacak ateliyle gözleme alındı. Gece boyunca artan, morfine rağmen geçmeyen bacak ağrısı.",
 {"n1":N("Gece 03:00","Ağrı muayeneyle orantısız şiddetli. Ayak parmaklarının **pasif ekstansiyonu çok ağrılı**. Bacak gergin. 1. ve 2. parmak arasında hafif uyuşma. Dorsalis pedis nabzı alınıyor.","KB 138/80 · Nb 112",[
   T("Kompartman basıncı ölçümü",3,15,"Anterior kompartman **54 mmHg**; diyastolik KB 80 → **ΔP 26 mmHg**.","ΔP (diyastolik KB − kompartman basıncı) <30 mmHg fasyotomi endikasyonu; tanı esas olarak kliniktir."),
   A("Ateli/bandajı tüm katmanlarıyla gevşet, bacağı kalp seviyesinde tut (yükseltme), hipotansiyonu önle; acil ortopedi — fasyotomi",4,15,"n2","Doğru. Nabzın varlığı kompartman sendromunu dışlamaz."),
   A("Analjezik dozunu artır, bacağı yükselt, sabah vizitini bekle",-5,240,"n9","Yükseltme perfüzyon basıncını düşürür; analjezik ihtiyacının artması önemli bir uyarıdır. Gecikme kalıcı kas nekrozuna yol açar."),
 ]),
 "n2":E("Acil fasyotomi","Hasta 1 saat içinde ameliyata alındı; dört kompartman fasyotomisi ve kırığa eksternal fiksatör uygulandı. Kaslar canlıydı.\n\n**Akılda kalsın**\n- En erken ve en güvenilir bulgu: **orantısız ağrı** ve **pasif germe ile ağrı**.\n- Parestezi, solukluk, nabızsızlık, paralizi **geç** bulgulardır; **nabız varlığı dışlamaz**.\n- Tüm sargıyı/alçıyı gevşet, ekstremite **kalp seviyesinde** (yükseltme yok).\n- ΔP (diyastolik − kompartman) **<30 mmHg** → fasyotomi.\n- Risk: tibia kırığı, ezilme, reperfüzyon, sıkı alçı, antikoagülan.\n\n*Kaynak: BOAST 2016 akut kompartman sendromu; AAOS.*","good"),
 "n9":E("Kas nekrozu","Sabah fasyotomi yapıldığında anterior kompartman kasları nekrotikti; düşük ayak kaldı, rabdomiyoliz ve böbrek hasarı gelişti.\n\nKompartman sendromunda saatler önemlidir.","bad"),
}))
Qs+=[Q("c40q1","Akut kompartman sendromunun en erken bulgusu hangisidir?",["Nabızsızlık","Paralizi","Orantısız ağrı ve pasif germe ile ağrı","Solukluk","Hipotermi"],2,"Nabızsızlık ve paralizi geç bulgulardır.","Ortopedi"),
 Q("c40q2","Fasyotomi için kullanılan basınç ölçütü hangisidir?",["Kompartman basıncı >10 mmHg","ΔP (diyastolik KB − kompartman basıncı) <30 mmHg","Sistolik KB <90","Ortalama arter basıncı >100","Kompartman basıncı <20"],1,"ΔP <30 mmHg yetersiz perfüzyon göstergesidir.","Ortopedi"),
 Q("c40q3","Kompartman sendromu şüphesinde ekstremite pozisyonu nasıl olmalıdır?",["Kalp seviyesinin belirgin üstünde","Kalp seviyesinde","Sarkıtılmış","Buz ve kompresyon","Turnike"],1,"Yükseltme perfüzyon basıncını azaltır.","Ortopedi")]

P={"id":"ilk-nobet-4","title":"İlk Nöbet Vakaları — 4. Paket","desc":"Digoksin ve TCA zehirlenmesi, çocukta dehidratasyon, omuz çıkığı, distal radius kırığı, akut glokom, septik artrit, epidural hematom, torsades de pointes, kompartman sendromu.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 4. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 4. Paket","topic":"Acil tıp","order":4,"req":[2],"desc":"Toksikoloji, ortopedi, göz ve nöroşirürji acillerinden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
