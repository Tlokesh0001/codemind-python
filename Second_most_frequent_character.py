s=input()
l=list(s)
e=[]
for i in l:
    e.append(l.count(i))
m=max(e)
for i in l:
    if l.count(i)==m:
        while l.count(i)>0:
            l.remove(i)
k=l.count(max(l))
f=0
e1=[]
for i in l:
    if l.count(i)>=k:
            e1.append(i)
for i in e1:
    if l.count(i)==1:
        print(-1)
        break
else:
    print(e1[0])