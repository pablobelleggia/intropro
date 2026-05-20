def suscriptores():
    pass

def en_Condiciones(n):
    pass

def sorteados(lista):
    pass


planes = suscriptores()
habilitados = []

for i in range (len(planes)):
    n = planes [i]
    
    if en_Condiciones(n) == True:
        habilitados.append(n)
        
ganadores = sorteados(habilitados)

print (ganadores)