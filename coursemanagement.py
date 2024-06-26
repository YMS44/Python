import sys

courselst = [("DBDA", 100),("DAI", 40)]
def addnewcourse():
    cname = input("Enter course name: ")
    capacity = int(input("Enter capacity: "))
    courselst.append((cname, capacity))
    return True
def dlt():
    print("*"*10,"Delete any Course","*"*10)
    str1 = input("enter the name of the course to delete")
    x = str1.upper()

    for pos,i in enumerate(lst):
        if x == i[0]:
            lst.pop(pos)
            return True
    return False
'''
def modcrs():
    print("*"10, "Modify Course Name","*"*10)
    str1 = input("enter")'''
   
def displayall(lst = courselst):
    for cname, capa in lst:
        print(f"({cname}----->{capa})")

def searchsourses(searchc):
    lst=[]
    for cname, capa in courselst:
        if capa > searchc:
            lst.append(cname, capa)
    return lst

def searchbyname(old):
    for pos, c in enumerate(courselst):
        if c[0] == old:
            return pos, c
        else:
            return -1, None

def modifybycourseName(old, naw):
    pos, cdetails = searchbycname(old)
    if pos != -1:
        ans = input(f"do you want to modify{old} with {new}")
        if ans == "y":
            courselst[pos]=(new, cdatails[1])
            return 1
        else:
            return 2
    else:
        return 3

choice = 0
while choice != 7:
    choice = int(input('''
    1. add new course
    2. delete the course
    3. modify course duration
    4. modify course name
    5. display all
    6. display only course with capacity > given capacity
    7. exit
    choice: '''
))



    if choice == 1:
        status = addnewcourse()
        if status:
            print("new course added successfully")

    elif choice == 2:
        x = dlt()
        if x==False:
             

    elif choice == 3:
        pass

    elif choice == 4:
        oldcourse = input("Enter old course name")
        newcourse = input("Enter new course name")
        status = modifybycourseName(oldcourse, newcourse)
        if status == 1:
            print("found and modification done")

        elif status == 2:
            print("found and not modified")

        else:
            print("not found")

    elif choice == 5:
        displayall()

    elif choice == 6:
        search = int(input("enter capacity to search course"))
        lstc = searchcources(searchc)
        displayall(lstc)

    elif choice == 7:
        print("thank you for visiting....")
        #sys.exit(0)
        
