t=int(input())
for ty in range(t):
    x=int(input())
    l=[int(i)for i in input().split()]
    k=[]
    l.sort(reverse=True)
    if x%2==0:
        h=x//2
    else:
        h=x//2+1
    for i in range(h):
            k.append(l[i])
            k.append(l[(0-i+(x-1))])
    if x%2!=0:
        k.remove(k[-1])
    print(*k)
    #print(h)