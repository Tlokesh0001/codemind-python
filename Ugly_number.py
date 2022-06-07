x=int(input())
f=1
while x!=1:
    if x%2==0:
        x=x//2
    elif x%3==0:
        x=x//3
    elif x%5==0:
        x=x//5
    else:
        f=0
        break
if f==0:
    print('Not Ugly Number')
else:
    print('Ugly Number')