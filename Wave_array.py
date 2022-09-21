n=int(input())
l=[int(i) for i in input().split()]
s=0
h=0
for i in range(n-1):
    if i%2!=0:
        h+=1
        if l[i]>l[(i-1)] and l[i]>l[(i+1)] or l[i]<l[(i-1)] and l[i]<l[(i+1)]:
            s+=1
if h==s:
    print("yes")
else:
    print("no")
    