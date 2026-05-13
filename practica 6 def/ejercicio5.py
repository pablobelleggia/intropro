#Defnir una función que devuelva el valor absoluto de un número. (Hacerlo sin utilizar la función abs)

def absoluto(x):
    if x < 0:
        x = x*-1
    return x


x = int(input("numerito: "))
print(absoluto(x))