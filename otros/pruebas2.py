def cantidaddivisoresprimos(numero): #369
    numero_str = str(numero)
    lista = []
    for a in range (len(numero_str)):
        actual = numero_str[a]
        actual = int(actual)
                
        for b in range (1,actual +1):
            if actual % 2 == 0:
                cont = 0
                
                for c in range (1,b+1):
                    if b % c == 0:
                        cont += 1
                if cont == 2:
                    lista.append(b)
    
    listasinrepetidos = []
    for i in range (len(lista)):
        actual = lista[i]
        veces = 0
        for j in range (len(lista)):
            if actual == j:
                veces +=1
        if veces == 1:
            listasinrepetidos.append(actual)                        
                                    
    return listasinrepetidos

print (cantidaddivisoresprimos(369))