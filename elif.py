t = int(input("number of cases"))
while t>0:
    age = int(input("enter age"))
    t=t-1
    if age< 5:
        print("Age is greater than 5")
        print("You can not drive the car")
    elif age >= 5 and age < 18:
        print("You are not allowed to drive the car")
    elif age >18 and age < 60:
        print("You are allowed to deive the car")
    else:
        print("abe apna  kaam kr na bhai ku yaha aaya hai")
