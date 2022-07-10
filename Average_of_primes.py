def prime(x):
    if x==1:
        return 0
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            return 0
    else:
        return 1
x=int(input())
l=list(map(int,input().split()))
e=[i for i in l if prime(i)==1]
print('%.2f'%(sum(e)/len(e)))