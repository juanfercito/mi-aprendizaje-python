# FUNCION PARA GUARDAR CADA INSCRIPCION EN UN ARCHIVO TXT
def guardar_inscripcion(nombre, email, charla):
    with open("inscripciones_charlas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(nombre + "," + email + "," + charla + "\n")

# ESTA FUNCION LEE EL ARCHIVO DE INSCRIPCIONES Y DEVUELVE 
# UNA LISTA DE DICCIONARIOS CON LA INFORMACION
def leer_inscripcion():
    inscripciones = []

    try:
        with open("inscripciones_charlas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                inscripciones.append({
                    "nombre": datos[0],
                    "email": datos[1],
                    "charla": datos[2]
                })

        return inscripciones
    except FileNotFoundError:
        print("No hay inscripciones registradas.")
        return []
    
