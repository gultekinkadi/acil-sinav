# İlk Nöbet Vakaları — 1. Paket (özgün senaryolar; konu listesi esinlenme, metinler kendimize ait)
import json, sys
def T(label,pts,mins,res,fb=""): return {"kind":"test","label":label,"pts":pts,"min":mins,"res":res,"fb":fb}
def A(label,pts,mins,to,fb=""): return {"kind":"act","label":label,"pts":pts,"min":mins,"to":to,"fb":fb}
def N(title,text,vitals="",opts=None): return {"title":title,"text":text,"vitals":vitals,"opts":opts or []}
def E(title,text,outcome): return {"title":title,"text":text,"end":True,"outcome":outcome,"opts":[]}
def case(key,title,topic,intro,nodes): return {"key":key,"title":title,"topic":topic,"intro":intro,"start":"n1","order":list(nodes.keys()),"nodes":nodes}
def Q(key,stem,opts,correct,expl,topic): return {"key":key,"stem":stem,"options":opts,"correct":correct,"explanation":expl,"topic":topic}
S=[]; Qs=[]

# 1 ── AKUT GÖĞÜS AĞRISI: inferior STEMI + sağ ventrikül tutulumu + tam AV blok
S.append(case("c01","Akut göğüs ağrısı — 58 yaşında erkek","Kardiyoloji",
 "58 yaşında erkek. 40 dakikadır göğsün ortasında baskı tarzı ağrı, terleme ve bulantı. Sigara içiyor, hipertansiyon için ilaç kullanıyor. Triajda solgun ve terli.",
 {"n1":N("Triaj — ilk dakikalar","Hasta monitöre alındı, damar yolu açıldı. Ağrı 8/10, yayılım yok.","KB 98/62 · Nb 54 · SS 20 · SpO₂ %96 (oda havası) · Ateş 36,6",[
    T("12 derivasyonlu EKG",3,5,"Sinüs bradikardisi 54/dk. **II, III ve aVF'de 3 mm ST elevasyonu**; III'teki elevasyon II'den belirgin. **I ve aVL'de ST çökmesi** (ayna görüntüsü).","İlk temastan sonra 10 dakika içinde EKG — en önemli ilk adım."),
    T("Sağ prekordiyal derivasyonlar (V4R)",2,3,"**V4R'de 1 mm ST elevasyonu** → sağ ventrikül tutulumu.","İnferior MI'da V4R çekmek sağ ventrikül tutulumunu gösterir; nitrat ve sıvı kararını değiştirir."),
    T("Yüksek duyarlıklı troponin",0,60,"İlk değer hafif yüksek. (Sonuç 1 saatte geldi.)","STEMI tanısı EKG ile konur; reperfüzyon kararı için troponin beklenmez."),
    T("Toraks BT anjiyografi (diseksiyon için)",-2,45,"Aort diseksiyonu yok. Reperfüzyon 45 dakika gecikti.","Tipik inferior STEMI'de, diseksiyonu düşündüren bulgu (sırta yayılan yırtılır tarzda ağrı, nabız/KB farkı, mediasten genişliği, yeni AY üfürümü) yoksa rutin BTA gerekmez."),
    A("STEMI kodu: girişimsel kardiyolojiyi ara; ASA 150–300 mg çiğnet, P2Y12 yüklemesi (ör. tikagrelor 180 mg), anfraksiyone heparin 70–100 Ü/kg IV",4,10,"n2","Doğru. EKG STEMI ile uyumlu: hedef, tanıdan tel geçişine en kısa sürede (PKG merkezinde ≤60 dk) primer PKG."),
    A("Ağrı için dil altı nitrogliserin ver, ağrı geçerse yeniden değerlendir",-3,5,"n3","Sağ ventrikül tutulumu olan inferior MI'da nitratlar önyükü düşürüp derin hipotansiyona yol açar. Ayrıca reperfüzyon kararı gecikiyor."),
    A("İlk troponin sonucunu bekle, ona göre karar ver",-4,60,"n9","STEMI'de troponin beklemek reperfüzyonu geciktirir; her dakika miyokard kaybıdır."),
  ]),
  "n3":N("Nitrogliserinden 4 dakika sonra","Hasta sersemlediğini söylüyor, bilinci bulanıklaşıyor. Akciğerler temiz, juguler venöz dolgunluk var.","KB 72/44 · Nb 50 · SpO₂ %95",[
    A("Nitratı bırak; 250–500 mL kristaloid bolus, bacakları kaldır; STEMI kodunu başlat (ASA, P2Y12, heparin)",2,10,"n2","Doğru. Sağ ventrikül infarktında ventrikül önyüke bağımlıdır: dikkatli sıvı ve hızlı reperfüzyon."),
    A("Akciğer ödemi olabilir — furosemid 40 mg IV",-4,5,"n8","Akciğerler temiz, JVD sağ ventrikül yetmezliğinden. Diüretik önyükü daha da azaltır → kardiyojenik şok."),
  ]),
  "n2":N("Kateter laboratuvarı hazırlanırken","Yükleme ilaçları verildi, laboratuvar 15 dakika içinde hazır olacak. Monitörde ritim değişiyor; hasta baş dönmesi tarifliyor.","KB 84/50 · Nb 38 · SpO₂ %95",[
    T("Ritim şeridi / EKG",1,2,"**Tam (3. derece) AV blok**, dar QRS'li kaçış ritmi 38/dk. P dalgaları QRS'lerden bağımsız.","İnferior MI'da AV nodal blok sıktır ve çoğu reperfüzyonla düzelir."),
    A("Atropin 0,5–1 mg IV (3–5 dakikada bir tekrarlanabilir, toplam 3 mg); transkutan pace pedlerini tak; PKG'yi geciktirme",3,5,"n4","Doğru. Dar QRS'li nodal blokta atropin çoğunlukla etkilidir; yanıt yoksa transkutan pace. Asıl tedavi reperfüzyon."),
    A("Hız düşük ama ağrı sürüyor — metoprolol IV ver",-4,5,"n8","Bradikardi, AV blok ve hipotansiyonda beta bloker kontrendikedir."),
    A("Bradikardi düzelene kadar kateter laboratuvarını ertele",-3,30,"n9","Blok büyük olasılıkla iskemiye bağlı; en etkili tedavi reperfüzyon. Pace desteği ile PKG'ye gidilir."),
  ]),
  "n4":E("Primer PKG — sağ koroner açıldı","Atropin sonrası hız 58/dk. Sağ koroner proksimal tıkanıklığa stent takıldı; kapıdan balona 68 dakika. AV blok işlem sonrası düzeldi, hasta koroner yoğun bakımda stabil.\n\n**Akılda kalsın**\n- İlk temastan sonra **10 dk içinde EKG**.\n- İnferior MI'da **V4R** çek; sağ ventrikül tutulumunda **nitrat ve diüretikten kaçın**, hipotansiyonda dikkatli sıvı ver.\n- STEMI'de **troponin beklenmez**.\n- Tanıdan tel geçişine 120 dk içinde PKG yapılamayacaksa fibrinolitik düşünülür.\n\n*Kaynak: ESC 2023 Akut Koroner Sendromlar Kılavuzu.*","good"),
  "n8":E("Kardiyojenik şok","Hipotansiyon derinleşti; hasta entübe edilip inotrop desteğiyle kateter laboratuvarına alınabildi. Reperfüzyon gecikti, sağ ventrikül fonksiyonu ciddi bozuldu.\n\nSağ ventrikül infarktında önyükü azaltan ilaçlar (nitrat, diüretik, morfin) ve negatif kronotroplar şoku derinleştirir.","bad"),
  "n9":E("Gecikmiş reperfüzyon","Kateter laboratuvarına 2 saat sonra gidildi. Geniş inferior-posterior infarkt; ejeksiyon fraksiyonu %35'e düştü.\n\nSTEMI tanısı EKG ile konur; troponin, ek görüntüleme ya da bradikardi reperfüzyonu geciktirmemeli.","bad"),
 }))
Qs+= [Q("c01q1","İnferior STEMI'de sağ ventrikül tutulumunu göstermek için en yararlı derivasyon hangisidir?",["aVR","V4R","V1","V6","aVL"],1,"V4R'de ≥1 mm ST elevasyonu sağ ventrikül infarktını gösterir. İnferior MI'larda rutin çekilmelidir.","Kardiyoloji"),
 Q("c01q2","Sağ ventrikül tutulumlu inferior STEMI'de hipotansif hastada aşağıdakilerden hangisinden kaçınılmalıdır?",["Dikkatli kristaloid bolusu","Asetilsalisilik asit","Nitrogliserin","Anfraksiyone heparin","Primer PKG"],2,"Sağ ventrikül önyüke bağımlıdır; nitratlar ve diüretikler derin hipotansiyona yol açabilir.","Kardiyoloji"),
 Q("c01q3","ST elevasyonlu MI tanısı ve primer PKG kararı için aşağıdakilerden hangisi doğrudur?",["İlk troponin pozitifleşmeden karar verilmez","İki troponin arasındaki artış beklenir","EKG kriterleri ve klinik yeterlidir; troponin beklenmez","Ekokardiyografi zorunludur","BT anjiyografi ile diseksiyon dışlanmalıdır"],2,"STEMI'de reperfüzyon kararı EKG ve klinikle verilir; biyobelirteç beklemek miyokard kaybını artırır.","Kardiyoloji"),
 Q("c01q4","Göğüs ağrısıyla başvuran hastada ilk tıbbi temastan EKG'ye kadar hedef süre nedir?",["5 dakika","10 dakika","20 dakika","30 dakika","60 dakika"],1,"Kılavuzlar ilk temastan sonra en geç 10 dakika içinde 12 derivasyonlu EKG çekilmesini önerir.","Kardiyoloji")]

# 2 ── HİPOGLİSEMİ: inme taklidi, sülfonilüre + böbrek yetmezliği
S.append(case("c02","Konuşma bozukluğu — 74 yaşında kadın","Endokrin",
 "74 yaşında kadın. Kızı, sabah kahvaltıdan sonra konuşmasının bozulduğunu ve sağ elini kullanamadığını fark etmiş. Tip 2 diyabet (gliklazid), hipertansiyon ve kronik böbrek hastalığı var. Son normal görülme 45 dakika önce. Ambulans “kod inme” ön bildirimi yaptı.",
 {"n1":N("Acil kapısı","Hasta terli, huzursuz. Sağ kolda kuvvet 3/5, konuşması peltek ve anlamsız kelimeler var.","KB 168/90 · Nb 104 · SS 18 · SpO₂ %97 · Ateş 36,4",[
    T("Kapiller kan glukozu",3,1,"**38 mg/dL**","İnme kodunda trombolizden önce zorunlu tek laboratuvar testi glukozdur; hipoglisemi en sık inme taklitçilerindendir."),
    T("Kontrastsız beyin BT",-2,25,"Akut kanama veya erken iskemi bulgusu yok. 25 dakika geçti.","Glukoz bakılmadan BT'ye gitmek, en kolay düzeltilebilir nedeni atlamaktır."),
    T("Böbrek fonksiyon testleri",1,40,"Kreatinin 2,3 mg/dL (eGFR ≈ 21 mL/dk/1,73 m²). Son ayda yükselmiş.","Böbrek yetmezliğinde sülfonilüre birikir → uzamış ve tekrarlayan hipoglisemi."),
    A("IV %20 dekstroz 75–100 mL (≈15–20 g) ver; 10–15 dakika sonra glukozu tekrar ölç",4,5,"n2","Doğru. Bilinç değişikliği olan hastada IV glukoz; ağızdan verilmez."),
    A("Kod inme protokolü: doğrudan BT'ye götür, trombolize hazırlan",-3,25,"n3","Glukoz bakılmadan inme protokolünde ilerlemek hem zaman kaybı hem de gereksiz tromboliz riskidir."),
    A("Ağızdan şekerli su içir",-3,5,"n7","Bilinç ve yutma etkilenmişken ağızdan verilen sıvı aspirasyona yol açar."),
  ]),
  "n3":N("BT normal","BT'den döndünüz; tromboliz için ekip hazır. Hemşire “glukoz bakılmadı” diyor.","KB 170/92 · Nb 108",[
    T("Kapiller kan glukozu",2,1,"**34 mg/dL**","Hipoglisemi saptandı — neyse ki tromboliz başlamadan."),
    A("IV %20 dekstroz 75–100 mL, 10–15 dakika sonra kontrol",1,5,"n2","Doğru tedavi ama yaklaşık 30 dakika gecikmeyle."),
    A("Glukoza bakmadan alteplaz başla",-5,5,"n6","Hipoglisemi dışlanmadan tromboliz yapılmaz."),
  ]),
  "n2":N("Dekstrozdan 15 dakika sonra","Konuşma ve sağ kol tamamen düzeldi. Hasta “kahvaltıyı az yaptım, ilacımı içtim” diyor.","KB 150/84 · Nb 92 · Glukoz 146 mg/dL",[
    T("1 saat sonra glukoz kontrolü",2,60,"**58 mg/dL** — yeniden düşmüş.","Sülfonilüre hipoglisemisi saatlerce sürebilir; tek doz dekstroz yetmez."),
    A("Gözlem/yatış: %10 dekstroz infüzyonu, saatlik glukoz, en az 24 saat izlem; gliklazidi kes; tekrarlarsa oktreotid (ör. 50 mcg SC, 6–8 saatte bir) düşün",4,20,"n4","Doğru. Böbrek yetmezliği + sülfonilüre: uzamış hipoglisemi beklenir. Oktreotid insülin salınımını baskılar."),
    A("Düzeldi — bol şekerli besinle taburcu et",-4,10,"n5","Sülfonilüre etkisi sürerken taburculuk evde tekrarlayan ve daha ağır hipoglisemiye yol açar."),
    A("Glukagon 1 mg IM ile taburcu et",-3,10,"n5","Glukagon kısa etkilidir ve sülfonilüre hipoglisemisinde insülin salınımını artırarak tabloyu kötüleştirebilir; gözlem şarttır."),
  ]),
  "n4":E("İyi sonuç — dirençli hipoglisemi kontrol altında","Gece iki kez glukoz 60'ların altına indi; oktreotid sonrası stabil seyretti. 30. saatte taburcu edildi; gliklazid kesildi, böbrek fonksiyonuna uygun tedavi için endokrin kontrolü planlandı.\n\n**Akılda kalsın**\n- Her bilinç değişikliği ve **her kod inmede ilk iş glukoz**.\n- Hipoglisemi: <70 mg/dL (düzey 1), <54 mg/dL (düzey 2).\n- Bilinci değişik hastaya ağızdan verme; **IV dekstroz**, damar yolu yoksa glukagon 1 mg IM.\n- **Sülfonilüre + böbrek yetmezliği** → uzamış/tekrarlayan hipoglisemi: yatırarak izle, gerekirse oktreotid.\n\n*Kaynak: ADA Standards of Care 2025; JBDS hipoglisemi kılavuzu.*","good"),
  "n5":E("Evde tekrarlayan hipoglisemi","Hasta gece evde bilinçsiz bulundu; ambulansta glukoz 22 mg/dL, nöbet geçirdi. Yoğun bakıma yatırıldı.\n\nSülfonilüre hipoglisemisinde ilk düzelme yanıltıcıdır; ilaç etkisi böbrek yetmezliğinde 24 saati aşabilir.","bad"),
  "n6":E("Gereksiz tromboliz","Alteplaz infüzyonu sürerken ölçülen glukoz 30 mg/dL çıktı. Tablo bir inme taklitçisiydi; hasta trombolitiğin kanama riskine gereksiz yere maruz kaldı.\n\nHer kod inmede trombolizden önce glukoz ölçülür.","bad"),
  "n7":E("Aspirasyon","Hasta içerken öksürmeye başladı, SpO₂ %86'ya düştü; aspirasyon pnömonisi gelişti. Sonradan ölçülen glukoz 30 mg/dL çıktı.\n\nBilinç veya yutma bozukken ağızdan bir şey verilmez; tedavi IV dekstrozdur.","bad"),
 }))
Qs+= [Q("c02q1","Kod inme ile gelen hastada trombolizden önce mutlaka bakılması gereken tek laboratuvar değeri hangisidir?",["INR","Trombosit","Kan glukozu","Kreatinin","Troponin"],2,"Hipoglisemi inmeyi taklit eder ve hızla düzeltilebilir. Antikoagülan kullanımı veya kanama şüphesi yoksa INR/trombosit beklenmez.","Endokrin"),
 Q("c02q2","Böbrek yetmezliği olan ve sülfonilüre kullanan hastada dekstroza rağmen tekrarlayan hipoglisemide eklenecek ilaç hangisidir?",["Glukagon","Oktreotid","Hidrokortizon","Diazoksit tek başına","Tiamin"],1,"Oktreotid pankreastan insülin salınımını baskılar; sülfonilüre hipoglisemisinde dekstroz ihtiyacını azaltır.","Endokrin"),
 Q("c02q3","Bilinci kapalı, damar yolu açılamayan hipoglisemik erişkinde ilk seçenek hangisidir?",["Ağızdan şekerli içecek","Glukagon 1 mg IM","Oktreotid IV","Hidrokortizon IM","Rektal dekstroz"],1,"Glukagon 1 mg IM/SC (veya 3 mg intranazal) damar yolu yokken uygundur; ardından ağızdan karbonhidrat ve IV erişim sağlanır.","Endokrin"),
 Q("c02q4","Düzey 2 (klinik olarak anlamlı) hipoglisemi eşiği hangisidir?",["<80 mg/dL","<70 mg/dL","<54 mg/dL","<40 mg/dL","<30 mg/dL"],2,"ADA: <70 mg/dL düzey 1, <54 mg/dL düzey 2; düzey 3 başkasının yardımını gerektiren ağır tablo.","Endokrin")]

# 3 ── ANAFİLAKSİ
S.append(case("c03","IV antibiyotik sonrası kaşıntı — 24 yaşında kadın","Alerji / Resüsitasyon",
 "24 yaşında kadın, idrar yolu enfeksiyonu nedeniyle gözlem alanında IV seftriakson infüzyonu başlandı. 5 dakika sonra tüm vücutta kaşıntı, ses kısıklığı ve nefes darlığı başladı. Dudaklarında şişme var. Hemşire sizi çağırıyor.",
 {"n1":N("Gözlem alanı — dakika 0","Yaygın ürtiker, dudak ve dil ödemi. Ses kısık, konuşurken nefesi yetmiyor.","KB 82/50 · Nb 128 · SS 28 · SpO₂ %91",[
    T("Akciğer oskültasyonu",1,1,"Yaygın ekspiratuvar wheezing; hava girişi azalmamış.","Solunum ve dolaşım bulguları birlikte → anafilaksi."),
    T("Serum triptaz",0,5,"Örnek alındı (sonuç günler içinde).","Tanıyı sonradan desteklemek için yararlı; tedaviyi beklemez."),
    T("Akciğer grafisi",-1,20,"Normal.","Anafilakside tanı kliniktir; görüntüleme tedaviyi geciktirmemeli."),
    A("İnfüzyonu durdur; adrenalin 0,5 mg IM (1 mg/mL'den 0,5 mL) uyluk anterolateraline; yüksek akım O₂, yatırarak bacakları kaldır, IV kristaloid",4,2,"n2","Doğru. Anafilaksinin ilk ve en önemli ilacı IM adrenalindir; gecikmesi ölüm riskini artırır."),
    A("Feniramin + metilprednizolon IV ver; adrenalini düzelmezse düşün",-4,5,"n3","Antihistaminik ve steroid ne hava yolu ödemini ne de şoku hızla düzeltir; adrenalin gecikiyor."),
    A("Adrenalin 1 mg IV bolus (1 mg/mL'den)",-5,1,"n9","Dolaşımı olan hastaya 1 mg IV bolus adrenalin ciddi hipertansiyon, aritmi ve miyokard iskemisine yol açabilir. Arrest dozu arrest dışında verilmez."),
  ]),
  "n3":N("5 dakika sonra — kötüleşme","Stridor başladı, hasta oturmak istiyor, ajite.","KB 70/40 · Nb 140 · SS 32 · SpO₂ %87",[
    A("Hemen adrenalin 0,5 mg IM; hava yolu ekibini çağır, zor hava yolu hazırlığı; hızlı kristaloid",2,2,"n2","Geç ama doğru. Stridorda erken hava yolu hazırlığı hayat kurtarır."),
    A("İkinci doz antihistaminik ver",-4,5,"n9","Tablo antihistaminikle geri dönmez; adrenalin verilmediği sürece kardiyak arrest riski hızla artar."),
  ]),
  "n2":N("İlk adrenalinden 5 dakika sonra","Ürtiker azaldı, ses biraz açıldı ama wheezing sürüyor.","KB 88/54 · Nb 118 · SS 24 · SpO₂ %93",[
    A("Yanıt yetersiz: 5 dakika sonra ikinci IM adrenalin dozu; 500–1000 mL kristaloid bolus; wheezing için salbutamol nebül",3,5,"n4","Doğru. Yetersiz yanıtta IM adrenalin 5 dakikada bir tekrarlanır. İki doza yanıt yoksa (dirençli anafilaksi) IV adrenalin infüzyonu ve uzman desteği gerekir."),
    A("Kısmi düzelme yeterli — antihistaminik ekle ve bekle",-2,15,"n4","Hipotansiyon ve bronkospazm sürerken yeni doz adrenalin geciktirilmemeli; düzelme daha yavaş oldu."),
  ]),
  "n4":N("30 dakika sonra","Semptomlar tamamen geçti, hasta “eve gidebilir miyim?” diye soruyor. Toplam 2 doz adrenalin gerekti. Düzenli metoprolol kullanmıyor.","KB 112/70 · Nb 96 · SpO₂ %98",[
    A("Kendini iyi hissediyor — 1 saat sonra taburcu et",-3,60,"n8","Bifazik reaksiyon riski. Erken (2 saat) taburculuk yalnızca tek doza hızlı yanıt veren hastalar içindir; iki doz gerekmişse en az 6 saat gözlem."),
    A("Belirtiler geçtikten sonra en az 6 saat gözlem (2 doz adrenalin gerekti); taburculukta adrenalin oto-enjektörü reçetesi ve kullanım eğitimi, seftriakson alerjisini kayda geçir, alerji polikliniğine yönlendir",3,15,"n5","Doğru. Gözlem süresi reaksiyonun ağırlığına göre: tek doza hızlı yanıtta 2 saat sonra taburculuk düşünülebilir; 2 doz gerekmişse ≥6 saat; ikiden fazla doz, ağır astım ya da gece/ulaşım sorunu varsa ≥12 saat."),
  ]),
  "n5":E("İyi sonuç","Gözlemde bifazik reaksiyon olmadı. Hasta oto-enjektör, yazılı eylem planı ve alerji kartıyla taburcu edildi.\n\n**Akılda kalsın**\n- Anafilakside ilk ilaç **IM adrenalin**: erişkin 0,5 mg, çocuk 0,01 mg/kg (en çok 0,5 mg), uyluk anterolateral; yanıt yoksa **5 dakikada bir** tekrar.\n- Antihistaminik ve steroid **yardımcıdır**, adrenalinin yerine geçmez.\n- **1 mg IV bolus** yalnızca kardiyak arrestte.\n- Beta bloker kullanan dirençli hastada **glukagon** IV düşün.\n- Gözlem: tek doza hızlı yanıt → 2 saat; **2 doz → ≥6 saat**; >2 doz ya da ağır tablo → ≥12 saat.\n- Taburculukta **oto-enjektör + eğitim + alerji yönlendirmesi**.\n\n*Kaynak: Resuscitation Council UK 2021; NICE NG258; EAACI 2021.*","good"),
  "n8":E("Bifazik reaksiyon — evde","Taburculuktan 4 saat sonra hasta yeniden nefes darlığı ve ürtikerle ambulansla getirildi. Evde adrenalin yoktu.\n\nİki doz adrenalin gereken anafilakside en az 6 saat gözlem ve oto-enjektörle taburculuk gerekir.","mid"),
  "n9":E("Kardiyak arrest / ciddi aritmi","Hasta ventriküler taşikardiye girdi / dolaşım çöktü; resüsitasyon gerekti.\n\nAnafilakside doğru ilaç ve doğru yol: **adrenalin 0,5 mg IM**, gecikmeden ve gerekirse tekrar.","bad"),
 }))
Qs+= [Q("c03q1","Erişkin anafilakside ilk tercih edilen tedavi hangisidir?",["Feniramin 45 mg IV","Metilprednizolon 1 mg/kg IV","Adrenalin 0,5 mg IM (1 mg/mL)","Adrenalin 1 mg IV bolus","Salbutamol nebül"],2,"IM adrenalin anafilaksinin ilk basamak ilacıdır; yanıt yoksa 5 dakikada bir tekrarlanır.","Alerji / Resüsitasyon"),
 Q("c03q2","IM adrenalin için önerilen enjeksiyon yeri neresidir?",["Deltoid","Gluteal bölge","Uyluk anterolateral (vastus lateralis)","Karın derisi altı","Ön kol"],2,"Uyluk anterolaterali en hızlı ve güvenilir emilimi sağlar.","Alerji / Resüsitasyon"),
 Q("c03q3","Beta bloker kullanan ve adrenaline yanıt vermeyen anafilakside eklenebilecek ilaç hangisidir?",["Glukagon","Atropin","Vazopressin tek başına","Aminofilin","Kalsiyum glukonat"],0,"Glukagon beta reseptörden bağımsız olarak cAMP'yi artırır; beta blokerli dirençli olgularda önerilir.","Alerji / Resüsitasyon"),
 Q("c03q4","İki doz IM adrenalin gereken anafilaksi sonrası, belirtiler geçtikten sonra önerilen en kısa gözlem süresi hangisidir?",["1 saat","2 saat","4 saat","6 saat","24 saat"],3,"Resuscitation Council UK 2021: tek doza hızlı yanıtta 2 saat; iki doz gerekmişse en az 6 saat; ikiden fazla doz veya ağır tabloda en az 12 saat.","Alerji / Resüsitasyon")]

# 4 ── AKUT İNME (sağ MCA, büyük damar tıkanıklığı)
S.append(case("c04","Sol tarafında güçsüzlük — 66 yaşında erkek","Nöroloji",
 "66 yaşında erkek. Eşi saat 07:40'ta normal olduğunu, 08:10'da kahvaltıda sol kolunu kaldıramadığını ve ağzının kaydığını fark etmiş. Hipertansiyon ve hiperlipidemi var; antikoagülan kullanmıyor. Acile varış 08:35.",
 {"n1":N("Acil kapısı — 08:35","Sol yüz-kol-bacakta belirgin güçsüzlük, sağa bakış deviasyonu, sol tarafı ihmal ediyor. Bilinç açık.","KB 196/104 · Nb 88 (düzenli) · SpO₂ %96 · Glukoz (ambulans) 118 mg/dL",[
    T("NIHSS",1,3,"**NIHSS 15**: bakış deviasyonu, sol hemiparezi, sol hemihipoestezi, ihmal, dizartri.","Kortikal bulgular (bakış, ihmal) büyük damar tıkanıklığını düşündürür."),
    T("Kanama paneli (INR, aPTT, trombosit) — sonucu bekle",-2,40,"Normal. 40 dakika geçti.","Antikoagülan kullanmayan, kanama şüphesi olmayan hastada tromboliz için koagülasyon sonucu beklenmez."),
    A("Kod inme: doğrudan BT'ye — kontrastsız BT + BT anjiyografi; nöroloji ve girişimsel ekibi bilgilendir",4,15,"n2","Doğru. Kapıdan BT'ye ≤20–25 dk, kapıdan iğneye ≤60 dk (ideal ≤45) hedeflenir."),
    A("Nöroloji konsültasyonu iste, servise yatışını planla",-4,60,"n9","Zamana bağımlı tedavi penceresi kaçırılıyor. İnme şüphesi = acil görüntüleme."),
  ]),
  "n2":N("Görüntüleme — 08:52","**Kontrastsız BT:** kanama yok, ASPECTS 9.\n**BT anjiyografi:** sağ MCA M1 segmentinde tıkanıklık.\nSemptom başlangıcından (son normal 07:40) bu yana 1 saat 12 dakika.","KB 194/106 · Nb 86",[
    A("KB'yi ≤185/110'a indir (ör. labetalol 10–20 mg IV veya nikardipin infüzyonu — kurumunuzun protokolündeki ajan), ardından IV tromboliz başlat (alteplaz 0,9 mg/kg, en çok 90 mg; %10'u 1 dakikada bolus, kalanı 60 dakikada — ya da tenekteplaz 0,25 mg/kg tek bolus) ve trombektomi için girişimsel merkezi aktive et",4,15,"n3","Doğru. Uygun hastada IV tromboliz trombektomiyi beklemeden verilir; büyük damar tıkanıklığında ikisi birlikte planlanır."),
    A("KB 220/120'nin altında — antihipertansif vermeden tromboliz başla",-3,5,"n8","Tromboliz öncesi KB <185/110 olmalıdır; daha yüksek değerlerde intrakraniyal kanama riski artar."),
    A("BT normal, büyük olasılıkla TİA — MR için yatır",-4,90,"n9","Erken saatlerde BT çoğu iskemik inmede normaldir; BTA'da M1 tıkanıklığı var."),
  ]),
  "n3":N("Tromboliz sırasında — 09:15","Alteplaz infüzyonu sürüyor. Hasta trombektomi için anjiyografi ünitesine alınacak. Hemşire, infüzyonun 40. dakikasında KB'nin yükseldiğini bildiriyor.","KB 188/102 · Nb 84",[
    A("Tromboliz sırasında ve sonraki 24 saatte KB <180/105 hedefle; IV antihipertansifi titre et, 15 dakikada bir nörolojik muayene ve KB",3,5,"n4","Doğru. Tromboliz sonrası KB hedefi <180/105; yeni baş ağrısı, kusma veya nörolojik kötüleşmede infüzyonu durdur ve acil BT."),
    A("Hemen aspirin 300 mg ve DMAH başla",-3,5,"n8","Tromboliz sonrası ilk 24 saatte antitrombotik başlanmaz (kanama riski); 24. saat görüntülemesinden sonra karar verilir."),
  ]),
  "n4":E("İyi sonuç — rekanalizasyon","Trombektomi ile sağ M1 tam açıldı (TICI 3). 24. saat NIHSS 3; kontrol BT'de kanama yok.\n\n**Akılda kalsın**\n- Son normal görülme zamanını net öğren.\n- Kod inmede **glukoz** dışında laboratuvar beklenmez (antikoagülan/kanama şüphesi yoksa).\n- Tromboliz öncesi **KB <185/110**, sonraki 24 saat **<180/105**.\n- Alteplaz 0,9 mg/kg (en çok 90 mg, %10 bolus) ya da tenekteplaz 0,25 mg/kg.\n- **Büyük damar tıkanıklığında trombektomi** (seçilmiş hastalarda 24 saate kadar); tromboliz trombektomiyi geciktirmez.\n\n*Kaynak: AHA/ASA 2019 akut iskemik inme kılavuzu; ESO 2023 tromboliz kılavuzu.*","good"),
  "n8":E("İntrakraniyal kanama","Tromboliz sonrası 3. saatte bilinç bozuldu; BT'de sağ hemisferde parankimal hematom.\n\nTromboliz öncesi ve sonrası KB hedeflerine uymak ve ilk 24 saatte antitrombotik vermemek kanama riskini azaltır.","bad"),
  "n9":E("Tedavi penceresi kaçtı","Hasta serviste ertesi gün değerlendirildi; geniş sağ MCA infarktı, kalıcı sol hemipleji.\n\nİnme bir acil durumdur: görüntüleme ve reperfüzyon kararı dakikalar içinde verilmelidir.","bad"),
 }))
Qs+= [Q("c04q1","IV tromboliz öncesi kan basıncı hangi değerin altına indirilmelidir?",["220/120 mmHg","200/110 mmHg","185/110 mmHg","160/90 mmHg","140/90 mmHg"],2,"Tromboliz öncesi <185/110, tromboliz sırasında ve sonraki 24 saatte <180/105 mmHg hedeflenir.","Nöroloji"),
 Q("c04q2","Alteplazın akut iskemik inmede doğru dozu hangisidir?",["0,6 mg/kg, tamamı bolus","0,9 mg/kg (en çok 90 mg), %10'u bolus, kalanı 60 dakikada","1 mg/kg tek bolus","100 mg 2 saatte","0,25 mg/kg tek bolus"],1,"Alteplaz 0,9 mg/kg (en çok 90 mg): %10'u 1 dakikada bolus, kalanı 60 dakikada. 0,25 mg/kg tek bolus tenekteplaz dozudur.","Nöroloji"),
 Q("c04q3","Sağa bakış deviasyonu ve sol ihmal ile gelen hastada en olası tıkanıklık yeri hangisidir?",["Sol MCA","Sağ MCA (büyük damar)","Baziler arter","Sol PCA","Lakuner (küçük damar)"],1,"Kortikal bulgular (bakış deviasyonu, ihmal) büyük damar tıkanıklığını düşündürür; lezyon tarafına bakış (sağ hemisfer → sağa).","Nöroloji"),
 Q("c04q4","IV tromboliz yapılan hastada antitrombotik (aspirin vb.) ne zaman başlanır?",["Hemen, tromboliz ile birlikte","İnfüzyon biter bitmez","24. saat görüntülemesinde kanama yoksa","7. günde","Hiç başlanmaz"],2,"İlk 24 saatte antitrombotik verilmez; 24. saat kontrol görüntülemesinden sonra başlanır.","Nöroloji")]

# 5 ── ASTIM ATAĞI (ağır)
S.append(case("c05","Nefes darlığı — 28 yaşında kadın","Solunum",
 "28 yaşında kadın, astımlı. İki gündür nezle, dün geceden beri artan nefes darlığı. Evde salbutamol inhaleri saatte bir kullanmış, rahatlamamış. Düzenli kontrol ilacı yok.",
 {"n1":N("Resüsitasyon alanı","Öne eğilerek oturuyor, ancak kelime kelime konuşabiliyor. Yardımcı solunum kasları kullanılıyor; yaygın wheezing.","KB 132/80 · Nb 126 · SS 32 · SpO₂ %89 · Ateş 37,4",[
    T("PEF (zirve akım)",1,2,"Beklenenin **%35'i**.","PEF ≤%50 ağır atak; <%33 hayatı tehdit eden atak ölçütüdür."),
    T("Venöz/arteriyel kan gazı",2,10,"pH 7,37 · **pCO₂ 43 mmHg** · HCO₃ 24.","Ağır atakta hasta hiperventilasyon nedeniyle hipokapnik olmalıdır; **normal ya da yükselen pCO₂ yorulmanın ve yaklaşan solunum yetmezliğinin işaretidir**."),
    T("Akciğer grafisi",0,20,"Hiperinflasyon. Pnömotoraks veya konsolidasyon yok.","Rutin değildir; pnömotoraks, pnömoni şüphesi veya tedaviye yanıtsızlıkta istenir."),
    A("O₂ (hedef SpO₂ %93–95); salbutamol 5 mg + ipratropium 0,5 mg nebül (ilk saatte 20 dakikada bir ×3); sistemik kortikosteroid (prednizolon 40–50 mg PO ya da eşdeğeri IV)",4,5,"n2","Doğru. Ağır atakta kısa etkili beta agonist + ipratropium + erken sistemik steroid."),
    A("Çok anksiyöz — midazolam 2 mg IV ile sakinleştir",-5,5,"n9","Ağır astımda sedasyon solunum dürtüsünü baskılayıp arreste yol açabilir; entübasyon kararı dışında sedatif verilmez."),
    A("Yalnız O₂ ver, evde zaten salbutamol aldı; gözlemle",-3,30,"n3","Bronkodilatör ve steroid gecikirse tablo ilerler."),
  ]),
  "n3":N("30 dakika sonra — kötüleşme","Konuşamıyor, wheezing azaldı (sessiz göğüse doğru), uykuya meyilli.","Nb 138 · SS 34 · SpO₂ %86",[
    A("Hayatı tehdit eden atak: sürekli nebül salbutamol + ipratropium, sistemik steroid, MgSO₄ 2 g IV 20 dakikada; yoğun bakım ve hava yolu ekibini çağır",2,10,"n2","Doğru ama gecikmiş. Sessiz göğüs ve bilinç değişikliği hayatı tehdit eden atak bulgularıdır."),
    A("Sedatif ver, hasta yorgun",-5,5,"n9","Uykuya meyil hiperkapninin işaretidir; sedasyon arreste götürür."),
  ]),
  "n2":N("1 saat sonra","Üç doz nebül ve steroid verildi. Hasta cümle kurabiliyor ama wheezing sürüyor.","Nb 112 · SS 26 · SpO₂ %92 · PEF %45",[
    A("Yetersiz yanıt: MgSO₄ 2 g IV, 20 dakikada; nebülleri sürdür, yakın izlem",3,20,"n4","Doğru. İlk tedaviye yanıt vermeyen ağır atakta tek doz IV magnezyum önerilir."),
    A("Aminofilin yükleme dozu başla",-1,20,"n4","Aminofilin yan etkisi fazla, ek yararı sınırlı; rutin önerilmez. Hasta yine de düzeldi."),
    A("Düzeliyor — taburcu et",-3,10,"n8","PEF %45 ve SpO₂ %92 taburculuk için yetersiz."),
  ]),
  "n4":N("3 saat sonra","Hasta rahat, wheezing hafif.","Nb 96 · SS 18 · SpO₂ %96 · PEF %75",[
    A("Taburculuk: 5–7 gün oral prednizolon; inhaler tekniğini göster; inhaler kortikosteroid içeren kontrol tedavisi başla; yazılı eylem planı; 2–7 gün içinde kontrol",3,15,"n5","Doğru. Her atak, kontrol tedavisini başlatmak/artırmak için bir fırsattır."),
    A("Yalnız salbutamol inhaleri reçete edip taburcu et",-2,10,"n8","Yalnız kısa etkili beta agonist tedavisi atak ve ölüm riskini artırır; inhaler kortikosteroid şarttır."),
  ]),
  "n5":E("İyi sonuç","Hasta kontrol tedavisi ve eylem planıyla taburcu edildi; 1 hafta sonraki kontrolde PEF %90.\n\n**Akılda kalsın**\n- Ağır atak: kelime kelime konuşma, SS >30, Nb >120, SpO₂ <%90, PEF ≤%50.\n- Hayatı tehdit eden: **sessiz göğüs**, siyanoz, bilinç değişikliği, PEF <%33, **normal/yüksek pCO₂**.\n- Tedavi: O₂ (%93–95) + SABA + ipratropium + **erken sistemik steroid**; yanıtsızlıkta **MgSO₄ 2 g IV**.\n- Sedasyon yok.\n- Taburculukta **inhaler kortikosteroid** içeren kontrol tedavisi ve 5–7 gün oral steroid.\n\n*Kaynak: GINA 2024.*","good"),
  "n8":E("Erken dönüş","Hasta 18 saat sonra yeniden ağır atakla getirildi.\n\nYetersiz yanıtla taburculuk ve yalnız SABA reçetesi en sık geri dönüş nedenleridir.","mid"),
  "n9":E("Solunum arresti","Hasta apneik oldu; zor koşullarda entübe edildi, yoğun bakıma alındı.\n\nAğır astımda yorgunluk ve normal pCO₂ alarmdır; sedatif vermek solunumu durdurabilir.","bad"),
 }))
Qs+= [Q("c05q1","Ağır astım atağında kan gazında aşağıdakilerden hangisi en endişe verici bulgudur?",["pCO₂ 30 mmHg","pH 7,46","pCO₂ 44 mmHg","HCO₃ 22","pO₂ 75 mmHg"],2,"Ağır atakta beklenen hipokapnidir; normal veya yüksek pCO₂ solunum kaslarının yorulduğunu gösterir.","Solunum"),
 Q("c05q2","İlk tedaviye yanıt vermeyen ağır astım atağında önerilen magnezyum sülfat dozu hangisidir?",["1 g IV bolus","2 g IV, 20 dakikada","4 g IV, 5 dakikada","6 g IV infüzyon 24 saat","Magnezyum önerilmez"],1,"Tek doz 2 g IV MgSO₄ 20 dakikada; ağır, yanıtsız ataklarda hastaneye yatışı azaltır.","Solunum"),
 Q("c05q3","Hangisi hayatı tehdit eden astım atağının bulgusu değildir?",["Sessiz göğüs","Siyanoz","PEF <%33","Bilinç değişikliği","Cümle kurarak konuşabilme"],4,"Cümle kurabilmek hafif-orta atağı gösterir; diğerleri hayatı tehdit eden atak bulgularıdır.","Solunum"),
 Q("c05q4","Astım atağı sonrası taburculukta en önemli tedavi değişikliği hangisidir?",["Yalnız salbutamol reçetesi","İnhaler kortikosteroid içeren kontrol tedavisi başlamak","Uzun süreli oral steroid (3 ay)","Teofilin başlamak","Antibiyotik"],1,"GINA: yalnız SABA tedavisi önerilmez; her hastada inhaler kortikosteroid içeren tedavi olmalıdır.","Solunum")]

# 6 ── ATRİYAL FİBRİLASYON (hızlı ventrikül yanıtlı)
S.append(case("c06","Çarpıntı — 70 yaşında erkek","Kardiyoloji",
 "70 yaşında erkek. 6 saattir çarpıntı ve hafif nefes darlığı. Hipertansiyon için amlodipin kullanıyor; daha önce benzer yakınması olmamış. Göğüs ağrısı ve bayılma yok.",
 {"n1":N("Muayene odası","Hasta kooperatif, konuşabiliyor. Akciğerler temiz, periferik ödem yok.","KB 132/80 · Nb 148 (düzensiz) · SS 20 · SpO₂ %96",[
    T("12 derivasyonlu EKG",2,5,"**Atriyal fibrilasyon**, ventrikül hızı ≈150/dk, dar QRS. Delta dalgası yok. Akut iskemi bulgusu yok.","Düzensiz dar QRS taşikardi; geniş/çok değişken QRS olsaydı WPW düşünülmeliydi."),
    T("Yatak başı eko (POCUS)",1,5,"Sol ventrikül sistolik fonksiyonu korunmuş görünüyor; perikardiyal sıvı yok.","Hız kontrolü ilacını seçmek için ejeksiyon fraksiyonu önemli."),
    T("Elektrolitler, TSH, böbrek fonksiyonları",1,45,"K 3,6 · Mg 1,9 · TSH normal · Kreatinin 1,0.","Tetikleyicileri ve antikoagülan dozunu belirlemek için gerekli."),
    A("Hemodinamik olarak stabil: hız kontrolü — diltiazem 0,25 mg/kg IV 2 dakikada (EF korunmuş) ya da IV beta bloker; hedef istirahat hızı <110",3,20,"n2","Doğru. EF >%40'ta diltiazem/verapamil veya beta bloker; EF düşükse beta bloker ve/veya digoksin (diltiazem kaçınılır)."),
    A("Hemen senkronize elektriksel kardiyoversiyon",-2,30,"n3","Stabil hastada acil kardiyoversiyon gerekmez; sedasyon riskine girildi. Ayrıca antikoagülasyon kararı atlanmamalı."),
    A("Adenozin 6 mg hızlı IV",-2,5,"n3","Adenozin AF'yi sonlandırmaz; yalnızca birkaç saniyelik yavaşlama yapar. Düzensiz ritim AF'yi zaten düşündürüyor."),
  ]),
  "n3":N("Yeniden değerlendirme","Ritim hâlâ AF; hız 140'larda. Hasta stabil.","KB 128/78 · Nb 142",[
    A("Diltiazem 0,25 mg/kg IV ile hız kontrolü",2,20,"n2","Doğru — stabil AF'de ilk adım hız kontrolü."),
  ]),
  "n2":N("1 saat sonra","Hasta rahatladı.","KB 124/76 · Nb 92 (düzensiz) · SpO₂ %97",[
    T("Kanama riski değerlendirmesi",1,5,"Aktif kanama, anemi ve böbrek/karaciğer yetmezliği yok; düşme öyküsü yok.","Kanama risk faktörlerini düzeltmek önemlidir; tek başına antikoagülanı engellemez."),
    A("CHA₂DS₂-VA = 2 (hipertansiyon + yaş 65–74): kontrendikasyon yoksa doğrudan oral antikoagülan (DOAK) başla; oral hız kontrolü; kardiyoloji polikliniği takibi",3,15,"n4","Doğru. CHA₂DS₂-VA ≥2'de oral antikoagülan önerilir; DOAK'lar varfarine tercih edilir."),
    A("Antikoagülan gerekmez, aspirin 100 mg başla",-3,10,"n8","Aspirin AF'de inmeyi etkin önlemez, kanama riski yine vardır."),
    A("Hız düzeldi, ilaçsız taburcu et",-3,10,"n8","Hem hız kontrolü hem inme önlemi eksik kaldı."),
  ]),
  "n4":E("İyi sonuç","Hasta oral beta bloker ve DOAK ile taburcu edildi; kardiyoloji kontrolünde ritim/hız stratejisi planlandı.\n\n**Akılda kalsın**\n- **Instabilite** (hipotansiyon, şok, iskemi, akut kalp yetmezliği) varsa → **senkronize kardiyoversiyon**.\n- Stabilse önce **hız kontrolü**: EF >%40 diltiazem/verapamil veya beta bloker; EF düşükse beta bloker/digoksin.\n- **WPW'li AF**'de (geniş, düzensiz, çok hızlı QRS) AV nod blokerleri **kontrendike**.\n- Her AF'de inme riski: **CHA₂DS₂-VA** ≥2 → oral antikoagülan; aspirin alternatif değildir.\n\n*Kaynak: ESC 2024 Atriyal Fibrilasyon Kılavuzu.*","good"),
  "n8":E("3 ay sonra inme","Hasta 3 ay sonra sol MCA embolik inmeyle getirildi.\n\nAF'de antikoagülan endikasyonunu acil serviste başlatmak ya da kesinleştirmek, inmeyi önlemenin en etkili yoludur.","bad"),
 }))
Qs+= [Q("c06q1","ESC 2024'e göre CHA₂DS₂-VA skoru kaç ve üzerinde oral antikoagülan önerilir (I sınıf)?",["0","1","2","3","4"],2,"CHA₂DS₂-VA ≥2 → oral antikoagülan önerilir; 1 → düşünülmelidir. Yeni skor cinsiyeti içermez.","Kardiyoloji"),
 Q("c06q2","Hipotansif ve göğüs ağrılı hızlı AF'de ilk tedavi hangisidir?",["Diltiazem IV","Amiodaron oral","Senkronize elektriksel kardiyoversiyon","Digoksin IV","Adenozin"],2,"Hemodinamik instabilitede acil senkronize kardiyoversiyon yapılır.","Kardiyoloji"),
 Q("c06q3","Geniş ve düzensiz QRS'li, hızı 250/dk'ya ulaşan AF'de (WPW şüphesi) hangisi kontrendikedir?",["Elektriksel kardiyoversiyon","Prokainamid","Verapamil","İbutilid","Uzman konsültasyonu"],2,"Preeksitasyonlu AF'de AV nod blokerleri (verapamil, diltiazem, beta bloker, digoksin, adenozin) aksesuar yoldan iletimi artırıp VF'ye yol açabilir.","Kardiyoloji"),
 Q("c06q4","Ejeksiyon fraksiyonu %25 olan hızlı AF'li stabil hastada hangisinden kaçınılmalıdır?",["Beta bloker (dikkatli)","Digoksin","Diltiazem","Amiodaron","Antikoagülan"],2,"Diltiazem ve verapamil negatif inotroptur; düşük EF'de kaçınılır.","Kardiyoloji")]

# 7 ── SEPSİS / SEPTİK ŞOK (ürosepsis)
S.append(case("c07","Ateş ve konfüzyon — 78 yaşında kadın","Enfeksiyon",
 "78 yaşında kadın, huzurevinde kalıyor. Bakıcısı, iki gündür idrarının koktuğunu, bugün ateşlendiğini ve “saçmalamaya” başladığını söylüyor. Diyabet ve hipertansiyon var. Yaklaşık 60 kg.",
 {"n1":N("Resüsitasyon alanı","Konfüze, cildi sıcak; böğür hassasiyeti şüpheli.","KB 82/46 (OAB 58) · Nb 118 · SS 26 · SpO₂ %93 · Ateş 38,9",[
    T("Laktat (kan gazı)",2,5,"**Laktat 4,6 mmol/L**; pH 7,31.","Laktat ≥2 doku hipoperfüzyonunu, ≥4 yüksek mortaliteyi gösterir; tedaviye yanıtı izlemek için tekrarlanır."),
    T("Kan kültürü (2 set)",2,5,"Alındı; sonuç 24–48 saatte.","Antibiyotikten önce alınır — ama antibiyotiği geciktirmeden."),
    T("Tam idrar tetkiki",1,15,"Lökosit +++, nitrit +, bakteri bol.","Odak: üriner sistem."),
    T("Prokalsitonin sonucunu bekle",-2,60,"Yüksek. 1 saat geçti.","Septik şokta antibiyotik kararı için biyobelirteç beklenmez."),
    A("İlk saat paketi: 2 set kan kültürü; geniş spektrumlu antibiyotik (ör. piperasilin-tazobaktam; yerel direnç ve risk faktörlerine göre); 30 mL/kg (≈1800 mL) kristaloid (dengeli solüsyon tercih); laktatı tekrar ölç",4,15,"n2","Doğru. Şokta antibiyotik ilk 1 saat içinde; hipoperfüzyonda ilk 3 saatte en az 30 mL/kg kristaloid."),
    A("Kültür ve idrar sonucunu bekleyip hedefe yönelik antibiyotik başla",-4,120,"n9","Septik şokta antibiyotikte her saatlik gecikme mortaliteyi artırır."),
    A("Parasetamol ver, servise yatır",-4,60,"n9","Sepsis ve hipoperfüzyon bulguları atlanıyor."),
  ]),
  "n2":N("Sıvıdan sonra (≈1 saat)","1800 mL dengeli kristaloid ve antibiyotik verildi. Bilinç biraz düzeldi. Akciğerler temiz; POCUS'ta VCI dar değil, B çizgisi yok.","KB 86/48 (OAB 60) · Nb 110 · SpO₂ %94",[
    A("Norepinefrin başla (OAB ≥65 hedefi); santral kateteri beklemeden periferik geniş damar yolundan başlanabilir; arteriyel kateter planla",3,15,"n3","Doğru. Sıvıya rağmen hipotansiyon = septik şok; ilk vazopresör norepinefrin."),
    A("Bir 30 mL/kg sıvı daha ver",-2,60,"n4","Sıvıya yanıt ve tolerans değerlendirilmeden ek büyük hacim sıvı akciğer ödemine yol açabilir."),
    A("Dopamin infüzyonu başla",-1,15,"n3","Dopamin daha fazla aritmiyle ilişkili; norepinefrin önerilir."),
  ]),
  "n4":N("Ek sıvıdan sonra","Hasta takipneik, bazallerde raller.","KB 84/46 · SpO₂ %88 · SS 30",[
    A("Sıvıyı durdur, O₂ ver, norepinefrin başla",1,15,"n3","Doğru — vazopresör geciktirilmemeli."),
  ]),
  "n3":N("2. saat","Norepinefrin 0,1 mcg/kg/dk ile OAB 70.","KB 108/56 · Nb 98 · Laktat 2,6 mmol/L",[
    T("Böbrek ultrasonografisi",2,20,"**Sağ hidronefroz**, proksimal üreterde 9 mm taş.","Obstrüktif ürosepsis acil kaynak kontrolü gerektirir."),
    A("Kaynak kontrolü: acil üroloji/girişimsel radyoloji (nefrostomi/JJ stent); yoğun bakım yatışı; laktatı 2–4 saatte tekrar",3,20,"n5","Doğru. Antibiyotik tek başına tıkalı, enfekte sistemi temizleyemez."),
    A("Laktat düşüyor — servise yatır, antibiyotiğe devam",-2,20,"n8","Tıkalı enfekte böbrek drene edilmeden şok tekrarlar."),
  ]),
  "n5":E("İyi sonuç","Acil nefrostomi takıldı; 48 saatte vazopresör kesildi. Kan kültüründe E. coli üredi, antibiyotik daraltıldı.\n\n**Akılda kalsın**\n- Şok veya olası sepsiste **ilk 1 saatte antibiyotik**; önce kültür, ama gecikmeden.\n- Hipoperfüzyonda ilk 3 saatte **≥30 mL/kg kristaloid**, sonra yanıta göre.\n- Sıvıya rağmen hipotansiyon → **norepinefrin**, hedef **OAB ≥65**; periferik yoldan başlanabilir.\n- **Laktatı** tekrarla.\n- **Kaynak kontrolü** (tıkanıklık, apse, nekroz) unutulmaz.\n\n*Kaynak: Surviving Sepsis Campaign 2021.*","good"),
  "n8":E("Kötüleşme","Gece şok tekrarladı; hasta yoğun bakıma geç alındı, akut böbrek hasarı gelişti.\n\nObstrüktif enfeksiyonda drenaj, antibiyotik kadar acildir.","mid"),
  "n9":E("Refrakter septik şok","Antibiyotik 3 saat gecikti; hasta yüksek doz vazopresöre rağmen çoklu organ yetmezliğine girdi.\n\nSepsis zamana bağımlı bir acildir.","bad"),
 }))
Qs+= [Q("c07q1","Septik şokta ilk tercih edilen vazopresör hangisidir?",["Dopamin","Adrenalin","Norepinefrin","Fenilefrin","Dobutamin"],2,"Surviving Sepsis 2021: ilk seçenek norepinefrin; yetersizse vazopressin eklenir.","Enfeksiyon"),
 Q("c07q2","Septik şokta önerilen başlangıç ortalama arter basıncı hedefi hangisidir?",["≥55 mmHg","≥65 mmHg","≥75 mmHg","≥85 mmHg","Sistolik ≥120 mmHg"],1,"Başlangıç hedefi OAB ≥65 mmHg.","Enfeksiyon"),
 Q("c07q3","Septik şok olasılığı yüksek hastada antibiyotik ne zaman başlanmalıdır?",["Kültür sonucu geldiğinde","Prokalsitonin yüksekse","İlk 1 saat içinde","İlk 6 saat içinde","Yoğun bakıma yatınca"],2,"Şokta ve sepsis olasılığı yüksek hastada antibiyotik tanıdan sonra en geç 1 saat içinde verilir.","Enfeksiyon"),
 Q("c07q4","Sepsise bağlı hipoperfüzyonda ilk 3 saatte önerilen kristaloid miktarı en az ne kadardır?",["10 mL/kg","20 mL/kg","30 mL/kg","50 mL/kg","Sabit 4 litre"],2,"SSC 2021: en az 30 mL/kg kristaloid, sonrasında dinamik değerlendirmeye göre.","Enfeksiyon")]

# 8 ── PULMONER EMBOLİ (orta-yüksek risk → dekompanzasyon)
S.append(case("c08","Nefes darlığı ve bayılma — 46 yaşında kadın","Solunum / Kardiyoloji",
 "46 yaşında kadın. 3 hafta önce diz artroskopisi geçirmiş. Bugün merdiven çıkarken ani nefes darlığı ve kısa süreli bayılma. Oral kontraseptif kullanıyor.",
 {"n1":N("Resüsitasyon alanı","Taşipneik, anksiyöz. Sağ baldırda hafif şişlik.","KB 104/68 · Nb 122 · SS 28 · SpO₂ %89 · Ateş 37,1",[
    T("12 derivasyonlu EKG",1,5,"Sinüs taşikardisi; S1Q3T3; **V1–V4'te T negatifliği**.","Sağ ventrikül yüklenme bulguları; tanı koydurmaz ama destekler."),
    T("Yatak başı eko (POCUS)",2,5,"**Sağ ventrikül dilate** (RV/LV >1), septum düzleşmiş (D bulgusu); perikardiyal sıvı yok.","Sağ ventrikül disfonksiyonu risk sınıflaması için önemli."),
    T("D-dimer",-1,45,"Yüksek. 45 dakika geçti.","Klinik olasılık yüksekse D-dimer gereksizdir; doğrudan görüntüleme yapılır."),
    T("BT pulmoner anjiyografi",3,30,"**Bilateral ana pulmoner arterlerde trombüs**, RV/LV oranı 1,3.","Tanı doğrulandı."),
    T("Troponin",1,45,"Yüksek.","Sağ ventrikül disfonksiyonu + troponin yüksekliği → **orta-yüksek risk**."),
    A("Orta-yüksek risk PE: hemen antikoagülan — DMAH (ör. enoksaparin 1 mg/kg SC 12 saatte bir) ya da reperfüzyon gerekebileceği düşünülüyorsa anfraksiyone heparin infüzyonu; monitörlü izlem, dekompanzasyon planı",3,15,"n2","Doğru. Hemodinamik instabilite yoksa rutin tromboliz önerilmez; yakın izlem ve kurtarıcı reperfüzyon hazırlığı."),
    A("KB normal, ama RV dilate — hemen sistemik tromboliz",-2,15,"n7","Normotansif orta-yüksek riskte rutin tam doz tromboliz, kanama riskini artırırken mortaliteyi anlamlı azaltmaz."),
    A("Bacakta ödem var — furosemid 40 mg IV",-4,5,"n9","Sağ ventrikül yetmezliğinde diüretik önyükü düşürüp şoku başlatır."),
  ]),
  "n2":N("2 saat sonra — dekompanzasyon","Hasta solgun, bilinci bulanık. Heparin infüzyonu sürüyor.","KB 76/48 · Nb 138 · SpO₂ %84",[
    A("Yüksek riskli PE: kurtarıcı sistemik tromboliz — alteplaz 100 mg 2 saatte (arrest/periarrestte 0,6 mg/kg 15 dakikada); heparin infüzyonunu durdur, sonra yeniden başla; gerekirse norepinefrin; kontrendikasyon varsa cerrahi/kateter tedavisi",4,10,"n4","Doğru. Hemodinamik instabilitede reperfüzyon tedavisi endikedir."),
    A("Hipotansiyon için hızla 2 L kristaloid",-3,30,"n9","Aşırı sıvı dilate sağ ventrikülü daha da genişletip septumu sola iterek debiyi düşürür; en çok küçük (≤500 mL) dikkatli bolus."),
    A("Yalnız norepinefrin başla, heparinle beklemeye devam et",-1,30,"n6","Vazopresör köprüdür; yüksek riskli PE'de reperfüzyon geciktirilmemeli."),
  ]),
  "n4":E("İyi sonuç","Trombolizden 1 saat sonra KB 112/70, SpO₂ %94. Yoğun bakımda izlendi; 2. gün DMAH'a, ardından DOAK'a geçildi.\n\n**Akılda kalsın**\n- Klinik olasılık yüksekse **D-dimer yerine doğrudan BTPA**; stabil değilse yatak başı eko.\n- Risk: **yüksek** (hemodinamik instabilite) → reperfüzyon; **orta-yüksek** (RV disfonksiyonu + troponin) → antikoagülan + yakın izlem + kurtarıcı tromboliz hazırlığı.\n- Alteplaz **100 mg 2 saatte**.\n- Sağ ventrikül yetmezliğinde **büyük hacim sıvı ve diüretikten kaçın**; norepinefrin.\n\n*Kaynak: ESC 2019 Pulmoner Emboli Kılavuzu.*","good"),
  "n6":E("Gecikmiş reperfüzyon","Vazopresör dozu giderek arttı; tromboliz ancak 1,5 saat sonra yapılabildi. Hasta uzun süre yoğun bakımda kaldı.\n\nYüksek riskli PE'de vazopresör yalnızca köprüdür; reperfüzyon geciktirilmez.","mid"),
  "n7":E("Majör kanama","Normotansif hastaya verilen tam doz trombolitik sonrası retroperitoneal kanama gelişti; transfüzyon gerekti.\n\nOrta-yüksek riskte rutin tromboliz önerilmez; antikoagülan + yakın izlem, dekompanzasyonda kurtarıcı tromboliz.","mid"),
  "n9":E("Obstrüktif şok — arrest","Hasta nabızsız elektriksel aktiviteye girdi.\n\nSağ ventrikül yetmezliğinde önyükü bozan girişimler (diüretik, aşırı sıvı) tabloyu hızla kötüleştirir.","bad"),
 }))
Qs+= [Q("c08q1","Yüksek riskli pulmoner embolinin tanımlayıcı özelliği hangisidir?",["D-dimer >5000","Troponin yüksekliği","Hemodinamik instabilite (şok, kalıcı hipotansiyon, arrest)","Bilateral trombüs","SpO₂ <%90"],2,"ESC 2019: yüksek risk = hemodinamik instabilite. RV disfonksiyonu + troponin orta-yüksek risktir.","Solunum / Kardiyoloji"),
 Q("c08q2","Yüksek riskli PE'de standart alteplaz rejimi hangisidir?",["0,9 mg/kg, %10 bolus","100 mg, 2 saatte","50 mg bolus","0,25 mg/kg bolus","10 mg, 1 saatte"],1,"PE'de alteplaz 100 mg 2 saatte; arrestte 0,6 mg/kg (en çok 50 mg) 15 dakikada.","Solunum / Kardiyoloji"),
 Q("c08q3","Klinik olasılığı yüksek PE şüphesinde doğru yaklaşım hangisidir?",["Önce D-dimer","Doğrudan BT pulmoner anjiyografi","Önce akciğer grafisi","Önce alt ekstremite doppler zorunlu","24 saat gözlem"],1,"Yüksek olasılıkta D-dimer tanıyı dışlayamaz; doğrudan görüntüleme yapılır.","Solunum / Kardiyoloji"),
 Q("c08q4","PE'ye bağlı sağ ventrikül yetmezliği ve hipotansiyonda hangisi zararlıdır?",["Norepinefrin","Dikkatli ≤500 mL sıvı","Agresif çok litrelik sıvı yüklemesi","Reperfüzyon tedavisi","Oksijen"],2,"Aşırı volüm sağ ventrikülü genişletip sol ventrikül dolumunu bozar.","Solunum / Kardiyoloji")]

# 9 ── HİPERKALEMİ (diyaliz hastası)
S.append(case("c09","Halsizlik — 64 yaşında diyaliz hastası","Nefroloji / Metabolik",
 "64 yaşında erkek, haftada 3 gün hemodiyalize giriyor; son seansı kaçırmış (4 gün önce). Bugün halsizlik ve bacaklarda uyuşma. Anürik.",
 {"n1":N("Muayene odası","Halsiz, uyanık. Akciğer bazallerinde hafif raller.","KB 148/86 · Nb 46 · SS 20 · SpO₂ %95",[
    T("12 derivasyonlu EKG",3,5,"Bradikardi 46/dk, **sivri T dalgaları**, P dalgası basık, PR uzun, **QRS 148 ms**.","Hiperkalemide QRS genişlemesi ileri evre bulgusudur; sinüzoidal dalga ve arrest yakın olabilir."),
    T("Kan gazı (hızlı K)",2,5,"**K 7,8 mmol/L**, pH 7,24, HCO₃ 15.","Kan gazı potasyumu dakikalar içinde verir; biyokimya beklenmez."),
    T("Biyokimya sonucunu bekle",-3,50,"K 7,6. 50 dakika geçti.","EKG değişikliği olan hastada tedavi laboratuvarı beklemez."),
    A("Miyokardı koru: %10 kalsiyum glukonat 30 mL IV, 5–10 dakikada (ya da %10 kalsiyum klorür 10 mL, santral/geniş ven); monitör",4,10,"n2","Doğru. EKG değişikliğinde ilk adım kalsiyum; etkisi dakikalar içinde başlar ama potasyumu düşürmez."),
    A("Furosemid 80 mg IV",-3,10,"n3","Anürik diyaliz hastasında diüretik işe yaramaz; zaman kaybedildi."),
    A("Sodyum polistiren sülfonat (Kayexalate) oral ver, servise yatır",-4,30,"n9","Reçineler saatler içinde etki eder; EKG değişikliği olan hiperkalemide acil tedavi değildir."),
  ]),
  "n3":N("15 dakika sonra","Monitörde QRS daha da genişledi.","Nb 40 · KB 132/80",[
    A("Hemen %10 kalsiyum glukonat 30 mL IV",2,10,"n2","Doğru — gecikmeli."),
  ]),
  "n2":N("Kalsiyumdan sonra","QRS 112 ms'ye daraldı, hız 58/dk.","KB 150/84 · Nb 58 · Kapiller glukoz 98 mg/dL",[
    A("Potasyumu hücre içine al: 10 Ü kısa etkili insülin + 25 g glukoz (ör. %50 dekstroz 50 mL ya da %20 dekstroz 125 mL) 15 dakikada; salbutamol 10–20 mg nebül; glukoz <126 mg/dL olduğu için ardından %10 dekstroz infüzyonu; acil diyaliz için nefroloji",4,15,"n4","Doğru. İnsülin-glukoz 15–30 dakikada K'yı ≈0,6–1,2 mmol/L düşürür; kalıcı çözüm diyaliz."),
    A("Kalsiyum yeterli oldu — biyokimya tekrarını bekle",-4,60,"n9","Kalsiyum potasyumu düşürmez; etkisi 30–60 dakikada geçer."),
  ]),
  "n4":N("1 saat sonra","Hasta diyaliz için hazırlanıyor. Terliyor, “içim titriyor” diyor.","K 6,3 · Nb 70",[
    T("Kapiller glukoz",2,1,"**52 mg/dL**","İnsülin-glukoz tedavisinden sonraki saatlerde hipoglisemi sıktır (özellikle böbrek yetmezliğinde)."),
    A("Hipoglisemiyi düzelt (IV dekstroz), saatlik glukoz takibine (en az 6 saat) devam; acil hemodiyalize al",3,10,"n5","Doğru."),
    A("K düştü, diyalizi ertesi güne planla, taburcu et",-4,10,"n9","Hücre içine kayan potasyum birkaç saatte geri çıkar; anürik hastada kalıcı tedavi diyalizdir."),
  ]),
  "n5":E("İyi sonuç","Acil hemodiyaliz sonrası K 4,6; EKG normale döndü.\n\n**Akılda kalsın**\n- EKG değişikliği varsa **önce kalsiyum** (%10 kalsiyum glukonat 30 mL IV); EKG düzelmezse 5–10 dakikada tekrar.\n- Potasyumu hücre içine: **10 Ü insülin + 25 g glukoz** ve **salbutamol 10–20 mg** nebül.\n- **Hipoglisemi** riskine karşı en az 6 saat glukoz takibi.\n- Uzaklaştırma: **diyaliz** (anürikte tek etkili yol); potasyum bağlayıcılar yavaştır.\n- Kalsiyum potasyumu düşürmez.\n\n*Kaynak: UK Kidney Association 2023 hiperkalemi kılavuzu.*","good"),
  "n9":E("Kardiyak arrest","Hasta sinüzoidal ritimden asistoliye girdi; resüsitasyon sırasında kalsiyum ve acil diyaliz gerekti.\n\nHiperkalemide EKG değişikliği acil durumdur; laboratuvar sonucu veya yavaş etkili tedavi beklenmez.","bad"),
 }))
Qs+= [Q("c09q1","K 7,6 mmol/L ve QRS genişlemesi olan hastada ilk yapılacak tedavi hangisidir?",["İnsülin + glukoz","Salbutamol nebül","%10 kalsiyum glukonat IV","Sodyum bikarbonat","Furosemid"],2,"Kalsiyum membranı stabilize eder; EKG değişikliğinde ilk adımdır.","Nefroloji / Metabolik"),
 Q("c09q2","Hiperkalemide insülin-glukoz tedavisinin standart dozu hangisidir?",["5 Ü insülin + 10 g glukoz","10 Ü kısa etkili insülin + 25 g glukoz","0,1 Ü/kg/saat infüzyon","20 Ü insülin + 50 g glukoz","Yalnız 25 g glukoz"],1,"10 Ü kısa etkili insülin + 25 g glukoz 15 dakikada; glukoz düşükse ek dekstroz infüzyonu.","Nefroloji / Metabolik"),
 Q("c09q3","Kalsiyum glukonatın hiperkalemideki etkisi için doğru ifade hangisidir?",["Potasyumu hücre içine sokar","Böbrekten potasyum atılımını artırır","Serum potasyumunu düşürmez, kalbi korur","Bağırsaktan potasyumu bağlar","Etkisi 24 saat sürer"],2,"Kalsiyum yalnız miyokardı korur; etkisi 30–60 dakikadır. Potasyum düşürücü tedavi ayrıca verilmelidir.","Nefroloji / Metabolik"),
 Q("c09q4","İnsülin-glukoz tedavisinden sonra en sık görülen komplikasyon hangisidir?",["Hipokalsemi","Hipoglisemi","Hipernatremi","Ventriküler fibrilasyon","Akciğer ödemi"],1,"Özellikle böbrek yetmezliğinde insülin etkisi uzar; en az 6 saat glukoz izlenir.","Nefroloji / Metabolik")]

# 10 ── DİYABETİK KETOASİDOZ
S.append(case("c10","Kusma ve karın ağrısı — 19 yaşında kadın","Endokrin",
 "19 yaşında kadın, tip 1 diyabet. İki gündür kusma ve karın ağrısı; kusunca insülinini “yemek yemediği için” yapmamış. Yaklaşık 55 kg.",
 {"n1":N("Resüsitasyon alanı","Dehidrate, derin ve hızlı solunum (Kussmaul), nefeste aseton kokusu. Karında yaygın hassasiyet, defans yok.","KB 96/58 · Nb 124 · SS 30 · SpO₂ %99 · Glukoz 486 mg/dL",[
    T("Venöz kan gazı",3,5,"**pH 7,08** · HCO₃ 7 · pCO₂ 21 · Na 131 · Cl 98 · **K 5,6** · anyon açığı 26.","Ağır DKA. K yüksek görünse de vücut total potasyumu azalmıştır; insülinle hızla düşer."),
    T("Kapiller keton (β-hidroksibütirat)",2,2,"**5,8 mmol/L**","Ketonemi ≥3 mmol/L DKA ile uyumlu; tedavi yanıtını izlemede en iyi gösterge."),
    T("Karın BT",-2,40,"Akut patoloji yok. 40 dakika geçti.","DKA'da karın ağrısı sıktır ve asidoz düzeldikçe geçer; tetikleyici şüphesi yoksa rutin görüntüleme gerekmez."),
    T("Hemogram, böbrek fonksiyonu, idrar tetkiki, gebelik testi",1,30,"Lökositoz 14.000 (DKA'da beklenebilir); kreatinin 1,3; idrarda enfeksiyon yok; gebelik testi negatif.","Tetikleyici ara: enfeksiyon, gebelik, ilaç uyumsuzluğu."),
    A("Önce sıvı: ilk saatte 1000 mL %0,9 NaCl ya da dengeli kristaloid (sonra 500–1000 mL/saat, duruma göre); K sonucunu kontrol et; saatlik izlem planı",4,10,"n2","Doğru. DKA tedavisinin ilk ve en önemli adımı sıvı; insülin öncesi potasyum mutlaka bilinmeli."),
    A("Hemen 10 Ü IV bolus insülin ve yüksek doz infüzyon; sıvıyı sonra ver",-2,10,"n2","Yeterli sıvı olmadan insülin, dolaşımdaki sıvıyı hücre içine kaydırıp hipotansiyonu derinleştirebilir; bolus zorunlu değildir."),
    A("pH 7,08 — 100 mEq sodyum bikarbonat IV",-3,10,"n2","Bikarbonat yalnızca pH <7,0'da düşünülür; hipokalemi ve paradoks BOS asidozu riski."),
  ]),
  "n2":N("Sıvının ilk saati","1 L kristaloid verildi.","KB 104/64 · Nb 112 · K 5,6 mmol/L · Glukoz 430 mg/dL",[
    A("Sabit hızlı IV insülin infüzyonu 0,1 Ü/kg/saat (≈5,5 Ü/saat); K >5,0 olduğundan şimdilik KCl ekleme, 1–2 saatte bir K bak; K 3,5–5,0 olunca her litre sıvıya 20–40 mEq KCl",3,10,"n3","Doğru. K <3,5 ise insülin ertelenir ve önce potasyum verilir."),
    A("K yüksek, insülin hiperkalemiyi düzeltir — potasyum takibine gerek yok",-3,10,"n8","İnsülin ve sıvıyla potasyum hızla düşer; takipsiz kalınca ölümcül hipokalemi gelişebilir."),
  ]),
  "n3":N("4. saat","Kusma durdu, hasta daha iyi.","Glukoz 238 mg/dL · pH 7,19 · HCO₃ 11 · Keton 3,1 mmol/L · K 3,9",[
    A("Glukoz <250 mg/dL: insülin infüzyonunu sürdür ve %5–10 dekstroz ekle; KCl'yi sürdür; ketoz düzelene kadar (keton <0,6 mmol/L ve pH ≥7,3 ya da HCO₃ ≥18) infüzyonu kesme",4,10,"n4","Doğru. DKA'nın tedavi hedefi glukoz değil, ketoasidozun düzelmesidir."),
    A("Glukoz düştü — insülin infüzyonunu kes",-4,10,"n8","Asidoz sürerken insülini kesmek ketogenezi yeniden başlatır."),
  ]),
  "n4":N("12. saat","Hasta yemek yemek istiyor.","Glukoz 168 · pH 7,34 · HCO₃ 19 · Keton 0,4 · K 4,2",[
    A("Ketoasidoz düzeldi: yemekten önce subkutan bazal-bolus insülin yap, IV insülini SC dozdan 1–2 saat sonra kes; diyabet eğitimi (hasta gün kuralları)",3,10,"n5","Doğru. IV insülin, SC insülin etkisi başlamadan kesilirse DKA tekrarlar."),
    A("IV insülini hemen kes, SC insülini akşam başla",-3,10,"n8","Arada kalan insülinsiz dönem ketoasidozu yeniden başlatır."),
  ]),
  "n5":E("İyi sonuç","Hasta 2. gün taburcu edildi. “Hasta gün kuralları” anlatıldı: kusma/yemek yememe durumunda bazal insülin kesilmez, sık glukoz-keton takibi yapılır.\n\n**Akılda kalsın**\n- Önce **sıvı**; insülinden önce **K** bilinmeli (K <3,5 → önce K).\n- **0,1 Ü/kg/saat** sabit insülin infüzyonu.\n- Glukoz <250 mg/dL → **dekstroz ekle, insülini kesme**.\n- Bikarbonat yalnız **pH <7,0**.\n- Düzelme: **keton <0,6 mmol/L ve pH ≥7,3** (veya HCO₃ ≥18).\n- SC insülini yapıp **1–2 saat sonra** IV'yi kes.\n\n*Kaynak: ADA/EASD/JBDS 2024 hiperglisemik kriz uzlaşı raporu.*","good"),
  "n8":E("Komplikasyon","Potasyum takibi yapılmadığında ciddi hipokalemi ve aritmi; insülin erken kesildiğinde DKA'nın yeniden alevlenmesi gelişti. Hasta yoğun bakıma yatırıldı.\n\nDKA tedavisinde potasyum, dekstroz ve insülin geçişi saat saat yönetilir.","bad"),
 }))
Qs+= [Q("c10q1","DKA'da insülin infüzyonuna başlamadan önce serum potasyumu en az ne olmalıdır?",["2,5 mmol/L","3,0 mmol/L","3,5 mmol/L","4,5 mmol/L","5,5 mmol/L"],2,"K <3,5 ise insülin ertelenir ve önce potasyum verilir.","Endokrin"),
 Q("c10q2","DKA'da önerilen sabit hızlı insülin infüzyon dozu hangisidir?",["0,01 Ü/kg/saat","0,05 Ü/kg/saat","0,1 Ü/kg/saat","0,5 Ü/kg/saat","1 Ü/kg/saat"],2,"0,1 Ü/kg/saat; başlangıç bolusu zorunlu değildir.","Endokrin"),
 Q("c10q3","DKA'da sodyum bikarbonat hangi durumda düşünülür?",["pH <7,3","pH <7,2","pH <7,0","HCO₃ <15","Her hastada"],2,"Bikarbonat yalnız pH <7,0'da düşünülür.","Endokrin"),
 Q("c10q4","DKA tedavisinde glukoz 250 mg/dL'nin altına indiğinde ne yapılır?",["İnsülin kesilir","İnsülin yarıya indirilir ve sıvı kesilir","İnsülin sürdürülür, dekstroz eklenir","SC insüline geçilir","Bikarbonat başlanır"],2,"Hedef ketoasidozun düzelmesidir; hipoglisemiyi önlemek için dekstroz eklenip insülin sürdürülür.","Endokrin")]

P={"id":"ilk-nobet-1","title":"İlk Nöbet Vakaları — 1. Paket","desc":"Sık ve hayatı tehdit eden 10 acil: göğüs ağrısı (STEMI), hipoglisemi, anafilaksi, inme, astım, AF, sepsis, pulmoner emboli, hiperkalemi, DKA. Her biri dallanan sanal hasta + 4 alıştırma sorusu.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 1. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 1. Paket","topic":"Temel acil","order":1,"req":[1],
     "desc":"İlk nöbetlerinizde mutlaka karşılaşacağınız 10 hayatı tehdit eden tablo. Her vakada hasta gelir; siz tetkik ister, karar verirsiniz. Amaç tanı koymaktan önce **ölümcül nedeni kaçırmamak** ve **ilk 5 dakikayı** doğru yönetmektir.",
     "intro":"- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Vakaların sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."}}
out=sys.argv[1]
from ilk_degerlendirme import apply as _ilk
for c in S: _ilk(c)
json.dump(P,open(out,"w"),ensure_ascii=False,indent=1)
# yapı denetimi
for c in S:
    ns=c["nodes"]
    for k,n in ns.items():
        for o in n["opts"]:
            if o["kind"]=="act": assert o["to"] in ns,(c["key"],k,o["label"])
        if not n.get("end"): assert any(o["kind"]=="act" for o in n["opts"]),(c["key"],k)
    reach=set(); st=["n1"]
    while st:
        x=st.pop()
        if x in reach: continue
        reach.add(x); st+= [o["to"] for o in ns[x]["opts"] if o["kind"]=="act"]
    assert reach==set(ns),(c["key"],set(ns)-reach)
for q in Qs: assert len(q["options"])==5 and 0<=q["correct"]<5
print(len(S),"vaka",len(Qs),"soru")
