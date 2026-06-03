def distanciaNorte(n):
    pass

def distanciaSur(n):
    pass

def distanciaEste(n):
    pass

def distanciaOeste(n):
    pass

def prenderNorte(n):
    pass

def prenderSur(n):
    pass

def prenderEste(n):
    pass

def prenderOeste(n):
    pass

def apagarNorte(n):
    pass

def apagarSur(n):
    pass

def apagarEste(n):
    pass

def apagarOeste(n):
    pass

def dameVivos():
    pass


def Gameplay():
    robots = dameVivos()
    
    for n in range (len(robots)):
        robot = robots[n]
        distanciaN= distanciaNorte(robot)
        
        distanciaS=distanciaSur(robot)
        
        distanciaO= distanciaOeste(robot)
        
        distanciaE= distanciaEste(robot) 
        
        if distanciaN < 10:
            apagarSur(robot)
            prenderNorte(robot)
        else:
            apagarNorte(robot)
        if distanciaS < 10:
            apagarNorte(robot)
            prenderSur(robot)
        else:
            apagarSur(robot)
        if distanciaO < 10:
            apagarEste (robot)
            prenderOeste (robot)
        else: 
            apagarOeste(robot)
        if distanciaE < 10:
            apagarOeste (robot)
            prenderEste (robot)
        else:
            apagarEste(robot)
        
