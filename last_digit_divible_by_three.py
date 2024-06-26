num = int(input("Please enter a number: "))

l_digit = num % 10
print(l_digit)

if (l_digit % 3) == 0:
    print("The last digit of a number is divisible by 3")

else:
    print("The last digit of a number is not divisible by 3")
