x=int(input())
e=[]
while x>0:
    r=x%10
    e.append(r)
    x=x//10
print(max(e))