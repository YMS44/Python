num = int(input("enter number: "))

if num%2 == 0:
    print("number should be odd")

else:
    cnt = num // 2
    for i in range(1, num+1,2):
        print(" "*cnt,"*"*i,sep="")
        cnt = cnt - 1

    cnt = 1
    for i in range(num-2,0,-2):
        print(" "*cnt,"*"*i,sep="")
        cnt = cnt + 1

    
num1 = int(input("enter number"))

if num1%2 == 0:
    print("number should be odd")
else:
    for i in range(1,2*(num1+1)):
        if i < num1:
            print(" "*(num1-i),"*"*(2*i-1))
        elif i >= num1 and i <= (2*num1):
            print(" "*(i-(2*num1)+1),"*"*(i-(2*num1)-1))
