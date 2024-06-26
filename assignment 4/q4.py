import string
s=set(string.ascii_lowercase)
b = set()
a = input("please enter a string: ")

for i in a:
    if i.isalpha():
        b.add(i)
        
print(b)
print()

if s == b:
    print("pangram")
else:
    print("not a pangram")