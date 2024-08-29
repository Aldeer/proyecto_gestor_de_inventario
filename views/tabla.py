from tkinter.ttk import Treeview
from tkinter import Frame

CABECERA = ("CODIGO", "PRODUCTO", "PRECIO", "STOCK")

class TablaProducto(Treeview):
    """
    Clase que genera una tabla con campos a partir de la herencia de la clase
    Treeview de tkinter
    """

    def __init__(self, master:Frame) -> None:
        """
        Metodo constructor de clase. crea un widget tabla donde se muestran 
        los productos.
        Argumentos:
            -master (Frame): widgets padre al que pertenece
        """
        super().__init__(master)

        self.configure(columns=CABECERA)
        self.cabecera()

        self.grid(sticky="nsew", padx=20, pady=20)


    def cabecera(self) -> None:
        self.configure(show="headings")
        for cabecera in CABECERA:
            self.heading(cabecera, text=cabecera, anchor="w")

