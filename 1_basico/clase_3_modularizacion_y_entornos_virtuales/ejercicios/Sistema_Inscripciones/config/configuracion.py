import os

# Constantes y valores por defecto del proyecto.

# Esto es una aproximación de las variables de entorno, 
# que serán abarcadas más adelante en el curso, es una 
# práctica de seguridad y organización de proyectos.

# Ruta del archivo de persistencia
# Se procede de esta forma para facilitar futuras expansiones del proyecto y 
# que las rutas sean relativas al directorio base de persistencia pero sin aparecer 
# directamente en el directorio raíz del sistema de archivos.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Este es el directorio donde se guardarán los datos, 
# más adelante se puede mejorar para que sea configurable y que incluya 
# varias opciones, así como otro tiopo de almacenamiento.
DATA_DIR = os.path.join(BASE_DIR, "data")
# Archivo de persistencia obligatorio para el proyecto
DATA_FILE = os.path.join(DATA_DIR, "inscripciones_charlas.txt")

# Carpeta y nombre para el respaldo (complementario).
BACKUP_DIR = "backup"
BACKUP_FILE = "respalo.csv"

# Charla por defecto (si se quiere inicializar en memoria).
CHARLAS_INICIALES = [
    {"id": "CH-01", "titulo": "Introducción a Python", "descripcion": "Bases de Python.", "cupos": 25},
    {"id": "CH-02", "titulo": "Marketing Digital", "descripcion": "Estrategias de marketing y comunicación.", "cupos": 20},
    {"id": "CH-03", "titulo": "Finanzas Personales", "descripcion": "Conceptos básicos de finanzas y presupuesto.", "cupos": 20},
    {"id": "CH-04", "titulo": "Liderazgo", "descripcion": "Habilidades de liderazgo y trabajo en equipo.", "cupos": 15},
    {"id": "CH-05", "titulo": "Superación Personal", "descripcion": "Técnicas de motivación y crecimiento personal.", "cupos": 25},
    {"id": "CH-06", "titulo": "Redes Sociales", "descripcion": "Uso responsable y profesional de redes sociales.", "cupos": 30},
]

