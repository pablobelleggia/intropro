lista = [100,3,5,6,4,2,50,6,34,5,5,5,5,500]
a = 2
b = 9
mayornumero = lista[a]
mayorindice = 0

for i in range (a,b):
    if lista [i] > mayornumero:
        mayornumero = lista[i]
        mayorindice = i

print (mayorindice)
print (mayornumero)    
    

