s=input()
v='aeiouAEIOU'
e=[]
k=[]
l=list(s)
for i in range(len(l)):
    if l[i] in v:
        e.append(l[i])
        l[i]='!'
j=len(e)-1
for i in range(len(l)):
    if l[i]=='!':
        l[i]=e[j]
        j-=1
print(''.join(l))