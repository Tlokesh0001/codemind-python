x=int(input())
e=[]
while x>0:
    r=x%10
    e.append(r)
    x=x//10
for i in e:
    if e.count(i)!=1:
        print('Not Unique Number')
        break
else:
    print('Unique Number')