n = int(input("Ingrese un numero entero: "))

factores = []
divisor = 2

while n > 1:
    while n % divisor == 0:
        factores.append(divisor)
        n = n // divisor
    divisor += 1

print(factores)