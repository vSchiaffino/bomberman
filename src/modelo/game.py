from modelo.mapa import Mapa
from modelo.personaje import Personaje
from modelo.input_controller import Input_controller
import pickle
from event_manager.eventos import Move_event, Try_move_event

class Game():
    """
    Clase principal del modelo.
    """
    def __init__(self, players):
        # Aca se supone que lee un archivo.
        self.players = players
        self.create_mapa()
        self.nivel = 1
        # Aca lee otro archivo
        player_conf = None
        self.ic = Input_controller(player_conf)
        # Aca lee donde esta parado el personaje.

    def ganaron_nivel(self):
        """
        Función que se ejecuta cuando un personaje gana el nivel.
        """
        self.nivel += 1
        self.set_mapa(1)

    def get_direccion_bm(self):
        lista = []
        for personaje in self.personajes:
            lista.append(personaje.get_direccion())
        return lista

    def get_index_bm(self):
        lista = []
        for personaje in self.personajes:
            lista.append(personaje.get_index_img())
        return lista

    def get_posicion_personaje(self):
        lista = []
        for personaje in self.personajes:
            lista.append(personaje.get_pos())
        return lista

    def create_mapa(self):
        """
        Función que crea el mapa.
        """
        with open("mapa_1", "rb") as file:
            self.mapa = pickle.load(file)
        posiciones = ((2, 2), (2, 3))
        self.personajes = []
        for i in range(1, self.players + 1):
            posicionPJ = posiciones[i - 1]
            fila_pj = posicionPJ[0]
            col_pj = posicionPJ[1]
            celda_pj = self.mapa.get_celda(fila_pj, col_pj)
            self.pj_def_pos = celda_pj.get_middle_pos()
            personaje = Personaje(celda_pj, self.mapa, i)
            self.personajes.append(personaje)
            celda_pj.agregar_caminador(personaje)

    def set_mapa(self, level):
        """
        Función que setea el mapa
        """
        with open("mapa_" + str(level), "rb") as file:
            self.mapa = pickle.load(file)
        self.posicionesPJ = {
            1 : ((2, 2), (2, 3))
        }
        posicionesPJ = self.posicionesPJ[level]
        for i in range(1, self.players + 1):
            personaje = self.personajes[i - 1]
            posicionPJ = posicionesPJ[i]
            fila_pj = posicionPJ[0]
            col_pj = posicionPJ[1]
            celda_pj = self.mapa.get_celda(fila_pj, col_pj)
            self.pj_def_pos = celda_pj.get_middle_pos()
            personaje.pos = celda_pj.get_middle_pos()
            personaje.celda_actual = celda_pj
            celda_pj.agregar_caminador(personaje)
            self.mapa.set_em(self.em)

    def set_em(self, em):
        """
        Función que sirve para que el game conozca al Event Manager.
        """
        self.em = em
        self.mapa.set_em(em)
        for personaje in self.personajes:
            personaje.set_em(em)

    def get_mapa(self):
        return self.mapa

    def get_personaje(self):
        return self.personajes

    def get_bombas(self):
        return self.mapa.get_bombas()
    
    def get_enemigos(self):
        return self.mapa.get_enemigos()

    def get_explosiones(self):
        return self.mapa.get_explosiones()

    def get_vidas_pj(self):
        return str(self.personajes[0].get_vidas())

    def get_score(self):
        return str(self.mapa.get_score())

    def get_bombas_posibles(self):
        return str(self.personajes[0].get_bombas_posibles())

    def get_tiempo_restante(self):
        return self.mapa.get_tiempo_restante()

    def get_explosiones(self):
        return self.mapa.get_lista_explosiones()

    def get_all_celdas(self):
        return self.mapa.get_all_celdas()

    def get_lista_enemigos(self):
        return self.mapa.get_lista_enemigos()
    
    def get_bombas(self):
        return self.mapa.get_bombas()

    def get_players(self):
        return self.players