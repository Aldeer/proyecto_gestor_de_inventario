from tkinter import LabelFrame
from tkinter import Entry
from tkinter import StringVar
from tkinter import IntVar
from tkinter import DoubleVar
from tkinter import Button
from tkinter import Tk
from tkinter import Toplevel


class Formulario(Toplevel):


    def __init__(self, master: Tk) -> None:
        """
        Metodo que inicializa una ventana secundaria ligada a la aplicacion
        principal.
        Argumentos:
            -master (Tk): widgets padre
        """
        super().__init__(master)
        
        # variables de control
        self.producto = StringVar()
        self.precio = DoubleVar()
        self.stock = IntVar()

        # configuracion de ventana
        self.title("Formulario de Registro")
        self.geometry("200x300")

        # configuracion de la grilla de la ventana
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # labelframes
        self.producto_lbl = LabelFrame(self)
        self.precio_lbl = LabelFrame(self)
        self.stock_lbl = LabelFrame(self)

        # Entry
        self.producto_inp = Entry(self.producto_lbl)
        self.precio_inp = Entry(self.precio_lbl)
        self.stock_inp = Entry(self.stock_lbl)

        # Botones
        self.guardar_btn = Button(self)
        self.cancela_btn = Button(self)

        # configurar BOTONES
        self.guardar_btn.configure(text="GUARDAR")
        self.cancela_btn.configure(text="CANCELAR")

        # configuracion de ENTRIES
        self.producto_inp.configure(textvariable=self.producto)
        self.precio_inp.configure(textvariable=self.precio)
        self.stock_inp.configure(textvariable=self.stock)

        # configuracion de los labels
        self.producto_lbl.configure(text="Nombre Producto")
        self.precio_lbl.configure(text="Precio")
        self.stock_lbl.configure(text="Stock")

        # posicion de los labels
        self.producto_lbl.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.precio_lbl.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.stock_lbl.grid(row=2, column=0, columnspan=2, sticky="nsew")

        # posicion de los inputs
        self.producto_inp.grid()
        self.precio_inp.grid()
        self.stock_inp.grid()

        # posicion de los botones
        self.guardar_btn.grid(row=3, column=0)
        self.cancela_btn.grid(row=3, column=1)

        # enfoca la ventana
        self.focus_set()
        self.grab_set()
        


