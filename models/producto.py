class Producto:

    codigo:int = 0 # Atributo de clase que simula un id para cada instancia

    def __init__(self, producto:str = None, precio:float = None, stock:int = None, descripcion:str = None) -> None:
        """
        Metodo constructor de la clase Producto.
        Argumentos:
            -producto (str): nombre del producto.
            -precio(float): precio del producto.
            -stock(int): cantidad del producto en stock.
            -descripcion(str): descripcion del producto.
        Atributos de clase:
            -codigo(int): codigo del producto generado al instanciar
        Atributos de instancia:
            -codigo(int): codigo unico del objeto instanciado
            -producto (str): nombre del producto.
            -precio(float): precio del producto.
            -stock(int): cantidad del producto en stock.
            -descripcion(str): descripcion del producto.
        """
        self._codigo_autoincremental() # llamado de la funcion
        self._codigo = Producto.codigo # asignacion del codigo unico para el objeto
        self._producto = producto # asignacion del atributo de instancia del nombre del producto
        self._precio = precio # asignancion del atributo de instancia precio
        self._stock = stock # asignancion del atributo de instancia stock
        

    def _codigo_autoincremental(self) ->None:
        """
        Metodo de clase que incrementa en uno el atributo de clase con cada
        instancia creada de la clase Producto.
        """
        Producto.codigo += 1
