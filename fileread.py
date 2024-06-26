import re
lst=[]
lst1=[]
lst2=[]
sum=0
fh=open("mydata.txt")
for i in fh:
    i=i.rstrip('\n')
    print(i)
    lst.append(i)
print(lst)
fh.close()
print("-"*15)
    
fh=open("mydata.txt",'r')
fh1=open("mycopy.txt",'w')
for i in fh:
    m=re.search("game",i)
    if m!=None:
        fh1.write(i)
        print(fh1)
fh.close()
fh1.close()

with open("mydata.txt",'r') as fh:
    with open("mycopy.txt",'w') as fh1:
        for line in fh:
            lst=line.split(":")
            if lst[2]=="game":
                fh1.write(line)
                
fh.close()
fh1.close()
print("-"*15)

with open("mydata.txt",'r') as fh:
    with open("mycopy.txt",'w') as fh1:
        for line in fh:
            lst=line.split(":")
            sum=sum+int(lst[-1])
            print(lst)

print(sum)    
    
fh=open("mydata.txt")
lst=fh.readlines()
print(lst)
fh.close()
    

