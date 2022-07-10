def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return 0
    else:
        return 1
x=int(input())
l=[int(i)for i in input().split()]
hi=l.index(max(l))
h=l.index(min(l))
c=0
if h>hi:
    hi,h=h,hi
for i in range(h,hi+1) :
    if prime(l[i]):
        c+=1
print(c)