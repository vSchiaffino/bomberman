import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
import pickle
from enemigo import Enemigo
from contenidos.power_up.speed_up import Speed_up
from contenidos.power_up.flame_up import Flame_up
from contenidos.power_up.bomb_up import Bomb_up
from celda import Celda
sys.path.append(os.path.join(os.path.dirname(__file__), '../contenidos/'))
from contenido_dummy import Contenido_dummy
from pared_no_rompible import Pared_no_rompible
from pared_rompible import Pared_rompible
from explosion import Explosion
# ------------------------------------- 
#   0 = dummy
#   1 = obstáculo
#   2 = personaje
# -------------------------------------
pos_f = (0, 0)
class Grafo():
    def __init__(self, mapa = None):
        file = open("mapa_ex", "r+b")
        mapa = pickle.load(file)
        self.celdas = []
        i = 0
        for fila in mapa.celdas:
            j = 0
            self.celdas.append([])
            for celda in fila:
                # me fijo que tipo de celda es
                celda_de_mapa = mapa.get_celda(i + 1, j + 1)
                if celda_de_mapa._sos_personaje():
                    cosa = 2
                else:
                    if celda_de_mapa.comprobar_mov():
                        cosa = 0
                    else:
                        cosa = 1
                self.celdas[i].append(cosa)
                j += 1
            i += 1
        self.cambiar_celda(2, 2, 2)
    
    def __str__(self):
        salida = ""
        for fila in self.celdas:
            for celda in fila:
                if celda == 0:
                    salida += "  .  "
                if celda == 1:
                    salida += "  #  "
                if celda == 2:
                    salida += "  P  "
            salida += "\n"
        return salida
    
    def cambiar_celda(self, f, c, dato):
        self.celdas[f - 1][c - 1] = dato


grafo = Grafo()

print(grafo)