n=int(input("enter series limit:"))
z=9
t=0
sum=0
'''for i in range(1,n+1):
    z= "9"*i
    t = int(z)
    sum=sum+t
    '''

#print(sum)

for i in range(n):
    z= z+(9*(10**i))
    #t = int(z)
    #sum=sum+t

print(z)
