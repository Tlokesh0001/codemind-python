x=int(input())
l=[int(i)for i in input().split()]
e=([l[i]for i in range(len(l))if i%2==0])
print(sum(e))