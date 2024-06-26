num=''
add=0
product = 1
count = 1
while num!='q':
       num = input()
       count=count+1
       
       if num.isdecimal and num!='q':
           add=add+int(num)
           product=product*int(num)
        
         

print("avg: ",(add/count))
print("Product: ", product)
