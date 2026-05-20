#tome una lista de números y devuelva el índice del máximo elemento.

lista = [1,3,5,6,34,5]
numeromayor = lista[0]
posicionmayor = 0

for i in range (len(lista)):
    if lista[i] > numeromayor:
        numeromayor = lista[i]
        posicionmayor = i
print (posicionmayor)

