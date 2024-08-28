from views.formulario import Formulario

class FormularioController:

    def __init__(self, formulario:Formulario) -> None:
        self.formulario = formulario
        self.formulario.guardar_btn.bind("<Button-1>", lambda e: self.comprobar_campos())
        self.formulario.cancela_btn.bind("<Button-1>", lambda e: self.cancelar_formulario())

    def comprobar_campos(self) -> None:
        producto = self.formulario.producto.get()
        precio = self.formulario.precio.get()
        stock = self.formulario.stock.get()

        if not producto:
            print("Campo producto vacio")
        if not precio:
            print("Campo precio vacio")
        if not stock:
            print("Campo stock vacio")
    
    def cancelar_formulario(self) -> None:
        self.formulario.destroy()