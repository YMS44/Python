l1=[1,2,3,4,5,1,1,2,3,4,2,3,4,5]
n=int(input("enter a number to delete:"))
count=1
t=[]
for i in l1:
    print(l1[i])
    if l1[i]!=n:
        t.append(l1[i])
    else:
        count=count+1


print(f"number occured {count} times","\noriginal list:",l1,"\ntuple without the number=",t)

