def rev(x):
    i=0
    while x>0:
        r=x%10
        i=i*10+r
        x=x//10
    return i
x=int(input())#12
s=x*x#144
r=rev(x)#21
r2=r*r#441
print(s==rev(r2))