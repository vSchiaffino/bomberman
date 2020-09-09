import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../'))
from modelo.contenidos.power_up.power_up import Power_up


class Speed_up(Power_up):
    def __init__(self):
        self.ruta = "su"
    
    def ser_caminado(self, caminador):
        caminador.speed_up()
        return True