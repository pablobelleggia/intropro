def recuadrada(palabra):

    cantidad= (len(palabra))+2
    final = "*" * cantidad + "\n" + "*" + palabra +"*" + "\n" + "*" * cantidad

    
    return final

print (recuadrada("hola"))
    