from models.inventario import Inventario
from views.ventanaprincipal import VentanaPrincipal
from views.formulario import Formulario
from .formulariocontroller import FormularioController

class ProductoController:

    def __init__(self, inventario: Inventario, vista: VentanaPrincipal) -> None:
        self.inventario = inventario
        self.vista = vista

        self.vista.registrar_btn.bind("<Button-1>", lambda e: self.registrar_producto(e))

    def run(self) -> None:
        """
        Metodo del controlador que corre la aplicacion.
        """
        self.vista.mainloop()

    def registrar_producto(self, event) -> None:
        print(self.inventario.mostrar_inventario())
        formulario_controller = FormularioController(
            Formulario(self.vista),
            self.inventario,
            self.vista.tabla
            )

    def mostrar_lista_productos(self) -> None:
        pass

    def editar_producto(self) -> None:
        pass

    def eliminar_producto(self) -> None:
        pass