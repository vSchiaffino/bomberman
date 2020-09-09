from modelo.contenidos.obstaculo_movil import Obstaculo_movil
from modelo.contenidos.bomba import Bomba
from event_manager.eventos import Poner_bomba, Try_move_event, Eliminar_contenido, Personaje_murio_event, Defeat_event

class Personaje(Obstaculo_movil):
    """
    Clase que referencia al bomberman.
    """
    def __init__(self, celda_inicial, mapa, player):
        super().__init__(celda_inicial, mapa)
        self.default_pos = self.pos
        self.velocidad = 5
        self.vidas = 3
        self.delay_bomba = 3
        self.nivel_explosion = 1  
        self.lenght_index= 8
        self.n_bombas = 1
        self.player = player
    
    def perder_vida(self):
        self.vidas -= 1

    def set_default_pos(self, pos):
        self.default_pos = pos

    def get_vidas(self):
        return self.vidas

    def get_direccion(self):
        return self.direccion

    def get_index_img(self):
        return self.img_index

    def get_bombas_posibles(self):
        return self.mapa.cuantas_bombas_puedo_poner(self.n_bombas)

    def poner_bomba(self):
        """
        Pone una bomba, este mensaje puede ser ignorado por el mapa, 
        en el caso de que se exceda el limite de bombas.
        Devuelve None        
        """
        self.em.post(Poner_bomba(self.celda_actual, Bomba(self.em, self.nivel_explosion, self.delay_bomba, self.mapa, self.celda_actual), self.n_bombas))
    
    def _set_celda_actual(self, celda_actual):
        self.celda_actual = celda_actual
    
    def _get_celda_actual(self, celda_actual):
        return self.celda_actual
    
    def ser_caminado(self, caminador):
        if not caminador._sos_personaje():
            self.morir()
        return False
    
    def speed_up(self):
        """
        Función que utilizan los power_up
        """
        self.velocidad += 2
    
    def bomb_up(self):
        """
        Función que utilizan los power_up
        """
        self.n_bombas += 1

    def flame_up(self):
        """
        Función que utilizan los power_up
        """
        self.nivel_explosion += 1

    def fly(self):
        """
        Funcion de debug.
        """
        self.vuelo = True

    def _sos_personaje(self):
        return True
    
    def morir(self):
        """
        Función que se utiliza para la muerte del personaje.
        """
        print("MORISTE WN")
        self.vidas -= 1
        self.em.post(Try_move_event(self.default_pos, self.celda_actual, self, self.player))
        if self.vidas == 0:
            evento = Defeat_event()
        else:
            evento = Personaje_murio_event()
        self.em.post(evento)
    
    def ser_explotado(self):
        self.morir() 

    def notify(self, evento):
        if evento.nombre == "no_more_time_event":
            self.morir()
        elif evento.player == self.player:
            if evento.nombre == "input_poner_bomba":
                self.poner_bomba() 
            elif evento.nombre == "input_move_event":
                self.direccion = evento.direccion
                self.em.post(Try_move_event(self.mover(evento.direccion), self.celda_actual, self, self.player))
            elif evento.nombre == "move_event":
                self._set_pos(evento.pos)
                self._cambiar_index(self.direccion)
                self.celda_actual = evento.celda