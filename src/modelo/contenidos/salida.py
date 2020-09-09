from objeto import Objeto
from event_manager.eventos import Win_event


class Salida(Objeto):
    def __init__(self):
        self.ruta = "salida"

    def comprobar_mov(self):
        return True

    def ser_caminado(self, caminador):
        if caminador._sos_personaje():
            self.em.post(Win_event())
        