s=input()
l=list(s)
for i in l:
    if l.count(i)==1 and i>='a' and i<='z':
        print(i)
        break
else:
    print(-1)