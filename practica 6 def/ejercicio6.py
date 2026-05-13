#Escribir una función con el siguiente encabezado: def exclamar(unaCadena): que retorne la misma cadena entre símbolos de exclamación (½!)
#b) Escribir una función con el siguiente encabezado: def gritar(unaCadena): que retorne la misma cadena entre 3 símbolos de exclamación (½½½!!!)
#c) De no haberlo hecho en el punto anterior, escribir de nuevo la función gritar utilizando solo la función exclamar.
#Nota: gritar(Ouch) deberá devolver la cadena ½½½Ouch!!!
#Ayuda: Recordar que + utilizado entre cadenas las concate

def exclamar (unaCadena):
    return str("!"+unaCadena+"!")

print (exclamar("hola"))

def exclamar (unaCadena):
    return str("!!!"+unaCadena+"!!!")

print (exclamar("hola"))