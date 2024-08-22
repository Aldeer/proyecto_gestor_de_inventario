from tkinter import Tk
from tkinter import Button
from tkinter import Frame

class VentanaPrincipal(Tk):
    """
    Clase VentanaPrincipal que herda de la clase Tk para crear una aplicacion
    tkinter
    """

    def __init__(self) -> None:
        """
        Metodo constructor de la ventana principal. Inicializa todos los widgets
        de la aplicacion gestor de inventario.
        """
        super().__init__()

        # configuracion de la grilla de la ventana principal
        self.grid_columnconfigure(0, weight=1)
 
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(3,weight=3)

        # configuracion ventana principal
        self.title("GESTOR DE INVENTARIO") # titulo para la ventana principal
        self.geometry("1024x680") # tamanio de la ventana principal
        self.resizable(width=False, height=False) # desactiva el redimensionado de la ventana

        # frame para los botones
        self.botones_frame = Frame(self) # instancia para el frame de los botones
        self.botones_frame.configure(bg="#0D7C66") # color de fondo del frame de los botones
        self.botones_frame.grid(row=0,column=0, sticky="nsew")

        # frame para la tabla
        self.tabla_frame = Frame(self) # instancia para el frame de la tabla
        self.tabla_frame.configure(bg="#D7C3F1")
        self.tabla_frame.grid(row=3, column=0, sticky="nsew")

        # boton de registrar producto 
        self.registrar_btn = Button(self.botones_frame) # instancia del boton registrar
        self.registrar_btn.configure(bg="#0d6efd")
        self.registrar_btn.configure(fg="#fff")
        self.registrar_btn.configure(activebackground="#6ea8fe")
        self.registrar_btn.configure(text="REGISTRAR")
        self.registrar_btn.configure(width=10, height=2)

        self.editar_btn = Button(self.botones_frame) # instancia del boton editar
        self.editar_btn.configure(bg="#ffc107")
        self.editar_btn.configure(fg="#000")
        self.editar_btn.configure(activeforeground="#000")
        self.editar_btn.configure(activebackground="#FFDA6A")
        self.editar_btn.configure(text="EDITAR")
        self.editar_btn.configure(width=10, height=2)

        self.eliminar_btn = Button(self.botones_frame) # instancia del boton eliminar
        self.eliminar_btn.configure(bg="#dc3545")
        self.eliminar_btn.configure(fg="#fff")
        self.eliminar_btn.configure(activeforeground="#fff")
        self.eliminar_btn.configure(activebackground="#ea868f")
        self.eliminar_btn.configure(text="ELIMINAR")
        self.eliminar_btn.configure(width=10, height=2)

        
        self.registrar_btn.grid(row=0, column=0)
        self.editar_btn.grid(row=0, column=1)
        self.eliminar_btn.grid(row=0, column=2)
        
""" win = VentanaPrincipal()
win.mainloop() """