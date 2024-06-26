def f1 (a=12,b=13,c=14,*tp,**kwarg):
    print(a,b,c)
    print(tp)
    print(kwarg)
    s=a+b+c
    for d in tp:
        s=s+d
    for k in kwarg.values():
        s = s + k
    return s
print("sum",f1(1,2,3))
print("sum",f1(11,21,31,2,3,4,5,6,7,x=10,y=220,z=444))