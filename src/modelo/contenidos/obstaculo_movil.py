from visible import Visible
from contenido import Contenido
import sys

class Obstaculo_movil(Visible, Contenido):
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial.get_middle_pos())
        self.velocidad = 0
        self.celda_actual = celda_inicial
        self.mapa = mapa
        self.direccion = "abajo"
        self.img_index = 0
        self.lenght_index = 0
        self.vuelo = False
        self.ruta = ""

    def ser_explotado(self):
        self.morir()
        return False

    def get_direccion(self):
        return self.direccion        
    
    def get_posicion(self):
        return self.pos

    def mover_arriba(self):
        self._mover(0,-self.velocidad)
        self._cambiar_index("arriba")
        self.direccion = "arriba"
    
    def mover_derecha(self):
        self._mover(self.velocidad, 0)
        self._cambiar_index("derecha")
        self.direccion = "derecha"
    
    def mover_abajo(self):
        self._mover(0,self.velocidad)
        self._cambiar_index("abajo")
        self.direccion = "abajo"
    
    def mover_izquierda(self):
        self._mover(-self.velocidad, 0)
        self._cambiar_index("izquierda")
        self.direccion = "izquierda"
    
    def _cambiar_index(self, direccionLlamado):
        if self.direccion != direccionLlamado:
            self.img_index = 0
        else:
            if self.img_index == self.lenght_index - 1:
                self.img_index = 0
            else:
                self.img_index += 1
        self.direccion = direccionLlamado

    def morir(self):
        pass

    def comprobar_mov(self):
        return True
    
    def get_index_img(self):
        return self.img_index

    def _mover(self, mov_x, mov_y):
        pos_tentativa = (self._get_pos_x() + mov_x, self._get_pos_y() + mov_y)
        if self.mapa.comprobar_mov(pos_tentativa):
            self._set_pos(pos_tentativa)
            self.celda_actual = self.mapa.avisar_mov(self.pos, self.celda_actual, self)
    
    def mover(self, direccion):
        movs = {
            "izquierda" : (-self.velocidad, 0),
            "derecha" : (self.velocidad, 0),
            "abajo" : (0, self.velocidad),
            "arriba" : (0, -self.velocidad)
        }
        mov = movs[direccion]
        mov_x = mov[0]
        mov_y = mov[1]
        return (self._get_pos_x() + mov_x, self._get_pos_y() + mov_y)
    
    def cambiar_pos(self, pos):
        if self.mapa.comprobar_mov(pos):
            self._set_pos(pos)
            self.celda_actual = self.mapa.avisar_mov(self.pos, self.celda_actual, self)

    def speed_up(self):
        pass
    
    def bomb_up(self):
        pass

    def flame_up(self):
        pass