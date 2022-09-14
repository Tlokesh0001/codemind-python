#This will also work
'''import math
def fun (le , x):
    if le == 0:
        return x
    return fun(le-1,x//10)+((x%10)*10**le)
def rev(x):
    le = int(math.log10(x) + 1)
    return fun(le-1,x)
x=int(input())
print(rev(x))'''

#For finding Length
def lth(x,l):
    if (x%10 == x):
        return l
    return lth(x//10,l+1)
#Main Reversing Function
def fun(x, l):
    if (x%10 == x):
        return x
    return ((x%10)*10**l)+fun(x//10,l-1)
#rev Function
def rev(x):
    l = 0
    lent = lth(x,l)
    return fun(x,lent)

x=int(input())
Neg = False
if x<0: 
   Neg = True
   x = -x
print(rev(x) if Neg==False else '-'+str(rev(x)))