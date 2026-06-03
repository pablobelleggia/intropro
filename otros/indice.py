lista= [ 1 , 3 , -4 , 4 , 0 , 9 , 6 , -5 , 2 , 3 , 5 , -1 , 1 , 3 ] 
indice = 0

while indice < len(lista):
    if indice % 4 == 0:
        lista [indice] = lista [indice] * 2
    indice += 1

print (lista)
