x=int(input())
l=[int(i)for i in input().split()]
c=0
h=l.index(min(l))
h1=l.index(max(l))
def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return 0
    else:
        return 1
if h1<h:
    h1,h=h,h1
for i in range(h,h1+1):
    if prime(l[i])==1:
        c+=1
print(c)