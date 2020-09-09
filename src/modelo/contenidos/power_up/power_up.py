import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from contenido import Contenido

class Power_up(Contenido):
    def __init__(self):
        self.ruta = ""

    def ser_explotado(self):
        return False

    def ser_caminado(self):
        return True
    def comprobar_mov(self):
        return True
    
    