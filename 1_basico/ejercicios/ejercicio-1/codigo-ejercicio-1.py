# Antes de probar este código, lee la miniespecificación del ejercicio en el archivo
# 'miniespecificacion-ejercicio-1.md' para entender cómo funciona

# Inicio del programa
print("bienvenido a nuestro show")
decide = input("desea ingresar?")

# primera condición que debe cumplirse
if decide.lower() == "si" or decide.lower() == "yes":
  
    # si se cumple la condición, entramos en el ciclo
    while True:

        # el usuario ingresa los datos solicitados
        nombre = input("cual es su nombre?")
        edad = int(input("cual es su edad?"))
    
        # Empieza la siguiente serie de condiciones
        if edad < 18:
            pase = float(edad * 2 / 100)
            print(f"lo sentimos {nombre}, no puede pasar, pero le daremos ${pase} para el bus")

        elif edad >= 18 and edad <= 59:
            pase = float(edad * 2 / 10 * 15 / 100)
            print(f"felicidades {nombre}, puede pasar, son ${pase}")

        # En este último caso, se asume que la edad sera mayor a 59, por
        # lo que no es necesario validarlo
        else:
            pase = float(edad * 2 / 100)
            print(f"ok {nombre}, puede pasar pero tiene que pagar {pase}")

        # Después de procesar los datos, el usuario decide si repetir el
        #programa o no
        repeat = input("desea ingresar otra vez?")
        if repeat.lower() == "si" or repeat.lower() == "yes":
            continue
        else:
            break

# Se sale del bucle y termina el programa
print("gracias por su visita")