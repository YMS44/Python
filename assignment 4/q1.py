x=int(input("enter no of days in month:"))
y=input("enter first day of month:")

l=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

z=l.index(y)

print("\nMon Tue Wed Thu Fri Sat Sun")
print(" -  "*z,end="")
for i in range(1,x+1):
    
    if (i+z)%7==0:
        if len(str(i))==1:
             print(f"0{i}","\n")
        else:
            print(i,"\n")
   
    else:
        if len(str(i))==1:
             print(f"0{i}",end="  ")
        else:
            print(i,end="  ")
    
    

    
      
      
       
    
