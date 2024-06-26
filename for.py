for i in range(5):
    print("hello")

print("hello"*5)
print("hello\n"*5)

for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(10,1,-2):
    print(i)


s = 0
for i in range(10):
    num = int(input("enter number"))
    if num%10 == 0:
      print("you have entered a wrong number")
      break
    s = s + num
else:
    print(f"sum : {s}")
