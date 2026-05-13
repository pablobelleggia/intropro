def es_primo(numero):
    if numero < 2:
        return False

    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        return True
    else:
        return False


n = int(input("Ingrese un numero entero positivo: "))

candidato = n + 1

while es_primo(candidato) == False:
    candidato += 1

print("El primo mayor más cercano es:", candidato)