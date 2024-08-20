from tkinter import Tk

class VentanaPrincipal(Tk):
    """
    Clase VentanaPrincipal que herda de la clase Tk para crear una aplicacion
    tkinter
    """

    def __init__(self:Tk) -> None:
        """
        Metodo constructor de la ventana principal. Inicializa todos los widgets
        de la aplicacion gestor de inventario.
        """
        self.configuracion()

    def configuracion(self) -> None:
        """
        Carga las configuraciones basicas de la ventana principal.
        """
        self.title("GESTOR DE INVENTARIO") # titulo de la ventana principal
        self.geometry("1000x600") # tamaño de la ventana principal
        self.resizable(width=False, height=False) # desactiva la redimensionado