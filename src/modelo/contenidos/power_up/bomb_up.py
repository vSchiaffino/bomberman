from modelo.contenidos.power_up.power_up import Power_up


class Bomb_up(Power_up):
    def __init__(self):
        self.ruta = "bu"
    
    def ser_caminado(self, caminador):
        caminador.bomb_up()
        return True