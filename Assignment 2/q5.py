x=int(input("enter a number:"))
count=0
z=0
y=0
while x!=0:
    count=count+1
    y=x%10
    z=z+y
    x=x//10

print("no of digits:",count,"\nsum:",z)
    
