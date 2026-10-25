import sys; sys.path.insert(0,__file__.rsplit("/",1)[0])
from vaka_lib import *
S=[]; Qs=[]
INTRO="- Her vakayı önce **kendi bildiğinizle** çözün, sonra yeniden oynayıp farklı kararların sonucunu görün.\n- Sonuç ekranındaki **“Akılda kalsın”** bölümü vakanın özüdür.\n- Sonunda **pekiştirme sorularını** çözün; yanlışlarınız tekrar listenize eklenir.\n- İlaç dozları kılavuzlardan alınmıştır; uygulamada kurumunuzun protokollerini esas alın."

# 81 AKUT İSKEMİK EKSTREMİTE — üst ekstremite
S.append(case("c81","Soğuk ve uyuşuk kol — 69 yaşında erkek","Kalp-damar cerrahisi",
 "69 yaşında erkek, mitral darlığı ve AF; antikoagülan düzeyi takip edilmemiş. 2 saat önce sağ kolunda ani ağrı, uyuşma ve soğukluk başlamış.",
 {"n1":N("Muayene","Sağ el ve ön kol soluk, soğuk; brakiyal nabız dirsek üstünde alınıyor, **radial ve ulnar nabızlar yok**. Parmaklarda duyu azalmış, kavrama gücü hafif zayıf.","KB 134/80 (sol kol) · Nb 108 (düzensiz)",[
   T("Doppler (radial/ulnar)",2,5,"Arteriyel sinyal yok.","Duyu ve motor tutulum varsa acil revaskülarizasyon gerekir."),
   T("INR",1,20,"INR 1,3 (terapötik değil).","Embolik kaynak: AF + mitral darlığı."),
   A("Anfraksiyone heparin IV bolus + infüzyon; analjezi; acil damar cerrahisi — brakiyal embolektomi",4,15,"n2","Doğru. Üst ekstremite kollateral dolaşımı daha iyi olsa da duyu-motor kaybı varsa acil revaskülarizasyon gerekir."),
   A("Üst ekstremitede iskemi tolere edilir — oral antikoagülanı düzenleyip taburcu",-4,20,"n9","Nörolojik bulgulu akut iskemi her ekstremitede acildir."),
 ]),
 "n2":E("Embolektomi","Lokal anestezi altında brakiyal embolektomiyle nabızlar döndü. Ekokardiyografide sol atriyal trombüs; antikoagülasyon yeniden düzenlendi.\n\n**Akılda kalsın**\n- Üst ekstremite akut iskemisinin çoğu **kardiyak emboli** (AF, mitral darlık, MI).\n- 6P; duyu/motor kaybı = **acil revaskülarizasyon**.\n- **Heparin** + embolektomi (çoğu lokal anesteziyle).\n- Emboli kaynağını ara (ekokardiyografi), antikoagülasyonu düzelt.\n- Torasik çıkış sendromu, diseksiyon, vaskülit, iyatrojenik (arteriyel kateter) ayırıcı tanıda.\n\n*Kaynak: ESVS 2020 akut ekstremite iskemisi kılavuzu.*","good"),
 "n9":E("Gangren","Hasta 3 gün sonra parmaklarda kuru gangrenle döndü; parmak amputasyonları gerekti.","bad"),
}))
Qs+=[Q("c81q1","Üst ekstremite akut arteriyel iskemisinin en sık nedeni hangisidir?",["Ateroskleroz","Kardiyak emboli","Vaskülit","Travma","Raynaud"],1,"AF ve kapak hastalığı başlıca kaynaklardır.","Kalp-damar cerrahisi"),
 Q("c81q2","Duyu kaybı olan akut kol iskemisinde doğru yaklaşım hangisidir?",["Oral antikoagülan ve taburculuk","Heparin + acil embolektomi","Sıcak uygulama","NSAİİ","Gözlem"],1,"Nörolojik tutulum acil revaskülarizasyon gerektirir.","Kalp-damar cerrahisi"),
 Q("c81q3","Embolektomi sonrası emboli kaynağı için hangi tetkik yapılmalıdır?",["Ekokardiyografi","Kolonoskopi","Beyin MR","Spirometri","Tiroid USG"],0,"Sol atriyal/ventriküler trombüs, vejetasyon araştırılır.","Kalp-damar cerrahisi")]

# 82 ALKALİ GÖZ YANIĞI
S.append(case("c82","Gözüne lavabo açıcı sıçrayan hasta — 35 yaşında kadın","Göz",
 "35 yaşında kadın. 15 dakika önce lavabo açıcı (sodyum hidroksit) gözüne sıçramış. Evde birkaç saniye musluk suyuyla yıkamış. Gözünü açamıyor, şiddetli ağrı var.",
 {"n1":N("Triaj","Sağ göz kapakları spazmda, kızarık. Hasta gözünü açamıyor.","Nb 104",[
   T("Görme keskinliği ve tam göz muayenesi (önce)",-3,15,"Hasta gözünü açamadığı için muayene yapılamadı; 15 dakika kaybedildi.","Kimyasal yanıkta yıkama muayeneden önce gelir (yalnız hızlı pH ölçümü)."),
   T("pH turnusolü (konjunktival fornikse)",1,1,"**pH 11**.","Hedef yıkama sonrası 7,0–7,5."),
   A("**Hemen bol yıkama**: topikal anestezik damla, kapak ekartörü/Morgan lens, en az 1–2 L SF veya Ringer laktat (30 dakika), forniksleri süpür (partikül), yıkama bittikten 5–10 dakika sonra pH ölç, gerekirse yıkamaya devam",4,40,"n2","Doğru. Alkaliler lipofilik olup dokuya hızla penetre olur (likefaksiyon nekrozu); yıkama süresi prognozu belirler."),
   A("Asitli bir solüsyonla nötralize et",-5,5,"n9","Nötralizasyon ekzotermik reaksiyonla ek hasar yapar; yalnız bol yıkama."),
 ]),
 "n2":N("Yıkama sonrası","3 L sonrası pH 7,4. Floresein: geniş epitel defekti; limbusun yaklaşık 1/3'ünde iskemi (beyazlama).","",[
   A("Sikloplejik, topikal antibiyotik, analjezi; **acil göz konsültasyonu** (aynı gün; limbal iskemi → ağır yanık); tetanoz durumu",3,15,"n3","Doğru. Limbal iskemi prognozu kötüleştirir; göz uzmanı tedaviyi (steroid, askorbat, amniyon membranı) planlar."),
   A("Topikal steroid başla, kapama yap, 1 hafta sonra kontrol",-3,10,"n9","Steroid ve tedavi kararı göz uzmanına aittir; ağır yanık yakın izlem gerektirir."),
 ]),
 "n3":E("Görme korundu","Göz kliniğinde yoğun tedavi uygulandı; 3 haftada epitel kapandı, görme 0,8.\n\n**Akılda kalsın**\n- Kimyasal göz yanığı = **gerçek oftalmolojik acil**; **önce yıka, sonra muayene et**.\n- **Alkali** (lavabo açıcı, kireç, amonyak, çimento) asitten daha tehlikelidir.\n- Topikal anestezik + **bol yıkama (≥1–2 L)**, forniks süpürme, **pH 7,0–7,5** olana kadar.\n- Nötralizasyon yok.\n- Limbal iskemi ve kornea opasitesi ağırlık göstergesidir → acil göz.\n\n*Kaynak: Royal College of Ophthalmologists; Roper-Hall/Dua sınıflaması.*","good"),
 "n9":E("Kornea hasarı","Yetersiz yıkama/yanlış tedaviyle kornea perforasyonu ve kalıcı görme kaybı gelişti.","bad"),
}))
Qs+=[Q("c82q1","Kimyasal göz yanığında ilk yapılacak işlem hangisidir?",["Görme keskinliği ölçümü","Bol miktarda yıkama","Göz kapama","Steroid damla","Nötralizan solüsyon"],1,"Yıkama muayeneden önce gelir.","Göz"),
 Q("c82q2","Kimyasal yanıkta yıkama ne zamana kadar sürdürülür?",["Ağrı geçene kadar","Konjunktival pH 7,0–7,5 olana kadar (5–10 dk sonra kontrol)","1 dakika","Hasta istemeyene kadar","Yıkama gerekmez"],1,"pH normale dönene kadar.","Göz"),
 Q("c82q3","Hangisi daha ağır göz hasarı yapma eğilimindedir?",["Seyreltik asit","Alkali (ör. sodyum hidroksit, kireç)","Su","Serum fizyolojik","Sabun"],1,"Alkaliler likefaksiyon nekrozuyla derine ilerler.","Göz")]

# 83 SİGMOİD VOLVULUS
S.append(case("c83","Aşırı karın şişliği — 82 yaşında erkek","Genel cerrahi",
 "82 yaşında erkek, huzurevinde kalıyor; kronik kabızlık, Parkinson. 2 gündür gaz-gaita çıkaramıyor, karnı hızla şişmiş, kusmaya başlamış.",
 {"n1":N("Muayene","Karın belirgin distandü, timpanik; hafif yaygın hassasiyet, defans/rebound yok.","KB 132/76 · Nb 102 · Ateş 37,2",[
   T("Direkt karın grafisi",3,15,"Sol alt kadrandan sağ üste uzanan, dev, **ters U şeklinde (“kahve çekirdeği”) distandü sigmoid**.","Sigmoid volvulus."),
   T("Laktat, lökosit",1,30,"Laktat 1,6, lökosit 11.000.","İskemi bulgusu yok."),
   T("BT",1,30,"Mezenterde “girdap” (whirl) işareti; bağırsak duvarı kontrastlanıyor, serbest hava yok.","Tanı ve iskemi değerlendirmesi."),
   A("Peritonit/iskemi yok: sıvı, NG dekompresyon; **endoskopik (fleksibl sigmoidoskopi) detorsiyon** + rektal tüp; ardından aynı yatışta elektif sigmoid rezeksiyon planı (uygun hastada)",4,30,"n2","Doğru. Endoskopik detorsiyon çoğunlukla başarılıdır ama nüks sıktır."),
   A("Kabızlık — lavman ve laksatif ile huzurevine geri gönder",-5,20,"n9","Kapalı loop obstrüksiyon iskemi ve perforasyona ilerler."),
 ]),
 "n2":E("Endoskopik detorsiyon","Fleksibl sigmoidoskopiyle detorsiyon sağlandı, mukoza canlıydı; rektal tüp bırakıldı. Nüks riski nedeniyle aynı yatışta sigmoid rezeksiyonu planlandı.\n\n**Akılda kalsın**\n- Sigmoid volvulus: yaşlı, kronik kabızlık, nörolojik/psikiyatrik hastalık, kurumda yaşama.\n- Grafi: **kahve çekirdeği**; BT: **girdap işareti**.\n- Peritonit/iskemi/perforasyon yoksa **endoskopik detorsiyon**; varsa **acil cerrahi** (Hartmann).\n- **Çekal volvulus** endoskopik değil, cerrahi tedavi edilir.\n\n*Kaynak: ASCRS 2021 kolonik volvulus kılavuzu.*","good"),
 "n9":E("Perforasyon","Hasta 24 saat sonra perforasyon ve fekal peritonitle döndü; acil Hartmann ameliyatı, yoğun bakım.","bad"),
}))
Qs+=[Q("c83q1","Sigmoid volvulusun klasik direkt grafi bulgusu hangisidir?",["Kahve çekirdeği (ters U)","Çift baloncuk","Merdiven basamağı tek başına","Serbest hava","Hedef işareti"],0,"Dev distandü sigmoid loop.","Genel cerrahi"),
 Q("c83q2","Peritonit bulgusu olmayan sigmoid volvulusta ilk tedavi hangisidir?",["Acil laparotomi","Endoskopik detorsiyon","Lavman ve taburculuk","Antibiyotik","Gözlem"],1,"Ardından nüksü önlemek için elektif rezeksiyon düşünülür.","Genel cerrahi"),
 Q("c83q3","Çekal volvulusun tedavisi hangisidir?",["Endoskopik detorsiyon","Cerrahi","Lavman","Konservatif","Antibiyotik"],1,"Endoskopik detorsiyon başarısı düşüktür; cerrahi gerekir.","Genel cerrahi")]

# 84 İNFEKTİF ENDOKARDİT
S.append(case("c84","Ateş ve öksürük — 31 yaşında erkek","Enfeksiyon / Kardiyoloji",
 "31 yaşında erkek, damar içi madde kullanıyor. 1 haftadır yüksek ateş, titreme, plöritik göğüs ağrısı ve öksürük. Kollarda enjeksiyon izleri var.",
 {"n1":N("Muayene","Toksik görünümlü. Sol sternal kenarda inspiryumla artan **pansistolik üfürüm**. Parmak uçlarında küçük ağrısız hemorajik lezyonlar (Janeway), tırnak altı kıymık hemorajileri.","KB 104/62 · Nb 118 · SS 24 · SpO₂ %93 · Ateş 39,6",[
   T("Kan kültürü — 3 set (farklı ven ponksiyonlarından, antibiyotikten önce)",3,30,"Alındı; 18 saatte 3/3 şişede **S. aureus** üredi.","Duke ölçütleri: tipik mikroorganizma ile tekrarlayan pozitif kültür majör ölçüttür."),
   T("Toraks BT",2,30,"İki akciğerde periferik, kaviteli **septik emboliler**.","Sağ kalp (triküspit) endokarditi."),
   T("Ekokardiyografi",3,40,"Triküspit kapakta 18 mm vejetasyon, ciddi triküspit yetersizliği.","Majör ölçüt (vejetasyon)."),
   A("Kültürler alındıktan hemen sonra **ampirik IV antibiyotik** (ör. vankomisin ± gentamisin ya da yerel protokol; S. aureus — MRSA olasılığı); endokardit ekibi (kardiyoloji, enfeksiyon, kalp cerrahisi); bağımlılık tedavisine yönlendirme",4,15,"n2","Doğru. Hemodinamik bozulma ve sepsis varsa antibiyotik kültürden hemen sonra; sonuçlara göre daraltılır."),
   A("Pnömoni — oral amoksisilin-klavulanat ile taburcu",-5,10,"n9","Damar içi madde kullanımı + üfürüm + çoklu periferik akciğer nodülü = sağ kalp endokarditi."),
 ]),
 "n2":E("Endokardit tedavisi","Kültürde MSSA üredi, antibiyotik flukloksasilin/sefazoline daraltıldı; 6 hafta IV tedavi verildi. Büyük vejetasyon ve kalıcı bakteriyemi nedeniyle cerrahi değerlendirildi.\n\n**Akılda kalsın**\n- Ateş + yeni üfürüm + risk (damar içi madde, protez kapak, önceki IE, kalp hastalığı) → **IE düşün**.\n- **Antibiyotikten önce 3 set kan kültürü**; ekokardiyografi (TTE, gerekirse TEE).\n- Bulgular: embolik fenomenler (Janeway, splinter, septik emboli, inme), immünolojik (Osler, Roth, glomerülonefrit).\n- Ampirik tedavi yerel protokole göre; endokardit ekibi.\n- IE'ye bağlı embolik inmede **tromboliz önerilmez**.\n\n*Kaynak: ESC 2023 Endokardit Kılavuzu.*","good"),
 "n9":E("Komplikasyon","Hasta septik şok ve akut triküspit yetersizliğine bağlı sağ kalp yetmezliğiyle döndü.","bad"),
}))
Qs+=[Q("c84q1","İnfektif endokardit şüphesinde antibiyotikten önce yapılması gereken nedir?",["Tek set kan kültürü","Farklı ponksiyonlardan 3 set kan kültürü","Yalnız CRP","Boğaz kültürü","İdrar kültürü tek başına"],1,"Sürekli bakteriyemiyi göstermek için.","Enfeksiyon / Kardiyoloji"),
 Q("c84q2","Damar içi madde kullananlarda en sık tutulan kapak hangisidir?",["Aort","Mitral","Triküspit","Pulmoner","Hepsi eşit"],2,"Sağ kalp endokarditi ve septik pulmoner emboliler.","Enfeksiyon / Kardiyoloji"),
 Q("c84q3","Endokardite bağlı akut iskemik inmede hangisi önerilmez?",["Antibiyotik","IV tromboliz","Nöroloji konsültasyonu","Görüntüleme","Ekokardiyografi"],1,"Mikotik anevrizma ve kanama riski nedeniyle.","Enfeksiyon / Kardiyoloji")]

# 85 RETROBULBER HEMORAJİ
S.append(case("c85","Yüz travması sonrası görme kaybı — 27 yaşında erkek","Göz / Travma",
 "27 yaşında erkek, kavgada sol gözüne yumruk almış. 40 dakikadır sol gözde artan ağrı, şişlik ve görmede bulanıklık.",
 {"n1":N("Muayene","Sol göz **proptotik**, göz kapakları gergin, göz hareketleri kısıtlı, subkonjonktival kanama. Sol gözde **relatif afferent pupil defekti**. Görme: 1 metreden parmak sayma. Palpasyonda orbita taş gibi sert.","KB 146/90 · Nb 98",[
   T("Göz içi basıncı",2,5,"Sol **52 mmHg**.","Orbital kompartman sendromu."),
   T("BT (cerrahi öncesi)",-3,40,"Retrobulber hematom. 40 dakika kaybedildi.","Klinik tanı açıkken BT dekompresyonu geciktirmemeli."),
   A("**Lateral kantotomi + inferior kantoliz** (acil hekimi, hemen); ardından GİB ve görme kontrolü; göz konsültasyonu; tıbbi tedavi (asetazolamid, mannitol) yardımcı",4,10,"n2","Doğru. Retina iskemisi ≈90–120 dakikada kalıcı hasar yapar; işlem yatak başında yapılır."),
   A("Soğuk uygulama + analjezik, sabah göz polikliniği",-5,20,"n9","Orbital kompartman sendromu dakikalar-saatler içinde körlük yapar."),
 ]),
 "n2":E("Görme korundu","Kantotomi/kantoliz sonrası GİB 24 mmHg'ye indi, RAPD kayboldu; görme 0,7'ye yükseldi.\n\n**Akılda kalsın**\n- Orbital kompartman sendromu: travma/cerrahi sonrası **proptozis, ağrı, görme kaybı, RAPD, GİB yüksekliği (>40), gergin orbita**.\n- **Klinik tanıdır**: görüntüleme beklenmez.\n- **Lateral kantotomi + kantoliz** acil hekiminin yapması gereken görme kurtarıcı işlemdir.\n- Antikoagülan kullananlar risklidir.\n\n*Kaynak: Roberts & Hedges' Clinical Procedures; Royal College of Emergency Medicine.*","good"),
 "n9":E("Kalıcı körlük","Sabah göz polikliniğinde görme ışık hissi düzeyindeydi; optik sinir hasarı kalıcıydı.","bad"),
}))
Qs+=[Q("c85q1","Retrobulber hemorajide görmeyi kurtaran acil işlem hangisidir?",["Göz kapama","Lateral kantotomi + inferior kantoliz","Topikal steroid","Soğuk kompres","Pupil dilatasyonu"],1,"Orbita basıncını hemen düşürür.","Göz / Travma"),
 Q("c85q2","Orbital kompartman sendromunda tanı nasıl konur?",["Yalnız BT ile","Klinik olarak (proptozis, görme kaybı, RAPD, GİB yüksekliği)","MR ile","Ultrasonla zorunlu","Kan testiyle"],1,"Görüntüleme işlemi geciktirmemelidir.","Göz / Travma"),
 Q("c85q3","Retina iskemisinde kalıcı hasar ne kadar sürede gelişebilir?",["5 dakika","≈90–120 dakika","24 saat","1 hafta","Hiçbir zaman"],1,"Zaman kritik.","Göz / Travma")]

# 86 MİKSÖDEM KOMASI
S.append(case("c86","Kış günü evde bulunan uykulu hasta — 78 yaşında kadın","Endokrin",
 "78 yaşında kadın, yalnız yaşıyor. Hipotiroidi tanısı var ama ilaçlarını aylardır kullanmıyor. Kızı onu soğuk evde uyuklarken, yanıtları çok yavaş bulmuş. 1 haftadır pnömoni belirtileri var.",
 {"n1":N("Resüsitasyon alanı","Letarjik (GKS 11), yüz şiş, deri kuru-kaba, dil büyük, refleksler gecikmeli gevşeme.","KB 88/52 · **Nb 44** · **SS 8** · SpO₂ %88 · **Isı 33,4 °C** · Glukoz 58",[
   T("TSH, sT4, kortizol (tedaviden önce örnek)",2,40,"**TSH 68**, sT4 çok düşük. (Kortizol sonucu sonra gelecek.)","Primer hipotiroidi; adrenal yetmezlik eşlik edebilir."),
   T("Na, kan gazı",2,10,"Na 124, pCO₂ 68, pH 7,24.","Hiponatremi ve hiperkapnik solunum yetmezliği."),
   A("Hava yolu/ventilasyon desteği (hiperkapni); **IV hidrokortizon 100 mg** (8 saatte bir) — tiroid hormonundan önce/birlikte; **IV levotiroksin** yükleme (ör. 200–400 mcg; yaşlı/kardiyak hastada düşük doz, 100–200 mcg); pasif ısıtma; hipoglisemi ve hiponatremi tedavisi; tetikleyici (pnömoni) için antibiyotik; yoğun bakım",4,20,"n2","Doğru. Steroidsiz tiroid hormonu, eşlik eden adrenal yetmezlikte krizi tetikleyebilir."),
   A("Hızlı aktif dış ısıtma (ısıtıcı battaniye, sıcak su) ve oral levotiroksin",-4,30,"n9","Agresif dış ısıtma periferik vazodilatasyonla şoka yol açabilir; oral emilim güvenilmez; steroid atlandı."),
 ]),
 "n2":E("Yoğun bakımda düzelme","NIV ve ardından kısa süreli entübasyonla ventilasyon desteklendi; 48 saatte bilinç düzeldi, ısı 36,5 °C. Kortizol düşük çıktı; hidrokortizon azaltılarak sürdürüldü.\n\n**Akılda kalsın**\n- Miksödem koması: **bilinç değişikliği + hipotermi + bradikardi + hipoventilasyon**, hiponatremi, hipoglisemi; tetikleyici: enfeksiyon, soğuk, sedatif, ilaç bırakma.\n- **Önce/birlikte hidrokortizon**, sonra **IV levotiroksin** (yaşlı/kardiyakta düşük doz).\n- **Pasif ısıtma**; ventilasyon desteği; hiponatremi ve hipoglisemi tedavisi.\n- Tedaviye laboratuvarı beklemeden başlanır.\n\n*Kaynak: ATA 2014 hipotiroidi kılavuzu.*","good"),
 "n9":E("Kollaps","Ani ısıtma sonrası hipotansiyon derinleşti; hasta arrest oldu.","bad"),
}))
Qs+=[Q("c86q1","Miksödem komasında tiroid hormonundan önce/birlikte verilmesi gereken ilaç hangisidir?",["Propranolol","Hidrokortizon","Furosemid","Digoksin","Amiodaron"],1,"Eşlik edebilecek adrenal yetmezlik nedeniyle.","Endokrin"),
 Q("c86q2","Miksödem komasında levotiroksin hangi yoldan verilir?",["Oral","IV","İntramüsküler","Rektal","Topikal"],1,"Bağırsak ödemi nedeniyle oral emilim güvenilmez.","Endokrin"),
 Q("c86q3","Miksödem komasında hipotermi nasıl yönetilir?",["Hızlı aktif dış ısıtma","Pasif ısıtma (battaniye)","Soğutma","Hiçbir şey","Sıcak su banyosu"],1,"Aktif dış ısıtma vazodilatasyon ve şok riski taşır.","Endokrin")]

# 87 PNEUMATOSİS İNTESTİNALİS (iskemik)
S.append(case("c87","Karın ağrısı ve BT'de bağırsak duvarında hava — 74 yaşında kadın","Genel cerrahi",
 "74 yaşında kadın, KKY ve AF. 12 saattir karın ağrısı, kusma; son saatlerde ağrı yayıldı. Bir önceki merkezde çekilen BT raporunda “pneumatosis intestinalis” yazıyor.",
 {"n1":N("Muayene","Karın distandü, yaygın hassasiyet ve defans.","KB 88/50 · Nb 124 · Ateş 38,1",[
   T("Laktat, kan gazı",2,10,"**Laktat 6,2**, pH 7,24.","Sistemik hipoperfüzyon/iskemi."),
   T("BT'nin yeniden değerlendirilmesi",3,10,"İnce bağırsak duvarında lineer gaz + **portal venöz gaz**; süperior mezenter arterde dolum defekti.","Pnömatozis + portal venöz gaz + peritonit + laktat = **transmural iskemi**."),
   A("Resüsitasyon, geniş spektrum antibiyotik, heparin; **acil cerrahi** (laparotomi) + damar cerrahisi",4,20,"n2","Doğru. Pnömatozis tek başına değil, klinikle birlikte yorumlanır; tehlike işaretleri varken cerrahi gerekir."),
   A("Pnömatozis çoğunlukla iyi huyludur — konservatif izlem, oral beslenme",-5,30,"n9","Peritonit, laktat yüksekliği ve portal venöz gaz iyi huylu pnömatozisi dışlar."),
 ]),
 "n2":E("Acil laparotomi","SMA embolektomisi ve nekrotik ileum rezeksiyonu yapıldı; ikinci bakışta kalan bağırsak canlıydı.\n\n**Akılda kalsın**\n- Pnömatozis intestinalis bir **görüntüleme bulgusudur**, tanı değil.\n- **İyi huylu**: asemptomatik, KOAH, steroid/kemoterapi, endoskopi sonrası — konservatif.\n- **Tehlikeli**: karın ağrısı + **peritonit**, **laktat ↑**, asidoz, hipotansiyon, **portal venöz gaz** → bağırsak iskemisi → **acil cerrahi**.\n\n*Kaynak: DuBose ve ark., PIPES çalışması (JAMA Surg 2013); Tintinalli.*","good"),
 "n9":E("Ölüm","Konservatif izlenen hasta septik şokla kaybedildi; otopside yaygın bağırsak nekrozu.","bad"),
}))
Qs+=[Q("c87q1","Pnömatozis intestinaliste hangisi tehlikeli (iskemik) formu düşündürür?",["Asemptomatik hasta","Portal venöz gaz + laktat yüksekliği + peritonit","KOAH öyküsü","Steroid kullanımı","Endoskopi sonrası"],1,"Bu bulgular transmural iskemiyi gösterir.","Genel cerrahi"),
 Q("c87q2","Asemptomatik, laboratuvarı normal pnömatozisli hastada yaklaşım hangisidir?",["Acil laparotomi","Konservatif izlem","Tromboliz","Antikoagülan","Hemen kolektomi"],1,"İyi huylu formlar sıktır.","Genel cerrahi"),
 Q("c87q3","Pnömatozis intestinalis için doğru ifade hangisidir?",["Her zaman cerrahi gerektirir","Bir görüntüleme bulgusudur; klinikle yorumlanır","Yalnız çocuklarda görülür","Tanı koydurucudur","Hiçbir zaman tehlikeli değildir"],1,"Klinik bağlam kararı belirler.","Genel cerrahi")]

# 88 KORNEAL ÜLSER (lens ilişkili keratit)
S.append(case("c88","Kırmızı, ağrılı göz — 23 yaşında kadın","Göz",
 "23 yaşında kadın, aylık yumuşak kontakt lens kullanıyor; sık sık lensle uyuyor ve lensi musluk suyuyla temizliyor. 1 gündür sağ gözde artan ağrı, kızarıklık, ışığa hassasiyet ve görme bulanıklığı.",
 {"n1":N("Muayene","Sağ gözde silier enjeksiyon, kornea ortasında **beyaz infiltrat**, ön kamarada hafif hipopiyon. Görme 0,3.","",[
   T("Floresein boyama (yarık lamba/mavi ışık)",3,5,"İnfiltrat üzerinde **3 mm epitel defekti** boyanıyor.","Bakteriyel keratit (lens kullanıcılarında Pseudomonas sık; Acanthamoeba unutulmamalı)."),
   A("Lensi çıkar (ve sakla/kültüre gönder); **aynı gün acil göz konsültasyonu** (kazıntı/kültür, yoğun topikal antibiyotik — ör. saatlik florokinolon); kapama yok, steroid yok; lens kullanmayı bırak",4,15,"n2","Doğru. Korneal ülser görmeyi tehdit eder; tedavi göz hekimince yoğun topikal antibiyotikle yapılır."),
   A("Konjonktivit — steroid-antibiyotik kombine damla ve göz kapama",-5,10,"n9","Steroid enfeksiyonu ağırlaştırabilir; lens kullanıcısında kapama Pseudomonas için uygun ortam yaratır."),
 ]),
 "n2":E("İyileşme","Kültürde Pseudomonas üredi; yoğun topikal antibiyotikle 2 haftada ülser skarla iyileşti, görme 0,8.\n\n**Akılda kalsın**\n- Kırmızı göz kırmızı bayrakları: **görme azalması, şiddetli ağrı, fotofobi, kornea opasitesi/infiltrat, hipopiyon, lens kullanımı**.\n- Lens kullanıcısında ağrılı kırmızı göz = **keratit** aksi kanıtlanana kadar.\n- **Aynı gün göz**; kazıntı/kültür, yoğun topikal antibiyotik.\n- **Kapama yok, acilde steroid yok**.\n- Lensle uyumak ve musluk suyu (Acanthamoeba) büyük risk.\n\n*Kaynak: AAO Bakteriyel Keratit Tercihli Uygulama Örüntüsü (PPP).*","good"),
 "n9":E("Kornea perforasyonu","Ülser derinleşti, kornea perforasyonu gelişti; acil keratoplasti gerekti.","bad"),
}))
Qs+=[Q("c88q1","Kontakt lens kullanıcısında ağrılı kırmızı gözde ilk düşünülmesi gereken hangisidir?",["Alerjik konjonktivit","Mikrobiyal keratit","Episklerit","Subkonjonktival kanama","Kuru göz"],1,"Pseudomonas ve Acanthamoeba başlıca etkenler.","Göz"),
 Q("c88q2","Lens ilişkili korneal ülserde hangisi yapılmamalıdır?",["Lensi çıkarmak","Göz kapama ve steroidli damla","Acil göz konsültasyonu","Kültür","Yoğun topikal antibiyotik"],1,"Kapama ve steroid enfeksiyonu kötüleştirir.","Göz"),
 Q("c88q3","Hangi bulgu kırmızı gözde ciddi patolojiyi düşündürür?",["Kaşıntı","Sulu akıntı","Görme keskinliğinde azalma ve fotofobi","Bilateral hafif kızarıklık","Yanma"],2,"Kırmızı bayraklar acil değerlendirme gerektirir.","Göz")]

# 89 KAROTİS ARTER DİSEKSİYONU
S.append(case("c89","Boyun ağrısı ve göz kapağında düşme — 38 yaşında kadın","Nöroloji",
 "38 yaşında kadın. 3 gün önce kuaförde saçları yıkanırken boynu uzun süre geriye bükülmüş. O günden beri sol boyun ve şakak ağrısı; bugün sol göz kapağının düştüğünü fark etmiş. 1 saat önce 10 dakika süren sağ elde güçsüzlük olmuş, geçmiş.",
 {"n1":N("Muayene","Sol **pitoz ve miyozis** (Horner sendromu), anhidroz yok. Şu an nörolojik defisit yok.","KB 128/80 · Nb 78",[
   T("BT anjiyografi (boyun + beyin)",4,30,"Sol internal karotis arterde **diseksiyon** (alev şeklinde daralma, intramural hematom).","Ağrılı Horner + TİA = karotis diseksiyonu."),
   T("Beyin MR (difüzyon)",1,60,"Sol hemisferde küçük akut iskemik odak.","Sessiz/küçük infarktlar."),
   A("Diseksiyona bağlı TİA/inme: **antitrombotik tedavi** (antiplatelet veya antikoagülan — benzer etkinlik), nöroloji yatışı/inme ünitesi; yeni defisit gelişir ve pencere içindeyse tromboliz kontrendike değildir",4,20,"n2","Doğru. CADISS ve TREAT-CAD çalışmaları; tedavi seçimi nörolojiyle."),
   A("Migren + gerilim — analjezik ile taburcu",-5,10,"n9","Genç hastada ağrılı Horner sendromu karotis diseksiyonudur; inme riski en yüksek ilk günlerdedir."),
 ]),
 "n2":E("İnme önlendi","Antiplatelet tedaviyle izlendi; yeni iskemik olay olmadı. 3. ayda damar rekanalize oldu.\n\n**Akılda kalsın**\n- Genç inmenin önemli nedeni; minör travma (boyun manipülasyonu, spor, kuaför), bağ dokusu hastalıkları.\n- **Ağrılı Horner** (pitoz + miyozis), boyun/yüz/baş ağrısı, TİA/inme, pulsatil tinnitus.\n- Tanı: **BT/MR anjiyografi**.\n- **Antitrombotik** (antiplatelet ≈ antikoagülan); diseksiyon tek başına trombolize engel değil.\n- Vertebral diseksiyon: ense ağrısı + arka dolaşım inmesi.\n\n*Kaynak: ESO 2021 servikal arter diseksiyonu kılavuzu.*","good"),
 "n9":E("İnme","Hasta 2 gün sonra sağ hemipleji ve afaziyle getirildi.","bad"),
}))
Qs+=[Q("c89q1","Ağrılı Horner sendromu (pitoz + miyozis + baş/boyun ağrısı) hangi tanıyı düşündürür?",["Migren","İnternal karotis diseksiyonu","Bell paralizisi","Glokom","Sinüzit"],1,"Sempatik liflerin karotis duvarında hasarı.","Nöroloji"),
 Q("c89q2","Servikal arter diseksiyonunda inme önleme tedavisi hangisidir?",["Tromboliz herkese","Antiplatelet veya antikoagülan","Steroid","Cerrahi her olguda","Hiçbir şey"],1,"İki strateji benzer etkinlikte bulunmuştur.","Nöroloji"),
 Q("c89q3","Karotis diseksiyonu tanısında tercih edilen görüntüleme hangisidir?",["Direkt grafi","BT veya MR anjiyografi","Ekokardiyografi","EEG","LP"],1,"Lümen daralması ve intramural hematom gösterilir.","Nöroloji")]

# 90 DİJİTAL İSKEMİ (adrenalin oto-enjektörü)
S.append(case("c90","Parmağa adrenalin enjeksiyonu — 26 yaşında kadın","El cerrahisi / Toksikoloji",
 "26 yaşında kadın, çocuğunun adrenalin oto-enjektörünü kontrol ederken yanlışlıkla sol baş parmağına batırmış (0,3 mg). 20 dakikadır parmak bembeyaz, soğuk ve ağrılı.",
 {"n1":N("Muayene","Sol baş parmak distal falanks soluk-beyaz, soğuk; kapiller dolum >4 sn. Sistemik belirti yok.","KB 132/80 · Nb 96",[
   A("**Fentolamin** lokal infiltrasyonu (ör. 0,5–1 mg, 1–5 mL lidokain/SF ile seyreltilmiş, enjeksiyon yerine/parmak kaidesine); ılık ortam; yanıt izlemi; alternatif: topikal nitrogliserin",4,15,"n2","Doğru. Alfa bloker fentolamin vazospazmı dakikalar içinde geri çevirir."),
   A("Parmağa buz koy ve izle",-4,30,"n9","Soğuk vazokonstriksiyonu artırır."),
   A("Hiçbir şey yapma — kendiliğinden geçer, taburcu",-1,10,"n3","Olguların çoğu kendiliğinden düzelir ama uzamış iskemi riski için izlem ve tedavi seçeneği sunulmalıdır."),
 ]),
 "n3":N("1 saat sonra","Parmak hâlâ soluk, ağrı artıyor.","",[
   A("Fentolamin lokal infiltrasyonu",2,15,"n2","Doğru — gecikmeli."),
 ]),
 "n2":E("Perfüzyon döndü","Fentolaminden 10 dakika sonra parmak pembeleşti, kapiller dolum 2 sn. 1 saat izlenip taburcu edildi; oto-enjektör kullanımı yeniden anlatıldı.\n\n**Akılda kalsın**\n- Dijital iskemi nedenleri: **vazokonstriktör enjeksiyonu** (adrenalin oto-enjektör), emboli, Raynaud/skleroderma, vaskülit, travma, ergot, kokain.\n- Adrenalin enjeksiyonunda: **fentolamin lokal**, ılık ortam; soğuk uygulama yok.\n- Not: **adrenalinli lokal anestezik** sağlıklı parmakta güvenli kabul edilir; sorun yüksek dozlu oto-enjektördedir.\n- Raynaud/skleroderma kaynaklı kritik iskemide: sıcak, kalsiyum kanal blokeri, iloprost; romatoloji.\n\n*Kaynak: Muck ve ark., Ann Emerg Med 2010 (sistematik derleme).*","good"),
 "n9":E("Uzamış iskemi","Soğuk uygulama sonrası iskemi uzadı; parmak ucunda doku kaybı gelişti.","bad"),
}))
Qs+=[Q("c90q1","Adrenalin oto-enjektörünün parmağa yanlışlıkla enjeksiyonunda kullanılan antidot hangisidir?",["Nalokson","Fentolamin (lokal infiltrasyon)","Atropin","Propranolol","Heparin"],1,"Alfa-adrenerjik vazospazmı geri çevirir.","El cerrahisi / Toksikoloji"),
 Q("c90q2","Dijital vazospazmda hangisinden kaçınılmalıdır?",["Ilık ortam","Soğuk uygulama (buz)","Fentolamin","Topikal nitrat","Gözlem"],1,"Soğuk vazokonstriksiyonu artırır.","El cerrahisi / Toksikoloji"),
 Q("c90q3","Adrenalinli lokal anesteziğin parmakta kullanımı için güncel görüş hangisidir?",["Kesinlikle kontrendike","Sağlıklı parmaklarda genellikle güvenli","Yalnız çocuklarda","Her zaman fentolamin gerekir","Kangren yapar"],1,"Düşük konsantrasyonlu adrenalinli lidokainin güvenliği gösterilmiştir.","El cerrahisi / Toksikoloji")]

P={"id":"ilk-nobet-9","title":"İlk Nöbet Vakaları — 9. Paket","desc":"Üst ekstremite akut iskemisi, alkali göz yanığı, sigmoid volvulus, infektif endokardit, retrobulber hemoraji, miksödem koması, pnömatozis intestinalis, korneal ülser, karotis diseksiyonu, dijital iskemi.",
   "source":"Gazi Acil Tıp — özgün senaryolar (güncel kılavuzlara dayanır; klinik kontrol sonrası yayınlayın)",
   "pool":"İlk Nöbet Vakaları — 9. Paket","sims":S,"questions":Qs,
   "module":{"title":"İlk Nöbet Vakaları — 9. Paket","topic":"Acil tıp","order":9,"req":[3],"desc":"Göz, damar, endokrin ve nadir abdominal acillerden 10 vaka.","intro":INTRO}}
build(P,sys.argv[1])
