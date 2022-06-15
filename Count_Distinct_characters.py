s=input().lower()
e=[]
c=0
for i in s:
    if i>='a' and i<='z' and i not in e:
        e.append(i)
print(len(e))