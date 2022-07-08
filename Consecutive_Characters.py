s=input()
c=0
m=0
l=[]
for i in range(len(s)):
    c=0
    for j in range(i,len(s)):
        if s[i]==s[j]:
            #print(s[i])
            c+=1
        else:
            m=c
            c=0
        l.append(c)
print(max(l))