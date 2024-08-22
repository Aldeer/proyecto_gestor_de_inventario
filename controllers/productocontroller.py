from models.inventario import Inventario
from views.ventanaprincipal import VentanaPrincipal

class ProductoController:

    def __init__(self, inventario: Inventario, vista: VentanaPrincipal) -> None:
        self.inventario = inventario
        self.vista = vista

        
