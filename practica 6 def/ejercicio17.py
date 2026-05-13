def cuantas(cadena):

    contador =0


    for i in range(len(cadena)):
        for j in range(len(cadena)):
            if cadena[i] == cadena [j] and i!=j:
                return True
    return False


print (cuantas("b"))

#En resumen, i != j garantiza que estás comparando dos posiciones distintas en la cadena, es decir, dos letras diferentes en posiciones distintas. Si son iguales, entonces hay una repetición real. Sin esa condición, cada letra coincidiría consigo misma, lo que no es lo que buscás.


def aparecer (letra, cadena):
    for i in range (len(cadena)):
        if cadena[i] == letra:
            return True
        
    return False
        
print (aparecer("a","pp"))

def repetida (cadena):
    for i in range(len(cadena)):
        for j in range(len(cadena)):
            if cadena[i] == cadena [j] and i!=j:
                return cadena[i]

print (repetida("appatt"))

def sinrepetida (cadena,letra):
    final = ""
    contador = 0
    for i in range (len(cadena)):
        if cadena[i] == letra:
            contador += 1
            if contador ==1:
                final += cadena[i]
        else:
            final += cadena[i]

            
        
                
    return (final)
  
                
print (sinrepetida("mate cocido", "c"))