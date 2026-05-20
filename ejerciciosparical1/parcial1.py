def productosCliente(cliente):
    pass
def saldoCuentaCorriente(cliente, mes):
    pass
def comprasConTarjeta(cliente,mes):
    pass
def ganador (clientes,puntos):
    pass


ClientesBanco = []


def GanadorDelSorteo ():

    PuntosClintes = []
    
    for i in range (len(ClientesBanco)):
        
        puntosCliente = 0
        
        cliente = ClientesBanco[i]
        
        Productos = productosCliente(cliente) 
        
        for k in range (len(Productos)):
            
            producto = Productos[k]
            
            if producto == "CC":
                
                for j in range (12):
                    
                    mes = j
                    
                    sald = saldoCuentaCorriente(cliente,mes)
                    
                    if sald >= 0:
                        
                        puntosCliente +=5
                        
                    if sald < 0:
                        
                        puntosCliente +=10
                        
            if producto == "TAR":
                
                for x in range (12):
                    
                    mes = x
                    
                    compras = comprasConTarjeta(cliente,mes)
                    
                    for y in range (len(compras)):
                        monto = compras[y]
                        if monto > 10000:
                            puntosCliente+=10
                        else:
                            puntos +=1
        PuntosClintes.append(puntosCliente)
    
    elganador_es = ganador (ClientesBanco,PuntosClintes)
    
    return elganador_es
                    
                        
            
        