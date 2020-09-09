class Event_manager():
    def __init__(self, game):
        self.actualizar_listeners(game)

    def actualizar_listeners(self, game):
        mapa = game.get_mapa()
        personaje = game.get_personaje()
        explosiones = game.get_explosiones()
        bombas = game.get_bombas()
        enemigos = game.get_enemigos()
        self.listeners = {
            "tick_event" : [bombas, enemigos, explosiones],
            "sec_event" : [mapa],
            "no_more_time_event" : [personaje],
            "input_move_event" : [personaje],
            "try_move_event" : [mapa],
            "move_event" : [personaje],
            "input_poner_bomba" : [personaje],
            "poner_bomba" : [mapa],
            "bomba_exploto" : [mapa],
            "eliminar_contenido" : [mapa],
            "agregar_contenido" : [mapa],
            "personaje_murio" : [mapa],
            "defeat_event" : [],
            "se_rompio_pared" : [mapa],
            "se_mato_enemigo" : [mapa],
            "win_event" : []
        }
    
    def post(self, evento):
        for listener in self.listeners[evento.nombre]:
            if isinstance(listener, list):
                for item in listener:
                    item.notify(evento)
            else:
                listener.notify(evento)