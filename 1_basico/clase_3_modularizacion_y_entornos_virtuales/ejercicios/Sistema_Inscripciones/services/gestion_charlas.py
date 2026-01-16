# gestion_charlas.py
# Lógica de negocio simple: lista de charlas en memoria y operaciones con ellas.
from models.charla import charla_from_dict
from models.inscripcion import Inscripcion
from datetime import datetime
from config.configuracion import CHARLAS_INICIALES
from utils.excepciones import CuposAgotadosError, ValidacionError
from persistence import manejo_archivos

# Inicializamos charlas en memoria (mutable lista)
_charlas = [charla_from_dict(d) for d in CHARLAS_INICIALES]

def obtener_charla_por_id(charla_id):
    charla_id = charla_id.upper()
    for c in _charlas:
        if c.id == charla_id:
            return c
    return None

def _aplicar_inscripciones_previas():
    """
    Lee el archivo de inscripciones y descuenta los cupos
    correspondientes a cada charla.
    """
    inscripciones = manejo_archivos.cargar_inscripciones()
    for ins in inscripciones:
        charla = obtener_charla_por_id(ins.charla_id)
        if charla and charla.cupos > 0:
            charla.cupos -= 1


# Aplicamos persistencia al iniciar el módulo
_aplicar_inscripciones_previas()

def listar_charlas():
    """Retorna la lista actual de charlas (en memoria)."""
    return _charlas.copy()


def inscribir(nombre, correo, charla_id):
    """Intenta inscribir a una persona en la charla indicada.

    Reglas:
    - Si la charla no existe -> raise ValidacionError
    - Si no hay cupos -> raise CuposAgotadosError
    - En caso exitoso se decrementa el cupo en memoria y se retorna la Inscripcion (sin persistir)
    """
    charla = obtener_charla_por_id(charla_id)
    if charla is None:
        raise ValidacionError(f"Charla con id '{charla_id}' no encontrada")
    if charla.cupos <= 0:
        raise CuposAgotadosError(f"No hay cupos disponibles para la charla {charla.titulo}")

    # Decrementamos cupo en memoria (estado mutable)
    charla.cupos -= 1

    # Creamos la inscripción
    # Aquí se genera la inscripción que aparecerá tanto en pantalla como 
    # en el archivo de persistencia.
    ins = Inscripcion(
        timestamp=datetime.now(),
        nombre=nombre,
        correo=correo,
        charla_id=charla.id,
        charla_titulo=charla.titulo
    )
    return ins

