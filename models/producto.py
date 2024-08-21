class Producto:

    contador:int = 0 # Atributo de clase que simula un id para cada instancia
    
    def __init__(self, producto:str = None, precio:float = None, stock:int = None, descripcion:str = None) -> None:
        """
        Metodo constructor de la clase Producto.
        Argumentos:
            -producto (str): nombre del producto.
            -precio (float): precio del producto.
            -stock (int): cantidad del producto en stock.
            -descripcion (str): descripcion del producto.
        Atributos de clase:
            -codigo (int): codigo del producto generado al instanciar
        Atributos de instancia:
            -codigo (int): codigo unico del objeto instanciado
            -producto (str): nombre del producto.
            -precio (float): precio del producto.
            -stock (int): cantidad del producto en stock.
            -descripcion (str): descripcion del producto.
        """
        Producto.contador += 1
        self._codigo = Producto.contador 
        self._producto = producto
        self._precio = precio
        self._stock = stock
        self._descripcion = descripcion
    
    @property
    def codigo(self) -> int:
        return self._codigo
    
    @property
    def producto(self) -> str:
        return self._producto
    
    @producto.setter
    def producto(self, producto: str) -> None:
        if isinstance(producto, str):
            self._producto = producto
        else:
            raise ValueError("Valor del campo producto es incorrecto")

    @property
    def precio(self) -> float:
        return self._precio
    
    @precio.setter
    def precio(self, precio:float) -> None:
        if isinstance(precio, float):
            self._precio = precio
        else:
            raise ValueError("Valor del campo precio es incorrecto")
        
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, stock: int) -> None:
        if isinstance(stock, int):
            self._stock = stock
        else:
            raise ValueError("Valor del campo stock es incorrecto")