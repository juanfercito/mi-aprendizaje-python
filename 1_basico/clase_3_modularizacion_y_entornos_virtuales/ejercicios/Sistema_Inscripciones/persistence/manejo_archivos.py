# manejo_archivos.py
# Operaciones de lectura/escritura sobre el archivo obligatorio 'inscripciones_charlas.txt'
# y función independiente para generar un respaldo CSV en la carpeta backups/.

import os
from models.inscripcion import inscripcion_from_line
from config.configuracion import DATA_FILE, BACKUP_DIR, BACKUP_FILE
from utils.excepciones import ArchivoInscripcionesError, exception


def _asegurar_directorio_archivo(path):
    directorio = os.path.dirname(path)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)


def cargar_inscripciones(path=DATA_FILE):
    inscripciones = []
    if not os.path.exists(path):
        return inscripciones
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ins = inscripcion_from_line(line)
                    inscripciones.append(ins)
                except exception:
                    # Saltar líneas mal formateadas (nivel inicial)
                    continue
        return inscripciones
    except Exception as e:
        raise ArchivoInscripcionesError(f"Error leyendo archivo de inscripciones: {e}") from e


def guardar_inscripcion(inscripcion, path=DATA_FILE):
    try:
        _asegurar_directorio_archivo(path)
        # Append simple: suficiente para nivel introductorio
        with open(path, 'a', encoding='utf-8') as f:
            f.write(inscripcion.to_line())
    except Exception as e:
        raise ArchivoInscripcionesError(f"Error al guardar inscripción: {e}") from e


def generar_respaldo_csv(destino_dir=BACKUP_DIR, nombre_archivo=BACKUP_FILE):
    # Lee el archivo obligatorio y escribe un CSV en destino_dir/nombre_archivo.
    if not os.path.exists(destino_dir):
        os.makedirs(destino_dir, exist_ok=True)

    inscripciones = cargar_inscripciones()
    destino = os.path.join(destino_dir, nombre_archivo)

    try:
        with open(destino, 'w', encoding='utf-8') as f:
            f.write('timestamp,nombre,correo,charla_id,charla_titulo\n')
            for ins in inscripciones:
                linea = (
                    f"{ins.timestamp.isoformat()},"
                    f"{ins.nombre},"
                    f"{ins.correo},"
                    f"{ins.charla_id},"
                    f"{ins.charla_titulo}\n"
                )
                f.write(linea)
        return destino
    except Exception as e:
        raise ArchivoInscripcionesError(f"Error generando respaldo: {e}") from e
