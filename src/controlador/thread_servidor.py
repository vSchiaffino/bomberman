import threading
import pickle
from pydispatch import dispatcher

class Thread_servidor(threading.Thread):
    def __init__(self, daemon, em):
        super().__init__(daemon=daemon)
        self.em = em
        threading.Thread.__init__(self)
        self.cola_de_eventos = []
        dispatcher.connect(self.recibir_evento, signal='xd')

    def recibir_evento(self, evento):
        self.cola_de_eventos.append(evento)    

    def run(self):
        while True:
            for evento in self.cola_de_eventos:
                self.em.post(evento)
                self.cola_de_eventos.remove(evento)