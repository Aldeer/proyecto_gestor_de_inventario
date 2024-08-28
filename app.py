from views.ventanaprincipal import VentanaPrincipal
from models.inventario import Inventario
from controllers.productocontroller import ProductoController

ventana = VentanaPrincipal()
modelo = Inventario()

controlador = ProductoController(modelo, ventana)
controlador.run()