#display menu o the user for addition of 2 numbers, find factorial

import sys

def addition(n1,n2):
    return n1+n2

def factorial(n1):
    s=1
    for i in range(2,n1+1):
        s=s*i
    return s

choise =0

while choise!=3:
    choise = int(input("""1-Addition
    2-Factorial
    3-exit"""))

    if choise ==1:
        n1 =int(input("enter number 1"))
        n2 = int(input("enter number 2"))
        a = addition(n1,n2)
        print(f"Addition:{a}")
    elif choise == 2:
        n1 = int(input("enter number"))
        ans= factorial(n1)
        print(f"fatorial : {ans}")
    elif choise == 3:
        print("thank you for the visit")
        sys.exit(0)
    else:
        print("wrong chosise")
