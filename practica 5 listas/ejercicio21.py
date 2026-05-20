lista = [1,2,7,4,49,6,7,8,9,10]

x = int(input("que numero quiere que sea el maximo permitido: "))

for i in range(len(lista)):
    if lista[i] < x:
        lista [i] = 0


print(lista)