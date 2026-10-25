import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Önce **ilk değerlendirme** (muayene, monitör, damar yolu, oksijen) — gereksiz girişim puan kaybettirir.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 121 DERİN VEN TROMBOZU
S.append(case("c121","Baldırda şişlik — 52 yaşında kadın","Vasküler / Hematoloji",
 "52 yaşında kadın. 10 gün önce diz artroskopisi geçirmiş. 3 gündür sol baldırda ağrı ve şişlik. Nefes darlığı ve göğüs ağrısı yok. Böbrek fonksiyonu bilinen normal, 72 kg.",
 {"n1":N("Muayene","Sol baldır çevresi sağdan 4 cm fazla, **gode bırakan ödem** ve derin ven trasesi boyunca hassasiyet. Akciğer muayenesi normal.","KB 128/78 · Nb 84 · SS 16 · SpO₂ %98 · Ateş 36,9",[
   T("Wells DVT skoru",2,2,"Yakın cerrahi (+1), baldır farkı >3 cm (+1), gode ödem (+1), ven trasesinde hassasiyet (+1) = **4 → DVT olası**.","Olası DVT'de doğrudan görüntüleme."),
   T("Proksimal bacak venöz USG (kompresyon)",3,60,"**Sol popliteal ve femoral vende basılmayan trombüs**.","Tanı."),
   T("D-dimer",0,60,"Yüksek.","Olası DVT'de D-dimer görüntülemeyi değiştirmez; olası olmayan grupta dışlama için kullanılır."),
   A("Proksimal DVT: **DOAK** ile tedavi — ör. rivaroksaban 15 mg günde 2 kez 21 gün, sonra 20 mg/gün (ya da apiksaban 10 mg × 2, 7 gün → 5 mg × 2); provoke DVT → en az 3 ay; komplikasyon yoksa **ayaktan tedavi**; PE uyarıları",4,15,"n2","Doğru. Uygun hastada ayaktan DOAK tedavisi standarttır."),
   A("Görüntüleme 24 saat sonra; o zamana kadar tedavi yok",-3,10,"n9","Görüntüleme 4 saatte yapılamıyorsa **ara antikoagülasyon** başlanır."),
   A("Rutin vena kava filtresi",-3,60,"n9","Filtre yalnız antikoagülasyon kontrendike ise."),
 ]),
 "n2":E("Ayaktan tedavi","Hasta DOAK ile ayaktan izlendi; 3 ay sonra tedavi kesildi.\n\n**Akılda kalsın**\n- **Wells ≥2**: olası → **proksimal USG** (4 saat içinde; değilse ara antikoagülan); **<2**: D-dimer, negatifse DVT dışlanır.\n- Tedavi: **DOAK** (rivaroksaban/apiksaban yükleme dozlarıyla), gebelik/aktif kanser/ağır böbrek yetmezliğinde DMAH.\n- Provoke DVT **3 ay**; provoke edilmemişte uzun süre düşünülür.\n- Ayaktan tedavi kontrendikasyonları: masif DVT/flegmazi, yüksek kanama riski, PE ile instabilite.\n\n*Kaynak: NICE NG158 (2023); ASH 2020 VTE kılavuzu.*","good"),
 "n9":E("Pulmoner emboli","İki gün sonra ani nefes darlığıyla döndü; pulmoner emboli saptandı.","bad"),
}))
Qs+=[Q("c121q1","Wells skoru ≥2 olan hastada ilk adım hangisidir?",["D-dimer ile dışlama","Proksimal bacak venöz USG","BT anjiyo","Tedavisiz taburcu","Venografi"],1,"Olası DVT'de görüntüleme.","Vasküler / Hematoloji"),
 Q("c121q2","Rivaroksabanın DVT tedavisinde başlangıç rejimi hangisidir?",["20 mg/gün","15 mg günde 2 kez, 21 gün","10 mg/gün","5 mg günde 2 kez","2,5 mg günde 2 kez"],1,"Sonra 20 mg/gün.","Vasküler / Hematoloji"),
 Q("c121q3","Provoke DVT'de antikoagülasyon süresi en az ne kadardır?",["2 hafta","1 ay","3 ay","Ömür boyu","1 hafta"],2,"Geçici risk faktörü ortadan kalktıysa.","Vasküler / Hematoloji")]

# 122 PULMONER EMBOLİ — yüksek risk (masif)
S.append(case("c122","Bayılma ve hipotansiyon — 61 yaşında kadın","Göğüs / Kardiyoloji",
 "61 yaşında kadın. 2 hafta önce kalça protezi ameliyatı; tromboprofilaksiyi taburculukta bırakmış. Tuvalette ani nefes darlığı ve bayılma; ambulansla geldi.",
 {"n1":N("Muayene","Bilinç bulanık, siyanotik, soğuk ve terli. Boyun venleri dolgun. Akciğerler temiz.","KB 72/44 · Nb 132 · SS 34 · SpO₂ %84",[
   T("Yatak başı eko (POCUS)",3,5,"**Sağ ventrikül belirgin dilate** (RV/LV >1), septum düzleşmiş (D işareti), McConnell bulgusu; sol ventrikül küçük ve hiperdinamik. Perikardiyal sıvı yok.","Instabil hastada BT'ye gitmeden tanıyı destekler."),
   T("Bacak venöz USG",2,5,"Sağ femoral vende trombüs.","Tanıyı destekler."),
   T("BT pulmoner anjiyografi",-3,40,"Bilateral ana pulmoner arter trombüsü; hasta BT masasında peri-arrest.","Instabil hastayı BT'ye götürmek risklidir; POCUS yeterli destek sağlar."),
   A("**Yüksek riskli PE (şok)**: **sistemik tromboliz** — alteplaz 100 mg IV 2 saatte (ilk 10 mg bolus; ya da kurum protokolü); **anfraksiyone heparin**; dikkatli sıvı (≤500 mL), **norepinefrin**; O₂, entübasyondan mümkünse kaçın (hipotansiyon); trombolize kontrendikasyon varsa cerrahi embolektomi/kateter tedavisi/ECMO",4,10,"n2","Doğru. ESC 2019: yüksek riskli PE'de reperfüzyon tedavisi."),
   A("Agresif sıvı yüklemesi (3 L) ve heparin",-3,30,"n9","Aşırı sıvı RV'yi daha da genişletir, septal kayma ile LV dolumunu bozar."),
   A("DMAH ve servise yatış",-5,10,"n9","Şokta yalnız antikoagülasyon yetersiz; reperfüzyon gerekir."),
 ]),
 "n2":E("Reperfüzyon","Tromboliz sonrası 40 dakikada KB 104/66'ya, SpO₂ %94'e yükseldi. Yoğun bakımda heparin infüzyonuyla izlendi.\n\n**Akılda kalsın**\n- **Yüksek riskli PE** = şok/kalıcı hipotansiyon (sistolik <90 ≥15 dk ya da vazopresör ihtiyacı) veya arrest.\n- Instabil hastada **POCUS** (RV dilatasyonu) ile karar; BT'ye taşımak riskli.\n- **Sistemik tromboliz** (alteplaz 100 mg/2 saat; arrestte 50 mg bolus düşünülebilir); kontrendikasyonda **cerrahi/kateter** embolektomi.\n- Sıvı **dikkatli**; **norepinefrin** ilk vazopresör.\n\n*Kaynak: ESC 2019 akut PE kılavuzu; ERC 2021.*","good"),
 "n9":E("Arrest","Hasta nabızsız elektriksel aktiviteye girdi; resüsitasyon sırasında tromboliz verildi ama geri döndürülemedi.","bad"),
}))
Qs+=[Q("c122q1","Yüksek riskli PE'nin tanımı hangisidir?",["Troponin yüksekliği","Şok veya kalıcı hipotansiyon/arrest","Yalnız taşikardi","D-dimer yüksekliği","SpO₂ %92"],1,"Hemodinamik instabilite.","Göğüs / Kardiyoloji"),
 Q("c122q2","Şoktaki PE hastasında birinci basamak reperfüzyon tedavisi hangisidir?",["Yalnız DMAH","Sistemik tromboliz","Vena kava filtresi","Aspirin","Warfarin"],1,"Kontrendikasyonda cerrahi/kateter.","Göğüs / Kardiyoloji"),
 Q("c122q3","Masif PE'de POCUS'ta beklenen bulgu hangisidir?",["Sol ventrikül dilatasyonu","Sağ ventrikül dilatasyonu, septal düzleşme","Perikardiyal tamponad","Hiperdinamik RV","Normal görünüm"],1,"RV/LV >1, D işareti.","Göğüs / Kardiyoloji")]

# 123 HEMOPTİZİ — masif
S.append(case("c123","Ağızdan kan gelmesi — 58 yaşında erkek","Göğüs hastalıkları",
 "58 yaşında erkek. Gençliğinde tüberküloz geçirmiş, sağ üst lobda sekel bronşektazi var. Son 1 saatte 3 kez, toplam ≈300 mL taze kan öksürmüş.",
 {"n1":N("Muayene","Anksiyöz, öksürdükçe parlak kırmızı kan. Sağ üst zonda raller.","KB 108/66 · Nb 118 · SS 28 · SpO₂ %89",[
   T("Akciğer grafisi",2,15,"Sağ üst zonda eski fibrokaviter değişiklikler ve yeni buzlu cam (aspire kan).","Kanayan taraf sağ."),
   T("Hemogram, koagülasyon, kan grubu",2,40,"Hb 11,2; INR 1,1; trombosit normal.","Transfüzyona hazırlık."),
   A("**Masif hemoptizi**: **kanayan taraf (sağ) aşağıda** lateral dekübit; O₂; geniş damar yolu, kan hazırla; **traneksamik asit** (IV ya da nebül); erken anestezi/göğüs hastalıkları/girişimsel radyoloji; hava yolu gerekirse **büyük tüp (≥8,0)** ile entübasyon (bronkoskopiye izin vermek için) ya da sağlam tarafa selektif entübasyon; stabil olunca **BT anjiyografi → bronşiyal arter embolizasyonu**",4,15,"n2","Doğru. Ölüm genellikle kanamadan değil, asfiksiden olur."),
   A("Kanayan taraf yukarıda yatır, öksürük kesici ver",-4,10,"n9","Kan sağlam akciğere akar; öksürük kesici kanın temizlenmesini engeller."),
   A("Hemen kodein ve takip için servise yatır",-3,20,"n9","Masif hemoptizi yoğun bakım ve girişimsel tedavi gerektirir."),
 ]),
 "n2":E("Embolizasyon","BT anjiyografide sağ bronşiyal arterden kaynaklanan kanama gösterildi; girişimsel radyoloji embolize etti. Hasta entübe edilmeden toparlandı.\n\n**Akılda kalsın**\n- Masif hemoptizi: hacimden çok **hava yolunu tehdit** etmesi önemlidir.\n- **Kanayan akciğer aşağıda**; büyük tüple entübasyon veya sağlam tarafa selektif entübasyon.\n- **Traneksamik asit**, koagülopati düzeltme.\n- Kaynak çoğunlukla **bronşiyal arter**: **BT anjiyo → bronşiyal arter embolizasyonu**; başarısızlıkta cerrahi.\n\n*Kaynak: BTS bronşektazi kılavuzu 2019; Davidson & Shojaee, Respiration 2020.*","good"),
 "n9":E("Asfiksi","Kan sağlam akciğere aspire edildi; hasta hipoksik arrest geçirdi.","bad"),
}))
Qs+=[Q("c123q1","Masif hemoptizide hasta nasıl pozisyonlanır?",["Kanayan taraf yukarıda","Kanayan taraf aşağıda (lateral dekübit)","Trendelenburg","Yüzüstü","Oturur ve öne eğik"],1,"Sağlam akciğer korunur.","Göğüs hastalıkları"),
 Q("c123q2","Masif hemoptizide kanamanın en sık kaynağı hangisidir?",["Pulmoner arter","Bronşiyal arter","Pulmoner ven","Aort","Interkostal ven"],1,"Sistemik basınçlı dolaşım.","Göğüs hastalıkları"),
 Q("c123q3","Masif hemoptizide kesin tedavi seçeneklerinden biri hangisidir?",["Bronşiyal arter embolizasyonu","Öksürük kesici","Diüretik","Antihistaminik","Fizik tedavi"],0,"BT anjiyo ile kaynağı göster, embolize et.","Göğüs hastalıkları")]

# 124 KULAK TRAVMASI — aurikula hematomu
S.append(case("c124","Güreş sonrası kulak şişliği — 20 yaşında erkek","KBB",
 "20 yaşında güreşçi. Dün antrenmanda sağ kulağı yere sürtünmüş. Kulak kepçesinde ağrılı şişlik; işitme kaybı yok.",
 {"n1":N("Muayene","Sağ aurikula ön yüzünde **fluktuasyon veren mor-kırmızı şişlik**, kulak kepçesi kıvrımları silinmiş. Dış kulak yolu ve kulak zarı normal. Başka yaralanma yok.","KB 126/74 · Nb 78 · SpO₂ %99",[
   T("Kulak zarı ve işitme muayenesi",1,5,"Zar sağlam, fısıltı testi normal.","Eşlik eden zar perforasyonu ve temporal kemik yaralanması dışlanır."),
   A("**Aurikula hematomu**: lokal anestezi altında **iğne aspirasyonu ya da insizyonla boşaltma**; kıvrımlara uygun **bastırıcı pansuman (bolster)**; 24–48 saatte kontrol (tekrar birikim); güreşe dönüşte kulak koruyucu",4,15,"n2","Doğru. Perikondriyumdan ayrılan kıkırdak beslenemez; boşaltma ve bası şart."),
   A("Soğuk uygulama ve analjezik, kendiliğinden geçer",-4,5,"n9","Boşaltılmayan hematom fibrozis ve kıkırdak nekrozuna (karnabahar kulak) yol açar."),
 ]),
 "n2":E("İyileşme","Hematom boşaltıldı, bolster pansuman uygulandı; kontrolde tekrar birikim olmadı ve kulak şekli korundu.\n\n**Akılda kalsın**\n- Aurikula hematomu kıkırdağı perikondriyumdan ayırır → **avasküler nekroz, fibrozis: karnabahar kulak**.\n- **Erken boşaltma** (ideal ilk 7 gün) + **bası pansumanı** + kısa aralıklı kontrol.\n- Kulak travmasında kulak zarı, işitme ve fasiyal sinir muayenesi.\n- Perikondrit/kulak delinmesi sonrası enfeksiyonda *Pseudomonas*'ı kapsa.\n\n*Kaynak: Am Fam Physician 2017; ENT UK önerileri.*","good"),
 "n9":E("Karnabahar kulak","Hematom fibrozise dönüştü; kalıcı şekil bozukluğu gelişti.","bad"),
}))
Qs+=[Q("c124q1","Aurikula hematomunda tedavi hangisidir?",["Yalnız soğuk uygulama","Boşaltma + bası pansumanı","Antibiyotik tek başına","Steroid","Bekleme"],1,"Kıkırdak nekrozunu önler.","KBB"),
 Q("c124q2","Tedavi edilmeyen aurikula hematomunun sonucu nedir?",["Karnabahar kulak","Otoskleroz","Kolesteatom","Bell paralizisi","Menière"],0,"Fibrozis ve kıkırdak deformitesi.","KBB"),
 Q("c124q3","Kulak travmasında eşlik eden yaralanma için yapılması gereken hangisidir?",["Otoskopi ve işitme değerlendirmesi","EKG","Lomber ponksiyon","Abdominal USG","EEG"],0,"Zar perforasyonu ve temporal kemik kırığı aranır.","KBB")]

# 125 ANTERİOR MİYOKARDİYAL İSKEMİ — Wellens
S.append(case("c125","Geçen göğüs ağrısı — 54 yaşında erkek","Kardiyoloji",
 "54 yaşında erkek, sigara içiyor. Son 2 günde eforla gelen, 10–15 dakika süren göğüs ağrıları. Son ağrı 3 saat önce geçti; şu an ağrısı yok.",
 {"n1":N("Muayene","Rahat, ağrısız. Kardiyak muayene normal.","KB 134/82 · Nb 72 · SS 16 · SpO₂ %98",[
   T("12 derivasyonlu EKG",3,5,"**V2–V3'te derin, simetrik T negatifliği** (V4'e uzanan); ST elevasyonu yok; R progresyonu korunmuş; Q yok.","Ağrısız dönemde **Wellens paterni** (tip B) → kritik proksimal LAD darlığı."),
   T("Yüksek duyarlıklı troponin",2,60,"Hafif yüksek (sınırın 2 katı).","Wellens'te troponin normal ya da hafif yüksek olabilir."),
   A("**Wellens sendromu**: yatış, aspirin, antikoagülan, nitrat gerektiğinde; **stres testi yapma**; **erken koroner anjiyografi** (<24 saat); kardiyoloji",4,15,"n2","Doğru. Stres testi ve taburculuk anterior MI'ya yol açabilir."),
   A("Ağrısı yok, troponin hafif — eforlu stres testi planla",-5,30,"n9","Kritik LAD darlığında stres testi büyük anterior MI tetikleyebilir."),
   A("Taburcu, kardiyoloji polikliniği",-4,10,"n9","Wellens hastalarının önemli kısmı haftalar içinde anterior MI geçirir."),
 ]),
 "n2":E("Önlendi","Ertesi sabah anjiyografide **proksimal LAD'de %95 darlık** saptandı, stent takıldı.\n\n**Akılda kalsın**\n- **Wellens**: ağrısız dönemde V2–V3'te **bifazik (tip A)** ya da **derin simetrik T negatifliği (tip B)**, ST elevasyonu yok, Q yok, troponin normal/hafif.\n- **Kritik proksimal LAD darlığı** → **stres testi kontrendike**, erken anjiyografi.\n- Benzer “STEMI eşdeğerleri”: de Winter T dalgaları, posterior MI, Sgarbossa pozitif LBBB.\n\n*Kaynak: ESC 2023 AKS kılavuzu; de Zwaan ve ark., Am Heart J 1982.*","good"),
 "n9":E("Anterior MI","Hasta stres testinde/evde geniş anterior MI geçirdi; EF %30'a düştü.","bad"),
}))
Qs+=[Q("c125q1","Wellens sendromu hangi damarda kritik darlığı gösterir?",["Sağ koroner","Proksimal LAD","Sirkumfleks","Distal LAD","Posterior desendan"],1,"V2–V3 T değişiklikleri.","Kardiyoloji"),
 Q("c125q2","Wellens paterninde hangisi kontrendikedir?",["Aspirin","Koroner anjiyografi","Eforlu stres testi","Yatış","Antikoagülan"],2,"Anterior MI'yı tetikleyebilir.","Kardiyoloji"),
 Q("c125q3","Wellens EKG değişiklikleri ne zaman görülür?",["Göğüs ağrısı sırasında","Ağrısız dönemde","Yalnız egzersizde","Yalnız gece","Hiçbir zaman"],1,"Ağrı sırasında EKG normal ya da psödonormal olabilir.","Kardiyoloji")]

# 126 İNFERİOR MİYOKARDİYAL İSKEMİ — silik inferior STEMI
S.append(case("c126","Epigastrik ağrı ve bulantı — 63 yaşında kadın","Kardiyoloji",
 "63 yaşında kadın, diyabet. 2 saattir epigastrik yanma, bulantı, terleme. “Midem bozuldu” diyor; antiasit almış, geçmemiş.",
 {"n1":N("Muayene","Terli, solgun. Karın yumuşak, epigastrik hafif hassasiyet. Akciğerler temiz.","KB 112/70 · Nb 64 · SS 18 · SpO₂ %97",[
   T("12 derivasyonlu EKG",3,5,"III ve aVF'de **1 mm ST elevasyonu**, III'te T dalgası geniş-hiperakut; **aVL'de 1 mm ST çökmesi ve T negatifliği** (ayna); V1–V3'te 1 mm ST çökmesi.","aVL'deki ayna değişiklik silik inferior STEMI'nin erken ve duyarlı işaretidir; V1–V3 çökmesi posterior uzanımı düşündürür."),
   T("Posterior derivasyonlar (V7–V9)",2,5,"V8–V9'da **0,5–1 mm ST elevasyonu**.","Posterior tutulum."),
   T("Lipaz ve karın USG",-1,45,"Normal.","Diyabetik kadında atipik AKS'yi akılda tut."),
   A("**İnferoposterior STEMI**: kateter laboratuvarı (primer PKG); aspirin, heparin, P2Y12 (kardiyolojiyle); sağ derivasyonlar (V4R) ve nitrat öncesi RV tutulumu kontrolü",4,10,"n2","Doğru. Silik ST elevasyonu + ayna değişiklik = STEMI."),
   A("Gastrit — PPI, antiemetik, troponin sonucuna göre karar",-4,60,"n9","Diyabetik kadında epigastrik ağrı AKS olabilir; EKG zaten tanısal."),
 ]),
 "n2":E("Primer PKG","Sağ koroner orta segmentte tam tıkanıklık açıldı; kapıdan balona 58 dakika.\n\n**Akılda kalsın**\n- **Kadın, diyabetik ve yaşlıda** AKS epigastrik ağrı, bulantı, halsizlikle başvurabilir: **10 dakikada EKG**.\n- İnferior STEMI'de **aVL'de ayna ST çökmesi** erken ve duyarlı işarettir.\n- V1–V3'te ST çökmesi → **posterior uzanım**; **V7–V9** çek (≥0,5 mm elevasyon).\n- İnferior MI'da **V4R** (sağ ventrikül) ve nitrat dikkati.\n\n*Kaynak: ESC 2023 AKS kılavuzu; Bischof & Smith, J Electrocardiol 2016 (aVL).*","good"),
 "n9":E("Geç tanı","Troponin yüksek gelince EKG yeniden incelendi; 4 saat gecikmeyle PKG yapıldı, inferoposterior duvar hareket kusuru kaldı.","bad"),
}))
Qs+=[Q("c126q1","Silik inferior STEMI'nin erken işaretlerinden biri hangisidir?",["aVL'de ayna ST çökmesi","aVR'de T pozitifliği","V6'da Q","Uzun PR","Sağ dal bloğu"],0,"Yüksek duyarlılık.","Kardiyoloji"),
 Q("c126q2","V1–V3'te ST çökmesi olan göğüs ağrılı hastada hangi derivasyonlar çekilmelidir?",["V4R","V7–V9","Yalnız ritim şeridi","Lewis","Hiçbiri"],1,"Posterior MI'yı gösterir.","Kardiyoloji"),
 Q("c126q3","Hangi hasta grubunda AKS sıklıkla atipik başvurur?",["Genç erkek","Diyabetik, yaşlı ve kadın","Sporcu","Çocuk","Gebe olmayan genç kadın tek başına"],1,"Epigastrik ağrı, nefes darlığı, halsizlik.","Kardiyoloji")]

# 127 AV TAM BLOK
S.append(case("c127","Bayılma ve yavaş nabız — 81 yaşında erkek","Kardiyoloji",
 "81 yaşında erkek. Bugün iki kez kısa süreli bayılmış. Halsiz. Hipertansiyon için amlodipin kullanıyor; beta bloker, digoksin yok.",
 {"n1":N("Muayene","Bilinç açık ama yavaş yanıt veriyor; soğuk terli. Boyunda düzensiz büyük “a” dalgaları (kanon dalgası).","KB 82/48 · Nb 32 · SS 18 · SpO₂ %95",[
   T("12 derivasyonlu EKG",3,5,"**P dalgaları ile QRS arasında ilişki yok (AV disosiyasyon)**; atriyal hız 84, ventriküler kaçış ritmi 32/dk, **geniş QRS**.","Tam blok, infranodal kaçış — atropine yanıt düşük."),
   T("K, Mg, troponin, (digoksin varsa düzey)",2,40,"K 4,6; troponin normal.","Geri döndürülebilir nedenler: iskemi, hiperkalemi, ilaç."),
   A("**Atropin IV** (ERC 2021: 0,5 mg; AHA 2020: 1 mg — 3–5 dk'da tekrar, en çok 3 mg) ile birlikte hemen **transkutan pacing** pedlerini hazırla/başlat (analjezi-sedasyonla) ya da **adrenalin 2–10 mcg/dk** infüzyonu; kardiyoloji — **geçici transvenöz pace**, ardından kalıcı pacemaker",4,10,"n2","Doğru. Geniş QRS'li kaçışta atropin genellikle etkisiz; pacing/kronotrop hazır olmalı."),
   A("Atropin ver, yanıt yoksa bekle ve izle",-2,15,"n3","Instabil hastada pacing/kronotrop hazırlığı ertelenmemeli."),
   A("Hipotansiyon için 2 L hızlı SF ve gözlem",-3,30,"n9","Sorun hız; sıvı tek başına yetmez."),
 ]),
 "n3":N("Kötüleşme","Hasta bayıldı, monitörde 8 saniyelik asistoli, sonra kaçış 24/dk.","KB 64/38 · Nb 24",[
   A("Transkutan pacing + adrenalin infüzyonu, transvenöz pace için kardiyoloji",2,10,"n4","Doğru ama geç."),
   A("Atropini tekrarla ve bekle",-4,5,"n9","Kalıcı asistoli riski."),
 ]),
 "n2":E("Pacemaker","Transkutan pacing ile yakalama sağlandı; aynı gün geçici transvenöz pace, 2 gün sonra kalıcı çift odacıklı pacemaker takıldı.\n\n**Akılda kalsın**\n- Instabil bradikardi (şok, senkop, iskemi, KY): **atropin** (ERC 2021: **0,5 mg**; AHA 2020: **1 mg**; en çok 3 mg) → yanıtsızsa **transkutan pacing** veya **adrenalin 2–10 mcg/dk / dopamin 5–20 mcg/kg/dk** → **transvenöz pacing**.\n- **Mobitz II ve tam blok (özellikle geniş QRS)** atropine yanıtsız olabilir; pacing hazır olsun.\n- Geri döndürülebilir nedenler: **iskemi (inferior MI), hiperkalemi, ilaç (BB, KKB, digoksin)**, Lyme.\n\n*Kaynak: ERC 2021 erişkin ileri yaşam desteği; AHA 2020 ACLS; ESC 2021 pacing kılavuzu.*","good"),
 "n4":E("Geç pacing","Pacing ile toparlandı; ancak düşmeye bağlı kafa yarası ve 1 gün yoğun bakım oldu.","mid"),
 "n9":E("Asistoli","Hasta asistolik arreste girdi.","bad"),
}))
Qs+=[Q("c127q1","Instabil bradikardide ERC 2021'e göre ilk ilaç ve dozu hangisidir?",["Atropin 0,5 mg IV","Adenozin 6 mg","Amiodaron 300 mg","Adrenalin 1 mg bolus","Digoksin 0,25 mg"],0,"3–5 dakikada bir, en çok 3 mg; AHA 2020 ilk dozu 1 mg önerir.","Kardiyoloji"),
 Q("c127q2","Geniş QRS kaçış ritimli tam blokta atropine yanıt neden zayıftır?",["Blok AV düğümün altında (infranodal)","Atropin metabolize olmaz","Hiperkalemi vardır","Vagal tonus yüksektir","Atropin ters etki yapar"],0,"Atropin düğümde etkilidir.","Kardiyoloji"),
 Q("c127q3","Atropine yanıtsız instabil bradikardide seçeneklerden biri hangisidir?",["Transkutan pacing","Beta bloker","Diltiazem","Digoksin","Magnezyum"],0,"Ya da adrenalin/dopamin infüzyonu.","Kardiyoloji")]

# 128 GÖZDE YABANCI CİSİM — metalik korneal
S.append(case("c128","Taşlama sonrası gözde batma — 40 yaşında erkek","Göz",
 "40 yaşında oto tamircisi. Dün taşlama makinesiyle çalışırken koruyucu gözlük takmamış. Bu sabah sağ gözde batma, sulanma ve ışığa hassasiyet. Çekiçle metale vurma öyküsü yok.",
 {"n1":N("Muayene","Sağ gözde konjonktival kızarıklık; korneada saat 10 hizasında **1 mm koyu metalik cisim** ve çevresinde **pas halkası**. Pupil yuvarlak, ön kamara derin. Görme 0,8.","KB 128/80 · Nb 76 · SpO₂ %99",[
   T("Topikal anestezik + floresein ile yarık lamba muayenesi; Seidel",2,10,"Yüzeyel korneal yabancı cisim; **Seidel negatif**; üst göz kapağı ters çevrildiğinde başka cisim yok.","Penetrasyon dışlanır; kapak altı mutlaka kontrol edilir."),
   T("Orbita BT",0,30,"Göz içi yabancı cisim yok.","Taşlamada yüzeyel cisim tipiktir; **yüksek hızlı** (çekiç-metal) mekanizmada BT gerekir."),
   A("Topikal anestezik altında yarık lambada **ince iğne (25–27G) ile çıkarma**; pas halkası için göz hekimine (gerekirse ertesi gün çapak frezi); **topikal antibiyotik** damla; **kapama yok**; evde topikal anestezik **verilmez**; koruyucu gözlük eğitimi",4,15,"n2","Doğru."),
   A("Eve topikal anestezik damla reçetele, göz kapat",-4,10,"n9","Sürekli topikal anestezik kornea epitel iyileşmesini bozar ve ülsere yol açar; kapama yarar sağlamaz."),
   A("Pamuklu çubukla sertçe silerek çıkarmaya çalış",-2,5,"n9","Geniş epitel defekti yapar; cisim gömülüyse çıkmaz."),
 ]),
 "n2":E("İyileşme","Cisim çıkarıldı; pas halkası ertesi gün göz polikliniğinde temizlendi. 2 günde epitel iyileşti.\n\n**Akılda kalsın**\n- Gözde YC: **görme keskinliği**, floresein, **kapak çevirme**, **Seidel**.\n- **Yüksek hızlı mekanizma (çekiç-metal, patlama)** → göz içi YC şüphesi: **BT**, **MR yok**.\n- Çıkarma: topikal anestezik, yarık lamba, iğne; **pas halkası** göz hekimi.\n- Topikal antibiyotik; **kapama ve eve topikal anestezik yok**; kontakt lens kullananda psödomonasa dikkat.\n\n*Kaynak: Am Fam Physician 2013 (corneal abrasion & FB); RCOphth.*","good"),
 "n9":E("Korneal ülser","Hasta kornea ülseri ve enfeksiyonla döndü; uzun tedavi gerekti.","bad"),
}))
Qs+=[Q("c128q1","Korneal yabancı cisim çıkarıldıktan sonra hangisi yapılmamalıdır?",["Topikal antibiyotik","Eve topikal anestezik damla vermek","Kontrol","Koruyucu gözlük önerisi","Görme keskinliği ölçümü"],1,"Epitel iyileşmesini bozar.","Göz"),
 Q("c128q2","Hangi mekanizmada göz içi yabancı cisim şüphesiyle BT gerekir?",["Rüzgârla toz kaçması","Çekiçle metale vurma","Kirpik","Böcek","Göz kırpma"],1,"Yüksek hızlı partikül.","Göz"),
 Q("c128q3","Gözde yabancı cisim muayenesinde atlanmaması gereken adım hangisidir?",["Üst göz kapağını ters çevirme","EKG","Kulak muayenesi","Karın muayenesi","Fundus dilatasyonu her zaman"],0,"Kapak altında cisim kalabilir.","Göz")]

# 129 İSKEMİK İNME — uyanma inmesi
S.append(case("c129","Sabah konuşamayarak uyandı — 67 yaşında erkek","Nöroloji",
 "67 yaşında erkek. Gece 23:00'te normal yatmış; 06:30'da sağ kolu güçsüz ve konuşamaz hâlde uyanmış. Saat 07:15'te acilde. Antikoagülan kullanmıyor.",
 {"n1":N("Muayene","Motor afazi, sağ yüz-kol güçsüzlüğü (kol 2/5), bacak 4/5. **NIHSS 9**.","KB 172/94 · Nb 84 (düzenli) · SS 16 · SpO₂ %97 · Kapiller glukoz 126",[
   T("Kontrastsız BT + BT anjiyografi",3,20,"Kanama yok, belirgin erken iskemi yok (ASPECTS 10). BTA'da **büyük damar tıkanıklığı yok**.","Trombektomi adayı değil."),
   T("Beyin MR (DWI + FLAIR)",3,30,"Sol frontal-insular alanda **DWI'da difüzyon kısıtlaması**, aynı alanda **FLAIR'de belirgin sinyal yok** (**DWI-FLAIR uyumsuzluğu**).","İnfarkt büyük olasılıkla <4,5 saatlik."),
   A("Başlangıç zamanı bilinmeyen inme, **DWI-FLAIR uyumsuzluğu**: **IV tromboliz** — alteplaz 0,9 mg/kg (en çok 90 mg; %10 bolus, kalanı 60 dk) ya da tenekteplaz (kurum protokolü); öncesinde KB <185/110; inme ünitesi",4,20,"n2","Doğru. WAKE-UP çalışması ve ESO 2021: uyumsuzlukta tromboliz önerilir."),
   A("Son normal görülme 8 saat önce — tromboliz yok, aspirin ve yatış",-2,10,"n3","Görüntüleme seçimiyle tromboliz şansı kaçırıldı."),
   A("Hemen trombektomi için anjiyo",-2,30,"n3","Büyük damar tıkanıklığı yok."),
 ]),
 "n3":E("Kaçırılan fırsat","Hasta aspirinle izlendi; afazi ve kol güçsüzlüğü kısmen kaldı (mRS 3).","mid"),
 "n2":E("Düzelme","Tromboliz sonrası 24 saatte NIHSS 3'e indi; kanama olmadı. 3. ayda mRS 1.\n\n**Akılda kalsın**\n- **Uyanma inmesi / bilinmeyen başlangıç**: ileri görüntüleme ile seçim — **MR DWI-FLAIR uyumsuzluğu** (WAKE-UP) ya da **BT/MR perfüzyon kurtarılabilir doku** (EXTEND).\n- Uygunsa **IV tromboliz** (alteplaz 0,9 mg/kg; tenekteplaz 0,25 mg/kg alternatif).\n- **Büyük damar tıkanıklığı** varsa 24 saate kadar **trombektomi** (DAWN/DEFUSE-3).\n- Tromboliz öncesi KB <185/110, sonrası 24 saat <180/105.\n\n*Kaynak: ESO 2021 IV tromboliz kılavuzu; AHA/ASA 2019; WAKE-UP (NEJM 2018).*","good"),
}))
Qs+=[Q("c129q1","Başlangıç zamanı bilinmeyen inmede tromboliz kararı için MR'da aranan bulgu hangisidir?",["DWI-FLAIR uyumsuzluğu","T1 hiperintensite","Mikrokanama yokluğu","Beyaz cevher hastalığı","Normal MR"],0,"DWI pozitif, FLAIR negatif → <4,5 saat olasılığı.","Nöroloji"),
 Q("c129q2","Alteplazın iskemik inmede dozu nedir?",["0,9 mg/kg (en çok 90 mg)","1,5 mg/kg","0,25 mg/kg","100 mg sabit","50 mg bolus"],0,"%10 bolus, kalanı 60 dakikada.","Nöroloji"),
 Q("c129q3","Tromboliz öncesi KB hedefi nedir?",["<140/90","<185/110","<220/120","<160/100","Hedef yok"],1,"Sonrasında <180/105.","Nöroloji")]

# 130 GUİLLAİN-BARRÉ SENDROMU
S.append(case("c130","Bacaklardan başlayan güçsüzlük — 36 yaşında erkek","Nöroloji",
 "36 yaşında erkek. 2 hafta önce ishal geçirmiş. 4 gündür ayaklarda karıncalanma, 2 gündür merdiven çıkamıyor; bugün kollarında da güçsüzlük ve hafif nefes darlığı.",
 {"n1":N("Muayene","Alt ekstremite 3/5, üst 4/5 simetrik güçsüzlük; **derin tendon refleksleri alınamıyor**. Bilateral hafif fasiyal güçsüzlük. Duyu kaybı hafif. Tek nefeste 1'den 12'ye kadar sayabiliyor.","KB 156/94 (dalgalı) · Nb 112 · SS 24 · SpO₂ %96",[
   T("FVC ve NIF (yatak başı)",3,10,"**FVC 18 mL/kg**, NIF −24 cmH₂O.","**20/30/40 kuralı**: FVC <20 mL/kg, NIF > −30, MEP <40 → yüksek solunum yetmezliği riski."),
   T("Lomber ponksiyon",1,60,"Protein 92 mg/dL, hücre 2/mm³ (**albüminositolojik disosiyasyon**).","İlk haftada normal olabilir; tanı klinik + EMG."),
   T("EKG / monitör",1,5,"Sinüs taşikardisi; KB 120–180 arasında dalgalanıyor.","Otonom disfonksiyon."),
   A("**GBS, solunum yetmezliği riski yüksek**: **yoğun bakım**; FVC/NIF seri izlem, elektif entübasyon hazırlığı (süksinilkolinden kaçın); **IVIG 0,4 g/kg/gün × 5 gün** (ya da plazmaferez); otonom izlem, tromboprofilaksi, ağrı tedavisi; nöroloji",4,20,"n2","Doğru. Steroid etkisiz; immünoterapi erken başlanır."),
   A("Yüksek doz metilprednizolon ve serviste izlem",-4,20,"n9","Steroid GBS'de etkisiz; solunum riski olan hasta servise uygun değil."),
   A("SpO₂ %96 — solunum güvenli, nöroloji polikliniği",-5,10,"n9","Nöromüsküler solunum yetmezliğinde SpO₂ geç düşer; FVC belirleyicidir."),
 ]),
 "n2":E("İyileşme","Hasta 2. günde FVC 12 mL/kg'a düşünce elektif entübe edildi; IVIG sonrası 3 haftada ekstübe edildi, rehabilitasyonla yürümeye başladı.\n\n**Akılda kalsın**\n- GBS: enfeksiyon sonrası (ör. *Campylobacter*), **asendan simetrik güçsüzlük + arefleksi**.\n- Solunum: **SpO₂ geç düşer** → **FVC/NIF** izle; **20/30/40** kuralı, bulber tutulum, hızlı ilerleme → yoğun bakım.\n- **Otonom disfonksiyon** (KB dalgalanması, aritmi).\n- Tedavi: **IVIG 2 g/kg (5 günde)** ya da **plazmaferez**; **steroid yok**.\n\n*Kaynak: EAN/PNS 2023 GBS kılavuzu.*","good"),
 "n9":E("Solunum arresti","Hasta gece hipoventilasyonla solunum arresti geçirdi; acil entübe edildi.","bad"),
}))
Qs+=[Q("c130q1","GBS'de solunum yetmezliği riskini en iyi gösteren parametre hangisidir?",["SpO₂","FVC (ve NIF)","Kalp hızı","Ateş","Laktat"],1,"SpO₂ geç bir bulgudur.","Nöroloji"),
 Q("c130q2","GBS'de etkisiz olan tedavi hangisidir?",["IVIG","Plazmaferez","Kortikosteroid","Destek tedavisi","Tromboprofilaksi"],2,"Steroidler yararsızdır.","Nöroloji"),
 Q("c130q3","GBS'de BOS'ta tipik bulgu hangisidir?",["Nötrofilik pleositoz","Albüminositolojik disosiyasyon","Düşük glukoz","Ksantokromi","Oligoklonal bant zorunlu"],1,"Yüksek protein, normal hücre.","Nöroloji")]

P={"id":"ilk-nobet-13","title":"İlk Nöbet Vakaları — 13. Paket (vaka 121–130)","desc":"Derin ven trombozu, yüksek riskli pulmoner emboli, masif hemoptizi, aurikula hematomu, Wellens sendromu, silik inferoposterior STEMI, AV tam blok, korneal yabancı cisim, uyanma inmesi, Guillain-Barré sendromu.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 13. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 13. Paket","topic":"Temel acil","order":13,"req":[2],"desc":"Tromboembolik, kardiyak ve nörolojik acillerle 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
