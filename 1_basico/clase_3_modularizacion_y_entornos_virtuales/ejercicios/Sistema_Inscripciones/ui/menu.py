# Menú interactivo sencillo: delega en services y persistence.

from services import gestion_charlas
from services import validaciones
from persistence import manejo_archivos
from ui import mensajes
from utils.excepciones import ValidacionError, ArchivoInscripcionesError, CuposAgotadosError, exception

# Funciones para cada opción del menú

# Función para mostrar charlas disponibles
# Invoca a services/gestion_charlas.py
def mostrar_charlas():
    charlas = gestion_charlas.listar_charlas()
    print('\nCharlas disponibles:')
    for c in charlas:
        print(f"{c.id} - {c.titulo} (Cupos: {c.cupos})")
    print('')

# Función para inscribir a una charla
# Invoca a services/validaciones.py y services/gestion_charlas.py
def opcion_inscribir():
    try:
        # En este bloque llamamos a validaciones.py para cada dato
        mostrar_charlas()

        nombre = validaciones.pedir_input_recursivo(
            'Ingrese su nombre completo (hasta 50 caracteres): ',
            validaciones.validar_nombre
        )

        charla_id = validaciones.pedir_input_recursivo(
            'Ingrese el id de la charla a la que desea inscribirse: ',
            validaciones.validar_id_charla
        )

        correo = validaciones.pedir_input_recursivo(
            'Correo electrónico: ',
            validaciones.validar_correo
        )

        inscripcion = gestion_charlas.inscribir(
            nombre=nombre,
            correo=correo,
            charla_id=charla_id
        )

        manejo_archivos.guardar_inscripcion(inscripcion)
        print('\nInscripción registrada correctamente.')

    except ValidacionError as ve:
        print('Validación:', ve)
    except CuposAgotadosError as ce:
        print('No fue posible inscribir:', ce)
    except ArchivoInscripcionesError as ae:
        print('Error en archivo:', ae)
    except exception as e:
        print('Ocurrió un error inesperado:', e)

# Función para consultar inscripciones
# Invoca a persistence/manejo_archivos.py
def opcion_consultar_inscripciones():
    inscripciones = manejo_archivos.cargar_inscripciones()
    if not inscripciones:
        print('\nNo hay inscripciones registradas.\n')
        return

    print('\nInscripciones:')
    for ins in inscripciones:
        print(
            f"{ins.timestamp.isoformat()} - "
            f"{ins.nombre} - "
            f"{ins.correo} - "
            f"{ins.charla_id} - "
            f"{ins.charla_titulo}"
        )
    print('')

# Función para generar respaldo CSV
# Invoca a persistence/manejo_archivos.py
def opcion_generar_respaldo():
    try:
        path = manejo_archivos.generar_respaldo_csv()
        print(f'Archivo de respaldo generado en: {path}')
    except ArchivoInscripcionesError as e:
        print('Error generando respaldo:', e)

# Punto de entrada del menú
def run():
    """
    Punto de ejecución del menú.
    Se define explícitamente para que main.py pueda importarlo
    sin cambiar su lógica.
    """
    print(mensajes.TEXTO_BIENVENIDA)

    while True:
        print(mensajes.TEXTO_MENU)
        opcion = input('Opción: ').strip()

        if opcion == '1':
            opcion_inscribir()
        elif opcion == '2':
            opcion_consultar_inscripciones()
        elif opcion == '3':
            mostrar_charlas()
        elif opcion == '4':
            opcion_generar_respaldo()
        elif opcion == '0':
            print('Saliendo. Gracias.')
            break
        else:
            print('Opción no reconocida. Intente de nuevo.')

