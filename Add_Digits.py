x=int(input())
s=0
while x>0:
    r=x%10
    s+=r
    x=x//10
    if s>9 and x==0:
        x=s
        s=0
print(s)