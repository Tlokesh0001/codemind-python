t=int(input())
for ty in range(t):
    x=int(input())
    l=[int(i)for i in input().split()]
    if l==sorted(l):
        print(0)
    else:
        print(max(l)-min(l))