class Event_manager():
    """
    Clase que se encarga de la comunicación entre los
    objetos del modelo.
    """
    def __init__(self, vista, game, controlador):
        self.actualizar_listeners(vista, game, controlador)

    def actualizar_listeners(self, vista, game, controlador):
        """
        Setea los listeners que son necesarios para que
        el modelo funcione.
        """
        mapa = game.get_mapa()
        personaje = game.get_personaje()
        explosiones = game.get_explosiones()
        bombas = game.get_bombas()
        enemigos = game.get_enemigos()
        self.listeners = {
            "tick_event" : [vista, bombas, enemigos, explosiones],
            "sec_event" : [mapa],
            "no_more_time_event" : [personaje],
            "input_move_event" : [personaje],
            "try_move_event" : [mapa],
            "move_event" : [personaje],
            "input_poner_bomba" : [personaje],
            "poner_bomba" : [mapa],
            "bomba_exploto" : [mapa, vista],
            "eliminar_contenido" : [mapa],
            "agregar_contenido" : [mapa],
            "personaje_murio" : [mapa, controlador],
            "defeat_event" : [controlador, vista],
            "se_rompio_pared" : [mapa],
            "se_mato_enemigo" : [mapa, vista],
            "win_event" : [controlador, vista]
        }
    
    def post(self, evento):
        """
        Función que sirve para que los objetos avisen
        de eventos que ocurren en el juego.
        """
        for listener in self.listeners[evento.nombre]:
            if isinstance(listener, list):
                for item in listener:
                    item.notify(evento)
            else:
                listener.notify(evento)