class Event():
    """
    Evento genérico.
    """
    def __init__(self):
        self.nombre = "Evento genérico"


class Sec_event(Event):
    """
    Evento que sirve para avisar del paso de un segundo
    en el programa.
    Listeners: Mapa
    Triggerers: Controlador.
    """
    def __init__(self):
        self.nombre = "sec_event"


class No_more_time_event(Event):
    """
    Evento que sirve para avisar que el personaje se quedo sin
    tiempo.
    Listeners: Personaje
    Triggerers: Mapa
    """
    def __init__(self):
        self.nombre = "no_more_time_event"


class Defeat_event(Event):
    """
    Evento que sirve para señalizar la derrota del jugador.
    Listeners: Controlador.
    Triggerers: Jugador.
    """
    def __init__(self):
        self.nombre = "defeat_event"


class Tick_event(Event):
    """
    Evento que señaliza que paso un bucle del juego. Transporta
    a su vez, el tiempo estimado que tardó.
    Listeners: Vista, bombas, enemigos, explosiones
    Triggerers: Controlador
    """
    def __init__(self, tiempo):
        self.nombre = "tick_event"
        self.tiempo = tiempo


class Input_move_event(Event):
    """
    Evento que señaliza que el usuario intento moverse. Contiene
    la dirección tentativa.
    Listeners: Personaje.
    Triggerers: Controlador.
    """
    def __init__(self, direccion, player):
        self.nombre = "input_move_event"
        self.direccion = direccion
        self.player = player


class Try_move_event(Event):
    """
    Evento que señaliza el intento de movimiento personaje. Contiene
    la posición tentativa.
    Listeners: Mapa.
    Triggerers: Personaje.
    """
    def __init__(self, pos, celda_anterior, caminador, player):
        self.nombre = "try_move_event"
        self.pos = pos
        self.caminador = caminador
        self.celda_anterior = celda_anterior
        self.player = player


class Move_event(Event):
    """
    Evento que señaliza el correcto movimiento del personaje. Contiene
    la celda nueva y la posición.
    Listeners: Personaje.
    Triggerers: Mapa.
    """
    def __init__(self, celda, pos, player):
        self.nombre = "move_event"
        self.celda = celda
        self.pos = pos
        self.player = player


class Eliminar_contenido(Event):
    """
    Evento que señaliza la eliminación de un contenido de
    una celda, el encargado es el mapa.
    Listeners: Mapa
    Triggerers: Personaje, Bomba
    """
    def __init__(self, contenido, celda):
        self.nombre = "eliminar_contenido"
        self.contenido = contenido
        self.celda = celda


class Agregar_contenido(Event):
    """
    Evento que señaliza la agregación de un contenido a
    una celda. El encargado es el mapa.
    Listeners: Mapa.
    Triggerers: Pared_rompible
    """
    def __init__(self):
        self.nombre = "agregar_contenido"


class Input_poner_bomba(Event):
    """
    Evento que señaliza que el usuario intento poner una bomba.
    Listeners: Personaje
    Triggerer: Controlador
    """
    def __init__(self, player):
        self.nombre = "input_poner_bomba"
        self.player = player


class Poner_bomba(Event):
    """
    Evento que señaliza cuando el personaje, le pide al mapa
    poner una bomba, esto puede ser realizado como no, dependiendo
    de lo que el mapa decida.
    Listeners: Mapa
    Triggerer: Personaje
    """
    def __init__(self, celda, bomba, n_bombas):
        self.nombre = "poner_bomba"
        self.celda = celda
        self.bomba = bomba
        self.n_bombas = n_bombas


class Bomba_exploto(Event):
    """
    Evento que señaliza cuando la bomba explota.
    Listeners: Mapa
    Triggerer: Bomba
    """
    def __init__(self, bomba, celda, nivel_exp):
        self.nombre = "bomba_exploto"
        self.bomba = bomba
        self.celda = celda
        self.nivel_exp = nivel_exp


class Personaje_murio_event(Event):
    """
    Evento que señaliza cuando un personaje muere.
    Listeners: Mapa, controlador
    Triggerer: Personaje
    """
    def __init__(self):
        self.nombre = "personaje_murio"


class Se_rompio_pared(Event):
    """
    Evento que avisa cuando se rompe una pared.
    Sirve para agregar score.
    Listeners: Mapa
    Triggerers: celdas
    """
    def __init__(self):
        self.nombre = "se_rompio_pared"


class Win_event(Event):
    """
    Evento que avisa cuando el jugador gana.
    Listener: Controlador
    Triggerer: Salida
    """
    def __init__(self):
        self.nombre = "win_event"