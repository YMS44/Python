#regular expression
#pattern finding

import re
s="Something is there somewhere"
m=re.search("s.*e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

m=re.match("s.*e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
print("-"*15)

m=re.search("s.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    
m=re.match("s.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
print("-"*15)
 
m=re.search("t.*e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

m=re.match("t.*e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
print("-"*15)
    
m=re.search("t.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

m=re.match("t.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    
print("-"*83)    
    
lst=re.finditer("s.*?e",s,re.I|re.M)
if lst!=None:
    for n in lst:
        print(n.group())
        print(n.span())
else:
    print("not found")


lst=re.findall("s.*?e",s,re.I|re.M)
if lst!=None:
    print(lst)
else:
    print("not found")

s1=re.sub("s.*?e","any",s,flags=re.I|re.M)
print(s1)
print("-"*83)

myreg=re.compile("s.*?e",re.I|re.M)
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
    
mob=input("enter mobile number:")
m=re.match("^\+91-[987]\d{9}",mob)
if m!=None:
    print("mobile no is valid")
else:
    print("not found")

s2="this is home"
m=re.match("^(\w+)\s(\w+)\s\w+$",s2)
if m!=None:
    print("found")
    print(m.group(),m.span())
    print(m.group(1),m.span(1))
    print(m.group(2),m.span(2))
else:
    print("not found")
print("-"*83)

ac="XXXX1234XXXX"
m=re.match("^X{4}(\d{4})X{4}$",ac)
if m!=None:
    print(m.group(),m.span())
else:
    print("not found")

