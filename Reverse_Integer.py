n=int(input())
f=n
n=abs(n)

s=0
while n:
    r=n%10
    s=s*10+r
    n=n//10
if f<0:
    print(-s)
else:
    print(s)
    