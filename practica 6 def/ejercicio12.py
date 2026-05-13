def poderoso (numero):

    for i in range (1, numero+1):
        if numero % i == 0:
            contador = 0
            
            for j in range(1, i+1):
                if i%j ==0:
                    contador +=1
                    
            if contador == 2:
                if numero % (i**2) ==0:
                    return True
                
    return False
                
print (poderoso(32))