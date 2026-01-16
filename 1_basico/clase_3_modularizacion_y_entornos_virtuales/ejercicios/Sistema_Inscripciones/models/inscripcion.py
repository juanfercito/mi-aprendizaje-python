# Con este archivo definimos Inscripcion y funciones básicas de serialización

from datetime import datetime

# Definimos la clase Inscripcion, uno objeto de este tipo 
# representa una inscripción a una charla
class Inscripcion:
    def __init__(self, timestamp, nombre, correo, charla_id, charla_titulo):
        if isinstance(timestamp, datetime):
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now()

        self.nombre = str(nombre)
        self.correo = str(correo)
        self.charla_id = str(charla_id)
        self.charla_titulo = str(charla_titulo)

    # esta función convierte la inscripción a una línea de texto para guardarla en un archivo
    def to_line(self):
        # Formato CSV simple: timestamp,nombre,correo,charla_id,charla_titulo
        # usamos el método isoformat() para el timestamp y facilitar su lectura
        return (
            self.timestamp.isoformat() + "," +
            self.nombre + "," +
            self.correo + "," +
            self.charla_id + "," +
            self.charla_titulo + "\n"
        )

def inscripcion_from_line(linea):
    """
    Crea un objeto Inscripcion a partir de una línea del archivo txt.
    """
    partes = linea.strip().split(",")

    if len(partes) < 5:
        raise ValueError("Línea de inscripción con formato inválido")

    timestamp = datetime.fromisoformat(partes[0])
    nombre = partes[1]
    correo = partes[2]
    charla_id = partes[3]
    charla_titulo = ",".join(partes[4:])

    return Inscripcion(timestamp, nombre, correo, charla_id, charla_titulo)
