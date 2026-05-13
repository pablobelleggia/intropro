

def ObtenerCantidadLlamados(nroCliente):
    pass
    
def ObtenerTiempoPorLlamada(nroCliente, nroLlamada):
    pass
def ObtenerCostoPorLlamada():
    pass
def ObtenerCostoPorTiempo(seg):
    pass
    
clientes = [1, 2, 3, 4, 5]

for nroCliente in clientes:
    total = 0
    cantidadLlamados = ObtenerCantidadLlamados(nroCliente)

    for i in range(cantidadLlamados):
        segundos = ObtenerTiempoPorLlamada(nroCliente, i)
        costoFijo = ObtenerCostoPorLlamada()
        costoTiempo = ObtenerCostoPorTiempo(segundos)

        total = total + costoFijo + costoTiempo

    print("Cliente", nroCliente, "debe pagar", total)
    
    
    
    
    
"""    clientes = [1, 2, 3]
CantLlamados = [2, 3, 1]

tiempos = [[10, 20],[5, 15, 30],[12]]

def ObtenerCantidadLlamados(nroCliente):
    for i in range(len(clientes)):
        if nroCliente == clientes[i]:
            return CantLlamados[i]

def ObtenerTiempoPorLlamada(nroCliente, nroLlamada):
    for i in range(len(clientes)):
        if nroCliente == clientes[i]:
            return tiempos[i][nroLlamada]

def ObtenerCostoPorLlamada():
    return 12

def ObtenerCostoPorTiempo(seg):
    return seg * 1.5

"""