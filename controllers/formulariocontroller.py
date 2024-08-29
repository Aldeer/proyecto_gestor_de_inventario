from views.formulario import Formulario
from views.tabla import TablaProducto
from models.producto import Producto
from models.inventario import Inventario


class FormularioController:

    def __init__(self, formulario:Formulario, inventario:Inventario, tabla: TablaProducto) -> None:
        self.formulario = formulario
        self.inventario = inventario
        self.tabla = tabla
        

        # Eventos de botones
        self.formulario.guardar_btn.bind("<Button-1>", lambda e: self.obtener_datos())
        self.formulario.cancela_btn.bind("<Button-1>", lambda e: self.cancelar_formulario())

    def obtener_datos(self) -> None:
        nuevo_producto = Producto()
        producto = self.formulario.producto.get()
        precio = self.formulario.precio.get()
        stock = self.formulario.stock.get()
    
        if not producto:
            print("Campo producto vacio")
        if not precio:
            print("Campo precio vacio")
        if not stock:
            print("Campo stock vacio")

        nuevo_producto.producto = producto
        nuevo_producto.precio = precio
        nuevo_producto.stock = stock

        self.inventario.agregar_producto(nuevo_producto)
        self.mostrar_datos_tabla(nuevo_producto)
        self.formulario.destroy()
        
        
    
    def cancelar_formulario(self) -> None:
        self.formulario.destroy()

    def mostrar_datos_tabla(self, producto: Producto) -> None:
        self.tabla.insert("", "end", values=producto.tupla_datos())