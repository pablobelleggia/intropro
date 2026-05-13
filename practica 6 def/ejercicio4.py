
#a) Escribir una función que reciba dos números reales como parámetros y retorne su promedio.
#b) Hacer un programa que pida al usuario dos números reales y muestre por pantalla el resultado de llamar a la función del primer inciso.
#c) Idem de los dos anteriores pero con tres números. Escribir la función en el mismo archivo donde se escribió la del item a

def promedio (valor1, valor2):
   valorpromedio = (valor1 + valor2)/2
   return valorpromedio

valor1 = int(input("que numero 1 quiere; "))
valor2 = int(input("que numero 2 quiere; "))

print (promedio(valor1,valor2))