x=int(input())
l=[int(i)for i in input().split()]
e=[i for i in l if i%2==0]
o=[i for i in l if i%2==1]
k=[]
if len(e)>len(o):
    for i in range(len(o)):
        k.append(o[i])
        k.append(e[i])
    r=e[len(o)::]
    if len(r)%2==1:
        r.append(0)
    r=k+r
    print(*r)
else:
    for i in range(len(e)):
        k.append(o[i])
        k.append(e[i])
    r=o[len(e)::]
    if len(r)%2==1:
        r.append(0)
    r=k+r
    print(*r)