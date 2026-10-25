import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Önce **ilk değerlendirme** (muayene, monitör, damar yolu, oksijen) — gereksiz girişim puan kaybettirir.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 111 EL-BİLEK TRAVMASI — skafoid
S.append(case("c111","Düşme sonrası bilek ağrısı — 23 yaşında erkek","Ortopedi / El",
 "23 yaşında erkek. Futbol oynarken gergin el üzerine düştü. Sağ bilekte başparmak tarafında ağrı; hafif şişlik.",
 {"n1":N("Muayene","Belirgin deformite yok. **Anatomik enfiye çukurunda hassasiyet**, skafoid tüberkülünde hassasiyet ve başparmağın aksiyel yüklenmesinde ağrı. Nörovasküler muayene normal.","KB 124/76 · Nb 82 · SpO₂ %99",[
   T("El bileği grafisi + skafoid grafileri (4 yön)",2,15,"Kırık hattı **görülmüyor**.","İlk grafilerde skafoid kırıklarının önemli bir kısmı görünmez."),
   T("Bilek MR (ulaşılabiliyorsa)",2,120,"Skafoid belinde **non-deplase kırık**.","NICE: ilk grafi negatif ve klinik şüphe varsa MR ilk tercih (yoksa tespit + 10–14 gün sonra tekrar)."),
   A("Klinik skafoid kırığı şüphesi: **başparmak dahil atel/alçı** ile immobilizasyon, analjezi; MR veya 10–14 gün sonra tekrar değerlendirme için ortopedi/el polikliniği",4,10,"n2","Doğru. Grafi normal olsa da klinik şüphede immobilize edilir."),
   A("Grafi normal — elastik bandaj, NSAİİ, taburcu",-4,10,"n9","Kaçırılan skafoid kırığı kaynamama ve avasküler nekroz riski taşır."),
 ]),
 "n2":E("Uygun takip","Kırık skafoid belinde non-deplase; 8 hafta alçıyla kaynadı.\n\n**Akılda kalsın**\n- **Enfiye çukuru hassasiyeti**, skafoid tüberkül hassasiyeti, başparmak aksiyel yük ağrısı → skafoid kırığı şüphesi.\n- İlk grafide görülmeyebilir: **immobilize et** ve **MR** (ya da 10–14 günde tekrar grafi/BT).\n- Proksimal kutup kanlanması retrograddır → **kaynamama ve avasküler nekroz** riski.\n\n*Kaynak: NICE NG38 (kırıklar, kompleks olmayan); BSSH skafoid önerileri.*","good"),
 "n9":E("Kaynamama","Üç ay sonra ağrı sürünce çekilen BT'de kaynamamış skafoid kırığı ve proksimal kutupta avasküler nekroz saptandı; cerrahi gerekti.","bad"),
}))
Qs+=[Q("c111q1","Skafoid kırığı için en önemli muayene bulgusu hangisidir?",["Ulnar stiloid hassasiyeti","Anatomik enfiye çukuru hassasiyeti","Hipotenar hassasiyet","5. metakarp hassasiyeti","Dirsek ağrısı"],1,"Skafoid tüberkül hassasiyeti ve aksiyel yük ağrısı da eklenir.","Ortopedi / El"),
 Q("c111q2","Grafisi normal ama klinik şüphe olan hastada yaklaşım hangisidir?",["Taburcu","İmmobilizasyon ve MR/tekrar değerlendirme","Elastik bandaj","Fizik tedavi","Steroid enjeksiyonu"],1,"Kaçırılan kırık ciddi komplikasyon yapar.","Ortopedi / El"),
 Q("c111q3","Skafoid kırığının en korkulan komplikasyonu hangisidir?",["Kompartman sendromu","Proksimal kutup avasküler nekrozu","Yağ embolisi","Tendon yırtığı","Raynaud"],1,"Kanlanma distalden proksimale doğrudur.","Ortopedi / El")]

# 112 PARONİŞİ
S.append(case("c112","Tırnak kenarında şişlik — 35 yaşında kadın","Cerrahi / Deri",
 "35 yaşında kadın, aşçı. 3 gündür sağ işaret parmağında tırnak yanında artan ağrı, kızarıklık ve şişlik. Tırnak etlerini koparma alışkanlığı var.",
 {"n1":N("Muayene","Lateral tırnak kıvrımında kızarık, gergin, **fluktuasyon veren sarı birikim**. Parmak pulpası yumuşak; kızarıklık parmağa yayılmamış; vezikül yok. Fleksör kılıf bulguları yok.","Ateş 36,8 · Nb 78 · KB 122/74 · SpO₂ %99",[
   T("Parmak grafisi",0,15,"Normal.","Basit paronişide gerekmez; yabancı cisim/osteomiyelit şüphesinde."),
   A("**Akut paronişi + apse**: dijital blok, eponişyumun bistüri sırtı/ucu ile kaldırılarak **drenaj**; ılık su ile günde 3–4 kez pansuman; selülit yoksa rutin antibiyotik gerekmez",4,15,"n2","Doğru. Apse varsa tedavinin esası drenajdır."),
   A("Yalnız oral antibiyotik, drenaj yok",-2,10,"n3","Apsede antibiyotik tek başına yetersiz."),
   A("Pulpaya balık ağzı insizyon",-3,15,"n9","Paronişi tırnak kıvrımı enfeksiyonudur; pulpa insizyonu gereksiz hasar yapar."),
 ]),
 "n3":N("3 gün sonra","Ağrı ve şişlik artmış, birikim büyümüş.","Ateş 37,4",[
   A("Drenaj",2,15,"n4","Gecikmeli ama doğru."),
   A("Antibiyotiği değiştir",-2,10,"n9","Drenaj yapılmadan iyileşmez."),
 ]),
 "n2":E("İyileşme","Drenaj sonrası ağrı hemen azaldı; 5 günde iyileşti.\n\n**Akılda kalsın**\n- Akut paronişi: genellikle *S. aureus*/streptokok; **apse varsa drenaj**.\n- Apse yoksa ılık pansuman ± topikal/oral antibiyotik.\n- **Herpetik dolama** (veziküller) **insize edilmez**!\n- Fleksör tenosinovit bulguları (Kanavel) ve **felon** (pulpa apsesi) ayırt edilmeli.\n- Kronik paronişi: ıslak işte çalışma, irritan; kandidal/irritan dermatit.\n\n*Kaynak: Am Fam Physician 2017 — Acute and chronic paronychia.*","good"),
 "n4":E("Gecikmeli iyileşme","Drenaj sonrası düzeldi, ancak 3 gün iş kaybı oldu.","mid"),
 "n9":E("Komplikasyon","Gereksiz/yanlış girişim sonrası enfeksiyon yayıldı; el cerrahisi gerekti.","bad"),
}))
Qs+=[Q("c112q1","Apseli akut paronişide temel tedavi hangisidir?",["Yalnız antibiyotik","Drenaj","Steroid","Antifungal","Tırnak çekimi zorunlu"],1,"Eponişyum kaldırılarak drenaj.","Cerrahi / Deri"),
 Q("c112q2","Hangi durumda parmak lezyonu insize edilmemelidir?",["Paronişi apsesi","Herpetik dolama","Felon","Sebase kist","Yabancı cisim"],1,"İnsizyon viral yayılım ve süperenfeksiyon riski taşır.","Cerrahi / Deri"),
 Q("c112q3","Fleksör tenosinovit için Kanavel bulgusu hangisidir?",["Pasif ekstansiyonda ağrı","Tırnak altı hematom","Veziküller","Kaşıntı","Tırnak çizgileri"],0,"Fusiform şişlik, hafif fleksiyon pozisyonu, kılıf boyunca hassasiyet.","Cerrahi / Deri")]

# 113 PNÖMOTORAKS — sekonder (KOAH)
S.append(case("c113","KOAH'lı hastada ani nefes darlığı — 68 yaşında erkek","Göğüs hastalıkları",
 "68 yaşında erkek, ağır KOAH (evde inhaler). 3 saat önce öksürük nöbeti sonrası ani sol göğüs ağrısı ve belirgin nefes darlığı başladı.",
 {"n1":N("Muayene","Konuşurken nefesi kesiliyor, yardımcı solunum kasları aktif. **Solda solunum sesleri belirgin azalmış**, hiperrezonans. Trakea orta hatta, boyun venleri normal.","KB 146/88 · Nb 112 · SS 28 · SpO₂ %86 (oda havası)",[
   T("Akciğer grafisi",3,15,"**Sol pnömotoraks**, apeks-kubbe mesafesi ≈4 cm; amfizematöz akciğerler; mediasten kayması yok.","Sekonder pnömotoraks — altta yatan akciğer hastalığı."),
   T("Kan gazı",1,10,"pH 7,33 · pCO₂ 56 · pO₂ 52.","Hiperkapni: oksijen hedefi %88–92."),
   A("**Sekonder spontan pnömotoraks, semptomatik**: kontrollü O₂ (hedef SpO₂ %88–92); **küçük çaplı göğüs tüpü** (Seldinger); yatış; göğüs cerrahisi/göğüs hastalıkları",4,20,"n2","Doğru. BTS 2023: semptomatik sekonder pnömotoraksta göğüs tüpü ve yatış."),
   A("Konservatif izlem, taburcu",-5,10,"n9","Sekonder pnömotoraks kötü tolere edilir; mortalite belirgin."),
   A("Rezervuarlı maskeyle %100 O₂ ve izlem",-2,20,"n3","Hiperkapnik KOAH'ta yüksek akım O₂ CO₂ retansiyonunu artırır; drenaj da yapılmadı."),
 ]),
 "n3":N("1 saat sonra","Uykuya meyilli, pCO₂ 72.","SpO₂ %97 · SS 14",[
   A("O₂'yi hedef %88–92'ye düşür, göğüs tüpü tak, gerekirse NIV (dren takıldıktan sonra)",2,20,"n4","Doğru düzeltme."),
   A("O₂'yi sürdür, izle",-4,30,"n9","Hiperkapnik koma gelişir."),
 ]),
 "n2":E("Düzelme","Tüp sonrası akciğer ekspanse oldu; hava kaçağı 3 günde kesildi. Nüks önleme için göğüs cerrahisi ile görüşüldü.\n\n**Akılda kalsın**\n- **Sekonder** pnömotoraks (KOAH, kistik fibrozis vb.): küçük pnömotoraks bile ağır semptom yapar.\n- Semptomatik → **küçük çaplı göğüs tüpü**, yatış; nüks önleme (plörodez/cerrahi) değerlendirilir.\n- Hiperkapni riskinde **O₂ hedefi %88–92** (Venturi).\n- Pnömotoraks drene edilmeden **NIV/pozitif basınç** tehlikelidir.\n\n*Kaynak: BTS 2023 plevral hastalık kılavuzu; BTS O₂ kılavuzu.*","good"),
 "n4":E("Geç düzelme","Dren ve kontrollü O₂ ile düzeldi; ancak hiperkapni nedeniyle 2 gün yoğun bakımda kaldı.","mid"),
 "n9":E("Solunum yetmezliği","Hasta hiperkapnik solunum yetmezliğiyle entübe edildi.","bad"),
}))
Qs+=[Q("c113q1","Semptomatik sekonder spontan pnömotoraksta yaklaşım hangisidir?",["Konservatif izlem ve taburcu","Göğüs tüpü ve yatış","Yalnız analjezi","Yüksek akım O₂ ile taburcu","Fizik tedavi"],1,"Altta yatan hastalık toleransı azaltır.","Göğüs hastalıkları"),
 Q("c113q2","Hiperkapni riski olan KOAH hastasında O₂ hedefi nedir?",["%100","%94–98","%88–92","%80–85","Önemsiz"],2,"Fazla O₂ CO₂ retansiyonunu artırır.","Göğüs hastalıkları"),
 Q("c113q3","Drene edilmemiş pnömotoraksta hangisinden kaçınılmalıdır?",["Göğüs tüpü","Pozitif basınçlı ventilasyon/NIV","Analjezi","O₂","Grafi"],1,"Tansiyon pnömotoraksa dönebilir.","Göğüs hastalıkları")]

# 114 ANJİOÖDEM — ACE inhibitörü
S.append(case("c114","Dil ve dudakta şişlik — 59 yaşında erkek","Hava yolu / Alerji",
 "59 yaşında erkek. 2 yıldır ramipril kullanıyor. Sabah uyandığında dil ve alt dudakta şişlik fark etmiş; giderek artıyor, konuşması bozuldu. Kaşıntı ya da döküntü yok.",
 {"n1":N("Muayene","Dil belirgin ödemli, ağız tabanı ödemi; **ürtiker ve kaşıntı yok**. Hafif ses değişikliği; stridor yok. Salya biriktiriyor.","KB 152/90 · Nb 94 · SS 20 · SpO₂ %97",[
   T("Yatak başı nazofaringolaringoskopi (fiberoptik)",3,10,"Dil kökü ve **ariepiglottik plikalarda ödem**; glottis görülüyor, açıklık daralmış.","Larinks tutulumu yüksek risk."),
   T("Serum triptaz",0,60,"Normal.","Mast hücre aracılı olmadığını destekler ama kararı geciktirmemeli."),
   A("**Bradikinin aracılı anjiyoödem**: ACE inhibitörünü kes; **zor hava yolu hazırlığı** (anestezi + KBB; uyanık fiberoptik entübasyon, cerrahi hava yolu seti); yoğun izlem; ikatibant/C1-inhibitör/TDP düşünülebilir (kanıt sınırlı); adrenalin denenebilir ama yanıt beklenmez",4,15,"n2","Doğru. Antihistaminik ve steroid etkisizdir; asıl risk hava yolu."),
   A("Anafilaksi tedavisi (antihistaminik + steroid) verip 2 saat izle, sonra taburcu",-4,30,"n9","Histamin aracılı değildir; ödem 24–48 saat ilerleyebilir."),
   A("Hemen hızlı ardışık entübasyon (RSI), direkt laringoskopi",-2,10,"n3","Ödemli hava yolunda RSI 'entübe edilemez–oksijenlenemez' durumuna yol açabilir; uyanık fiberoptik tercih edilir."),
 ]),
 "n3":N("Başarısız laringoskopi","Glottis görülemiyor; SpO₂ düşüyor.","SpO₂ %82",[
   A("Krikotirotomi (skalpel-buji-tüp)",1,5,"n4","Entübe edilemez–oksijenlenemez: cerrahi hava yolu."),
   A("Tekrar laringoskopi dene",-5,5,"n9","Her deneme ödemi artırır."),
 ]),
 "n2":E("Güvenli hava yolu","Ödem 6 saat boyunca arttı; anestezi ekibi uyanık fiberoptik entübasyon yaptı. 48 saatte ödem geriledi, ekstübe edildi. ACE inhibitörü kalıcı olarak kesildi.\n\n**Akılda kalsın**\n- ACEi anjiyoödemi **bradikinin aracılıdır**: ürtiker ve kaşıntı yok; ilacı yıllardır kullanırken de çıkabilir.\n- **Antihistaminik ve steroid etkisiz**; adrenalin sınırlı.\n- Öncelik **hava yolu**: erken uzman, **uyanık fiberoptik entübasyon**, cerrahi hava yolu hazır.\n- İkatibant / C1-INH / TDP (kanıt sınırlı); **ACEi ömür boyu kesilir**.\n\n*Kaynak: EAACI/WAO kalıtsal ve edinsel anjiyoödem önerileri; Difficult Airway Society.*","good"),
 "n4":E("Cerrahi hava yolu","Krikotirotomi ile oksijenasyon sağlandı; hasta yoğun bakımda iyileşti.","mid"),
 "n9":E("Hava yolu kaybı","Hasta evde/gözlemde stridor ve hipoksiyle arrest oldu.","bad"),
}))
Qs+=[Q("c114q1","ACE inhibitörüne bağlı anjiyoödemin aracısı hangisidir?",["Histamin","Bradikinin","IgE","Lökotrien","Serotonin"],1,"Bu nedenle antihistaminik/steroid etkisizdir.","Hava yolu / Alerji"),
 Q("c114q2","ACEi anjiyoödemini anafilaksiden ayıran bulgu hangisidir?",["Ürtiker ve kaşıntının olmaması","Hipotansiyon","Wheezing","Kızarıklık","Kusma"],0,"Bradikinin aracılı ödem ürtikersizdir.","Hava yolu / Alerji"),
 Q("c114q3","İlerleyici dil/larinks ödeminde tercih edilen hava yolu yöntemi hangisidir?",["RSI ile direkt laringoskopi","Uyanık fiberoptik entübasyon (cerrahi hava yolu hazır)","Nazal kanül","LMA","Bekle-gör"],1,"Ödemli hava yolunda spontan solunum korunur.","Hava yolu / Alerji")]

# 115 BOKSÖR KIRIĞI + kavga ısırığı
S.append(case("c115","Kavga sonrası el ağrısı — 24 yaşında erkek","Ortopedi / El",
 "24 yaşında erkek. Dün gece kavgada birine yumruk attı. Sağ elin dış tarafında ağrı ve şişlik; 5. parmak eklem üzerinde küçük bir yara.",
 {"n1":N("Muayene","5. metakarp başında hassasiyet, eklem çıkıntısı silik. Yumruk yapınca **5. parmak 4. parmağın altına kayıyor (makaslama)**. 5. MKF ekleminin üzerinde **4 mm laserasyon**, kenarları kızarık. Nörovasküler muayene normal.","KB 132/80 · Nb 84 · SpO₂ %99 · Ateş 37,1",[
   T("El grafisi (AP, oblik, lateral)",2,15,"**5. metakarp boyun kırığı**, 35° volar açılanma; eklem içine uzanım yok, yabancı cisim (diş) yok.","Boyunda açılanmanın tolere edilebilir sınırı genişse de **rotasyon kusuru tolere edilmez**."),
   T("Yaranın eklem hareketiyle muayenesi",2,5,"Yumruk pozisyonunda yara, **ekstansör tendon ve eklem kapsülü hizasında**; tendon kılıfında küçük kesi.","Kavga ısırığı: diş eklem içine ulaşmış olabilir."),
   A("**Kavga ısırığı (closed fist injury)**: yara yıkama, **amoksisilin-klavulanat** (penisilin alerjisinde alternatif), tetanoz; **el cerrahisi** — eklem eksplorasyonu/irrigasyon ve rotasyon kusuru nedeniyle kırığın tespiti; ulnar oluklu atel",4,20,"n2","Doğru. Rotasyon kusuru ve olası septik artrit el cerrahisini gerektirir."),
   A("Yarayı primer sütürle kapat, ulnar atel, kontrol",-4,15,"n9","Isırık yarası kapatılmaz; eklem enfeksiyonu riski."),
   A("Boksör kırığı — açılanma tolere edilir, askı ve analjezik",-3,10,"n9","Rotasyon kusuru ve kavga ısırığı atlandı."),
 ]),
 "n2":E("Uygun tedavi","El cerrahisi eklemi yıkadı, kırık perkütan tellerle tespit edildi. Enfeksiyon gelişmedi, el fonksiyonu tam düzeldi.\n\n**Akılda kalsın**\n- 5. metakarp boyun kırığında **rotasyon kusuru (makaslama)** her zaman kontrol edilir; varsa redüksiyon/tespit.\n- MKF üzerinde yara + yumruk öyküsü = **kavga ısırığı**: polimikrobiyal (*Eikenella*, streptokok, anaerob) → **amoksisilin-klavulanat**, kapatma, **el cerrahisi**.\n- Yarayı **yumruk pozisyonunda** muayene et (tendon yarası parmak açıkken kayar).\n\n*Kaynak: BSSH; IDSA 2014 deri ve yumuşak doku enfeksiyonları kılavuzu.*","good"),
 "n9":E("Septik artrit","İki gün sonra MKF ekleminde septik artrit gelişti; cerrahi debridman ve uzun antibiyotik gerekti, eklem hareketi kısıtlı kaldı.","bad"),
}))
Qs+=[Q("c115q1","Metakarp kırığında asla tolere edilmeyen bulgu hangisidir?",["Hafif volar açılanma","Rotasyon kusuru (makaslama)","Şişlik","Ekimoz","Ağrı"],1,"Fonksiyonel kayıp yapar.","Ortopedi / El"),
 Q("c115q2","Kavga ısırığında (closed fist injury) ampirik antibiyotik hangisidir?",["Sefaleksin","Amoksisilin-klavulanat","Siprofloksasin","Metronidazol","Antibiyotik gerekmez"],1,"Eikenella ve anaeroblar kapsanmalı.","Ortopedi / El"),
 Q("c115q3","MKF eklemi üzerindeki kavga ısırığı yarası nasıl yönetilir?",["Primer sütür","Kapatılmaz; yıkama, antibiyotik, el cerrahisi","Yalnız pansuman","Steroid","Doku yapıştırıcı"],1,"Eklem ve tendon tutulumu araştırılır.","Ortopedi / El")]

# 116 KALP YETMEZLİĞİ — akut dekompanse (ıslak-sıcak)
S.append(case("c116","Bacaklarda şişlik ve nefes darlığı — 70 yaşında erkek","Kardiyoloji",
 "70 yaşında erkek; iskemik kalp yetmezliği (EF %30). Evde furosemid 40 mg/gün kullanıyor. 10 gündür giderek artan nefes darlığı, ortopne, bacaklarda şişlik; 5 kg almış. Bayramda tuzlu yemek yemiş.",
 {"n1":N("Muayene","Oturur pozisyonda, cümle kurabiliyor. Juguler venöz dolgunluk, bibaziler raller, diz hizasına kadar **gode bırakan ödem**. Ekstremiteler sıcak.","KB 138/82 · Nb 98 · SS 24 · SpO₂ %92",[
   T("Akciğer grafisi + akciğer USG",2,15,"Kardiyomegali, bilateral plevral efüzyon; USG'de yaygın **B çizgileri**.","Konjesyon."),
   T("NT-proBNP, kreatinin, elektrolit, troponin",2,60,"NT-proBNP 8.400; kreatinin 1,4 (bazal 1,2); K 4,2; troponin hafif, düz seyir.","Tetikleyiciler araştırılır (iskemi, aritmi, enfeksiyon, uyumsuzluk)."),
   T("EKG",1,5,"Sinüs; eski Q dalgaları; yeni iskemik değişiklik yok.","AKS ve aritmi dışlanır."),
   A("**Islak-sıcak ADHF**: oturur pozisyon, O₂ (hedef %94–98); **IV furosemid** — evdeki oral dozun 1–2 katı (ör. 80 mg IV); **2. saatte spot idrar Na** (<50–70 mmol/L → dozu iki katına çıkar) ve 6. saatte idrar çıkışı (<100–150 mL/saat → artır); günlük kilo, K/kreatinin; tuz/sıvı danışmanlığı",4,20,"n2","Doğru. ESC 2021/2023: natriürez yanıtına göre diüretik titrasyonu."),
   A("Furosemid 20 mg oral, taburcu",-3,10,"n9","Belirgin konjesyon; düşük oral doz yetersiz."),
   A("Dobutamin infüzyonu",-3,20,"n9","Perfüzyon iyi (sıcak, KB normal); inotrop endike değil ve aritmi riski."),
 ]),
 "n2":E("Dekonjesyon","İlk 2 saatte idrar Na 92 mmol/L, ilk 6 saatte 1,4 L idrar; 4 günde 5 kg verdi. Taburculukta kılavuz ilaçları (ARNI, beta bloker, MRA, SGLT2i) optimize edildi.\n\n**Akılda kalsın**\n- Profil: **ıslak/kuru – sıcak/soğuk**. Islak-sıcak: diüretik ± vazodilatör.\n- IV furosemid: **oral dozun 1–2 katı**; **2. saat idrar Na <50–70** veya **6. saat idrar <100–150 mL/saat** → yanıt yetersiz, doz artır / ardışık nefron blokajı (tiyazid, asetazolamid).\n- Tetikleyicileri ara (**CHAMPIT**: AKS, hipertansiyon, aritmi, mekanik, PE, enfeksiyon, tamponad) ve uyumsuzluk.\n\n*Kaynak: ESC 2021 KY kılavuzu ve 2023 güncellemesi; HFA 2019 diüretik bildirisi.*","good"),
 "n9":E("Kötüleşme","Hasta 2 gün sonra akciğer ödemiyle döndü / aritmi gelişti; yoğun bakım gerekti.","bad"),
}))
Qs+=[Q("c116q1","Akut dekompanse KY'de IV furosemid başlangıç dozu nasıl seçilir?",["Her hastada 10 mg","Evdeki oral dozun 1–2 katı","Oral dozun yarısı","Yalnız kiloya göre 5 mg/kg","Verilmez"],1,"ESC 2021 önerisi.","Kardiyoloji"),
 Q("c116q2","Diüretik yanıtının erken göstergesi hangisidir?",["2. saatte spot idrar Na >50–70 mmol/L","24. saatte kilo","Ateş","Laktat","Troponin"],0,"Düşükse doz artırılır.","Kardiyoloji"),
 Q("c116q3","'Islak-sıcak' profilde hangisi uygun değildir?",["Diüretik","Gerekirse vazodilatör","Rutin inotrop","Oturur pozisyon","O₂ (hipoksemide)"],2,"İnotrop hipoperfüzyonda (soğuk) düşünülür.","Kardiyoloji")]

# 117 EPİLEPSİ — bilinen hastada tek nöbet
S.append(case("c117","Bilinen epilepsi, nöbet geçirdi — 27 yaşında kadın","Nöroloji",
 "27 yaşında kadın. 10 yıldır epilepsi, levetirasetam 1000 mg günde iki kez. 2 gündür gastroenterit nedeniyle ilaçlarını kusmuş. Bugün evde 2 dakikalık jeneralize nöbet geçirmiş; ambulansla geldi. Başını çarpmamış.",
 {"n1":N("Muayene","Tamamen uyanık ve oryante (GKS 15), dil lateralinde ısırık. Fokal nörolojik bulgu yok. Kafa travması bulgusu yok.","KB 124/76 · Nb 92 · SS 16 · SpO₂ %98 · Ateş 37,0 · Kapiller glukoz 98",[
   T("Gebelik testi",2,15,"Negatif.","Doğurganlık çağındaki kadında ilaç seçimi ve eklampsi açısından."),
   T("Elektrolitler (Na, Ca, Mg)",1,40,"Na 136, Ca ve Mg normal.","Kusma sonrası elektrolit bozukluğu dışlanır."),
   T("Beyin BT",-2,30,"Normal.","Bilinen epilepside, tipik nöbet, tam düzelme, travma ve yeni bulgu yoksa rutin BT gerekmez."),
   T("Levetirasetam düzeyi",0,240,"Düşük.","Klinik karar için gerekli değil."),
   A("Tetikleyici açık (ilaç alınamaması): antiemetik, oral hidrasyon; **evdeki levetirasetamı yeniden başla** (kusma sürerse IV verilebilir); nöbet güvenliği ve araç kullanma uyarısı; nöroloji polikliniği",4,10,"n2","Doğru. Tipik, provoke nöbette yükleme ve görüntüleme rutin değildir."),
   A("Fenitoin 20 mg/kg IV yükleme",-3,30,"n9","Gereksiz ve yeni ilaç ekleme; etkileşim ve yan etki."),
 ]),
 "n2":E("Taburcu","Kusması geçti, ilacını aldı; 4 saat gözlemde yeni nöbet olmadı, uyarılarla taburcu edildi.\n\n**Akılda kalsın**\n- Bilinen epilepside tek, tipik nöbet: **tetikleyiciyi bul** (ilaç uyumsuzluğu, uykusuzluk, alkol, enfeksiyon, ilaç etkileşimi).\n- **Glukoz** ve doğurganlık çağında **gebelik testi**.\n- Rutin BT gereksiz: **yeni fokal bulgu, travma, antikoagülan, uzamış konfüzyon, ateş, farklı nöbet tipi** varsa görüntüle.\n- Hastaya **araç kullanma**, yüzme, yükseklik uyarıları.\n\n*Kaynak: ACEP 2014 nöbet klinik politikası; NICE NG217.*","good"),
 "n9":E("Komplikasyon","Gereksiz fenitoin yüklemesi sonrası hipotansiyon ve ataksi gelişti; hasta gece yatırıldı.","bad"),
}))
Qs+=[Q("c117q1","Bilinen epilepsisi olan, tam düzelen ve travması olmayan hastada rutin beyin BT gerekli midir?",["Her zaman","Hayır, yeni bulgu/kırmızı bayrak yoksa gerekmez","Yalnız kadınlarda","Yalnız gece","Her nöbette MR"],1,"Görüntüleme kırmızı bayrağa göre.","Nöroloji"),
 Q("c117q2","Nöbet geçiren doğurganlık çağındaki kadında yapılması gereken test hangisidir?",["Gebelik testi","Troponin","Lipaz","TSH","D-dimer"],0,"Eklampsi ve ilaç seçimi açısından.","Nöroloji"),
 Q("c117q3","Epileptik hastada nöbetin en sık tetikleyicisi hangisidir?",["Antiepileptik ilaç uyumsuzluğu/alınamaması","Kahve","Egzersiz","Soğuk hava","Yüksek protein"],0,"Uykusuzluk ve alkol de sıktır.","Nöroloji")]

# 118 STATUS EPİLEPTİKUS — benzodiazepine dirençli
S.append(case("c118","Durmayan nöbet, iki doz midazolam sonrası — 52 yaşında erkek","Nöroloji",
 "52 yaşında erkek. Alkol kullanım öyküsü. Evde başlayan jeneralize nöbet; paramedik 10 mg IM midazolam yapmış. Acilde 10 mg IV diazepam verildi; nöbet 20. dakikada hâlâ sürüyor. Yaklaşık 80 kg.",
 {"n1":N("Status","Jeneralize tonik-klonik aktivite sürüyor. Damar yolu var. Ağızda sekresyon.","KB 172/98 · Nb 136 · SpO₂ %90 · Ateş 37,9 · Kapiller glukoz 112",[
   T("Kan gazı + elektrolit (Na, Ca, Mg)",1,10,"pH 7,18 (laktik), Na 134, Ca ve Mg normal.","Laktik asidoz nöbetle beklenir."),
   A("**Benzodiazepine dirençli SE — 2. basamak** (ESETT): **levetirasetam 60 mg/kg IV (en çok 4500 mg) 10 dakikada** ya da valproat 40 mg/kg (en çok 3000 mg) ya da fosfenitoin 20 mg FE/kg; **tiamin 500 mg IV** (alkol); hava yolu, aspirasyon, O₂",4,10,"n2","Doğru. Üç ajan eşit etkinlikte; ikinci basamak gecikmeden."),
   A("Üçüncü doz diazepam",-2,5,"n3","İki dozdan sonra ek benzodiazepinin etkisi azdır; solunum depresyonu artar."),
   A("Beyin BT'ye götür, sonra karar ver",-4,30,"n9","Nöbet sürerken görüntülemeye gitmek tedaviyi geciktirir."),
 ]),
 "n3":N("Nöbet sürüyor","Solunum yüzeyelleşti, nöbet devam ediyor (30. dk).","SpO₂ %85 · SS 8",[
   A("Levetirasetam 60 mg/kg IV + hava yolu desteği",2,10,"n2","Gecikmeli 2. basamak."),
   A("Bekle",-5,20,"n9","Uzayan status nöronal hasar yapar."),
 ]),
 "n2":N("Levetirasetam sonrası","Infüzyon bitiminden 10 dakika sonra nöbet hâlâ sürüyor (40. dk): **refrakter SE**.","KB 158/90 · Nb 128 · SpO₂ %88",[
   A("**3. basamak**: RSI ile entübasyon (ör. ketamin/propofol + roküronyum), **midazolam ya da propofol infüzyonu**; sürekli EEG; nöroloji ve yoğun bakım; nedeni araştır (BT, LP gerekirse, toksik/metabolik)",4,20,"n4","Doğru. Refrakter SE'de anestezik ajan ve EEG izlemi."),
   A("İkinci bir 2. basamak ilaç (valproat 40 mg/kg) ve izlem",1,15,"n5","Kabul edilebilir bir ara adım; ama hava yolu ve anestezik hazırlık ertelenmemeli."),
   A("Fenitoin 20 mg/kg ekle, entübasyonu ertele",-2,30,"n9","Refrakter SE'de zaman kaybı."),
 ]),
 "n4":E("Nöbet kontrolü","Propofol infüzyonu ve sürekli EEG ile nöbet aktivitesi durdu; BT'de eski kontüzyon sekeli dışında bulgu yoktu; alkol yoksunluğu ile tetiklenmiş SE olarak değerlendirildi.\n\n**Akılda kalsın**\n- **0–5 dk** stabilize, glukoz; **5–20 dk** benzodiazepin (IM midazolam 10 mg / IV lorazepam 0,1 mg/kg / IV diazepam 0,15–0,2 mg/kg) — en çok 2 doz.\n- **20–40 dk** 2. basamak: **levetirasetam 60 mg/kg** (≤4500) / **valproat 40 mg/kg** (≤3000) / **fosfenitoin 20 mg FE/kg**.\n- **>40 dk** refrakter: entübasyon + **midazolam/propofol/(tiyopental)** infüzyonu, **sürekli EEG**.\n- Alkol/malnütrisyonda **tiamin**.\n\n*Kaynak: AES 2016 kılavuzu; ESETT (NEJM 2019); NCS 2012.*","good"),
 "n5":E("Geç kontrol","Valproat sonrası nöbet kısa süre durdu, sonra tekrarladı; sonunda entübe edilip propofol başlandı. Yoğun bakımda kalış uzadı.","mid"),
 "n9":E("Uzamış status","Nöbet 90 dakika sürdü; hasta aspirasyon pnömonisi ve hipoksik beyin hasarıyla yoğun bakıma alındı.","bad"),
}))
Qs+=[Q("c118q1","Benzodiazepine dirençli statusta levetirasetam dozu nedir?",["10 mg/kg","20 mg/kg","60 mg/kg (en çok 4500 mg)","100 mg/kg","500 mg sabit"],2,"ESETT dozu.","Nöroloji"),
 Q("c118q2","ESETT çalışmasında karşılaştırılan ikinci basamak ilaçlar hangileridir?",["Levetirasetam, valproat, fosfenitoin","Midazolam, propofol, ketamin","Diazepam, lorazepam, klonazepam","Fenobarbital, tiyopental, propofol","Karbamazepin, lamotrijin, topiramat"],0,"Etkinlikleri benzer bulundu.","Nöroloji"),
 Q("c118q3","Refrakter status epileptikusta izlem için gerekli olan hangisidir?",["Sürekli EEG","Holter","Spirometri","Ekokardiyografi","Doppler"],0,"Nonkonvülzif nöbetler ancak EEG ile görülür.","Nöroloji")]

# 119 GÖZ TRAVMASI — açık glob
S.append(case("c119","Gözüne tel sıçradı — 34 yaşında erkek","Göz",
 "34 yaşında erkek. Bahçede tel keserken sol gözüne bir parça sıçradı. Ağrı, görme bulanıklığı ve sulanma. Gözlük takmıyormuş.",
 {"n1":N("Muayene","Sol gözde korneada 3 mm tam kat görünümlü kesi, **pupil damla (gözyaşı) şeklinde** ve kesiye doğru çekilmiş; ön kamara sığ. Görme: 1 metreden parmak sayma.","KB 136/82 · Nb 92 · SpO₂ %99",[
   T("Seidel testi (floresein)",2,5,"**Pozitif**: kesiden akan aköz sıvı floreseini seyreltiyor.","Tam kat yaralanma — açık glob."),
   T("Orbita BT (ince kesit)",2,30,"Göz içinde **2 mm metalik yabancı cisim**; orbita kırığı yok.","**MR kontrendike** (metal)."),
   T("Göz içi basıncı (tonometri)",-3,5,"Ölçüm sırasında göz içeriği dışarı itildi.","Açık globda tonometri ve göze bası yapılmaz."),
   A("**Açık glob**: göze dokunma/bastırma; **sert göz kalkanı** (pansuman değil); başı 30°; aç bırak; **antiemetik ve analjezi** (öksürük/kusma basıncı artırır); **tetanoz**; sistemik antibiyotik (ör. moksifloksasin ya da vankomisin + seftazidim — kurum protokolü); topikal ilaç yok; **acil göz cerrahisi**",4,15,"n2","Doğru. Erken cerrahi onarım ve endoftalmi profilaksisi."),
   A("Göz yıkama, antibiyotikli pomad ve kapama, ertesi gün göz polikliniği",-5,10,"n9","Açık globda yıkama/pomad/bası göz içeriğinin çıkmasına ve enfeksiyona yol açar."),
 ]),
 "n2":E("Cerrahi onarım","Aynı gün kornea onarımı ve yabancı cisim çıkarımı yapıldı; endoftalmi gelişmedi. Görme kısmen düzeldi.\n\n**Akılda kalsın**\n- Açık glob bulguları: **damla şekilli pupil**, sığ ön kamara, **Seidel +**, yoğun subkonjonktival kanama, uveal doku prolapsusu.\n- **Bası yapma**, tonometri yapma, topikal ilaç verme; **sert kalkan**.\n- Antiemetik + analjezi, aç bırak, **tetanoz**, sistemik antibiyotik, **acil göz cerrahisi**.\n- Metalik yabancı cisim şüphesinde **BT**; **MR yapılmaz**.\n\n*Kaynak: AAO açık glob önerileri; Royal College of Ophthalmologists.*","good"),
 "n9":E("Endoftalmi","Gecikmiş onarım ve enfeksiyon sonucu endoftalmi gelişti; gözde kalıcı görme kaybı oldu.","bad"),
}))
Qs+=[Q("c119q1","Açık glob yaralanmasında hangisi yapılmamalıdır?",["Sert göz kalkanı","Antiemetik","Tonometri ile göz içi basıncı ölçümü","Tetanoz profilaksisi","Göz cerrahisine danışma"],2,"Bası göz içeriğini dışarı iter.","Göz"),
 Q("c119q2","Göz içi metalik yabancı cisim şüphesinde görüntüleme hangisidir?",["MR","Orbita BT","Direkt grafi yeterli","USG ile göze bastırarak","Görüntüleme gerekmez"],1,"MR metal nedeniyle kontrendikedir.","Göz"),
 Q("c119q3","Seidel testi pozitifliği neyi gösterir?",["Kornea abrazyonu","Tam kat yaralanmadan aköz sızıntı","Konjunktivit","Glokom","Retina dekolmanı"],1,"Floresein aköz akımla seyrelir.","Göz")]

# 120 HİPERKALEMİ — BRASH sendromu
S.append(case("c120","Halsizlik ve yavaş nabız — 79 yaşında kadın","Kardiyoloji / Metabolik",
 "79 yaşında kadın. Hipertansiyon ve kalp yetmezliği; metoprolol 100 mg, ramipril 10 mg ve spironolakton 25 mg kullanıyor. 3 gündür ishal ve az yemek; bugün halsizlik ve baş dönmesi.",
 {"n1":N("Muayene","Uykuya meyilli ama uyanıyor. Mukozalar kuru. Ekstremiteler soğuk.","KB 76/42 · Nb 34 · SS 18 · SpO₂ %95",[
   T("12 derivasyonlu EKG",2,5,"**Junctional bradikardi 34/dk**, sivri T dalgaları; QRS 110 ms.","Bradikardi + hiperkalemi + AV düğüm blokeri."),
   T("Kan gazı (K hızlı)",2,10,"**K 6,4**, kreatinin 2,6 (bazal 1,0), pH 7,28.","Orta derecede hiperkalemi tek başına bu kadar bradikardiyi açıklamaz — sinerji."),
   A("**BRASH sendromu** (Bradikardi, Renal yetmezlik, AV düğüm blokajı, Şok, Hiperkalemi) — hepsini birlikte tedavi et: **%10 kalsiyum glukonat 30 mL IV** (gerekirse tekrar), **insülin 10 Ü + dekstroz**, salbutamol nebül; **izotonik sıvı** (asidozda dengeli kristaloid/bikarbonat); bradikardi-hipotansiyon için **adrenalin infüzyonu**; beta bloker, ACEi ve spironolaktonu kes",4,15,"n2","Doğru. Kalsiyum ve adrenalin hızı artırır; sıvı ve böbrek perfüzyonu potasyum atılımını sağlar."),
   A("Atropin 1 mg, yanıt yoksa hemen transvenöz pacemaker",-1,30,"n3","Atropin sıklıkla yetersiz; altta yatan hiperkalemi ve hipoperfüzyon düzeltilmeden pacing tek başına başarısız olabilir."),
   A("K 6,4 — sadece sodyum polistiren sülfonat oral ver ve izle",-4,30,"n9","Etkisi saatler sürer; şok ve bradikardi tedavi edilmiyor."),
 ]),
 "n3":N("30 dakika sonra","Atropine yanıt yok; pacing yakalanması zayıf.","KB 70/40 · Nb 32",[
   A("Kalsiyum, insülin-dekstroz, sıvı ve adrenalin infüzyonu",2,15,"n4","Asıl tedavi."),
   A("Atropini tekrarla",-3,5,"n9","Mekanizma düzeltilmiyor."),
 ]),
 "n2":E("Düzelme","Kalsiyum ve adrenalinle hız 70'e, KB 110/60'a çıktı; sıvıyla idrar çıkışı arttı, K 4,8'e indi. Diyaliz gerekmedi; ilaçlar yeniden düzenlendi.\n\n**Akılda kalsın**\n- **BRASH**: bradikardi + böbrek yetmezliği + AV düğüm blokeri + şok + hiperkalemi → kısır döngü.\n- Orta derecede K yüksekliği bile AV düğüm blokeriyle birlikte ağır bradikardi yapar.\n- Tedavi: **kalsiyum**, **potasyumu hücre içine** (insülin-dekstroz, salbutamol), **sıvı/perfüzyon**, **adrenalin** infüzyonu; atropin sıklıkla yetersiz; pacing ve diyaliz yanıtsızlarda.\n\n*Kaynak: Farkas ve ark., J Emerg Med 2020 (BRASH); UK Kidney Association 2023 hiperkalemi kılavuzu.*","good"),
 "n4":E("Geç düzelme","Tedavi sonrası düzeldi ama hasta 2 gün yoğun bakımda kaldı ve geçici diyaliz gerekti.","mid"),
 "n9":E("Arrest","Hasta asistoliye girdi; resüsitasyonla dönse de çoklu organ yetmezliği gelişti.","bad"),
}))
Qs+=[Q("c120q1","BRASH sendromunun bileşenlerinden biri değildir:",["Bradikardi","Renal yetmezlik","AV düğüm blokeri","Hiperkalsemi","Şok"],3,"H: hiperkalemi.","Kardiyoloji / Metabolik"),
 Q("c120q2","Hiperkalemide miyokard membranını stabilize eden ilk ilaç hangisidir?",["İnsülin","Kalsiyum (glukonat/klorür)","Salbutamol","Furosemid","Sodyum polistiren"],1,"Etkisi dakikalar içinde başlar.","Kardiyoloji / Metabolik"),
 Q("c120q3","BRASH'te bradikardi-hipotansiyon için önerilen vazoaktif hangisidir?",["Adrenalin infüzyonu","Esmolol","Nitrogliserin","Diltiazem","Labetalol"],0,"Kronotrop ve K'yı hücre içine sokar.","Kardiyoloji / Metabolik")]

P={"id":"ilk-nobet-12","title":"İlk Nöbet Vakaları — 12. Paket (vaka 111–120)","desc":"Skafoid kırığı, paronişi, sekonder pnömotoraks, ACE inhibitörü anjiyoödemi, boksör kırığı ve kavga ısırığı, akut dekompanse kalp yetmezliği, bilinen epilepside nöbet, benzodiazepine dirençli status, açık glob, BRASH sendromu.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 12. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 12. Paket","topic":"Temel acil","order":12,"req":[1],"desc":"El ve göz travmasından hava yolu ve ritim acillerine 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
