t=int(input())
for t1 in range(t):
    x,y=map(int,input().split())
    l=[int(i)for i in input().split()]
    l1=[int(i)for i in input().split()]
    k=l+l1
    k.sort()
    print(*k)