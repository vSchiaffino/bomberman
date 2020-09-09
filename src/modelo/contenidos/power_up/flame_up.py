from modelo.contenidos.power_up.power_up import Power_up


class Flame_up(Power_up):
    def __init__(self):
        self.ruta = "fu"
    
    def ser_caminado(self, caminador):
        caminador.flame_up()
        return True