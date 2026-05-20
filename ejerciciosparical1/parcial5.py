def medicamentos(idEnvio):# retorna una lista de los códigos de los medicamentos recibidos.
    pass
def labo(codMed): #retorna el laboratorio fabricante del medicamento (lab)
    pass
def prod(codMed): #retorna el nombre del medicamento (med)
    pass
def cantidad(codMed): #retorna la cantidad del medicamento recibida.
    pass
def guardar(lab,med): #guarda el medicamento en la estantería y orden correspondiente
    pass
def actualizarStock(cantidad,codMed): #actualiza el stock del medicamento en el sistema de la farmacia.
    pass
def stock(codMed): #retorna la cantidad de un medicamento en stock.
    pass
def stockMin(codMed): #retorna el stock mínimo del medicamento.
    pass
def emiteSolicitud(codMed): #genera una solicitud de pedido del medicamento.
    pass


IdEnvio = int(input("selleccionar id de envio:   "))

CodMededicamentos = medicamentos (IdEnvio)

for i in range (len(CodMededicamentos)):
    
    CodMed = CodMededicamentos[i]
    lab = labo(CodMed)
    med = prod(CodMed)
    cant = cantidad(CodMed)
    guardar(lab,med)
    actualizarStock(cant,CodMed)
    
    if stock(CodMed) < stockMin(CodMed):
        emiteSolicitud(CodMed)
    
