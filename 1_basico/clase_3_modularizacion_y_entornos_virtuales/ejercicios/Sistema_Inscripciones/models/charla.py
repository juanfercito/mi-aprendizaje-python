# Definición simple de la estructura Charla, similar a la de Inscripción.

class Charla:
    def __init__(self, id, titulo, descripcion, cupos):
        self.id = str(id)
        self.titulo = str(titulo)
        self.descripcion = str(descripcion)
        try:
            self.cupos = int(cupos)
        except (TypeError, ValueError):
            self.cupos = 0


def charla_from_dict(d):
    """
    Crea un objeto Charla a partir de un diccionario.
    Se usa una función externa para evitar conceptos no vistos (decoradores, classmethod).
    """
    return Charla(
        d.get("id"),
        d.get("titulo"),
        d.get("descripcion"),
        d.get("cupos", 0)
    )
