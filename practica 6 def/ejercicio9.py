def mayor (a,b):
    
    masgrande = a

    if a > b:
            masgrande = a
    else:
            masgrande = b
        
    return (masgrande)
print (mayor(3,5))

def mayorq (a,b,c):
    
    masgrande = a

    if a > b and a > c:
            masgrande = a
    elif b > a and b > c:
            masgrande = b
    else: 
        masgrande = c
        
    return (masgrande)

print (mayorq(190,5,8))