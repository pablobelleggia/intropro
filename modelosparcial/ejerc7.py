def obtenerCantidadLlamados(nroCliente):
    pass


def obtenerTiempoPorLlamada(nroCliente, nroLlamado):
    pass


def obtenerCostoPorLlamada():
    pass


def obtenerCostoPorTiempo(segundos):
    pass

def esta(nroCliente):
    pass


def alta(nroCliente):
    pass


def baja(nroCliente):
    pass


clientes = []


for i in range(len(clientes)):
    nroCliente = clientes [i]
    cantidadllamados =  obtenerCantidadLlamados(nroCliente)
    tiempototal = 0
    monto = 0

    for llamados in range(cantidadllamados):
        segundos = obtenerTiempoPorLlamada(nroCliente, llamados)
        tiempototal += segundos
        costoxllamada = obtenerTiempoPorLlamada()
        costoxtiempo = obtenerCostoPorTiempo (segundos)
        monto += costoxtiempo + costoxllamada
        
    if tiempototal > 7200:

        if esta(nroCliente) == False:

            alta(nroCliente)
    else:

        if esta(nroCliente) == True:

            baja(nroCliente)