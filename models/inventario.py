from .producto import Producto
from typing import List

class Inventario:

    def __init__(self) -> None:
        """
        Metodo inicializador de la clase Inventario, inicia con una lista vacia
        de tipo Producto
        Atributos de instancia:
            -_productos (List[Producto]): lista de objetos de tipo Producto
        """
        self._productos: List[Producto] = []

    def agregar_producto(self, producto:Producto) -> None:
        """
        Metodo de clase que recibe como argumento un objeto de tipo producto
        y lo agrega a la lista
        Parametros:
            -producto (Producto): objeto de tipo producto
        """
        if isinstance(producto, Producto):
            self._productos.append(producto)
        else:
            raise ValueError("El argumento no es valido")