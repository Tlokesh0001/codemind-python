x=int(input())
a=0
b=1
while b<x:
    a,b=b,a+b
if x-a<b-x:
    print(a)
elif x-a>b-x:
    print(b)
else:
    print(a,b)