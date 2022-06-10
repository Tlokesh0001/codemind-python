x=int(input())
s=0
p=1
while x>0:
    r=x%10
    s+=r
    p*=r
    x=x//10
if p==s:
    print('Spy Number')
else:
    print('Not Spy Number')