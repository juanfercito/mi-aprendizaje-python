#                               QUÉ ES INT?

# 'int' se refiere al tipo de dato que representa enteros (números enteros, completos,
# sin parte decimal) en Python.
# Estos se usan para almacenar números positivos, negativos o cero sin decimales , como 3, -23 o 0.

#             CARACTERÍSTICAS PRINCIPALES DE LOS ENTEROS (int) EN PYTHON:
# 1. Son inmutables, pues una vez creados no pueden modificarse, pues no son objetos(datos)
#    secuenciales, ejemplo:

A = 25
print(A, type(A)) # con el metodo type() podemos obtener '<class 'int'>'

# Si intentáramos modificar el entero de la variable anterior, obtendríamos un error, así:
# A[1] = 4
# print(A) # En consola saldrá TypeError: 'int' object does not support item assignment

#    Pero si queremos cambiar el valor de la variable, podemos reasignarla:
A = 48
print(A, type(A))

#    incluso podemos convertir el tipo de dato al reasignarlo:
A = int(123.456) # convierte el float 123.456 a int, suprimiendo los decimales y quedando 123
print(A, type(A))

#    o también convertir la variable en un string "789":
A = str(789) # el metodo str() convierte el int 789 a string "789"
print(A, type(A)) # Ahora con el metodo type() obtenemos '<class 'str'>'

#    incluso podemos hacer lo opuesto, es decir, convertir un string de números a int:
A = int(A) # convierte el string "789" a int 789
print(A, type(A)) # Ahora con el metodo type() obtenemos '<class 'int'>'

# 2. Son hashables (pueden usarse como claves en dict y miembros de set), ejemplo:
D = {1: 'uno', 42: 'cuarenta y dos'}
print('\nDict con int como clave:', D[42])
print('tipo de dato para D =', type(D)) # se obtiene '<class 'dict'>'
print('hashear 42 =', hash(42)) # hash() devuelve el valor hash de un objeto (si tiene uno)

# 3. No son iterables, pues no implementan los métodos internos o nativos; esto los convierte en
#    datos escalares o singulares (no secuenciales ni colecciones). Esto significa que no se puede
#    recorrer un int con un bucle porque carece de elementos internos o métodos de iteración como
#    los índices o slices. Ejemplo:

# X = 42
# try:
#     for c in X:
#         print(c)
# except TypeError as e:
#     print("Error:", e)   # TypeError: 'int' object is not iterable

#    Por el contrario, si iteras un string, funcionará porque son secuenciales:
S = "hola"
print('lo que devuelve la variable S: ')
for ch in S:
    print(ch)

# 4. Operaciones aritméticas básicas con enteros devuelven `int` salvo que uses
#    operaciones que produzcan un float (por ejemplo la división, donde es más
#    probable obtener un float):

NUM_1 = 8
NUM_2 = 3
print('\nEL primer int es ', NUM_1)
print('El segundo int es ', NUM_2)
print('La suma devuelve un entero: ', NUM_1 + NUM_2)
print('La resta devuelve un entero: ', NUM_1 - NUM_2)
print('La multiplicación devuelve un entero: ', NUM_1 * NUM_2)
#    usando el método isinstance() podemos verificar si resultado es int o float, y devolverá
#    True o False:
print('La división devuelve un float: ', NUM_1 / NUM_2, isinstance(NUM_1 / NUM_2, float))

# 5. En cuanto a su tamaño en memoria, los int de Python pueden ser tan grandes como su
#    cantidad de dígitos, evitando overflow de memoria limitados solo por la memoria del
#    sistema; esto los hace ideales para cálculos matemáticos precisos y grandes.

#    Con el método sys.getsizeof() podemos ver el tamaño en bytes de varios int:
import sys # importa el módulo sys para usar las funciones del sistema
LITTLE_VAR = 2 # un int pequeño
print(f"\nTamaño en bytes de un int pequeño ({LITTLE_VAR}):", sys.getsizeof(LITTLE_VAR), "bytes")
HIGHER_VAR = 2*10 # int más grandes:
print(f"Tamaño en bytes de un int más grande (2*10 = {HIGHER_VAR}):", sys.getsizeof(HIGHER_VAR), "bytes")
BIGGER_VAR = 2**30 # int mucho más grandes:
print(f"Tamaño en bytes de un int mucho más grande (2**30 = {BIGGER_VAR}):", sys.getsizeof(BIGGER_VAR), "bytes")
HUGE_VAR = 2**100 # int extremadamente grandes:
print(f"Tamaño en bytes de un int extremadamente grande (2**100 = {HUGE_VAR}):", sys.getsizeof(HUGE_VAR), "bytes")
GIANT_VAR = 2**1000 # int colosalmente grandes:
print(f"Tamaño en bytes de un int gigantesco (2**1000 = {GIANT_VAR}):", sys.getsizeof(GIANT_VAR), "bytes")

#    Este es un ejemplo de iterar sobre una lista de enteros y mostrar su tamaño en bytes,
#    aunque está comentado para evitar mucha salida en consola, pero es el mismo principio
#    que el ejemplo anterior:
# vals = [0, 1, 2**30, 2**100, 2**1000]
# print("\nTamaños en bytes de varios int (sys.getsizeof):")
# for v in vals:
#    print(f"valor=2**{v.bit_length()-1 if v>0 else 0} -> {v} | getsizeof:
#    {sys.getsizeof(v)} bytes")

#                     ******* NOTAS ADICIONALES: ********
# - Python implementa enteros de precisión arbitraria (no hay overflow por límite fijo);
# esto implica mayor flexibilidad pero coste en memoria mayor comparado con enteros de tamaño
# fijo en C/Java, etc; profundizaré en esto más adelante.
# - A partir de Python 3, no hay distinción entre 'int' y 'long' como en otros lenguajes,
#  pues ambos se consideran del mismo tipo y facilita su manejo y uniformidad.
