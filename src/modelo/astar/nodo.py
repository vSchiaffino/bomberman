

class Nodo():
    def __init__(self, pos = [0, 0], padre = None, pos_f):
        self.pos = pos
        self.padre = padre
        self.h = distancia(self.pos, pos_f)