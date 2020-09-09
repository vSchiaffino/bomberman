import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), 'contenidos/'))
from obstaculo_movil import Obstaculo_movil
from random import randint

class Enemigo(Obstaculo_movil):
    """
    Clase que representa a los enemigos del juego.
    """
    def __init__(self, celda_inicial, mapa):
        super().__init__(celda_inicial, mapa)
        self.velocidad = 3
        self.lenght_index = 6
        celda_inicial.agregar_caminador(self)
        self.mov = (1, 0)
        self.tengo_que_cambiar = False
        self.ya_cambie = False
        self.ultima_celda_de_decision = self.celda_actual
        self.ultima_pos = self.pos

    def tick(self):
        """
        El enemigo se actualiza la posición, la dirección a la que va,
        etc.
        Devuelve None.
        """
        if self.ultima_pos == self.pos:
            self.tengo_que_cambiar = True
        if self.tengo_que_cambiar:
            self.cambiar_mov()
            self.tengo_que_cambiar = False
        proxima_celda = self.mapa.get_celda(self.celda_actual.fila + self.mov[1], self.celda_actual.columna + self.mov[0])
        if proxima_celda.comprobar_mov():
            self.mover_por_mov()
        else:
            self.invertir_mov()
        # if self.estoy_en_celda_de_decision() and not self.ya_cambie:
        #     self.tengo_que_cambiar = self.random(30)
        #     self.ya_cambie = True
        self.ultima_pos = self.pos

    def estoy_en_celda_de_decision(self):
        """
        Función que devuelve :
           True: si esta en una celda de decisión
           False: caso contrario.
        Llamamos "celda de decisión" a las celdas que, 
        sus celdas adyacentes no tienen obstaculos no
        rompibles.
        """
        fila = self.celda_actual.fila
        columna = self.celda_actual.columna
        return ((fila + columna) % 2 ) == 0

    def mover_por_mov(self):
        """
        Función que traduce el mov en formato (movx, movy)
        a formato de función de movimiento del obstaculo
        móvil.
        Ejemplo: Si recibe (1, 0) -> mueve derecha
        Devuelve None
        """
        dicc = {(1, 0) : self.mover_derecha,
                (-1, 0) : self.mover_izquierda,
                (0, 1) : self.mover_abajo,
                (0, -1) : self.mover_arriba}
        dicc[self.mov]()

    def invertir_mov(self):
        """
        Función que hace que el movimiento del enemigo sea
        contrario al que esta yendo.
        Ejemplo: si recibe (1, 0) -> (-1, 0)
                         (derecha)->(izquierda)
        Devuelve None
        """
        change_movs = {(1, 0) : (-1, 0),
                       (-1, 0) : (1, 0),
                       (0, 1) : (0, -1),
                       (0, -1) : (0, 1)}
        self.mov = change_movs[self.mov]
    
    def cambiar_mov(self):
        """
        Función que elige si cambiar o no el movimiento de forma aleatoria,
        y si lo cambia también lo convierte en un movimiento random.
        Devuelve None
        """
        # if not self.ultima_celda_de_decision == self.celda_actual:
        if self.random(20):
            if self.mov == (0, 1) or self.mov == (0, -1):
                # cambio a x
                if self.random(50):
                    self.mov = (1, 0)
                else:
                    self.mov = (-1, 0)
            else:
                # cambio a y
                if self.random(50):
                    self.mov = (0, 1)
                else:
                    self.mov = (0, -1)

    def random(self, probabilidades):
        """
        Función de aleatoriedad.
        Devuelve True o False
        """
        if randint(1, 100) <= probabilidades:
            return True
        return False
    
    def ser_caminado(self, caminador):
        pass

    def morir(self):
        """
        Función que se llama cuando un enemigo muere.
        """
        self.mapa.murio_enemigo()
        self.celda_actual.eliminar_contenido(self)
        self.mapa.liberar_enemigo(self)
    
    def entraste_a_mi(self, celda):
        """
        Función que se utiliza cuando un enemigo entra a una celda.
        Y es para poder saber si el enemigo tiene que cambiar o no el mov.
        """
        if self.celda_actual != celda:
            self.celda_actual = celda
            if self.estoy_en_celda_de_decision():
                self.tengo_que_cambiar = True

    def notify(self, evento):
        if evento.nombre == "tick_event":
            self.tick()
