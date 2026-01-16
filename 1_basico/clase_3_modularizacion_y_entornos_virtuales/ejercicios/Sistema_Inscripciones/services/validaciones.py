# Validaciones básicas con apoyo de recursividad

from utils.excepciones import ValidacionError
from services import gestion_charlas


def pedir_input_recursivo(mensaje, funcion_validacion):
    valor = input(mensaje).strip()
    try:
        funcion_validacion(valor)
        return valor
    except ValidacionError as e:
        print(e)
        return pedir_input_recursivo(mensaje, funcion_validacion)


def validar_nombre(nombre):
    if not nombre or len(nombre) < 3:
        raise ValidacionError("El nombre debe tener al menos 3 caracteres")
    if len(nombre) > 50:
        raise ValidacionError("El nombre no debe superar los 50 caracteres")
    return nombre.lower()


def validar_correo(correo):
    if "@" not in correo or "." not in correo:
        raise ValidacionError("Correo electrónico inválido")
    return correo.lower()


def validar_id_charla(charla_id):
    charla_id = charla_id.upper()
    charla = gestion_charlas.obtener_charla_por_id(charla_id)
    if charla is None:
        raise ValidacionError("ID de charla no válido. Intente nuevamente")
    return charla_id
