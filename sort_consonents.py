s=input()
s=s.split()
l=[]
al='bcdfghjklmnpqrstvwxyz'
for i in s:
    i=list(i)
    l=[]
    for j in range(len(i)):
        if i[j] in al:
            l.append(i[j])
            i[j]='!'
    l.sort()
    j=0
    for k in range(len(i)):
        if i[k]=='!':
            i[k]=l[j]
            j+=1
    print(''.join(i),end=' ')
        
'''j=0
l.sort()
for i in range(len(s)):
    if s[i]=='!':
        s[i]=l[j]
        j+=1
print(''.join(s))'''