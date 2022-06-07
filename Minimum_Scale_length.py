def LCM(x,y):
    h=0
    s=0
    if x>y:
        h=x
        s=y
    else:
        h=y
        s=x
    for i in range(h,0,-1):
        if h%i==0 and s%i==0:
            return i
x=int(input())
l=[int(i)for i in input().split()]
lcm=0
for i in l:
    lcm=LCM(lcm,i)
print(lcm)