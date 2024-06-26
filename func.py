def fun():
    global count
    print("you called f1",count)
    count = count+1

def f1(x,y):
    x=x+10
    y=y+5
    return x + y

def f2(a, b=5,c=6):
    a = b + c
    b = a + c
    return a+b+c

count =0
fun()
fun()
print(count)

print(f1(12,13))
print(f2(b=10, a=23 ))
print (f2(6, c=34,b=56))

def f1():
    x=34
    print(x)
    def f2():
        #global x
        nonlocal x
        x=45
        print(x)
    print(x)
    f2()
    print(x)

    
x= 10
print(x)
f1()
print(x)



x=9
print(x,bin(x))
y=11
print(y,bi(y))

newnum = x<<4
newx = newnum|y
print(newx,bin(newx))

y1 = newx&(int(obin1111))
print("y1",y1,"y",y)
print("x1",newx>>4,"x",x)



