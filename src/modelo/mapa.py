from modelo.celda import Celda
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'contenidos'))
from contenido_dummy import Contenido_dummy
from pared_no_rompible import Pared_no_rompible
from pared_rompible import Pared_rompible
from explosion import Explosion
from modelo.enemigo import Enemigo
from modelo.contenidos.power_up.speed_up import Speed_up
from modelo.contenidos.power_up.flame_up import Flame_up
from modelo.contenidos.power_up.bomb_up import Bomb_up
from modelo.contenidos.salida import Salida
from event_manager.eventos import Move_event, No_more_time_event
import pickle as pickle

class Mapa:
    def __init__(self):
        """
        Esto no se usa, pero es lo que se usaba en su momento antes de usar pickle
        para iniciar el mapa.
        """
        # Aca lee el mapa y crea todas las celdas.
        # pos_enemigos = [(6, 2), (8, 2), (4, 2)]
        # pos_enemigos = [(3, 11), (4, 5), (9, 7), (9, 11), (13, 9)]
        # self.explosiones = []
        # self.score = 0
        # self.time = 120
        # self.timeTotal = 120
        # alto = 15
        # largo = 15
        # self.ppc = 45
        # self.a__init__(alto, largo)
        # self.bombas = []
        # # Creo los enemigos
        # # Aca lee donde está cada enemigo y los crea.
        # self.lista_de_enemigos = []
        # for pos_enemigo in pos_enemigos:
        #     celda_ocupada = self.get_celda(pos_enemigo[0], pos_enemigo[1])
        #     self.lista_de_enemigos.append(Enemigo(celda_ocupada, self))


        with open("mapa_ex", "rb") as file:
            self = pickle.load(file)

    def get_tiempo_restante(self):
        """
        El mapa devuelve el tiempo restante en el formato correcto.
        Devuelve: Un string con el tiempo.
        """
        min = 0
        min = self.time // 60
        sec = self.time - (min * 60)
        min = str(min)
        sec = str(sec)
        if len(min) == 1: min = "0" + min
        if len(sec) == 1: sec = "0" + sec
        return min + ":" + sec

    def reset_tiempo(self):
        """
        Setea el tiempo en su tiempo default.
        Devuelve None
        """
        self.time = self.timeTotal

    def get_lista_enemigos(self):
        return self.lista_de_enemigos

    def get_lista_explosiones(self):
        return self.explosiones

    def a__init__(self, alto, largo):
        """
        Esto no se usa, pero es lo que se usaba en su momento antes de usar pickle
        para iniciar el mapa.
        """
        self.alto = alto
        self.largo = largo
        self.celdas = []
        for _ in range (0,self.alto):
            self.celdas.append([])
        # Primer fila
        for i in range(1, self.largo + 1):
            contenido = Pared_no_rompible()
            self.celdas[0].append(Celda(contenido, 1, i, self.ppc))
        # filas del medio
        for i in range(2, self.alto):
            contenido = Pared_no_rompible()
            self.celdas[i - 1].append(Celda(contenido, i, 1, self.ppc))
            for j in range(2, self.largo):
                if(i % 2 == 0):
                    # Dummy
                    contenido = Contenido_dummy()
                    self.celdas[i - 1].append(Celda(contenido, i, j, self.ppc))
                else:
                    # Paredes
                    if(j % 2 == 0):
                        contenido = Contenido_dummy()
                    else:
                        contenido = Pared_no_rompible()
                    self.celdas[i - 1].append(Celda(contenido, i, j, self.ppc))
            contenido = Pared_no_rompible()
            self.celdas[i - 1].append(Celda(contenido, i, self.largo, self.ppc))
        # Ultima fila
        for i in range(1, self.largo + 1):
            contenido = Pared_no_rompible()
            self.celdas[self.alto - 1].append(Celda(contenido, self.largo, i, self.ppc))
        total = 0
        # Paredes rompibles
        # fila 1
        filas = {
            2 : range(4, 15),
            3 : (4, 6, 8, 10, 14),
            4 : (2, 3, 5, 8, 9, 10, 11, 14),
            5 : (2, 8, 14),
            6 : (8, 9, 10, 14),
            7 : (2, 4, 6, 8, 10, 14),
            8 : range(2, 15),
            9 : (2, 4, 6, 8, 10, 14),
            10 : (2, 3, 4, 5, 6, 10, 14),
            11 : (2, 4, 6, 10, 14),
            12 : (2, 3, 4, 6, 10, 11, 13, 14),
            13 : (2, 4, 6, 10, 14),
            14 : (2, 3, 4, 5, 6, 10, 11, 12, 13, 14)
        }
        especiales = {
            (2, 13) : Bomb_up(),
            (12, 2) : Speed_up(),
            (13, 14) : Salida()
        }
        for fila in range(2, self.alto):
            for columna in filas[fila]:
                if (fila, columna) in especiales:
                    contenido_del_contenido = especiales[(fila, columna)]
                else:
                    contenido_del_contenido = Contenido_dummy()
                contenido = Pared_rompible(contenido_del_contenido)
                self.agregar_contenido(fila, columna, contenido)
        
        
        print(total)

    def agregar_contenido(self, fila, columna, contenido):
        """
        Agrega un contenido a una celda.
        Devuelve None
        """
        self.get_celda(fila, columna).agregar_contenido(contenido)

    def limpiar_explosiones_y_bombas(self):
        """
        Limpia las explosiones y las bombas del mapa.Para que
        cuando el player se muera, si la explosión esta en la celda
        default del personaje, no se vuelva a morir.
        Devuelve None
        """
        self.bombas.clear()
        self.explosiones.clear()
    
    def avisar_mov(self, pos, celda_anterior, caminador):
        """
        Función que utilizan los obstáculos móviles para moverse.
        Devuelve la celda caminada.
        """
        celda_caminada = self.get_celda_desde_posicion(pos)
        if celda_anterior != celda_caminada:
            celda_caminada.agregar_caminador(caminador)
            celda_anterior.eliminar_contenido(caminador)
            celda_caminada.personaje_entro_a_celda()
        celda_caminada.ser_caminado(caminador)
        return celda_caminada

    def poner_bomba(self, bomba, celda):
        """
        Función que utilizan los personajes para poner bombas.
        Devuelve None
        """
        celda.poner_bomba(bomba)
        self.agregar_bomba(bomba)

    def cuantas_bombas_puedo_poner(self, n):
        """
        Función que utilizan los personajes para saber,
        mediante las bombas que ya tienen puestas, cuantas bombas
        pueden poner.
        Devuelve un int
        """
        return n - len(self.bombas)

    def puedo_poner_bomba(self, n_bombas, celda):
        """
        Función que se utiliza para saber si se puede poner una bomba
        en una celda determinada.
        Devuelve None
        """
        return not (len(self.bombas) >= n_bombas or celda.puedo_poner_bomba())

    def bomba_explotar(self, bomba, celda, nivel_explosion):
        """
        Función que utilizan las bombas para esparcir sus explosiones
        por el mapa.
        Devuelve None
        """
        self.liberar_bomba(bomba)
        movs =  [(0, 1), (-1, 0), (0, -1), (1, 0)]
        nivel_exp_actual = nivel_explosion
        explosion = Explosion(self.em, celda, self)
        self.explosiones.append(explosion)
        for mov in movs:
            nivel_exp_actual = nivel_explosion
            celda_actual = celda
            bloque = False
            while nivel_exp_actual != 0 and not bloque:
                celda_tentativa = self.get_celda(celda_actual.fila + mov[0], celda_actual.columna + mov[1])
                if celda_tentativa.comprobar_mov():
                    # Se genere explosion
                    explosion = Explosion(self.em, celda_tentativa, self)
                    self.explosiones.append(explosion)
                    celda_actual = celda_tentativa
                else:
                    # Se explote pero no se genere
                    celda_tentativa.ser_explotado()
                    bloque = True
                nivel_exp_actual -= 1

    def get_score(self):
        return self.score

    def paso_segundo(self):
        self.time -= 1
        if self.time == 0:
            self.reset_tiempo()
            self.em.post(No_more_time_event())

    def set_em(self, em):
        """
        Función que sirve para que el mapa conozca al Event Manager.
        Devuelve None
        """
        self.em = em
        for fila in self.celdas:
            for celda in fila:
                celda.set_em(em)
        for enemigo in self.lista_de_enemigos:
            enemigo.set_em(em)

    def get_enemigos(self):
        return self.lista_de_enemigos

    def get_bombas(self):
        return self.bombas

    def get_explosiones(self):
        return self.explosiones

    def murio_enemigo(self):
        """
        Actualiza el score.
        Devuelve None
        """
        self.score += 100

    def rompio_pared(self):
        """
        Actualiza el score.
        Devuelve None
        """
        self.score += 20

    def liberar_enemigo(self, enemigo):
        """
        Elimina a un enemigo de la lista de enemigos.
        Devuelve None
        """
        self.lista_de_enemigos.remove(enemigo)
 
    def liberar_explosion(self, explosion):
        """
        Elimina un explosión de la lista de explosiones.
        Devuelve None
        """
        if explosion in self.explosiones:
            self.explosiones.remove(explosion)

    def liberar_bomba(self, bomba):
        """
        Elimina a una bomba de la lista de bombas.
        Devuelve None
        """
        if bomba in self.bombas:
            self.bombas.remove(bomba)

    def agregar_bomba(self, bomba):
        """
        Agrega una nueva bomba a la lista de bombas.
        Devuelve None        
        """
        self.bombas.append(bomba)

    def get_celda_desde_posicion(self, pos):
        """
        Dada una cierta posición, devuelve la celda que
        se encuentra ahi.
        Devuelve un objeto de tipo celda.
        """
        fila = (pos[1] // self.ppc) + 1
        columna = (pos[0] // self.ppc) + 1
        return self.get_celda(fila, columna)
    
    def get_celda(self, fila, columna):
        return self.celdas[int(fila-1)][int(columna-1)]

    def comprobar_mov(self, pos):
        """
        Dada una posición, devuelve una tupla  con True o False
        que indica si es caminable o no y la celda tentativa.
        """
        celda_tentativa = self.get_celda_desde_posicion(pos)
        return (celda_tentativa.comprobar_mov(), celda_tentativa)

    def get_all_celdas(self):
        return self.celdas

    def notify(self, evento):
        if evento.nombre == "poner_bomba":
            if self.puedo_poner_bomba(evento.n_bombas, evento.celda):
                self.poner_bomba(evento.bomba, evento.celda)
        elif evento.nombre == "try_move_event":
            comprobacion = self.comprobar_mov(evento.pos)
            if comprobacion[0] or evento.caminador.vuelo:
                celda_nueva = self.avisar_mov(evento.pos, evento.celda_anterior, evento.caminador)
                self.em.post(Move_event(celda_nueva, evento.pos, evento.player))
        elif evento.nombre == "bomba_exploto":
            self.bomba_explotar(evento.bomba, evento.celda, evento.nivel_exp)
        elif evento.nombre == "eliminar_contenido":
            evento.celda.eliminar_contenido(evento.contenido)
        elif evento.nombre == "personaje_murio":
            self.reset_tiempo()
            self.limpiar_explosiones_y_bombas()
        elif evento.nombre == "sec_event":
            self.paso_segundo()
        elif evento.nombre == "se_rompio_pared":
            self.rompio_pared()

