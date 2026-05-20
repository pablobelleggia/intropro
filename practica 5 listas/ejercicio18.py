n = int(input("Cuántos números primos quiere: "))
cantidad = 0
numero = 2
lista = []

while cantidad < n:
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        lista.append(numero)
        cantidad += 1

    numero += 1

print(lista)