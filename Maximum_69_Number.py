def rev(x):
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i
x=int(input())
r=rev(x)
#print(r)
c=0
i=0
while r>0:
    e=r%10
    if e<9:
        c+=1
    if e<9 and c==1:
        e=9
    i=i*10+e
    r=r//10
print(i)
    
    