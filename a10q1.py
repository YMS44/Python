import sqlite3

try:
    conn = sqlite3.connect("employee_data.db")
    print("connection done")
    
except Exception as e:
    print("Error occured", e)
    
def display_all():
    cursor.execute("select * from employee")
    for row in cursor.fetchall():
        print(f"name: {row[0]} id: {row[1]} salary: {row[2]}")
        
def sal_comp(sal):
    try:
        cursor.execute(f"select * from employee where salary > {sal} ")
        for row in curser.fetchall():
            print(f"name: {row[0]} id: {row[1]} salary: {row[2]}")
            
    except Exception as e:
        print("error", e)
            
        
def display_by_id():
    try:
        cursor.execute(f"select * from employee where id={id}")
        row = cursor.fetchone()
        print(f"name: {row[0]} id: {row[1]} salary: {row[2]}")
    except Exception as e:
        print("error",e)
        
def add_new_employee():
    try:
        name = input("enter name: ")
        eid = int(input("enter id: "))
        salary = float(input("enter salary: "))
        
        cursor.execute("insert into employee values(?,?,?)",(name,eid,salary))
        conn.commit()
    except Exception as e:
        print("error",e)
        conn.rollback()
        
        
def delet(name):
    try:
        cursor.exicute("delet from employee where name=?",(name,))
        conn.commit()
        return True
    except Exception as e:
        print("error", e)
        conn.rollback
        return False
    
def update(name,eid,salary):
    try:
        cursor.execute("update enployee set name=?, eid=?, salary=?",(name, eid, salary))
        conn.comit()
        return True
    except Exception as e:
        print("error",e)
        return False
    
cursor = conn.cursor()

choice = 0

while True:
    choice=int(input("""
1. add new product
2. delete product by id
3. update product by id
4. display all
5. display by id
6. exit"""))

    match choice:
        case 1:
            pass
        
    
    