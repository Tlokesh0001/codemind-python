s=input().lower()
l=s.split()
l1=list(l[0])
l.remove(l[0])
c=0
e=[]
for i in l1:
    for j in range(len(l)):
        if i not in l[j] and i not in e:
            break
    else:
        e.append(i)
print(len(e))