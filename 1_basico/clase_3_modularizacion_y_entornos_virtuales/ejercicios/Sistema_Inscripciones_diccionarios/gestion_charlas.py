from manejo_de_archivos import leer_inscripcion, guardar_inscripcion
charlas = {
    "c-1": "Programacion",
    "c-2": "Marketing Digital",
    "c-3": "Finanzas Personales",
    "c-4": "Liderazgo",
    "c-5": "Superacion",
    "c-6": "Redes Sociales"
}

cupos = {
    "c-1": 10,
    "c-2": 10,
    "c-3": 10,
    "c-4": 10,
    "c-5": 10,
    "c-6": 10
}

def charlas_disponibles():
    print("Charlas disponibles:")
    for codigo, nombre in charlas.items():
        print(f"{codigo} - {nombre} (Cupos disponibles: {cupos[codigo]})")
    

def inscribirse():
    print('-'*10)
    charlas_disponibles()
    
    print("-"*10)
    print("Por favor, ingrese sus datos completos para la inscripcion:")
    # Validar nombre para que no hayan campos vacios
    while True:
        nombre = input("Nombre completo: ")
        if len(nombre.strip()) > 3:
            break
        else:
            print("El nombre debe tener al menos 4 caracteres")
    # Validar email
    while True:
        email = input("Correo electrónico: ")
        if "@" in email:
            break
        else:
            print("Correo inválido. Debe contener '@'.")
    # Validar código de charla y cupos
    while True:
        charla = input("Código de la charla a la que desea inscribirse: ")

        if charla not in charlas:
            print("Código de charla inválido. Intente nuevamente.")
            continue

        if cupos[charla] <= 0:
            print("Lo sentimos, no hay cupos disponibles para esta charla.")
            continue

        # Si todo está bien
        cupos[charla] -= 1
        guardar_inscripcion(nombre, email, charla)
        print(f"Inscripción exitosa a la charla de {charlas[charla]}.")
        break
        
def consultar_inscripciones():
    print("-" * 10)
    print("Lista de inscripciones:")

    inscripciones = leer_inscripcion()

    for inscripcion in inscripciones:
        codigo = inscripcion["charla"]
        nombre_charla = charlas[codigo]

        print(
            "Nombre:", inscripcion["nombre"],
            "| Email:", inscripcion["email"],
            "| Charla:", nombre_charla
        )
    if not inscripciones:
        print("No hay inscripciones registradas.")
        return

def consultar_charlas_disponibles():
    print("Charlas disponibles:")
    for codigo, nombre in charlas.items():
        print(f"{nombre} (Cupos disponibles: {cupos[codigo]})")