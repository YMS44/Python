lst = [10,20,10,34]
lst.append("Hello")
print(lst)
print(len(lst))
lst.extend("Testing")
print(lst)
print(len(lst))

import copy

lst.pop()

lst.pop(2)
lst.remove(10)
print(100 in lst)
#lst.remove(100)

if 100 in lst:
    lst.remove(100)
else:
    print("not found")

print("index of 34", lst.index(34))
#lst.index(100)

lst = [5,6,51,2,6,7,5321,4,2,3]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.reverse()
print(lst)

lst2 = [12,23,34]
#it will copy the referance
#change in one list will bereflected in another list
lst3 = lst2

lst2.append(100)
print(lst2)
print(lst3)

#create a shalloe copy of the list
lst4 = lst2.copy()
lst2.append(200)
print(lst2,lst3)
print(lst4)

#creates a deep copy
lst = [10,20,30,[1,2,3]]
lst1 = copy.deepcopy(lst)
lst[3].append(100)
print(lst, lst1)

lst = [12,1,23]
lst1 = ["Pune", "Mumbai","Delhi"]

for i, j in zip(lst, lst1):
    print(i, "------>",j)

lst = ["a","b","c"]
cnt = 0

for i in lst:
    print(cnt, "----->",i)
    cnt = cnt + 1

#for pos, val in enumerate(lst):
#    if val % 2 == 0:
#        print(pos,"----->",val)

lst = [12,13,14,15,16,17]

lst1 = []
for num in lst:
    if num%2 == 0:
        lst1.append(num)
print(lst1)

lst1 = [num for num in lst if num%2 == 0]
print(lst1)

#lambda function
print(lst1)
lst2 = list(filter(lambda x:x%2==0 and x>10 , lst))
print(lst2)

def f1(n):
    n=n+10
    return n%2 == 0 and n>15

lst2 = list(filter(lambda x:f1(x), lst))
print(lst2)

lst = [1,2,12,13,10]
lst1=[]
for num in lst:
    lst1.append(num+10)
print(lst1)

lst1 = [num+10 for num in lst]
lst1 = list(map(lambda x:x+10,lst))
print(lst1)

import functools
s = functools.reduce(lambda acc,num:acc+num,lst)
print("addition",s)
print("addition",sum(lst))
lst = ["python","perl","linux","os"]
s1 = functools.reduce(lambda acc,num:acc+num,lst)
print(s1)

s2 = functools.reduce(lambda acc, s:acc+s[1:3],lst,"")
print(s2)

lst = [(1, "zzz", 45), (0, "bbb",56), (5,"aaa",46)]
lst.sort(key = lambda x:x[1], reverse = True)
print(lst)

