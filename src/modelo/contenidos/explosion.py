from objeto import Objeto
class Explosion(Objeto):
    def __init__(self, em, celda, mapa):
        super().__init__(celda.get_middle_pos())
        self.celda = celda
        self.ruta = "explosion"
        self.index = 0
        self.delayMs = 1000
        self.msActual = 0
        self.em = em
        self.mapa = mapa
    
    def tick(self, time):
        self.celda.ser_explotado()
        self.msActual += time
        if self.msActual % (self.delayMs // 5) == 0:
            self.sumIndex()
        if self.msActual >= self.delayMs:
            self.mapa.liberar_explosion(self)
    
    def sumIndex(self):
        if self.index == 4:
            self.index = 0
        else:
            self.index += 1

    def notify(self, evento):
        if evento.nombre == "tick_event":
            self.tick(evento.tiempo)
            
