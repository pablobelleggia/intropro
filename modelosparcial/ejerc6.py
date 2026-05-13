
def auto(alquiler):
    pass


def categoriaUnidad(auto_usado):
    pass


def precioDiario(alquiler):
    pass


def cantidadDias(alquiler):
    pass


def kmExcedidos(alquiler):
    pass


def valorKmExcedido(alquiler):
    pass


def limitado(alquiler):
    pass


def tanque(auto):
    pass


def registrar(alquiler, importe):
    pass

def costo(alquiler):
    importe = 0
    auto_usado = auto(alquiler)
    categoria_auto = categoriaUnidad(auto_usado)
    precioxdia = precioDiario(alquiler)
    cantidad_dias = cantidadDias(alquiler)
    km_excedidos = kmExcedidos(alquiler)
    precioexcedido = valorKmExcedido(alquiler)
    ilim = limitado (alquiler)
    preciotanque = tanque(auto_usado)
        
    if ilim == False:
        importe += (km_excedidos*precioexcedido) + (precioxdia*cantidad_dias) + preciotanque
        
        
    if ilim == True:
        importe += (precioxdia*cantidad_dias)*1.10 + preciotanque
    
    if categoria_auto == 2:
        registrar(alquiler, importe)
    
    return (importe)

















































def auto(alquiler):
    pass


def categoriaUnidad(auto):
    pass


def precioDiario(alquiler):
    pass


def cantidadDias(alquiler):
    pass


def kmExcedidos(alquiler):
    pass


def valorKmExcedido(alquiler):
    pass


def limitado(alquiler):
    pass


def tanque(auto):
    pass


def registrar(alquiler, importe):
    pass