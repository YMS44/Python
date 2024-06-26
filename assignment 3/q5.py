x=input("enter string1:")
y=input("enter string2:")
z=y[::-1]
d=len(x)
g=len(y)
b=max(d,g)

c=''
for i in range(min(d,g)):
    c=c+x[i]+z[i]
print("new string:",c)

    