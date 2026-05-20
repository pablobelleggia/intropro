lista = [2,3,9,10,11]
lista2 = [2,4,5,5,6,7,9,2,3]
lista3 = []

for i in range (len(lista)):
    if lista[i] not in (lista2):
        lista3.append(lista[i])
        
print (lista3)
