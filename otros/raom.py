"""
import random

reclutas= ["Rain", "Arthur", "Jericó", "Krislana", "Willow", "Silver", "Takkan", "Lomi"]
malos= ["Griklo", "Lanius", "Modi", "Gama", "Ulvash", "Hengest" , "Hambu"]
i = 0
while len(reclutas) > 0 and len(malos) > 0:
    recluta = reclutas [i]
    azar = random.randint (0, (len(malos)-1))
    malo = malos [azar]
    print (recluta, "Vs", malo)
    reclutas.pop(i)
    malos.pop(azar)

reclutas_1= ["Rain", "Arthur", "Jericó", "Krislana", "Willow", "Silver", "Takkan", "Lomi"]
reclutas_2= ["Rain", "Arthur", "Jericó", "Krislana", "Willow", "Silver", "Takkan", "Lomi"]

while len(reclutas_1) > 0 and len(reclutas_2) > 0:
    azar_1 = random.randint (0, (len(reclutas_1))-1)
    azar_2 = random.randint (0, (len(reclutas_2))-1)
    validacion = False
    while validacion == False:
        if azar_1 == azar_2:
            azar_2 = random.randint (0, (len(reclutas_2)-1))
        else:
            print (reclutas_1[azar_1], "vs", reclutas_2[azar_2])
            reclutas_1.pop (azar_1)
            reclutas_2.pop (azar_2)
            validacion = True
            
"""





paises_1 = ["Argentina", "Austria", "Algeria", "Jordania"]
paises_2 = ["Argentina", "Austria", "Algeria", "Jordania"]
partidos = []

i = 0
i2 = 0
banderita = True
while banderita:
    pais1 = paises_1[i]
    pais2 = paises_2[i2]
    
    if pais1 == pais2:
        i2 += 1
    else:
        partidos.append (pais1 + " vs " + pais2)
        i2 += 1
        
    if i2 == (len(paises_2)):
        i += 1
        i2 = 0
    if i == len(paises_1):
        banderita = False
print (partidos)

    ¿
