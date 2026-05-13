def enteros(numero):
    contador = 0
    for i in range (1,numero+1):
        if numero%i == 0:
            contador +=1
            print ("el",i,"es divisor de", numero , "y tiene tantos divisores", contador)
    print ("y tiene tantos divisores", contador)
    return (numero)

print(enteros(10))

def primo (numero):
    contador= 0
    for i in range (1,numero+1):
        if numero%i == 0:
            contador +=1
    if contador == 2:
        valor = True
    else:
        valor = False
    
    return (valor)

print (primo(4))


def factores(numero):
    lista = []
    for i in range (1,numero+1):
        if numero % i == 0:
            contador = 0
            
            for j in range(1,i+1):
                if i%j ==0:
                    contador +=1
            if contador == 2:
                lista.append(i)

    return (lista)

print (factores(10))