numero1=12
numero2= 24
mcd = 0
lista = []
for i in range(1,numero2+1):
    if numero1%i == 0 and numero2%i ==0:
        lista.append(i)
print (max(lista))