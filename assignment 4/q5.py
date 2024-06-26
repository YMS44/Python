l=['a','e','i','o','u']
s=input("enter a string:")
c=''
for i in s:
    match i:
        case 'a'|'A':
            c=c+i
        case 'e'|'E':
            c=c+i
        case 'i'|'I':
            c=c+i
        case 'o'|'O':
            c=c+i
        case 'u'|'U':
            c=c+i
        case ' '|' ':
            c=c+i
        case _:
            c=c+(i+"o"+i)

print(c)        
        
    
    
    
    
    
    
    
    
    
    
    
    
'''

if i!=l:
    print(i+"o"+i,end="")
else:
    print(i,end="")

'''
