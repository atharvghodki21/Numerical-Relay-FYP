import math
v=[39.93,41.36, 42.78, 44.20]
t=[0,0.00002,0.00004,0.00006]
vdash=[]
v2=[] #v^2
w=2*math.pi*50
a=[] #vdash/w
b=[] #(vdash/w)^2
c=[] #v^2+(vdash/w)^2
vm=[] #sqrt(v^2+(vdash/w)^2)
d=[] #v/(vdash/w)
phi_v=[] #atan(v/vdash/w))-wt
n=len(v)
for i in range(n-2):
    for j in range(i,i+3):
        for x in range(len(v)):
            vd=math.pow(v[x],2)
            v2.append(vd)
for q in range(2):
    for r in range(q, q + 3):
        for y in range(len(vdash)):
            e=vdash[y]/w
            a.append(e)
for s in range(2):
    for t in range(s, s + 3):
        for z in range(len(vdash)):
            f= math.pow((vdash[z]/w),2)
            b.append(f)
for u in range(2):
    for v in range(u, u + 3):
        for l in range(len(vdash)):
            g= (math.pow(v,2)+math.pow((vdash[l]/w),2))
            c.append(g)
for w in range(2):
    for a1 in range(w, w + 3):
        for k in range(len(vdash)):
            h=math.sqrt((math.pow(v,2)+math.pow((vdash[k]/w),2)))
            vm.append(h)
for b1 in range(2):
    for c1 in range(b1, b1 + 3):
        for m in range(len(vdash)):
            o=v/(vdash[m]/w)
            d.append(o)
for d1 in range(2):
    for e1 in range(d1, d1 + 3):
        for n in range(len(vdash)):
            p=a*tan(v/(vdash[n]/w))-w*t[j]
            phi_v.append(p)
print(vdash)
print(v2)
print(a)
print(b)
print(c)
print(vm)
print(d)
print(phi_v)





