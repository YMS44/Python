def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)
def fadd(x):
    if x==0:
        return 0
    else:
        return x+fadd(x-1)


x=int(input("enter a number:"))
print(f"factorial of {x}:",fact(x))
print(f"summation till {x}:",fadd(x))
