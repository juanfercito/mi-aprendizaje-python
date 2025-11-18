import time
import sys

print("¡Bienvenido a la tienda de libros!")
libreria = []

# Aaquí inicializamos los arreglos unidimensionales
nombres = []
apellidos = []
cantidades = []
precios_unitarios_list = []
totales_por_cliente = []

# Aquí preguntamos antes de iniciar cuántas ventas se registrarán
while True:
    try:
        total_ventas_a_registrar = int(input("¿Cuántas ventas desea registrar? (entero > 0): ").strip())
        if total_ventas_a_registrar > 0:
            break
        else:
            print("Ingrese un número mayor que 0.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

while True:
    time.sleep(1)

    print("*" * 10)
    print("Menú")
    print("*" * 10)
    print("1. Ingresar sus datos de usuario")
    print("2. Ver todas las ventas")
    print("3. Ver el promedio de ventas")
    print("4. Venta más alta y venta más baja")
    print("5. Salir")
    print("-" * 10)

    time.sleep(1)

    # Validación correcta del input del menú
    try:
        opcion = int(input("Seleccione una opción para continuar: ").strip())
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 5:
        print("Gracias por preferirnos.")
        time.sleep(1)
        sys.exit()
    else:
        if opcion == 1:
            # Verificamos si ya se alcanzó el número de ventas a registrar
            if len(libreria) >= total_ventas_a_registrar:
                print("Ya alcanzó el número máximo de ventas a registrar según lo indicado al inicio.")
                continue

            while True:
                ventas = {}
                nombre = input("Escriba su nombre: ").lower().strip()
                apellido = input("Escriba su apellido: ").lower().strip()
                if nombre == "" or apellido == "":
                    print("Nombre y apellido no pueden estar vacíos. Vuelva a intentarlo.")
                    continue

                print(f"¡Bienvenido {nombre.capitalize()} {apellido.capitalize()}!")
                time.sleep(1)
                # Establecí este control de entrada para cantidad de libros:
                # - Si el usuario presiona Enter (cadena vacía) -> vuelve al menú sin guardar
                # - Si ingresa texto no numérico -> reintentar
                # - Si ingresa número < 1 -> vuelve al menú sin guardar
                salir_sin_guardar = False
                while True:
                    raw = input("¿cuántos libros desea llevar?: ").strip()
                    if raw == "":
                        print("¿No desea llevar libros? ok, lo invitamos a consultar nuestro menú...")
                        salir_sin_guardar = True
                        break
                    try:
                        cant_libros = int(raw)
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
                    if cant_libros < 1:
                        print("¿No desea llevar libros? ok, lo invitamos a consultar nuestro menú...")
                        salir_sin_guardar = True
                        break

                    # PEDIR precio unitario para esta venta
                    while True:
                        raw_precio = input("Ingrese el precio unitario por libro (ej. 2.50): ").strip()
                        try:
                            precio_unitario = float(raw_precio)
                            if precio_unitario >= 0:
                                break
                            else:
                                print("El precio debe ser mayor o igual a 0.")
                        except ValueError:
                            print("Precio inválido. Ingrese un número válido (uso de punto para decimales).")

                    compras = {}

                    # Cálculo subtotal/desc/total
                    subtotal = cant_libros * precio_unitario
                    # Reglas de descuento (decisión: >=6 -> 40%)
                    if cant_libros == 1:
                        descuento = subtotal * 0.05
                    elif 2 <= cant_libros <= 3:
                        descuento = subtotal * 0.10
                    elif 4 <= cant_libros <= 5:
                        descuento = subtotal * 0.30
                    else:  # cant_libros >= 6
                        descuento = subtotal * 0.40

                    total = subtotal - descuento

                    id_compra = len(libreria) + 1

                    ventas["id_compra"] = id_compra
                    ventas["nombre"] = nombre
                    ventas["apellido"] = apellido

                    compras["cantidad_libros"] = cant_libros
                    compras["precio_unitario"] = precio_unitario
                    compras["subtotal"] = round(subtotal, 2)
                    compras["descuento"] = round(descuento, 2)
                    compras["total"] = round(total, 2)
                    ventas["compra"] = compras
                    break

                # Si detectamos la señal de salir sin guardar, no añadimos la venta
                if salir_sin_guardar:
                    # Volvemos al menú principal (salir del bucle de compras)
                    break

                # Añadir tanto a la lista de diccionarios como a los arreglos paralelos
                libreria.append(ventas)
                nombres.append(nombre)
                apellidos.append(apellido)
                cantidades.append(cant_libros)
                precios_unitarios_list.append(precio_unitario)
                totales_por_cliente.append(round(total, 2))

                print(f"Felicidades {nombre.capitalize()} {apellido.capitalize()}, "
                      f"Su compra ha sido registrada con éxito")
                time.sleep(1)
                print("Su factura es: ")
                print("-" * 10)
                print(f"Compra N°: {id_compra}"
                      f"\nCliente: {nombre.capitalize()} {apellido.capitalize()}"
                      f"\nCantidad de libros: {cant_libros}"
                      f"\nPrecio unitario: ${precio_unitario}"
                      f"\nSubtotal: ${subtotal:.2f}"
                      f"\nDescuento: ${descuento:.2f}"
                      f"\nTotal a pagar: ${total:.2f}")
                time.sleep(2)

                # Si ya alcanzamos el número de ventas requerido, avisar y volver al menú
                if len(libreria) >= total_ventas_a_registrar:
                    print("Se ha alcanzado el número de ventas a registrar. Volviendo al menú principal.")
                    break

                repetir = input("¿Desea realizar otra compra? (si/no): ").lower().strip()
                if repetir == "si" or repetir == "yes":
                    continue
                else:
                    break

        elif opcion == 2:
            if len(libreria) == 0:
                print("Registro vacío")
            else:
                print("Listado de todas las ventas realizadas:")
                for i, venta in enumerate(libreria, start=1):
                    mostrar = venta["compra"]
                    print(f"{i}. Compra N°: {venta['id_compra']} - "
                          f"{venta['nombre'].capitalize()} {venta['apellido'].capitalize()} - "
                          f"Cantidad de libros: {mostrar['cantidad_libros']} - "
                          f"Total: ${mostrar['total']:.2f}")

        elif opcion == 3:
            if len(libreria) == 0:
                print("Registro vacío")
            else:
                # Aquí usamos totales del arreglo paralelo para el promedio
                total_ventas = sum(totales_por_cliente)
                total_libros = sum(cantidades)

                promedio_ventas = total_ventas / len(totales_por_cliente)
                promedio_libros = total_libros / len(cantidades)

                print(f"El promedio de ventas es: ${promedio_ventas:.2f}")
                print(f"El promedio de libros vendidos es: {promedio_libros:.2f}")

                time.sleep(2)

        elif opcion == 4:
            if len(libreria) == 0:
                print("Registro vacío")
            else:
                # Construir listas acumuladas
                totales = totales_por_cliente[:]  # copia de arreglo paralelo
                cantidades_list = cantidades[:]

                max_venta = max(totales)
                min_venta = min(totales)
                # índice de las ventas correspondientes
                idx_max = totales.index(max_venta)
                idx_min = totales.index(min_venta)

                print(f"La venta más alta es: ${max_venta:.2f} - Cliente: {nombres[idx_max].capitalize()} {apellidos[idx_max].capitalize()} - {cantidades_list[idx_max]} libros.")
                print(f"La venta más baja es: ${min_venta:.2f} - Cliente: {nombres[idx_min].capitalize()} {apellidos[idx_min].capitalize()} - {cantidades_list[idx_min]} libros.")

                time.sleep(2)

        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

        time.sleep(1)
