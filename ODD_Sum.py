x=int(input())
l=[int(i)for i in input().split()]
print(sum(i for i in l if i%2==1))