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
            pass
        case 3:
            pass
        case 4:
            displayall()
        case 5:
            pass
        case 6:
            print("abc", conn.close())
        