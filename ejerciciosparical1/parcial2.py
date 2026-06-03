def color(valija): 
    pass
def dimensiones(valija): 
    pass
    
def tamaño():
    pass
    
def listaValijas(nroVuelo):
    pass
    
def azar(): 
    pass
    
def aplicacion (nroVuelo):
    valijasparaabrir = []
    valijas = listaValijas(nroVuelo)
    
    for i in range (10):
        
        numero = azar()
        
        valijasparaabrir.append(valijas[numero])    
        
    for i in range (len(valijas)):
        
        valija = valijas [i]
        
        colordevalija = color (valija)
        
        dimension = dimensiones(valija)
        
        permitido = tamaño ()
        
        if colordevalija == "rojo" or "verde":
            if valija not in valijasparaabrir:
            
                valijasparaabrir.append(valija)
            
        if dimension> permitido:
            if valija not in valijasparaabrir:
            
                valijasparaabrir.append(valija)
    
        
    
    