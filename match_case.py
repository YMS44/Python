choice = int (input("Enter number: "))
match choice:
    case 1:
        print("choice is 1")

    case 2:
        print("choice is 2")

    case _:
        print("choice is default case")

color = input("Enter color: ")
match choice:
    case "red" | "yellow":
        print("red or yellow")

    case "green":
        print("green is selected")

    case other:
        print("default case for color")
