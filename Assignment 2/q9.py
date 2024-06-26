def f(x):
    if x==0:
        return 1
    else:
        return x*f(x-1)

m=int(input("enter value x:"))
n=int(input("enter no of terms:"))
x=0

for i in range(n):
    x=x+((m**i)/(f(i)))

print(x)
