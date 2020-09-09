from objeto import Objeto

class Pared_no_rompible(Objeto):
    def __init__(self):
        self.ruta = "pnr"
    
    def comprobar_mov(self):
       return False