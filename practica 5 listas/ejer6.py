lista = [1, 4, 3, 4, 5]

for i in range(len(lista)):
    for j in range(i + 1, len(lista)):
        if lista[i] == lista[j]:
            print("El numero", lista[i], "se repite en la lista")