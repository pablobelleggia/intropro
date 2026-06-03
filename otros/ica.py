""""
nombres = ["a","b","c","d","e"]
notas = [5,10,7,9,3]
top3peores = []

while (len(top3peores))<3:
    peor_actual = notas[0]
    peor_alumno = nombres[0]
    indice_eliminar = 0
    
    for i in range(len(notas)):
        if notas[i] < peor_actual:
            peor_actual = notas [i]
            peor_alumno = nombres[i]
            indice_eliminar = i
            
    top3peores.append(peor_alumno)
    nombres.pop(indice_eliminar)
    notas.pop(indice_eliminar)
    
print (top3peores)

    
"""
n = int(input("dale amigo, cuantos queres: "))

numero_actual = 2
numeros_conseguidos = 0

suma = 0
numerador = 0

while numeros_conseguidos < (n*2):

    cont = 0

    for i in range(1, numero_actual + 1):

        if numero_actual % i == 0:

            cont += 1

    if cont == 2:

        numeros_conseguidos += 1

        if numeros_conseguidos % 2 == 1:

            numerador = numero_actual

        else:

            suma = suma + (numerador / numero_actual)

    numero_actual += 1

print(suma)
