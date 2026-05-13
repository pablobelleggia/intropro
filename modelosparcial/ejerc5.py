def Stock(producto, cantidad):
    pass


def Vencido(producto):
    pass


def Costo(producto):
    pass


def Venta(desayuno):
    pass

desayuno1 = ["cafe", "manteca"]

desayuno2 = ["manteca", "medialuna", "medialuna"]

desayunos = [desayuno1, desayuno2,]
gananciadesayunos = 0
for i in range(len(desayunos)):
    
    se_cumple= True
    desayunoactual= desayunos[i]

    for j in range(len(desayunoactual)):
        producto =desayunoactual[j]
        cantidad = desayunoactual.count(producto)
        if Stock(producto,cantidad) == False:
            se_cumple = False
        if Vencido(producto) == True:
                se_cumple = False
                
    if se_cumple == False:
        print(desayunoactual)
        
    if se_cumple == True:
        costo = 0
        ventaa = Venta(desayunoactual)
        for k in range(len(desayunoactual)):
            producto = desayunoactual[k]
            costo += Costo(producto)
        ganancia = ventaa - costo
        gananciadesayunos += ganancia
            
            
        
            
        
    
