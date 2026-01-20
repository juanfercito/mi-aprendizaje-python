from manejo_de_archivos import leer_inscripcion, guardar_inscripcion

# lISTAS DE CHARLAS, CODIGOS Y CUPOS  DISPONIBLES
# LAS LISTAS ESTAN RELACIONADAS POR INDICE, ES UNA ESTRUCTURA FACIL 
# DE MANEJAR PARA ESTA TAREA
codigos = ["01", "02", "03", "04", "05", "06"]
temas   = ["Programacion", "Marketing Digital", "Finanzas Personales",
           "Liderazgo", "Superacion", "Redes Sociales"]
cupos   = [15, 12, 20, 10, 12, 13]

# FUNCION PARA MOSTRAR LOS CUPOS DE CHARLAS
def cupos_de_charlas():
    print("Charlas disponibles:")
    for i in range(len(codigos)):
        print(codigos[i], "-", temas[i], "(Cupos disponibles:", cupos[i], ")")
    
# FUNCION PARA INSCRIBIRSE A UNA CHARLA
def inscribirse():
    print("-" * 10)
    cupos_de_charlas()
    print("-" * 10)
    print("Por favor, ingrese sus datos oara inscribirse:")
    # VALIDAR NOMBRE
    while True:
        nombre = input("Escriba su nombre completo: ")
        if len(nombre.strip()) > 3:
            break
        else:
            print("El nombre debe tener al menos 4 caracteres")
    # VALIDAR EMAIL
    while True:
        email = input("Escriba su correo electrónico: ")
        if "@" in email:
            break
        else:
            print("Correo inválido. Debe contener '@'.")
    # VALIDAR CODIGO Y CUPOS
    while True:
        charla = input("Escriba el código de la charla: ")

        if charla not in codigos:
            print("Código de charla inválido. Intente nuevamente.")
            continue

        indice = codigos.index(charla)

        if cupos[indice] <= 0:
            print("Sin cupos disponibles para esta charla, elija otra.")
            continue
        # SI LOS DATOS SONCORRECTOS, SE GUARDA LA INSCRIPCION Y SE 
        # ACTUALIZAN LOS CUPOS
        cupos[indice] -= 1
        guardar_inscripcion(nombre, email, charla)
        print("-" * 10)
        print(f"Inscripción exitosa a la charla de {temas[indice]}.")
        break

# FUNCION PARA CONSULTAR INSCRIPCIONES REALIZADAS        
def consultar_inscripciones():
    print("-" * 10)
    print("Lista de inscripciones:")

    inscripciones = leer_inscripcion()

    if not inscripciones:
        return

    # SE LEE CADA LINEA Y SE MUESTRA LA INFORMACION POR INDICE
    for inscripcion in inscripciones:
        codigo = inscripcion["charla"]
        indice = codigos.index(codigo)

        print(
            "Nombre:", inscripcion["nombre"],
            "| Email:", inscripcion["email"],
            "| Charla:", temas[indice]
        )
