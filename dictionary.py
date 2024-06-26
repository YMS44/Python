d={"DBDA":(100,60),"DAI":(200,50)}
print("length:",len(d))
print(d)

#to add new key value pair in dictionary
d["DAC"]=(11,12)
print("length:",len(d))
print(d)

#to check if the key value pair exists
k=input("enter key to search:")
v=d.get(k.upper())
if v==None:
    print("key not found")
else:
    print(f"value at {k}:",v)

sd=d.setdefault("DITISS",(100,12))
if sd==100:
    print("not found so added")    
else:
    print("key found and value",sd)
    
#gd=d.get

for k in d.keys():
    print(f"{k}------>{d[k]}")

#for k,b in d.items():
#    if b[1]>50:
#        print(f"{k}------>{b}")

l=[1,2,3]
d1=dict.fromkeys(l)
print(d1)

d2=dict.fromkeys(l,1000)
print(d2)

d3={'a':10,'b':20}
d4={'c':30,'b':40}
d3.update(d4)
print(d3,d4)

d5=**d3.update(**d4)
print(d5)

