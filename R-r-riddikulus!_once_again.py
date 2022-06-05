x,k=map(int,input().split())
l=[int(i)for i in input().split()]
while k>0:
    l.append(l[0])
    l.remove(l[0])
    k-=1
print(*l)