indice = 0
lista = [1,3,-4,4,0,9,6,-5,2,3,5,-1,1,3]
while (len(lista)) > indice:
    if indice % 4 == 0:
        valor = lista[indice]*2
        lista.pop(indice)
        lista.insert(indice, valor)
    indice += 1
print(lista)