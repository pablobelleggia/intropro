frase = "durante la carrera, sin dudas, debemos diseñar soluciones"
letra = "d"
lista = []
indice = 0
cont = 0
while (len(frase)) > indice:
    
    
    caracter = frase[indice] 
    if letra == caracter:
        cont += 1
        indice +=1
    if caracter == " ":
        lista.append(cont)
        cont = 0
    indice +=1
    
lista.append(cont)
print (lista)