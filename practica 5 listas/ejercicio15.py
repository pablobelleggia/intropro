lista = [2,3,5]
lista2 = [2,3,4]
lista3 = []

for i in range (len(lista)):
    if lista[i] not in (lista3):
        lista3.append(lista[i])

for i in range(len(lista2)):
    if lista2[i] not in (lista3):
        lista3.append(lista2[i])
        
print (lista3)
