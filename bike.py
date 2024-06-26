price = int(input("Please enter the price of bike: "))

if price > 100000:
    
    tax = (15/100)*price
    inssurance = (20/100)*price
    
    print(f"Tax = {tax}")
    print(f"Inssurance = {inssurance}")

elif 50000< price <= 100000:
    
    tax = (10/100)*price
    inssurance = (8/100)*price
    
    print(f"Tax = {tax}")
    print(f"Inssurance = {inssurance}")

else :
    
    tax = (5/100)*price
    inssurance = (5/100)*price
    
    print(f"Tax = {tax}")
    print(f"Inssurance = {inssurance}")
            

            
