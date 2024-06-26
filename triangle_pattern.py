import sqlite3

try:
    conn = sqlite3.connect("mydb.db")
    print("connection done")
except Exception as e:
    print("error occured",e)
    
def displayall():
    cursor.execute("select * from product")
    for row in cursor.fetchall():
        print(f"pid: {row[0]} pname{row[1]} qyt:{row[2]} price:{row[3]}")
        
def displaybyid(pid):
   try:
       cursor.execute("select * from product where pid=?",(pid),)
       row = cursor.fetchone()
       print(f"pid: {row[0]} pname{row[1]} qyt:{row[2]} price:{row[3]}")
     except Exception as e:
         print("error occured",e)
         
def addnewproduct():
    pid = int(input("enter pid"))
    pnm = input("enter name")
    qty = int(input("enter quantity"))
    price = float(input("enter price"))
    cursor.execute("insert into product values(?,?,?,?",)

cursor = conn.cursor()
choice = 0
while choice != 6 :
    choice = int(input("""
1. add new product
2. delete product
3. update product
4. display all
5. display by id
6. exit 
                       """))
                       
    match choice:
        case 1:
            pass
        case 2:
            pid = int(input("enter id"))
            status = deletebyid(pid)
        case 3:
            pass
        case 4:
            displayall()
        case 5:
            pid = int(input("enter id"))
            displaybyid(pid)
        case 6:
            print("abc", conn.close())