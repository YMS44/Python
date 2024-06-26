def f1(a,b):
    a=a+10
    b=b+20
    c=a+b
    return a,b,c

data=f1(23,24)
print(data)
x,y,z=f1(10,20)

#tuple of size 1

a=12,
print("%d is the number:" %(34,))

def addition(a,b=3,c=4,*t):
    s=a+b+c
    print(t)
    for n in t:
        s=s+n
    return s

print(addition(45,3,4,23))
print(addition(10,23,4,5,2,3,1,2,6,7,8,9))
