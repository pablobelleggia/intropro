entero = 12
lista = []

for i in range(1, entero + 1):
    if entero % i == 0:
        lista.append(i)

print(lista)