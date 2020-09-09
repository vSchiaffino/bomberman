import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from visible import Visible
from contenido import Contenido

class Objeto(Visible, Contenido):
    def __init__(self, pos):
        super().__init__(pos)
    
    def set_em(self, em):
        self.em = em
    
    
