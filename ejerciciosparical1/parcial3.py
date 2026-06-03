def olimpiadas(año, sede):
    pass
def siglas(país):
    pass
def deporte(país):
    pass
def disciplina(deporte):
    pass
def mejores_8(disciplina):
    pass


año = int(input("seleccionar año"))
sede = str(input("seleccionar sede"))

listapaises = olimpiadas(año, sede)

for i in range (len(listapaises)):
    
    pais = listapaises[i]
    
    sigla = siglas(pais)
    
    oro = 0
    plata = 0 
    bronce = 0

    deportes = deporte(pais)
    
    for j in range (len(deportes)):
        
        deporteactual = deportes[j]
        
        disciplinas = disciplina(deporteactual)
        
        for k in range (len(disciplinas)):
            
            disciplinaActual = disciplinas[k]
            
            mejores = mejores_8(disciplinaActual)
            