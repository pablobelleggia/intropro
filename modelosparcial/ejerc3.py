def pedirServidores():
    pass
def funciona(servidor):
    pass
def tiempoRespuesta(servidor):
    pass
def tiempoRespuestaMaximo(servidor):
    pass
def buscarAdministrador(servidor):
    pass
def enviarsms(mensaje, administrador):
    pass
def registrartiemporespuesta(servidor,tiempoRespuesta):
    pass


servidores = pedirServidores ()

while True:
    
    for i in range (len(servidores)):
        
        servidor = servidores[i]
        
        if funciona(servidor) == False:
            
            admin = buscarAdministrador(servidor)
            
            mensaje = "error en el servidor"
            
            enviarsms(mensaje, admin)
        else:
            tiempo = tiempoRespuesta(servidor)
            maximo = tiempoRespuestaMaximo(servidor)
            if tiempo > maximo:
                 admin = buscarAdministrador(servidor)
                 mensaje = "tiempo de respuesta excedido"
            
                 enviarsms(mensaje, admin)
        registrartiemporespuesta,(servidor,tiempo)                
        
        

