def usuarios ():
    pass
def busquedas(usuario):
    pass
def popularidad (tema):
    pass


def parcial ():
    lista_cantidad_cosas_menor30 = []
    listafinal = []
    lista = usuarios ()
    for i in range (len(lista)):
        usuario = lista [i]
        lista_temas = busquedas(usuario)
        cont = 0
        for j in range (len(lista_temas)):
            tema = lista_temas [j]
            popular = popularidad(tema)
            if popular < 30:
                cont +1
        lista_cantidad_cosas_menor30.append (cont)
 
        
    while len(listafinal)<10:
        mayor = lista_cantidad_cosas_menor30 [0]
        pos = 0
        
        for i in range (len(lista_cantidad_cosas_menor30)):
            if lista_cantidad_cosas_menor30 [i] > mayor:
                mayor = lista_cantidad_cosas_menor30 [i]
                pos = i
        listafinal.append(lista[pos])

        lista_cantidad_cosas_menor30.pop(pos)
        lista.pop(pos)
                
                
            
        
        #rever
        
        
puntajeraros = []
lista final =