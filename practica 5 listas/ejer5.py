lista = [1, 2, 3]
numero = int(input("Ingrese un numero: "))
contador = 0
for i in range(len(lista)):
    if numero % lista[i] == 0:
        contador = contador + 1
        
if contador == len(lista):
    print("El numero es divisible por todos los elementos de la lista")