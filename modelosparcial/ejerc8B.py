def obteneralimento (nroJaula):
    pass
def obtenerLitrosAgua(nroJaula):
    pass
def volcarAlimento(nroJaula,CantLitros):
    pass
def agregarAgua(nroJaula,cantLitros):
    pass
def alertarEncargado(nroJaula):
    pass



jaulas = []
for i in range (len(jaulas)):
    nroJaula = jaulas [i]
    pesocomida = obteneralimento(nroJaula)
    litrosagua = obtenerLitrosAgua(nroJaula)
    if pesocomida == 500 and litrosagua == 5:
        alertarEncargado(nroJaula)
    else:
        if pesocomida < 500:
            valorcomida = 500 - pesocomida
            volcarAlimento(nroJaula,valorcomida)
        if litrosagua < 5:
            valoragua = 5 - litrosagua
            agregarAgua(nroJaula, valoragua)