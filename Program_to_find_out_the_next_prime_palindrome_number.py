def prime(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f+=1
    return f==0
def pal(x):
    i=0
    s=x
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i==s
def npal(x):
    while pal(x)!=True:
        x+=1
    return x
x=int(input())
if pal(x):
    n=npal(x+1)
else:
    n=npal(x)
while prime(n)!=True:
    n=npal(n+1)
print(n)