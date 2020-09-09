import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from objeto import Objeto

class Contenido_dummy(Objeto):
    def __init__(self):
        self.ruta = "dummy"        
    
    def comprobar_mov(self):
        return True