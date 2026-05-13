dnis = [30435473, 35552144, 11421159, 28667796, 26959663, 30435473, 29927766]

materias = ["mate", "progra", "ingles", "mate", "progra", "mate", "ingles"]


def correlativas(materia):
    pass


def aprobada(dni, materia):
    pass


def horario(materia):
    pass


def controlaSuperposicion(dni, horario):
    pass


indice = 0

while indice < len(dnis):

    inscripcionValida = True

    dniAlumno = dnis[indice]
    materiaSolicitada = materias[indice]

    listaCorrelativas = correlativas(materiaSolicitada)

    # Verificar correlativas
    for i in range(len(listaCorrelativas)):

        correlativaActual = listaCorrelativas[i]

        if aprobada(dniAlumno, correlativaActual) == False:
            inscripcionValida = False

    # Verificar superposición horaria
    horarioMateria = horario(materiaSolicitada)

    if controlaSuperposicion(dniAlumno, horarioMateria) == False:
        inscripcionValida = False

    # Eliminar inscripción inválida
    if inscripcionValida == False:

        dnis.pop(indice)
        materias.pop(indice)

    else:
        indice += 1