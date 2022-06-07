l=[int(i) for i in input().split(',')]
c=0
f=0
s=0
e=[]
u=[]
def fs(x):
    s=0
    if x>0:
        for i in range(1,x+1):
            if x%i==0:
                s+=i
        return s
    if x<0:
        for i in range(-1,x-1,-1):
            if x%i==0:
                s+=i
        return s
for i in l:
    k=fs(i)
    e.append(k)
for i in range(len(e)):
    if e[i] in l:
        u.append(l[i])
u.sort()
if len(u)!=0:
    print(*u)
else:
    print(-1)
