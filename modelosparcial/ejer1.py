def obtenerGradosF(n):
    
    pass

def transformar(gradosF):
    
    pass

def estaPrendidoCalefon(n):
    pass
def estaPrendidoAire(n):
    
    pass
def esperarSegundos(n):
    pass



while True:

    for n in range (10):
        temp = obtenerGradosF
        tempB = transformar (temp)
        
        if tempB < 20:
            encenderCalefon(n)
            
            while temp < 20:
                esperarSegundos(1)
                
                temp = obtenerGradosF
                tempB = transformar (temp)
                
                apagarCalefon(n)
                
        elif tempB > 20:
            encenderAire(n)
            
            while temp > 20:
                esperarSegundos(1)
                
                temp = obtenerGradosF
                tempB = transformar (temp)
                
                apagarAire(n)
                
        esperarSegundos(60)