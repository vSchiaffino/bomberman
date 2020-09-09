from objeto import Objeto
from event_manager.eventos import Bomba_exploto, Eliminar_contenido
import sys
import os


class Bomba(Objeto):
    def __init__(self, em, nivel_explosion, delay, mapa, celda):
        super().__init__(celda.get_middle_pos())
        self.nivel_explosion = nivel_explosion
        self.celda = celda
        self.mapa = mapa
        self.ruta = "bomb"
        self.em = em
        self.index = 0
        self.msActual = 0
        self.dejo = True
        self.segundos = delay
    
    def explotar(self):
        self.em.post(Eliminar_contenido(self, self.celda))
        self.em.post(Bomba_exploto(self, self.celda, self.nivel_explosion))

    def ser_explotado(self):
        self.explotar()

    def comprobar_mov(self):
        return self.dejo
    
    def personaje_entro_a_celda(self):
        self.dejo = False
    
    def paso_seg(self):
        self.segundos -= 1
        self.index += 1
        if self.segundos == 0:
            self.explotar()
            self.ruta = ""
            return True
        return False
    
    def tick(self, time):
        if self.msActual >= 1000:
            self.paso_seg()
            self.msActual = 0
        else:
            self.msActual += time

    def sos_bomba(self):
        return True

    def notify(self, evento):
        if evento.nombre == "tick_event":
            self.tick(evento.tiempo)


        