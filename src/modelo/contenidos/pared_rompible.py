from objeto import Objeto
from event_manager.eventos import Se_rompio_pared

class Pared_rompible(Objeto):
    def __init__(self, contenido):
        self.ruta = "pr"
        self.contenido = contenido
    
    def ser_explotado(self):
        self.em.post(Se_rompio_pared())
        return self.contenido


    def comprobar_mov(self):
        return False

    def set_em(self, em):
        self.em = em
        self.contenido.set_em(em)
        