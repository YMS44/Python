p=float(input("Enter principle amount: "))
r=float(input("Enter rate: "))
n=int(input("Enter time in years: "))

if p>10000:
      a=p*(1+(r/100))**n
      print("compound interest:",a-p)
else:
      print("simple interest:",(p*r*n/100))

