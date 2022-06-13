x,y=map(int,input().split())
l=[int(i)for i in input().split()]
l1=[int(i)for i in input().split()]
e=[]
for i in l:
    if i not in l1:
        print(i,end=' ')
for i in l1:
    if i not in l:
        print(i,end=' ')