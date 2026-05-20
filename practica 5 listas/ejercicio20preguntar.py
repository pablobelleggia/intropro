lista = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
x = int(input("mi lista tiene que ser menor a X = "))
listafinal = []
valor = True
while valor:
    
    for i in range(len(lista)):
        if lista[i] < x:
            listafinal.append(lista[i])
            if lista[i] > x:
                valor ==False
        
print (listafinal)
