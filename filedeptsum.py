sum1=0
lst=[]
fh=open("mydata1.txt",'r')
dept=input("enter the dept whose sum you want:")
for line in fh:
    line=line.rstrip("\n")
    lst=line.split(":")
    if lst[4] == dept:
        sum1=sum1+int(lst[3])            
print(f"sum of salary of {dept} department is:",sum1) 
fh.close()