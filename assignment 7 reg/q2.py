import re
s=input("enter string:")
m=re.match("^(\d{0,1}\w*)?^(\w\w)",s)
print(m.group())
