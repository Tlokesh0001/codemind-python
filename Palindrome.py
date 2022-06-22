x=int(input())
s=x
i=0
while x>0:
    r=x%10
    i=i*10+r
    x=x//10
print(s==i)