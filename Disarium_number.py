def rev(x):
    s=str(x)
    s1=s[::-1]
    return int(s1)
x=int(input())
r=rev(x)
s=0
l=0
while r>0:
    e=r%10
    l+=1
    s+=(e**l)
    r=r//10
print(s==x)
    