s="Rise to vote sir"
j=''
for i in s:
    if i!=" " and i!=",":
        j=j+i
if j.lower()==j[::-1].lower():
    print("palindrome phrase")
else:
    print("not palindrome phrase")