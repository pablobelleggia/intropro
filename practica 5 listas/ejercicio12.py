lista = [1,2,3,4,5,6,7,8,9,10]

posA = 2
posB = 5

print(lista)

aux = lista[posA]
lista[posA] = lista[posB]
lista[posB] = aux

print(lista)