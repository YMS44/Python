class A:
    def __init__(self,a1=0,a2=0):
        print("in A constructor",a1,a2)
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f"A1: {self.__a1} A2: {self.__a2}"
    
class B(A):
    def __init__(self,b1=0,**kwarg):
        print("in B constructor",kwarg)  #a1,a2,c1,c2
        super().__init__(**kwarg)
        self.__b1=b1
        
    def __str__(self):
        return super().__str__()+f"return B1: {self.__b1}"
        

class C(A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("in C constructor",kwarg)  #a1,a2
        #calling parent constructor
        super().__init__(**kwarg)
        self.__c1=c1
        self.__c2=c2
        
    def __str__(self):
        return super().__str__()+f"return C1: {self.__c1}  C2: {self.__c2}"
    
class D(B,C):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("in d constructor",d1,d2,kwarg)
        super().__init__(**kwarg)
        self.__d1=d1
        self.__d2=d2
    def __str__(self):
        return super().__str__()+f"D1: {self.__d1} D2: {self.__d2}"
    
ob=D(a1=12,a2=11,b1=21,c1=31,c2=41,d1=100,d2=200)
print(ob)
print(D.mro())

