turno_deseado = str(input("M T o N"))
coms = []
turno = []
cant_alu = []

def parcial (turno_deseado, coms, turno, cant_alu):
    
    
    for i in range (len(turno)):
        actual = turno [i]
        if turno_deseado == turno:
            if cant_alu[i] > 0:
                valornuevo = cant_alu[i] - 1
                cant_alu.pop (i)
                
                cant_alu.insert(i, valornuevo)
                
                
                
                
                return (coms[i])
        
        return 0
        
dnis = []
turno = []

        
                    
   