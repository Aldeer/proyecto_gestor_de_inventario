from tkinter.ttk import Treeview
from tkinter import Tk
from tkinter import Frame

class TablaProducto(Treeview):
    """
    Clase que genera una tabla con campos a partir de la herencia de la clase
    Treeview de tkinter
    """

    def __init__(self:Treeview, master:Tk | Frame) -> None:
        """
        Metodo constructor de clase. crea un widget tabla donde se muestran 
        los productos.
        Argumentos:
            -master(Tk | Frame): widgets padre al que pertenece
        """
