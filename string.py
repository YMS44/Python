#s = "naam de re bhai"
#print(s[::3])
#print(s[0::2])
#print(s[::-1])

s1 = "this is a cat, cat is cute, wher is your cat? mine is her"
pos = s1.find("cat")
while pos != -1:
    print(pos)
    pos = s1.find("cat",pos+1)
print(s1.count("cat"))

print("="*60)
    
pos = s1.rfind("cat")
while pos != -1:
    print(pos)
    pos = s1.rfind("cat",0,pos)
print(s1.count("cat")) 


#pos = s1.rfind("cat")
#print(pos)

s2 = "this is a test"
print("uppercase: ", s2.upper())
print("lowercase: ", s2.lower())
print("startwith", s2.startswith("thi"))
print("endswith",s2.endswith("thi"))
print("split", s2.split(" "))
print("split: ", s2.split(","))
account = "xxxxxx556876xxxxxx"
print("strip", account.strip("x"))

lst = ["aaa", "bbb", "ccc"]
print(":".join(lst))
print("1234".isdecimal())
print("lsdf".isalpha())
print("this is new is this".replace("is", "abs",3))


a = 12
b=a
c = 12
print(id(a),id(b),id(c))
d = int(input("enter number"))
print(id(d))
a = 10
print(id(a),id(b),id(c))
print(a is b)
s = "hello"
t=s
x = "Hello"
y = input("enter string")
print(id(s),id(t),id(x),id(y))

################# List ###############
print("X"*50)
lst = [1,2,3,4,5,6]
lst1 = ["python","perl","test"]
lst2 = [12,12,34,12,"xxx","bbb",[34,56,23],56]
print(lst2[6][1])
print(lst[3])
print("lenght: ", len(lst))
lst[3]=45
print(lst)

for i in lst1:
    print(i)

st = "this is data"

for a in st:
    print(a)
    

wst = []
n=int(input("enter length"))
for i in range(n):
    num = int(input("enter the number"))
    wst.append(num)
print(wst)


