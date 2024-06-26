Total = int(input("Enter total days"))
present = int(input("Enter Present days"))
pp = ((present/Total)*100)
if pp >= 75:
    print("You are allowed to sit in exam")
    print(f"Your % presenty is: {pp}%")
else:
    print("You are not allowed to sit in exam")
    print(f"Your % presenty is: {pp}%")

