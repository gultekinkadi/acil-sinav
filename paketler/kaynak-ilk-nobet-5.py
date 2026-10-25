import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 41 AKUT EKSTREMİTE İSKEMİSİ (embolik)
S.append(case("c41","Soğuk ve ağrılı bacak — 76 yaşında kadın","Kalp-damar cerrahisi",
 "76 yaşında kadın, AF tanılı; antikoagülanı 2 ay önce kendisi bırakmış. 3 saat önce sol bacağında ani, şiddetli ağrı başlamış; bacağı soğuk ve uyuşuk.",
 {"n1":N("Muayene","Sol bacak dizden aşağıda soluk ve soğuk. Femoral nabız var; popliteal ve ayak nabızları **yok**. Ayak parmaklarında duyu azalmış, ayak bileği dorsifleksiyonu hafif zayıf.","KB 146/84 · Nb 112 (düzensiz) · SpO₂ %96",[
   T("El Doppler (ayak bileği arterleri)",2,5,"Arteriyel sinyal **yok**; venöz sinyal var.","Rutherford IIb: duyu kaybı ayak parmaklarının ötesinde + hafif-orta motor kayıp, arteriyel sinyal yok → **acil revaskülarizasyon**."),
   T("EKG",1,5,"AF, hız 110.","Embolik kaynak."),
   T("BT anjiyografi",1,30,"Sol popliteal arterde ani kesilme (emboli).","Revaskülarizasyonu geciktirmeyecekse planlamaya yardımcı."),
   A("Hemen anfraksiyone heparin IV (ör. 80 Ü/kg bolus, ardından infüzyon); analjezi; acil damar cerrahisi — embolektomi",4,15,"n2","Doğru. Akut ekstremite iskemisinde heparin trombüsün ilerlemesini önler; IIb'de saatler içinde revaskülarizasyon gerekir."),
   A("Periferik arter hastalığı — sıcak uygulama ve analjezik, poliklinik randevusu",-5,30,"n9","Sıcak uygulama doku hasarını artırır; ani başlangıç + nabızsızlık + nörolojik kayıp acildir."),
 ]),
 "n2":E("Embolektomi","Fogarty kateterle embolektomi yapıldı, distal nabızlar döndü. Reperfüzyon sonrası kompartman sendromu açısından izlendi; antikoagülan yeniden başlandı.\n\n**Akılda kalsın**\n- 6P: **ağrı, solukluk, nabızsızlık, parestezi, paralizi, soğukluk (poikilotermi)**.\n- **Rutherford**: I (canlı), IIa (az tehdit), **IIb (acil tehdit — revaskülarizasyon saatler içinde)**, III (geri dönüşsüz).\n- **Hemen heparin** + acil damar cerrahisi.\n- Embolik kaynak (AF) ve **reperfüzyon sonrası kompartman sendromu** unutulmasın.\n\n*Kaynak: ESVS 2020 akut ekstremite iskemisi kılavuzu.*","good"),
 "n9":E("Amputasyon","Hasta 24 saat sonra geri döndüğünde bacak geri dönüşsüz iskemideydi (Rutherford III); diz üstü amputasyon gerekti.","bad"),
}))
Qs+=[Q("c41q1","Akut ekstremite iskemisinde ilk ilaç tedavisi hangisidir?",["Aspirin tek başına","Anfraksiyone heparin IV","Kilostazol","Varfarin oral","Tromboliz herkese"],1,"Heparin trombüs ilerlemesini durdurur; revaskülarizasyon planlanır.","Kalp-damar cerrahisi"),
 Q("c41q2","Rutherford IIb akut ekstremite iskemisinin özelliği hangisidir?",["Duyu ve motor normal, Doppler sinyali var","Ayak parmaklarının ötesinde duyu kaybı ve hafif-orta motor kayıp","Derin felç ve rijidite","Yalnız kladikasyon","Kronik yara"],1,"IIb acil tehdittir; III geri dönüşsüzdür (derin duyu-motor kaybı).","Kalp-damar cerrahisi"),
 Q("c41q3","Revaskülarizasyon sonrası izlenmesi gereken önemli komplikasyon hangisidir?",["Kompartman sendromu","Pnömotoraks","Hipoglisemi","Menenjit","Hiponatremi"],0,"Reperfüzyon ödemi kompartman sendromuna yol açabilir.","Kalp-damar cerrahisi")]

# 42 BOERHAAVE
S.append(case("c42","Kusma sonrası göğüs ağrısı — 48 yaşında erkek","Göğüs cerrahisi",
 "48 yaşında erkek. Gece alkol aldıktan sonra defalarca şiddetli kusmuş; son kusmanın ardından göğüs kafesinin arkasında yırtılır tarzda, sırta vuran ağrı başlamış. Nefes alırken ağrı artıyor.",
 {"n1":N("Resüsitasyon alanı","Terli, taşipneik. Boyunda ve supraklaviküler bölgede **cilt altı amfizem** (krepitasyon).","KB 102/64 · Nb 122 · SS 26 · SpO₂ %93 · Ateş 37,9",[
   T("EKG + troponin",1,30,"Sinüs taşikardisi; iskemi yok.","AKS ayırıcı tanıda."),
   T("Akciğer grafisi",2,15,"**Pnömomediastinum**, sol plevral efüzyon.","Mackler triadı: kusma + göğüs ağrısı + cilt altı amfizem."),
   T("Toraks BT (IV kontrast + suda çözünür oral kontrast)",3,30,"Distal özofagus sol posterolateral duvarda perforasyon, kontrast kaçağı, mediastinal hava ve sıvı.","Tanıda tercih edilen yöntem. Baryum mediastinite yol açtığı için ilk tercih değildir."),
   A("Ağızdan hiçbir şey verme; sıvı resüsitasyonu; geniş spektrumlu IV antibiyotik (ör. piperasilin-tazobaktam) + antifungal; IV PPI; acil göğüs cerrahisi",4,15,"n2","Doğru. Özofagus rüptüründe ilk 24 saatte tedavi mortaliteyi belirgin azaltır."),
   A("AKS olabilir: ASA + heparin, kardiyolojiye danış",-3,30,"n9","Kusma sonrası ağrı + cilt altı amfizem AKS değil, özofagus rüptürüdür; antitrombotik yararsız ve zararlı olabilir."),
   A("Gastrit — PPİ ve antiemetik ile taburcu",-5,20,"n9","Mediastinit hızla sepsise ilerler."),
 ]),
 "n2":E("Erken cerrahi onarım","Hasta 6 saat içinde primer onarım + drenaj ile opere edildi; yoğun bakımdan sonra iyileşti.\n\n**Akılda kalsın**\n- **Boerhaave**: şiddetli kusma sonrası transmural özofagus rüptürü (en sık distal sol posterolateral).\n- **Mackler triadı**: kusma + retrosternal ağrı + cilt altı amfizem (hep birlikte nadir).\n- Grafi: pnömomediastinum, sol efüzyon. **BT (oral suda çözünür kontrastla)** tanı koydurur.\n- **Ağızdan hiçbir şey**, geniş spektrum antibiyotik + antifungal, PPI, **acil cerrahi**.\n- AKS, pankreatit, aort diseksiyonu ile karışır.\n\n*Kaynak: WSES 2019 özofagus perforasyonu kılavuzu.*","good"),
 "n9":E("Mediastinit — septik şok","Tanı 24 saat gecikti; mediastinit ve septik şok gelişti, mortalite riski çok yükseldi.","bad"),
}))
Qs+=[Q("c42q1","Mackler triadı hangisidir?",["Ateş, sarılık, karın ağrısı","Kusma, retrosternal ağrı, cilt altı amfizem","Hipotansiyon, JVD, kalp seslerinde azalma","Baş ağrısı, ateş, ense sertliği","Hematüri, böğür ağrısı, kitle"],1,"Boerhaave sendromuna özgü triad.","Göğüs cerrahisi"),
 Q("c42q2","Özofagus perforasyonu şüphesinde tercih edilen oral kontrast hangisidir?",["Baryum","Suda çözünür (iyotlu) kontrast","Kontrast gerekmez, endoskopi her zaman ilk","Gadolinyum","Mannitol"],1,"Baryum kaçağı ağır mediastinite yol açabilir.","Göğüs cerrahisi"),
 Q("c42q3","Boerhaave sendromunda en sık rüptür yeri neresidir?",["Servikal özofagus","Distal özofagus sol posterolateral duvar","Mide fundusu","Duodenum","Proksimal özofagus sağ duvar"],1,"Distal özofagusun sol posterolateral duvarı en zayıf bölgedir.","Göğüs cerrahisi")]

# 43 SEROTONİN SENDROMU
S.append(case("c43","Ajitasyon ve titreme — 34 yaşında kadın","Toksikoloji",
 "34 yaşında kadın, depresyon için sertralin kullanıyor. 2 gün önce diş ağrısı için tramadol başlanmış, bugün öksürük şurubu (dekstrometorfan) da almış. Son birkaç saatte huzursuzluk, terleme, titreme ve ishal başlamış.",
 {"n1":N("Muayene","Ajite, terli, pupiller midriyatik. Alt ekstremitelerde **belirgin hiperrefleksi ve indüklenebilir klonus**, oküler klonus. Rijidite yok.","KB 158/92 · Nb 128 · SS 22 · Ateş 39,2",[
   T("Hunter ölçütleri",2,2,"Serotonerjik ajan + **indüklenebilir klonus + ajitasyon + terleme** → ölçütler karşılanıyor.","Hunter: spontan klonus; ya da indüklenebilir/oküler klonus + ajitasyon veya terleme; ya da tremor + hiperrefleksi; ya da hipertoni + ateş >38 + klonus."),
   T("CK, elektrolit, böbrek fonksiyonu",1,40,"CK 1200, kreatinin 1,0.","Rabdomiyoliz ve komplikasyon takibi."),
   A("Serotonerjik ilaçları kes; destek tedavisi (IV sıvı, dış soğutma); **benzodiazepin** (ör. diazepam/midazolam) ajitasyon için; yanıt yetersizse **siproheptadin** 12 mg PO, ardından 2 saatte bir 2 mg",4,15,"n2","Doğru. Tedavinin temeli ilacı kesmek ve benzodiazepinle sedasyondur."),
   A("Fiziksel kısıtlama ve haloperidol",-4,10,"n9","Kısıtlama izometrik kasılma ile hipertermi ve laktik asidozu artırır; haloperidol antikolinerjik/ısı düzenleyici etkilerle tabloyu ağırlaştırabilir."),
   A("Nöroleptik malign sendrom — bromokriptin + dantrolen",-2,20,"n9","NMS antipsikotikle, günler içinde, kurşun boru rijidite ve bradikinezi ile gelişir; burada hızlı başlangıç, klonus ve hiperrefleksi serotonin sendromunu gösterir."),
 ]),
 "n2":N("2 saat sonra","Ajitasyon azaldı. Ateş 40,8 °C'ye yükseldi, kas tonusu artıyor.","Nb 140 · KB 172/98",[
   A("Ağır serotonin sendromu: derin sedasyon, **nondepolarizan** blokerle paralizi ve entübasyon, agresif soğutma; antipiretik (parasetamol) etkisizdir; yoğun bakım",4,20,"n3","Doğru. >41 °C'ye ilerleyen hipertermi kas aktivitesinden kaynaklanır; paralizi gerekir. Süksinilkolin hiperkalemi riski nedeniyle kaçınılır."),
   A("Parasetamol ver ve bekle",-3,30,"n9","Hipotalamik set noktası değişmediği için antipiretik etkisizdir."),
 ]),
 "n3":E("Yoğun bakımda düzelme","Paralizi + soğutma ile ateş 38'in altına indi; 24 saatte klinik düzeldi. İlaç listesi düzenlendi.\n\n**Akılda kalsın**\n- Triad: **mental durum değişikliği + otonomik bulgular + nöromüsküler hiperaktivite** (klonus, hiperrefleksi — özellikle alt ekstremite).\n- **Hunter ölçütleri**; başlangıç **saatler** içinde (NMS günler).\n- Tetikleyiciler: SSRI/SNRI + **tramadol, dekstrometorfan, linezolid, MAOİ, triptan, fentanil**.\n- Tedavi: ilacı kes, **benzodiazepin**, siproheptadin; ağırda paralizi + entübasyon. Antipiretik ve fiziksel kısıtlama yok.\n\n*Kaynak: Boyer & Shannon, NEJM 2005; Goldfrank's.*","good"),
 "n9":E("Ağır hipertermi","Ateş 42 °C'ye çıktı; rabdomiyoliz, DİK ve böbrek yetmezliği gelişti.","bad"),
}))
Qs+=[Q("c43q1","Serotonin sendromunu nöroleptik malign sendromdan ayıran bulgu hangisidir?",["Ateş","Klonus ve hiperrefleksi, hızlı başlangıç","Kurşun boru rijidite, bradikinezi","CK yüksekliği","Bilinç değişikliği"],1,"NMS'de rijidite ve bradikinezi, günler içinde başlangıç; SS'de klonus/hiperrefleksi, saatler içinde.","Toksikoloji"),
 Q("c43q2","Serotonin sendromunda kullanılan serotonin antagonisti hangisidir?",["Ondansetron","Siproheptadin","Bromokriptin","Dantrolen","Fizostigmin"],1,"Siproheptadin 12 mg PO, ardından 2 saatte bir 2 mg.","Toksikoloji"),
 Q("c43q3","SSRI kullanan hastada hangisi serotonin sendromu riskini artırmaz?",["Tramadol","Dekstrometorfan","Linezolid","Parasetamol","Fentanil"],3,"Parasetamol serotonerjik değildir.","Toksikoloji")]

# 44 İNVAJİNASYON
S.append(case("c44","Aralıklı ağlama krizleri — 10 aylık erkek","Pediatri",
 "10 aylık erkek bebek. Dünden beri 15–20 dakikada bir şiddetli ağlayıp bacaklarını karnına çekiyor, aralarda sakin ve halsiz. 3 kez kusmuş; son bezde çilek reçeli kıvamında kanlı-mukuslu dışkı var.",
 {"n1":N("Çocuk acil","Ataklar arasında uykulu, soluk. Sağ üst kadranda sosis şeklinde kitle ele geliyor.","Nb 156 · SS 34 · Ateş 37,4 · Kapiller dolum 3 sn",[
   T("Abdominal USG",3,15,"**Hedef (target/donut) işareti**: ileokolik invajinasyon. Serbest sıvı/perforasyon yok.","İnvajinasyon tanısında USG ilk tercihtir (duyarlılık ve özgüllük >%95)."),
   T("Direkt grafi",0,15,"Sağ alt kadranda gaz azlığı.","Tanıda zayıf; perforasyon şüphesinde serbest hava için."),
   A("IV damar yolu, 20 mL/kg izotonik bolus; pediatrik cerrahi ve radyoloji — peritonit/perforasyon yoksa USG veya floroskopi eşliğinde hidrostatik/pnömatik redüksiyon",4,30,"n2","Doğru. Stabil hastada lavmanla redüksiyon ilk seçenektir; başarısızlık veya perforasyonda cerrahi."),
   A("Gastroenterit ve kolik — ORS ve taburcu",-5,20,"n9","Aralıklı kolik ağlama + kusma + kanlı mukuslu dışkı + kitle invajinasyondur; gecikme bağırsak nekrozu yapar."),
 ]),
 "n2":E("Başarılı redüksiyon","Pnömatik redüksiyonla ileokolik invajinasyon açıldı; 24 saat izlendi, tekrarlamadı.\n\n**Akılda kalsın**\n- 3 ay–3 yaş; **aralıklı kolik ağrı** (bacakları karna çekme), kusma, letarji; **çilek reçeli dışkı geç bulgu**.\n- **USG: hedef işareti**.\n- Sıvı resüsitasyonu; stabilse **hidrostatik/pnömatik redüksiyon**.\n- Peritonit, perforasyon, şok → **cerrahi**.\n- Redüksiyon sonrası ilk 24–72 saatte **nüks** olabilir.\n\n*Kaynak: ESPR/ESPGHAN önerileri; Tintinalli Pediatrik acil.*","good"),
 "n9":E("Bağırsak nekrozu","Bebek 24 saat sonra şok ve peritonitle getirildi; laparotomide nekrotik ileum rezeke edildi.","bad"),
}))
Qs+=[Q("c44q1","İnvajinasyon tanısında ilk tercih edilen görüntüleme hangisidir?",["BT","Ultrasonografi","Baryumlu grafi","MR","Direkt grafi tek başına"],1,"USG'de hedef işareti; radyasyonsuz ve yüksek doğruluklu.","Pediatri"),
 Q("c44q2","İnvajinasyonda “çilek reçeli” dışkı için doğru ifade hangisidir?",["En erken bulgudur","Geç bulgudur; yokluğu tanıyı dışlamaz","Her hastada vardır","Yalnız erişkinde görülür","Gastroenteriti gösterir"],1,"Mukozal iskemiyi gösterir; geç ortaya çıkar.","Pediatri"),
 Q("c44q3","Stabil, peritonit bulgusu olmayan invajinasyonda ilk tedavi hangisidir?",["Laparotomi","Hidrostatik veya pnömatik redüksiyon","Antibiyotik ve gözlem","Kolonoskopi","Laksatif"],1,"Lavmanla redüksiyon çoğu olguda başarılıdır.","Pediatri")]

# 45 GAZLI GANGREN
S.append(case("c45","Yarada gaz ve kötü koku — 37 yaşında erkek","Enfeksiyon / Cerrahi",
 "37 yaşında erkek, tarım işçisi. 30 saat önce traktör kazasında sol bacağında toprakla kirlenmiş açık yara oluşmuş; başka bir merkezde yara primer kapatılmış. Son birkaç saatte dayanılmaz ağrı.",
 {"n1":N("Resüsitasyon alanı","Yara çevresinde **bronz-mor renk**, gergin ödem, hemorajik bül, kirli kahverengi ve tatlımsı kötü kokulu akıntı; belirgin **krepitasyon**. Ağrı muayeneyle orantısız. Hasta konfüze.","KB 84/48 · Nb 138 · SS 28 · Ateş 38,8",[
   T("Bacak grafisi",2,15,"Kas planları boyunca **tüylü görünümde gaz**.","Destekler ama görüntüleme cerrahiyi geciktirmemeli."),
   T("Yara Gram boyaması",1,15,"Büyük Gram pozitif çomaklar, lökosit az.","*Clostridium perfringens* ile uyumlu."),
   A("Septik şok resüsitasyonu; **acil cerrahi debridman** (gerekirse amputasyon); IV penisilin G + **klindamisin** (veya geniş spektrum + klindamisin); tetanoz profilaksisi; olanak varsa hiperbarik oksijen yardımcı",4,15,"n2","Doğru. Klostridyal miyonekroz saatler içinde yayılır; tedavinin temeli acil cerrahidir."),
   A("Yara enfeksiyonu — dikişleri al, oral antibiyotik, ertesi gün kontrol",-5,30,"n9","Krepitasyon, bronz renk, orantısız ağrı ve şok gazlı gangrendir."),
 ]),
 "n2":E("Acil debridman","Geniş debridman ve 24 saat sonra ikinci bakış yapıldı; uzuv korundu. HBO yardımcı olarak uygulandı.\n\n**Akılda kalsın**\n- **Gazlı gangren (klostridyal miyonekroz)**: kirli derin yara, ezilme, kas hasarı; saatler içinde ilerler.\n- **Orantısız ağrı**, bronz renk, bül, tatlımsı koku, **krepitasyon**, sistemik toksisite.\n- Kirli derin yaralar **primer kapatılmaz**.\n- Tedavi: **acil cerrahi debridman**, penisilin + **klindamisin**, şok tedavisi; HBO yardımcı.\n- Tetanoz profilaksisini unutma.\n\n*Kaynak: IDSA 2014 deri ve yumuşak doku enfeksiyonları kılavuzu.*","good"),
 "n9":E("Ölümcül seyir","Ertesi gün hasta çoklu organ yetmezliği ve hemolizle getirildi; kalça dezartikülasyonuna rağmen kaybedildi.","bad"),
}))
Qs+=[Q("c45q1","Gazlı gangrenin en sık etkeni hangisidir?",["Streptococcus pyogenes","Clostridium perfringens","Staphylococcus aureus","Pseudomonas aeruginosa","Vibrio vulnificus"],1,"C. perfringens alfa toksini miyonekroz ve hemoliz yapar.","Enfeksiyon / Cerrahi"),
 Q("c45q2","Gazlı gangrende antibiyotiğe klindamisin eklenmesinin nedeni nedir?",["Böbrek koruması","Toksin üretimini baskılamak","Antipiretik","Antikoagülan etki","Vankomisin yerine"],1,"Protein sentezi inhibisyonu ile toksin üretimini azaltır.","Enfeksiyon / Cerrahi"),
 Q("c45q3","Toprakla kirlenmiş derin bir yaranın yönetimi için doğru olan hangisidir?",["Primer kapatma","Debridman ve gecikmiş primer kapatma","Yalnız oral antibiyotik","Steril örtü ve 1 hafta sonra kontrol","Steroid"],1,"Kirli derin yaralar kapatılmadan debride edilir.","Enfeksiyon / Cerrahi")]

# 46 TRANSFÜZYON REAKSİYONU (akut hemolitik)
S.append(case("c46","Kan verilirken titreme — 64 yaşında kadın","Hematoloji",
 "64 yaşında kadın, üst GİS kanaması nedeniyle acilde eritrosit süspansiyonu takıldı. Transfüzyonun 10. dakikasında titreme, bel ağrısı, göğüste sıkışma ve “kötü bir şey olacak” hissi başladı.",
 {"n1":N("Transfüzyonun 10. dakikası","Terli, huzursuz. İnfüzyon yerinde yanma. Sonda torbasında koyu kırmızı idrar.","KB 82/48 · Nb 132 · SS 26 · SpO₂ %94 · Ateş 39,0 (önce 36,8)",[
   T("Hasta kimliği ve kan torbası etiketinin yatak başında kontrolü",3,3,"Torbadaki isim aynı servisteki başka bir hastaya ait; **ABO uyumsuzluğu** (A grubu kan, 0 grubu hasta).","Akut hemolitik reaksiyonların çoğu kimlik doğrulama hatasından kaynaklanır."),
   T("DAT (direkt Coombs), hemoliz paneli, DİK testleri",2,30,"DAT pozitif, LDH ↑, haptoglobin ↓, serbest Hb ↑, fibrinojen düşük.","Hemoliz ve DİK."),
   A("**Transfüzyonu hemen durdur**, seti değiştir, damar yolunu SF ile açık tut; torbayı ve setleri kan bankasına gönder, numuneler al; sıvı resüsitasyonu (idrar >1 mL/kg/saat, erişkinde ≈100 mL/saat), gerekirse vazopresör; DİK ve böbrek izlemi; olayı bildir",4,10,"n2","Doğru. Akut hemolitik reaksiyonda verilen kan miktarı prognozu belirler; ilk adım durdurmak."),
   A("Ateş için parasetamol ver, transfüzyonu yavaşlatarak sürdür",-5,20,"n9","Ateş + hipotansiyon + bel ağrısı + hemoglobinüri akut hemolitik reaksiyondur; devam etmek ölümcüldür."),
   A("Antihistaminik ver, transfüzyona devam et (alerjik reaksiyon)",-4,20,"n9","Yalnız ürtiker varsa (izole hafif alerjik) duraklatma + antihistaminik sonrası sürdürülebilir; ateş ve hipotansiyon varsa asla."),
 ]),
 "n2":E("Akut hemolitik reaksiyon kontrol altında","Hasta sıvı ve kısa süreli norepinefrinle stabilize edildi; idrar çıkışı korundu, DİK izlendi. Olay kan bankasına ve hemovijilans sistemine bildirildi; ikinci hastanın torbası da durduruldu.\n\n**Akılda kalsın**\n- Transfüzyon sırasında **her yeni belirti → durdur** ve değerlendir.\n- Akut hemolitik: ateş, titreme, bel/göğüs ağrısı, hipotansiyon, **hemoglobinüri**, DİK — çoğu **kimlik hatası**.\n- Ayırıcı: febril nonhemolitik (yalnız ateş), alerjik (ürtiker), anafilaksi (IgA eksikliği), **TRALI** (6 saat içinde hipoksi, nonkardiyojenik ödem), **TACO** (hipervolemi, hipertansiyon), sepsis (kontamine ürün).\n- Torba + set + numuneler **kan bankasına**; bildir.\n\n*Kaynak: SHOT 2023; BSH transfüzyon reaksiyonları kılavuzu.*","good"),
 "n9":E("Ağır hemoliz","Transfüzyon sürdü; hasta DİK, akut böbrek yetmezliği ve şok gelişerek yoğun bakıma alındı.","bad"),
}))
Qs+=[Q("c46q1","Transfüzyon sırasında ateş, hipotansiyon ve bel ağrısı gelişirse ilk yapılacak nedir?",["Parasetamol verip devam etmek","Transfüzyonu hemen durdurmak","Hızı artırmak","Antihistaminik verip devam etmek","Furosemid vermek"],1,"Her ciddi reaksiyonda ilk adım transfüzyonu durdurmaktır.","Hematoloji"),
 Q("c46q2","Akut hemolitik transfüzyon reaksiyonlarının en sık nedeni nedir?",["Bakteriyel kontaminasyon","Kimlik doğrulama hatasına bağlı ABO uyumsuzluğu","IgA eksikliği","Sıvı yüklenmesi","Sitrat toksisitesi"],1,"Hasta-ürün eşleştirme hataları en sık nedendir.","Hematoloji"),
 Q("c46q3","Transfüzyon sonrası 6 saat içinde gelişen hipoksi, bilateral infiltrasyon ve normal/düşük KB hangisini düşündürür?",["TACO","TRALI","Febril nonhemolitik reaksiyon","Gecikmiş hemolitik reaksiyon","Hiperkalemi"],1,"TRALI nonkardiyojenik ödemdir; TACO'da hipervolemi ve hipertansiyon öndedir.","Hematoloji")]

# 47 TEMPORAL ARTERİT (DEV HÜCRELİ ARTERİT)
S.append(case("c47","Yeni başlayan baş ağrısı — 74 yaşında kadın","Romatoloji / Göz",
 "74 yaşında kadın. 3 haftadır sağ şakakta yeni başlayan baş ağrısı, saçını tararken kafa derisinde hassasiyet, yemek yerken çenesinde yorulma/ağrı. Dün sağ gözünde birkaç dakika süren görme kaybı olmuş, geçmiş. Omuzlarında sabah tutukluğu var.",
 {"n1":N("Muayene","Sağ temporal arter kalın, hassas, nabzı zayıf. Görme keskinliği iki gözde normal. Nörolojik muayene normal.","KB 152/84 · Nb 86 · Ateş 37,6",[
   T("ESH ve CRP",2,30,"**ESH 96 mm/saat**, **CRP 78 mg/L**, trombosit 480.000.","Yüksek inflamatuvar belirteçler GCA'yı destekler."),
   T("Temporal arter USG",1,30,"Sağ temporal arterde **halo işareti**.","Deneyimli merkezde ilk tanı testi olabilir; tedaviyi geciktirmez."),
   T("Beyin BT",0,30,"Normal.","İnme/kanama ayrımı için, ama tanıyı koymaz."),
   A("Görme belirtisi var: hemen **IV metilprednizolon** (500–1000 mg/gün, 3 gün), ardından oral prednizolon 1 mg/kg (en çok 60 mg); acil göz ve romatoloji; biyopsi/USG tedaviyi geciktirmeden 1–2 hafta içinde",4,15,"n2","Doğru. Geçici görme kaybı kalıcı körlüğün habercisidir."),
   A("Temporal arter biyopsisi sonucunu bekle, sonra steroid başla",-5,1440,"n9","Biyopsi steroid başladıktan sonra 1–2 hafta içinde de tanısaldır; beklemek körlük riskini artırır."),
   A("Gerilim tipi baş ağrısı — NSAİİ ile taburcu",-5,10,"n9","50 yaş üstü yeni baş ağrısı + çene kladikasyonu + görme belirtisi GCA kırmızı bayraklarıdır."),
 ]),
 "n2":E("Görme korundu","Steroid sonrası baş ağrısı 48 saatte geriledi; yeni görme kaybı olmadı. Biyopsi tanıyı doğruladı; tosilizumab eklenmesi planlandı.\n\n**Akılda kalsın**\n- **>50 yaş + yeni baş ağrısı**: GCA'yı düşün.\n- Kırmızı bayraklar: **çene kladikasyonu**, kafa derisi hassasiyeti, **geçici/ani görme kaybı**, diplopi, polimiyalji romatika.\n- **ESH/CRP**; temporal arter USG (halo) veya biyopsi.\n- **Steroid tanı testini beklemez**: görme belirtisinde IV metilprednizolon; yoksa prednizolon 40–60 mg/gün.\n\n*Kaynak: EULAR 2018; ACR/VF 2021 GCA kılavuzu; BSR 2020.*","good"),
 "n9":E("Kalıcı körlük","Hasta 2 gün sonra sağ gözde kalıcı görme kaybıyla döndü (arteritik ön iskemik optik nöropati).","bad"),
}))
Qs+=[Q("c47q1","Dev hücreli arteritte en tehlikeli komplikasyon hangisidir?",["Hipertansiyon","Kalıcı görme kaybı","Anemi","Kilo kaybı","Ateş"],1,"Arteritik ön iskemik optik nöropati kalıcı körlüğe yol açar.","Romatoloji / Göz"),
 Q("c47q2","Görme belirtisi olan GCA şüphesinde doğru yaklaşım hangisidir?",["Biyopsi sonucu gelince steroid","Hemen yüksek doz IV metilprednizolon","NSAİİ","Antikoagülan","Antibiyotik"],1,"Steroid tanı testini beklemeden başlanır.","Romatoloji / Göz"),
 Q("c47q3","GCA için en özgül klinik bulgulardan biri hangisidir?",["Çene kladikasyonu","Bulantı","Ateş","Burun akıntısı","Ishal"],0,"Çene kladikasyonu GCA olasılığını belirgin artırır.","Romatoloji / Göz")]

# 48 MALİGN HİPERTERMİ (acilde süksinilkolin sonrası)
S.append(case("c48","Entübasyondan sonra ateş — 22 yaşında erkek","Anestezi / Toksikoloji",
 "22 yaşında erkek, motosiklet kazası sonrası GKS 8 olduğu için acilde süksinilkolin ile hızlı ardışık entübasyon yapıldı. Entübasyondan 20 dakika sonra mekanik ventilatörde end-tidal CO₂ hızla yükseliyor. Ailede “anestezi sırasında ölen bir dayı” varmış.",
 {"n1":N("Entübasyondan 20 dakika sonra","Masseter ve gövde kaslarında **rijidite**. Deri sıcak, terli.","KB 162/96 · Nb 148 · **EtCO₂ 78 mmHg** (dakika ventilasyonu artırılmasına rağmen) · Ateş 39,4 (yükseliyor)",[
   T("Kan gazı, K, CK",2,10,"pH 7,08, pCO₂ 92, laktat 6, **K 6,8**, CK yükseliyor.","Hipermetabolizma: artan CO₂ üretimi, asidoz, hiperkalemi, rabdomiyoliz."),
   A("Malign hipertermi: tetikleyiciyi kes (süksinilkolin; inhalasyon anesteziği varsa kapat); %100 O₂ ile yüksek akım hiperventilasyon; **dantrolen 2,5 mg/kg IV** (yanıta göre tekrar, toplam 10 mg/kg'a kadar); aktif soğutma; hiperkalemi tedavisi (kalsiyum, insülin-glukoz); idrar çıkışı",4,10,"n2","Doğru. Dantrolen ryanodin reseptörü üzerinden kalsiyum salınımını durdurur; erken verilmesi mortaliteyi belirgin düşürür."),
   A("Ateş için parasetamol, sedasyonu derinleştir",-5,20,"n9","MH'de antipiretik etkisizdir; dantrolen gecikmesi ölümcüldür."),
   A("Kalsiyum kanal blokeri (verapamil) ile taşikardiyi kontrol et",-4,10,"n9","Dantrolen ile birlikte verapamil ağır hiperkalemi ve kardiyovasküler kollaps yapabilir; kontrendikedir."),
 ]),
 "n2":E("Dantrolen sonrası düzelme","Toplam 5 mg/kg dantrolen sonrası EtCO₂ 42'ye, ateş 37,8'e indi. Hasta yoğun bakımda 48 saat izlendi (nüks riski); aileye genetik test ve uyarı kartı önerildi.\n\n**Akılda kalsın**\n- Tetikleyiciler: **süksinilkolin, volatil anestezikler**.\n- En erken bulgu: açıklanamayan **EtCO₂ artışı**; ardından taşikardi, rijidite (masseter), hipertermi (geç), asidoz, hiperkalemi, rabdomiyoliz.\n- Tedavi: tetikleyiciyi kes, %100 O₂ hiperventilasyon, **dantrolen 2,5 mg/kg** tekrarlı, soğutma, hiperkalemi tedavisi.\n- Dantrolen ile **kalsiyum kanal blokeri verme**.\n- Aile öyküsü sorulmalı; acil serviste dantrolen erişimi olmalı.\n\n*Kaynak: EMHG 2021 malign hipertermi kılavuzu; MHAUS.*","good"),
 "n9":E("Kardiyak arrest","Hiperkalemi ve hipertermiye bağlı ventriküler fibrilasyon gelişti.","bad"),
}))
Qs+=[Q("c48q1","Malign hipertermide en erken bulgu hangisidir?",["Ateş 42 °C","Açıklanamayan end-tidal CO₂ artışı","Hipoglisemi","Bradikardi","Miyozis"],1,"Ateş geç bulgudur; artan CO₂ üretimi erkendir.","Anestezi / Toksikoloji"),
 Q("c48q2","Malign hipertermide dantrolenin başlangıç dozu hangisidir?",["0,25 mg/kg","1 mg/kg","2,5 mg/kg IV, gerekirse tekrar","10 mg tek doz","20 mg/kg"],2,"2,5 mg/kg; yanıta göre tekrar (genelde toplam 10 mg/kg'a kadar).","Anestezi / Toksikoloji"),
 Q("c48q3","Malign hipertermiyi tetikleyen ilaç hangisidir?",["Rokuronyum","Süksinilkolin","Propofol","Ketamin","Fentanil"],1,"Süksinilkolin ve volatil anestezikler tetikleyicidir.","Anestezi / Toksikoloji")]

# 49 AMNİYOTİK SIVI EMBOLİSİ (doğum sonrası kollaps)
S.append(case("c49","Acilde doğum sonrası ani kollaps — 34 yaşında kadın","Kadın doğum / Resüsitasyon",
 "34 yaşında, 3. gebeliği, 39 haftalık kadın acil servise ileri eylemde geldi ve 10 dakika içinde acilde doğurdu. Plasenta doğduktan 5 dakika sonra aniden nefes darlığı, huzursuzluk ve “öleceğim” hissi başladı, ardından bilinci bulanıklaştı.",
 {"n1":N("Doğumdan 5 dakika sonra","Siyanotik, bilinci bulanık; ardından kısa bir jeneralize nöbet. Vajinal kanama artıyor ve pıhtılaşmıyor.","KB 68/34 · Nb 140 · SpO₂ %78 · SS 32",[
   T("POCUS (kalp)",2,3,"**Sağ ventrikül belirgin dilate**, sol ventrikül küçük ve hiperdinamik.","Akut sağ ventrikül yetmezliği AFE'nin erken hemodinamik tablosudur."),
   T("Pıhtılaşma testleri (fibrinojen, PT, aPTT, trombosit; varsa ROTEM)",2,20,"**Fibrinojen 0,9 g/L**, PT uzamış, trombosit 70.000.","AFE'de DİK sık ve erken; fibrinojen hızla düşer."),
   A("Yardım çağır (kadın doğum, anestezi, kan bankası); hava yolu + %100 O₂ (entübasyon); vazopresör (norepinefrin) ± inotrop (dobutamin/milrinon) — sağ ventrikülü aşırı sıvıyla yükleme; **masif transfüzyon protokolü** (eritrosit + TDP + trombosit, erken kriyopresipitat/fibrinojen konsantresi), traneksamik asit 1 g; uterus tonusu (oksitosin, masaj)",4,15,"n2","Doğru. AFE tedavisi destekleyicidir: oksijenasyon, sağ ventrikül desteği, DİK/kanama yönetimi."),
   A("Pulmoner emboli olabilir — sistemik tromboliz",-4,15,"n9","Doğum sonrası kanama ve DİK varken tromboliz ölümcül kanamaya yol açar."),
   A("Hızla 4 litre kristaloid ver",-3,20,"n9","Aşırı sıvı dilate sağ ventrikülü kötüleştirir ve koagülopatiyi dilüsyonla derinleştirir."),
 ]),
 "n2":N("10 dakika sonra","Nabız alınamıyor; monitörde nabızsız elektriksel aktivite.","",[
   A("Yüksek kaliteli KPR; adrenalin 1 mg 3–5 dakikada bir; geri döndürülebilir nedenleri ara (kanama/hipovolemi, hipoksi); transfüzyonu sürdür; varsa ECPR (ECMO) için merkez",3,10,"n3","Doğru. AFE'de arrest sık; standart İYD + kanama kontrolü. (Doğum gerçekleştiği için uterus yer değiştirme veya perimortem sezaryen gerekmez.)"),
   A("Resüsitasyonu sonlandır — AFE ölümcüldür",-5,0,"n9","AFE'de uygun destekle sağkalım mümkündür."),
 ]),
 "n3":E("Spontan dolaşımın dönüşü","4 dakikalık KPR sonrası dolaşım döndü; masif transfüzyon ve fibrinojenle kanama kontrol edildi, hasta yoğun bakıma alındı.\n\n**Akılda kalsın**\n- AFE: doğum sırasında/hemen sonrasında **ani hipoksi + hipotansiyon/arrest + DİK** (± nöbet, bilinç değişikliği).\n- Tanı klinik ve dışlamayladır.\n- Tedavi destekleyici: **oksijenasyon**, sağ ventrikül desteği (vazopresör, inotrop; aşırı sıvıdan kaçın), **erken kan ürünleri + fibrinojen**, traneksamik asit.\n- Arrestte yüksek kaliteli KPR; doğum gerçekleşmediyse **sol uterus yer değiştirme** ve 4–5 dakikada **perimortem sezaryen**.\n\n*Kaynak: SMFM 2016 AFE kılavuzu; ERC 2021 gebelikte arrest.*","good"),
 "n9":E("Ölüm","Hasta kanama ve refrakter şokla kaybedildi.","bad"),
}))
Qs+=[Q("c49q1","Amniyotik sıvı embolisinin klasik triadı hangisidir?",["Ateş, hipertansiyon, ödem","Ani hipoksi, hipotansiyon/arrest, koagülopati (DİK)","Baş ağrısı, görme bozukluğu, proteinüri","Karın ağrısı, vajinal kanama, şok","Göğüs ağrısı, ST elevasyonu, troponin"],1,"Doğum sırasında/sonrası ani kardiyopulmoner kollaps + DİK.","Kadın doğum / Resüsitasyon"),
 Q("c49q2","AFE'de koagülopati yönetiminde öncelikli olarak izlenip yerine konan faktör hangisidir?",["Vitamin K","Fibrinojen","Albümin","Heparin","Faktör VIII tek başına"],1,"Fibrinojen hızla düşer; kriyopresipitat/fibrinojen konsantresi erken verilir.","Kadın doğum / Resüsitasyon"),
 Q("c49q3","Gebelikte (doğum olmamış, 20. hafta üzeri) kardiyak arrestte uterus nasıl yönetilir?",["Sağa itilir","Sola itilir (manuel sol uterus yer değiştirme) ve 4–5 dakikada perimortem sezaryen düşünülür","Dokunulmaz","Yalnız oksitosin verilir","Hemen tokoliz"],1,"Aortokaval basıyı azaltmak için sol yer değiştirme; ROSC yoksa resüsitatif histerotomi.","Kadın doğum / Resüsitasyon")]

# 50 KARDİYAK TAMPONAD
S.append(case("c50","Nefes darlığı ve hipotansiyon — 58 yaşında erkek","Kardiyoloji",
 "58 yaşında erkek, akciğer kanseri nedeniyle kemoterapi alıyor. 1 haftadır artan nefes darlığı, yatamıyor; bugün baş dönmesi ve halsizlik.",
 {"n1":N("Resüsitasyon alanı","Oturur pozisyonda. Boyun venleri dolgun, kalp sesleri derinden geliyor, akciğerler temiz.","KB 84/62 · Nb 126 · SS 26 · SpO₂ %93 · **Pulsus paradoksus 22 mmHg**",[
   T("12 derivasyonlu EKG",1,5,"Sinüs taşikardisi, **düşük voltaj**, **elektriksel alternans**.","Büyük perikardiyal efüzyon bulguları."),
   T("POCUS",3,5,"Büyük perikardiyal efüzyon; **sağ ventrikülde diyastolik kollaps**, sağ atriyumda sistolik kollaps; VCI pletorik.","Tamponad: ekokardiyografik tanı + klinik."),
   A("USG eşliğinde **perikardiyosentez** (subksifoid veya apikal; perikardiyal kateter bırak); hazırlanırken küçük sıvı bolusu (≈500 mL) köprü olabilir; kardiyoloji",4,20,"n2","Doğru. Tamponadın kesin tedavisi drenajdır; birkaç yüz mL boşaltmak bile hemodinamiyi düzeltir."),
   A("Akciğer ödemi değil mi? Furosemid + nitrat",-5,10,"n9","Ön yükü azaltan ilaçlar tamponadda kardiyak debiyi daha da düşürür."),
   A("Hemen entübe edip pozitif basınçlı ventilasyon",-3,15,"n9","Pozitif basınç venöz dönüşü azaltır; tamponadlı hastada entübasyon sırasında kollaps riski çok yüksek — mümkünse önce drenaj."),
 ]),
 "n2":E("Perikardiyosentez","USG eşliğinde 650 mL hemorajik sıvı boşaltıldı; KB 122/76'ya yükseldi, pulsus paradoksus kayboldu. Malign efüzyon için perikardiyal pencere planlandı.\n\n**Akılda kalsın**\n- **Beck triadı**: hipotansiyon, JVD, derinden gelen kalp sesleri; **pulsus paradoksus >10 mmHg**.\n- EKG: düşük voltaj, **elektriksel alternans**.\n- POCUS: efüzyon + **sağ kalp boşluklarında diyastolik kollaps**, pletorik VCI.\n- Tedavi: **perikardiyosentez** (USG eşliğinde); travmada torakotomi.\n- Diüretik/vazodilatör yok; pozitif basınçlı ventilasyon tehlikeli.\n\n*Kaynak: ESC 2015 perikard hastalıkları kılavuzu.*","good"),
 "n9":E("Kardiyak arrest","Hasta nabızsız elektriksel aktiviteye girdi; acil perikardiyosentezle dolaşım ancak dönebildi.","bad"),
}))
Qs+=[Q("c50q1","Beck triadı hangisidir?",["Ateş, sarılık, ağrı","Hipotansiyon, juguler venöz dolgunluk, derinden gelen kalp sesleri","Hipertansiyon, bradikardi, düzensiz solunum","Taşikardi, taşipne, ateş","Raller, S3, ödem"],1,"Kardiyak tamponadın klasik bulguları.","Kardiyoloji"),
 Q("c50q2","Kardiyak tamponadda EKG'de hangi bulgu görülebilir?",["Delta dalgası","Elektriksel alternans","Sivri T","Epsilon dalgası","Brugada paterni"],1,"Kalbin sıvı içinde salınımı QRS amplitüdünü vuru-vuru değiştirir.","Kardiyoloji"),
 Q("c50q3","Tamponadlı hipotansif hastada hangisi kaçınılması gereken bir tedavidir?",["Perikardiyosentez","Küçük sıvı bolusu","Furosemid","Oksijen","USG eşliğinde drenaj"],2,"Ön yükü azaltmak debiyi düşürür.","Kardiyoloji")]

P={"id":"ilk-nobet-5","title":"İlk Nöbet Vakaları — 5. Paket","desc":"Akut ekstremite iskemisi, Boerhaave, serotonin sendromu, invajinasyon, gazlı gangren, transfüzyon reaksiyonu, temporal arterit, malign hipertermi, amniyotik sıvı embolisi, kardiyak tamponad.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 5. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 5. Paket","topic":"Acil tıp","order":5,"req":[2],"desc":"Atlanırsa öldüren, daha az sık 10 acil tablo.","intro":INTRO}}
build(P,sys.argv[1])
