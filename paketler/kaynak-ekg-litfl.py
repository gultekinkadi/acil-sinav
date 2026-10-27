# LITFL EKG örnek paketi — görüntüler LITFL ECG Library'den (CC BY-NC-SA 4.0), içe aktarmada indirilir.
# Yorumlar, işaretlemeler ve sorular Gazi Acil Tıp tarafından hazırlanmış uyarlamadır ve aynı lisansla (CC BY-NC-SA 4.0) paylaşılır.
import json, sys
U="https://litfl.com/wp-content/uploads/"
LIC="LITFL ECG Library (litfl.com), CC BY-NC-SA 4.0"
def credit(page,title): return f"Kaynak: {LIC} — “{title}”, https://litfl.com/{page}/. Yorum ve işaretlemeler: Gazi Acil Tıp (uyarlama, CC BY-NC-SA 4.0)."
A=[{
 "key":"inferior-stemi-1","title":"İnferior STEMI","cat":"EKG","topic":"Kardiyoloji",
 "media":[{"url":U+"2018/08/ECG-Inferior-AMI-STEMI.jpg","cap":"12 derivasyonlu EKG — "+LIC}],
 "desc":"Sinüs ritmi, hız ≈65/dk. **II, III ve aVF'de ST elevasyonu** (inferior duvar); **III'teki elevasyon II'dekinden belirgin** → en olası suçlu damar **sağ koroner arter (RCA)**. Göğüs derivasyonlarında belirgin ST çökmesi yok.\n\n"+credit("inferior-stemi-ecg-library","Inferior STEMI"),
 "pearls":"- İnferior STEMI'de **III > II** ST elevasyonu RCA, **II ≥ III** ve lateral tutulum sirkumfleksi düşündürür.\n- **aVL'de ayna ST çökmesi** erken ve duyarlı bir bulgudur.\n- Her inferior STEMI'de **V4R** (sağ ventrikül tutulumu) ve **V7–V9** (posterior uzanım) çek.\n- Sağ ventrikül tutulumunda **nitrattan kaçın** (önyük bağımlı); hipotansiyonda sıvı.\n- Bradikardi ve AV blok sıktır (AV düğüm çoğunlukla RCA'dan beslenir).",
 "findings":[
  {"id":"f3","shape":"ellipse","x":0.02,"y":0.57,"w":0.25,"h":0.12,"label":"III — ST elevasyonu (en belirgin)","text":"ST elevasyonu III'te en belirgin; III > II, RCA tıkanıklığını düşündürür."},
  {"id":"fF","shape":"ellipse","x":0.275,"y":0.57,"w":0.235,"h":0.12,"label":"aVF — ST elevasyonu","text":"İnferior duvarı gören üçüncü derivasyon."},
  {"id":"f2","shape":"ellipse","x":0.02,"y":0.355,"w":0.25,"h":0.10,"label":"II — ST elevasyonu","text":"II'de de ST elevasyonu var ama III'tekinden küçük."}],
 "tasks":[
  {"id":"t1","fid":"f3","prompt":"İnferior derivasyonlar içinde ST elevasyonunun EN belirgin olduğu derivasyonu tıklayın."},
  {"id":"t2","fid":"fF","prompt":"aVF'deki ST elevasyonunu gösterin."}],
 "source":LIC}]
Q=[
 {"key":"q01","imageUrl":U+"2018/08/ECG-Inferior-AMI-STEMI.jpg","topic":"EKG",
  "stem":"40 dakikadır göğüs ağrısı olan 62 yaşında erkeğin EKG'si görülüyor. En olası tanı hangisidir?",
  "options":["İnferior STEMI","Akut perikardit","Benign erken repolarizasyon","Anterior STEMI","Sol ventrikül hipertrofisi (strain)"],"correct":0,
  "explanation":"II, III ve aVF'de ST elevasyonu inferior STEMI ile uyumludur; perikarditte yaygın ST elevasyonu ve PR çökmesi beklenir. "+credit("inferior-stemi-ecg-library","Inferior STEMI")},
 {"key":"q02","imageUrl":U+"2018/08/ECG-Inferior-AMI-STEMI.jpg","topic":"EKG",
  "stem":"Aynı EKG'de ST elevasyonunun III'te II'den belirgin olması en olası hangi koroner arter tıkanıklığını düşündürür ve reperfüzyon öncesi hangi ek derivasyon çekilmelidir?",
  "options":["Sağ koroner arter — V4R","Sol ana koroner — aVR","Sol ön inen arter — V1–V3 tekrar","Sirkumfleks arter — I ve aVL","Septal dal — V5–V6"],"correct":0,
  "explanation":"III > II ve ayna değişiklikler RCA'yı düşündürür; RCA proksimal tıkanıklığında sağ ventrikül tutulumu olabileceğinden V4R çekilir, tutulum varsa nitrattan kaçınılır. "+credit("inferior-stemi-ecg-library","Inferior STEMI")},
]
P={"id":"ekg-litfl-ornek","title":"EKG Atlası (LITFL) — örnek","desc":"LITFL EKG kütüphanesinden örnek: inferior STEMI — işaretli atlas görüntüsü ve 2 görselli soru. Görüntüler içe aktarmada LITFL'den indirilir.",
   "source":LIC,"pool":"EKG Atlası (LITFL)","sims":[],"atlas":A,"questions":Q}
json.dump(P,open(sys.argv[1],"w"),ensure_ascii=False,indent=1); print("ok",len(A),len(Q))
