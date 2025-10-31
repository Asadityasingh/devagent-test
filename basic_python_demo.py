x=0
y=1
z=2
a="hello"
b="world"
c=[1,2,3,4,5]
d={"k":3}
e=True
f=False
def print_value(t):print(t)
p(a)
p(b)
for i in range(5):
    x+=i
p(x)
def s(n):
    r=0
    for i in range(n):
        r+=i
    return r
p(s(10))
g=0
for i in range(10):
    g+=i*i
p(g)
h=""
for ch in "python":
    h+=ch.upper()
p(h)
def m(n):
    if n==0:return 1
    return n*m(n-1)
p(m(5))
i=1
while i<6:
    p(i)
    i+=1
j=0
k=0
for v in c:
    j+=v
p(j)
for v in c:
    k+=v*v
p(k)
l=set(c)
p(l)
tup=(1,2,3)
p(tup)
p(len(tup))
u="".join([str(i) for i in c])
p(u)
p(a+b)
r=[i*2 for i in c]
p(r)
n=1
for i in range(1,6):
    n*=i
p(n)
w=[i for i in range(10) if i%2==0]
p(w)
q=[i for i in range(10) if i%2!=0]
p(q)
from random import randint
aa=[randint(1,10) for _ in range(5)]
p(aa)
p(sum(aa))
bb=list("randomtext")
p(bb)
bb.reverse()
p(bb)
cc="".join(bb)
p(cc)
dd=lambda x:x*3
p(dd(3))
ee=[dd(i) for i in range(5)]
p(ee)
ff={i:i*i for i in range(5)}
p(ff)
gg=max(c)
p(gg)
hh=min(c)
p(hh)
ii=sorted(c,reverse=True)
p(ii)
jj=[3,1,4,1,5,9]
jj.sort()
p(jj)
kk=tuple(jj)
p(kk)
ll=list(kk)
p(ll)
mm=set(ll)
p(mm)
nn=list(mm)
p(nn)
oo=[i for i in range(1,11)]
p(oo)
pp=[i*i for i in oo]
p(pp)
qq=[i for i in oo if i%3==0]
p(qq)
rr="python programming"
p(rr.upper())
p(rr.title())
p(rr.split())
ss="test"
p(ss*5)
tt={"a":1,"b":2}
tt["c"]=3
p(tt)
uu=tt.get("b")
p(uu)
vv=[1,2,3,4,5]
p(vv[2:])
p(vv[:2])
ww=0
for i in vv:
    ww+=i
p(ww)
xx=[i%2 for i in range(10)]
p(xx)
yy=str(12345)
p(yy[::-1])
zz=[i for i in range(20) if i%5==0]
p(zz)
aaa=sum([i*i for i in range(10)])
p(aaa)
bbb=1
for i in range(1,6):
    bbb+=i
p(bbb)
ccc="end"
p(ccc)
