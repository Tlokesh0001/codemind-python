def add(n,s):
    if (n == 0 and s<10):
        return s
    if (s>9 and n ==0):
        return add(s,0)
    return add(n//10,s+n%10)
x = int(input())
print(add(x,0))