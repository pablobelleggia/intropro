cadena = input("Ingrese una palabra: ")
mostradas = ""

for i in range(len(cadena)):
    if cadena[i] not in mostradas:
        contador = 0

        for j in range(len(cadena)):
            if cadena[j] == cadena[i]:
                contador += 1

        print(cadena[i], ":", 1 *contador)
        mostradas += cadena[i]