def add(x):
    s=0
    while x>0:
        r=x%10
        s+=r
        x=x//10
    return s
x=int(input())
s=x*x
if add(s)==x:
    print('Neon Number')
else:
    print('Not Neon Number')