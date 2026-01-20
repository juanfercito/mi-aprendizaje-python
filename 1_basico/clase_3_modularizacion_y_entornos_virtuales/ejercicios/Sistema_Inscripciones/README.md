# Sistema de Inscripciones a Charlas

## 1. Descripción general

Este proyecto corresponde a un **Sistema de Inscripciones a Charlas**, desarrollado en **Python**, orientado a estudiantes de **primer semestre** de la carrera.  
El sistema permite gestionar charlas con cupos limitados, registrar inscripciones de participantes y mantener la **persistencia de la información** mediante archivos de texto.

El programa se ejecuta en consola y ha sido diseñado aplicando principios básicos de programación estructurada y modularización, sin utilizar conceptos ni recursos avanzados fuera del contenido abordado en clase.

---

## 2. Objetivo de la actividad

Aplicar los conocimientos adquiridos en las siguientes unidades del curso:

- **Unidad 3: Manejo avanzado de datos y estructuras**
- **Unidad 4: Técnicas avanzadas y operaciones I/O**

Tipo de recurso: **Actividad Experimental**

A través del desarrollo de un programa que utilice:

- Funciones y paso de parámetros
- Recursividad
- Manejo de excepciones
- Lectura y escritura de archivos
- Uso de listas, diccionarios y estructuras básicas
- Organización del código en módulos

---

## 3. Estructura del proyecto

La estructura del proyecto se organizó de la siguiente manera:

```bash
Sistema_Inscripciones/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── config/
│ └── configuracion.py
│
├── models/
│ ├── charla.py
│ └── inscripcion.py
│
├── services/
│ ├── gestion_charlas.py
│ └── validaciones.py
│
├── persistence/
│ └── manejo_archivos.py
│
├── ui/
│ ├── menu.py
│ └── mensajes.py
│
├── utils/
│ └── excepciones.py
│
└── data/
├── inscripciones_charlas.txt
│
└── backup/
└── respaldo.csv
```
---
## 4. Descripción de carpetas y archivos

### 4.1 `main.py`
Archivo principal del sistema.  
Su función es **inicializar el programa** y delegar la ejecución al menú principal.  
Se mantiene lo más ligero posible, tal como se recomienda en buenas prácticas de programación.

---

### 4.2 Carpeta `config/`
Contiene la configuración general del sistema:
- Definición de las charlas iniciales
- Rutas de los archivos de persistencia

Separar la configuración del resto del código permite una mejor organización y facilita futuras modificaciones.

---

### 4.3 Carpeta `models/`
Define las estructuras de datos principales del sistema:
- `Charla`: representa una charla con identificador, descripción y cupos disponibles.
- `Inscripcion`: representa una inscripción realizada por un usuario.

Se utilizan **clases simples**, sin decoradores ni estructuras avanzadas, para facilitar su lectura.

---

### 4.4 Carpeta `services/`
Contiene la lógica de negocio del programa:
- `gestion_charlas.py`: controla las charlas, la asignación de cupos y sincroniza los datos con las inscripciones almacenadas.
- `validaciones.py`: valida las entradas del usuario utilizando recursividad y manejo de excepciones.

Esta separación permite que la lógica del programa no dependa de la interfaz de usuario.

---

### 4.5 Carpeta `persistence/`
Encargada de la lectura y escritura de archivos:
- Guarda las inscripciones en el archivo obligatorio `inscripciones_charlas.txt`.
- Lee las inscripciones al iniciar el programa para mantener la persistencia.
- Genera un respaldo en formato CSV (`respaldo.csv`).

Cumple con los requisitos de operaciones de entrada/salida (I/O).

---

### 4.6 Carpeta `ui/`
Contiene la interfaz de usuario por consola:
- `menu.py`: controla el flujo del programa y las opciones del usuario.
- `mensajes.py`: centraliza los mensajes mostrados en pantalla.

Esto permite mantener separada la presentación de la lógica del sistema.

---

### 4.7 Carpeta `utils/`
Incluye excepciones personalizadas utilizadas para controlar errores de forma clara y ordenada durante la ejecución del programa.

---

### 4.8 Carpeta `data/`
Contiene los archivos de persistencia:
- `inscripciones_charlas.txt`: almacena las inscripciones realizadas.

Separar los datos del código fuente es una buena práctica de organización.

---

### 4.9 Carpeta `backup/`
Contiene los archivos de respaldo en formato .csv (mejor recomendado) para exportación de datos a otros sistemas o bases de datos:
- `respaldo.csv`: respaldo generado desde el menú del sistema.

Puede contener más archivos de respaldo con formatos diferentes para usos variados.

Este proyecto inicia sin respaldo, pero la función ya esta probada, así que les animo a que la usen y salgan de dudas.

## 5. Cumplimiento de los requisitos académicos

El proyecto cumple con todos los criterios establecidos en la actividad:

- Uso de funciones y paso de parámetros
- Aplicación de recursividad en validación de datos
- Manejo de excepciones
- Lectura y escritura de archivos
- Uso de estructuras de datos básicas (listas y diccionarios)
- Persistencia de la información entre ejecuciones

---

## 6. Ejecución del programa

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
```

El sistema mostrará un menú interactivo que permite:

Inscribirse en una charla

Consultar inscripciones registradas

Ver charlas disponibles

Generar un respaldo de las inscripciones

---

7. Conclusión
Este proyecto demuestra la aplicación práctica de los fundamentos de programación vistos en clase, manteniendo una estructura clara, ordenada y funcional.
El sistema cumple con los requisitos académicos establecidos y presenta una solución coherente y escalable a una problemática real.

---
