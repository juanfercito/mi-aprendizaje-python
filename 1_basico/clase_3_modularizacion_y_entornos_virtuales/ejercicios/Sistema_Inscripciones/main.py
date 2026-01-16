# Punto de entrada mínimo: inicializa e invoca el menú CLI.
from utils.excepciones import exception
def main():
    """Arranca la aplicación delegando en ui.menu.run().
    Mantén este archivo lo más ligero posible (según la consigna).
    """
    try:
        from ui.menu import run
    except exception as e:
        print("Error al importar el menú:", e)
        return
    run()

if __name__ == '__main__':
    main()
