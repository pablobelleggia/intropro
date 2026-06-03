def tipoDeMaterial(pedido):
    pass 
def tipoDeAvion(pedido): 
    pass
def gamaDeColor(pedido): 
    pass
def hacerAvion(material, modelo, color):
    pass
def precio(pedido):
    pass
def registar(float, empleado): 
    pass

empleado = 123
pedidos =[]
def fabricarAviones(pedidos, empleado):
    
    totalpreciodetrabajosrealizados = 0
    
    imposible = []
    
    valor = True
        
    for i in range (len(pedidos)):
        pedido = pedidos [i]
        tipo = tipoDeAvion (pedido)
        color = gamaDeColor (pedido)
        material = tipoDeMaterial (pedido)
        valor = hacerAvion (material,tipo, color)
        
        if valor == True:
            valorfinal = precio(pedido)
            totalpreciodetrabajosrealizados += valorfinal
            registar (totalpreciodetrabajosrealizados, empleado)
        else:
            imposible.append(pedido)
            
    return imposible
            
        
        