x=int(input())
def prime(x):
    f=0
    for i in range(2,x):
        if x%i==0:
            f+=1
    return f==0
f=0
e=[]
for i in range(2,x):
    if x%i==0:
        if prime(i) and prime(x//i) and i!=x//i:
            e.extend((i,x//i))
            f=1
            break
if f==0:
    print(-1)
else:
    print(*e)