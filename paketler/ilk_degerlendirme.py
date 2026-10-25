# Başlangıç düğümüne tıklanarak açılan "İlk değerlendirme" adımları ekler:
# monitör + vitaller (vitaller tıklanınca görünür), fizik muayene, damar yolu, oksijen.
# Puanlar: gerekli adım +1/+2; gereksiz oksijen (SpO2 normal) -1; gereksiz damar yolu 0 (açıklamalı).
import re

def D(label,pts,mins,res,fb="",vit=False):
    o={"kind":"do","label":label,"pts":pts,"min":mins,"res":res,"fb":fb}
    if vit: o["vit"]=True
    return o

SKIP={"c57","c64"}                      # arrest: ilk ekranda doğrudan KPR kararı
NO_O2={"c13","c48","c49","c59","c68","c72","c74"}   # oksijen ana kararın parçası
NO_IV={"c71"}                           # damar yolu ana kararın kendisi

EXAM={
 "c01":"Solgun, terli. Hava yolu açık, konuşuyor. Kalp sesleri ritmik, üfürüm yok. Akciğerler temiz. Periferik nabızlar eşit. Ağrı 8/10, yayılım yok.",
 "c39":"Uyanık, oryante. Kalp sesleri ritmik, üfürüm yok. Akciğerler temiz. Nörolojik muayene normal.",
}
VITRES={"c39":"Monitörde birkaç saniyelik, QRS'leri eksen etrafında dönen **polimorfik VT atakları** kendiliğinden sonlanıyor."}
VITALS={"c88":"KB 118/72 · Nb 80 · Ateş 36,8"}

# SpO2'si yazılmamış vakalara klinik tabloya uygun değer (oksijen kararı anlamlı olsun)
SPO2_ADD={"c14":98,"c22":99,"c28":94,"c30":97,"c33":98,"c34":98,"c35":97,"c36":97,"c37":97,"c40":99,"c43":97,
 "c44":97,"c45":92,"c47":97,"c51":96,"c56":96,"c58":95,"c65":95,"c66":97,"c69":95,"c71":96,"c73":95,"c75":96,"c76":98,
 "c77":97,"c79":98,"c81":97,"c82":99,"c83":96,"c85":98,"c87":95,"c88":99,"c89":98,"c90":99,"c91":98,"c94":98,"c95":98,
 "c96":98,"c97":97,"c98":99,"c99":96,"c100":96}

IV_OK=("Geniş lümenli (18G) damar yolu açıldı; kan örnekleri laboratuvara gönderildi.",
       "Hastanın tedavisi için erken damar yolu ve kan örnekleri — ilaç/sıvı vermeyi geciktirmez.")
IV={ # key: (pts, res, fb)
 "c12":(0,"Nöbet sürerken damar yolu ancak 5. dakikada açılabildi.","Damar yolu denemesi benzodiazepini geciktirmemeli: damar yolu yoksa IM/intranazal/bukkal midazolam."),
 "c18":(0,"Damar yolu açıldı; çocuk ağladı.","İyi görünen, basit febril nöbet geçirmiş çocukta damar yolu ve rutin kan tetkiki gerekmez."),
 "c24":(0,"Damar yolu açılırken çocuk ağladı, öksürüğü arttı.","Stabil yabancı cisim aspirasyonunda çocuğu ağlatacak gereksiz girişimden kaçının; tıkanma tama dönüşebilir."),
 "c30":(0,"Damar yolu açıldı.","Rutin damar yolu gerekmez; öncelik mesanenin boşaltılması."),
 "c33":(0,"Damar yolu iki denemede açılabildi.","Orta dehidratasyonda ilk tercih oral (gerekirse NG) rehidratasyondur; damar yolu ağır dehidratasyonda veya ORS başarısız olursa."),
 "c35":(0,"Damar yolu açıldı.","Zorunlu değil; analjezi IV ya da hematom bloğu ile yapılabilir."),
 "c47":(0,"Damar yolu açıldı; kan örnekleri alındı.","Rutin damar yolu gerekmez; kan örnekleri alınır, steroid ağızdan başlanabilir."),
 "c82":(0,"Damar yolu açıldı — bu sırada göz yıkanmadı.","Kimyasal göz yanığında öncelik damar yolu değil, hemen bol sıvıyla irigasyondur."),
 "c88":(0,"Damar yolu açıldı.","Keratitte damar yolu gerekmez."),
 "c90":(0,"Damar yolu açıldı.","Sistemik belirtisi olmayan dijital adrenalin enjeksiyonunda damar yolu gerekmez."),
 "c98":(0,"Damar yolu açıldı.","Genel durumu iyi, komplike olmayan sistitte damar yolu gerekmez."),
}

O2_SPECIAL={
 "c24":(0,"Çocuğa yüz maskesi takılmak istendi; ağlamaya başladı.","SpO₂ %95: çocuğu ağlatmadan, annesinin kucağında tutun; O₂ gerekirse maskesiz (blow-by) verin."),
 "c29":(0,"Nemlendirilmiş O₂ başlandı.","SpO₂ %95: hastayı rahat ettiği pozisyonda, ajite etmeden izleyin; O₂ gerekirse nemlendirilmiş verilir."),
 "c53":(1,"Rezervuarlı maskeyle O₂ sürüyor; SpO₂ hâlâ %82.","Oksijen sürmeli, ama hipoksinin nedeni (tansiyon pnömotoraks) hemen dekomprese edilmeli."),
 "c60":(0,"Hasta mekanik ventilasyonda; FiO₂ SpO₂'ye göre ayarlandı.","Ventilatördeki hastada FiO₂'yi SpO₂ hedefine göre ayarlayın."),
 "c92":(0,"Nazal kanülle O₂ başlandı.","SpO₂ %97 — hipoksemi yok; rutin oksijen gerekmez (gözlem için yatırılan hastada bazı merkezler yüksek akım O₂ tercih eder)."),
}

def spo2(v):
    m=re.search(r"SpO₂\**\s*%\s*(\d+)",v or "")
    return int(m.group(1)) if m else None

def o2opt(key,v):
    if key in O2_SPECIAL:
        p,r,f=O2_SPECIAL[key]; return D("Oksijen başla",p,1,r,f)
    s=spo2(v)
    if s is None:
        return D("Oksijen başla",0,1,"Nazal kanülle 2–4 L/dk O₂ başlandı.",
                 "Önce SpO₂'ye bakın: hedef %94–98 (hiperkapni riski olanlarda %88–92). Hipoksemi yoksa rutin oksijen gerekmez.")
    if s<94:
        return D("Oksijen başla",2,1,"Yüksek akım O₂ (rezervuarlı maske) başlandı; SpO₂ hedefi %94–98'e göre titre ediliyor.",
                 f"Hipoksemi var (SpO₂ %{s}): oksijen ilk müdahalelerdendir.")
    m=re.search(r"KB[^0-9]*(\d+)/",v or "")
    if m and int(m.group(1))<90:
        return D("Oksijen başla",0,1,"Rezervuarlı maskeyle O₂ başlandı.",
                 f"SpO₂ %{s} ama hasta şokta: birçok protokol başlangıçta O₂ verip SpO₂ %94–98'e titre etmeyi önerir; hipoksemi yoksa hiperoksiden kaçının. Öncelik dolaşımın düzeltilmesi.")
    return D("Oksijen başla",-1,1,"Nazal kanülle O₂ başlandı.",
             f"SpO₂ %{s} — hipoksemi yok. Rutin oksijen yarar sağlamaz; hiperoksi (ör. AKS ve inmede) zararlı olabilir. Hedef %94–98.")

def clean(t):
    t=re.sub(r"Hasta monitöre alındı, damar yolu açıldı\.\s*","",t or "")
    return t.strip()

def apply(c):
    k=c["key"]
    if k in SKIP: return c
    n=c["nodes"][c["start"]]
    if any(o["kind"]=="do" for o in n["opts"]): return c
    if k in VITALS: n["vitals"]=VITALS[k]
    if k in SPO2_ADD and spo2(n.get("vitals")) is None: n["vitals"]=(n.get("vitals","")+f" · SpO₂ %{SPO2_ADD[k]}").strip(" ·")
    exam=EXAM.get(k) or clean(n["text"])
    ds=[D("Monitöre bağla, vital bulguları ölç",1,2,VITRES.get(k,""),
          "Her hastada ilk adım: monitör ve vital bulgular.",vit=True),
        D("Fizik muayene (ABCDE)",1,3,exam,"Sistematik ABCDE değerlendirmesi kritik bulguları kaçırmamanızı sağlar.")]
    if k not in NO_IV:
        p,r,f=IV.get(k,(1,)+IV_OK); ds.append(D("Damar yolu aç, kan örneklerini al",p,3,r,f))
    if k not in NO_O2: ds.append(o2opt(k,n.get("vitals","")))
    n["opts"]=ds+n["opts"]; n["vh"]=True
    n["text"]="Hasta sedyeye alındı. **İlk değerlendirme** adımlarından gerekli gördüklerinizi seçin; ardından tetkik isteyin ya da karar verin."
    return c
