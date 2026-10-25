# Ortak yardımcılar: sanal hasta paketleri
import json
def T(label,pts,mins,res,fb=""): return {"kind":"test","label":label,"pts":pts,"min":mins,"res":res,"fb":fb}
def A(label,pts,mins,to,fb=""): return {"kind":"act","label":label,"pts":pts,"min":mins,"to":to,"fb":fb}
def N(title,text,vitals="",opts=None): return {"title":title,"text":text,"vitals":vitals,"opts":opts or []}
def E(title,text,outcome): return {"title":title,"text":text,"end":True,"outcome":outcome,"opts":[]}
def case(key,title,topic,intro,nodes): return {"key":key,"title":title,"topic":topic,"intro":intro,"start":"n1","order":list(nodes.keys()),"nodes":nodes}
def Q(key,stem,opts,correct,expl,topic): return {"key":key,"stem":stem,"options":opts,"correct":correct,"explanation":expl,"topic":topic}
def best(c):
    ns=c["nodes"]
    def b(k,seen):
        n=ns[k]
        if n.get("end"): return (0,[k],n["outcome"])
        t=sum(max(0,o["pts"]) for o in n["opts"] if o["kind"]=="test"); r=[]
        for o in n["opts"]:
            if o["kind"]=="act" and o["to"] not in seen:
                s,p,oc=b(o["to"],seen|{k}); r.append((t+o["pts"]+s,[k]+p,oc))
        return max(r)
    return b("n1",set())
def build(P,out):
    S,Qs=P["sims"],P["questions"]
    keys=set()
    for c in S:
        assert c["key"] not in keys; keys.add(c["key"])
        ns=c["nodes"]
        for k,n in ns.items():
            for o in n["opts"]:
                if o["kind"]=="act": assert o["to"] in ns,(c["key"],k,o["label"])
            if not n.get("end"): assert any(o["kind"]=="act" for o in n["opts"]),(c["key"],k)
        reach=set(); st=["n1"]
        while st:
            x=st.pop()
            if x in reach: continue
            reach.add(x); st+=[o["to"] for o in ns[x]["opts"] if o["kind"]=="act"]
        assert reach==set(ns),(c["key"],set(ns)-reach)
        s,p,oc=best(c); assert oc=="good",(c["key"],p,oc)
        assert any(n.get("end") and n["outcome"]!="good" for n in ns.values()),(c["key"],"kötü son yok")
    qk=set()
    for q in Qs:
        assert len(q["options"])==5 and 0<=q["correct"]<5,q["key"]; assert q["key"] not in qk; qk.add(q["key"])
    json.dump(P,open(out,"w"),ensure_ascii=False,indent=1)
    print(P["id"],len(S),"vaka",len(Qs),"soru")
