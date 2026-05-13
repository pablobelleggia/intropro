def divisorespropios (numero):
    sumador= 0
    esperf = "si"
    for i in range (1,numero):
        if numero % i == 0:
            sumador+=i
    if sumador > numero:
        esperf = "si"
    else:
        esperf = "no"
            
    return (esperf)

print(divisorespropios(12))