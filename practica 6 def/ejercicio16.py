def cuantas(cadena, letra):

    contador =0
    
    for i in range (len(cadena)):
        if cadena[i] == letra:
            contador +=1
            
    return contador


print (cuantas("hola como estas","a"))    
