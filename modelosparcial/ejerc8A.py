def dameNrosAntenasCercanas():
    pass
def distancia(nroAntena):
    pass
def determinarUbicacion(nrosAntenas, distancias):
    pass
def dormir():
    pass
def despertar():
    pass
def estoyDormido():
    pass




def controlDeUbicacion():

    while True:
        
        nrosantenas = dameNrosAntenasCercanas()
        
        if len(nrosantenas) >=3:
            
            distancias = []
            
            despertar()
            
            for i in range (len(nrosantenas)):
                
                antena = nrosantenas[i]
                
                distanciadelrobot = distancia(antena)
                
                distancias.append(distanciadelrobot)
                
            if estoyDormido () == True:
                
                despertar()
                    
                determinarUbicacion (nrosantenas,distancias)
            else:
                dormir()
        






#?^M*wuLzm^AEgx7