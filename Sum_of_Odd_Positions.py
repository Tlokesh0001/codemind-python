x=int(input())
l=[int(i)for i in input().split()]
o=[l[i]for i in range(len(l))if i%2==1]
print(sum(o))