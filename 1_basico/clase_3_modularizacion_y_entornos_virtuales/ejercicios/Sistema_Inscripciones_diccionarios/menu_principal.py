from gestion_charlas import inscribirse, consultar_inscripciones, consultar_charlas_disponibles

def menu_principal():
    while True:
        print("-"*10)
        print("Estos son los servicios que ofrecemos: ")
        print("1 - Inscribirse a una charla")
        print("2 - Consultar Inscripciones")
        print("3 - Consultar charlas disponibles")
        print("4 - Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            inscribirse()
        elif opcion == "2":
            consultar_inscripciones()
        elif opcion == "3":
            consultar_charlas_disponibles()             
        elif opcion == "4":
            print("-"*10)
            print("Gracias por usar nuestro sistema. ¡Hasta luego!")
            print("-"*10)
            
            break
        else:
            print("opcion inválida, ingrese un número válido.")
