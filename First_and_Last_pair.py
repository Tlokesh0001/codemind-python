x=int(input())
l=[int(i)for i in input().split()]
h=len(l)//2
if x%2==1:
    l.insert(h+1,0)
for i in range(len(l)//2):
    print(l[i],l[(0-i+(len(l)-1))],end=' ')
#print(l)