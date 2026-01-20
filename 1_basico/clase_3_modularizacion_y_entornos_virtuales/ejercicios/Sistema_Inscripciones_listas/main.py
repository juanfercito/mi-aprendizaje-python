from gestion_charlas import inscribirse, consultar_inscripciones, cupos_de_charlas
# EL MENÙ PRINCIPAL PARA INTERACTUAR CON EL PROGRAMA
def menu_principal():
    print("INSCRIPCIONES A CHARLAS")
    while True:
        print("-"*10)
        print("ELIJA UNA OPCION PARA EMPEZAR: ")
        print("1 - Inscribirse a una charla")
        print("2 - Consultar Inscripciones")
        print("3 - Consultar cupos de charlas")
        print("4 - Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            inscribirse()
        elif opcion == "2":
            consultar_inscripciones()
        elif opcion == "3":
            cupos_de_charlas()             
        elif opcion == "4":
            print("-"*10)
            print("GRACIAS! VUELVA PRONTO!")
            print("-"*10)
            
            break
        else:
            print("opcion inválida, ingrese un número válido.")

# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    menu_principal()