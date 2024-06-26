x=int(input("enter value of x:"))
y=int(input("enter number of terms:"))
sum=0
for i in range(y):
    k=(x**((2*i)+1))*((-1)**i)
    sum=sum+k
    print("values:",k)

print(sum)
