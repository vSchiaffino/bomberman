class Contenido():
    def ser_caminado(self, caminador):
        return False
    
    def ser_explotado(self):
        return False

    def comprobar_mov(self):
        pass

    def get_ruta(self):
        return self.ruta
    
    def personaje_entro_a_celda(self):
        pass

    def sos_bomba(self):
        return False
    
    def _sos_personaje(self):
        return False
    
    def entraste_a_mi(self, celda):
        pass

    def set_em(self, em):
        self.em = em