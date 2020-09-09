import sys
import os
import pickle
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from vista.vista_cliente import Vista
import pygame
from modelo.game import Game
from menu import Menu
from cliente import Cliente
from event_manager.event_manager import Event_manager
from event_manager.eventos import Input_move_event, Input_poner_bomba, Tick_event, Sec_event
from modelo.contenidos.pared_rompible import Pared_rompible
from modelo.contenidos.contenido_dummy import Contenido_dummy
# casa de valen v
# path = "C:/Users/valen/luna/luna/bomberman/"
# casa de facu
# path = "C:/Users/facun/Desktop/luna/bomberman/"
# huergo
# path = "C:/Users/huergo/Desktop/luna/bomberman/"
# huergo arriba
# path = "C:/Users/alumno/Desktop/luna/bomberman/"

class Controlador():
    def __init__(self):
        # init de la vista y el juego.
        self.CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0], '32' : 'bomb'}
        self.cliente = Cliente()
        print("intentando conectarse")
<<<<<<< HEAD
        self.cliente.conectarse("192.168.23.251", 5000)
=======
        self.cliente.conectarse("192.168.23.253", 5000)
>>>>>>> a5c99499107192b1f092f56fa9f10bcc36c9edf2
        self.vista = Vista(self.cliente)
        self.menu = Menu(self.vista, self.CONTROLES)
        self.start_menu_loop()
    
    def cargar_imagenes(self):
        """
        Función que carga las imagenes desde el disco duro a la memoria ram.
        Le avisa a la vista que cargue todas las imagenes necesarias.
        """
        #self.vista.cargar_imagen_fondo(path + "img/fondo.png")
        os.chdir(os.path.join(os.path.dirname(__file__), "../../"))
        self.vista.cargar_imagenes_bomberman()
        self.vista.cargar_imagenes_enemigo()
        self.vista.cargar_contenidos()
        self.vista.cargar_hud()
    
    def start_menu_loop(self):
        """
        Función que muestra el menú, y luego de la elección del usuario
        entra en el loop principal del juego con la elección hecha.
        """
        players = self.menu.show_start_menu()
        self.cargar_imagenes()
        self.main_loop()

    def main_loop(self):
        SecEvent = pygame.USEREVENT + 1
        clock2 = pygame.time.Clock()
        t = 1000
        pygame.time.set_timer(SecEvent, t)
        run = True
        real_clock = pygame.time.Clock()
        clock = pygame.time.Clock()
        expected_time = 0
        pygame.key.set_repeat(10)
        self.vista.screen = pygame.display.set_mode((675, 720))
        while run:
            clock.tick()
            real_clock.tick()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: 
                self.cliente.post(Input_move_event("izquierda", 1))
                print("izquierda")
            elif keys[pygame.K_RIGHT]:
                self.cliente.post(Input_move_event("derecha", 1))
                print("derecha")
            elif keys[pygame.K_DOWN]:
                self.cliente.post(Input_move_event("abajo", 1))
                print("abajo")
            elif keys[pygame.K_UP]:
                self.cliente.post(Input_move_event("arriba", 1))
                print("arriba")
            if keys[pygame.K_SPACE]:
                self.cliente.post(Input_poner_bomba(1))
                print("bomba")
            # # player dos
            # if keys[pygame.K_a]: self.em.post(Input_move_event("izquierda", 2))
            # elif keys[pygame.K_d]: self.em.post(Input_move_event("derecha", 2))
            # elif keys[pygame.K_s]: self.em.post(Input_move_event("abajo", 2))
            # elif keys[pygame.K_w]: self.em.post(Input_move_event("arriba", 2))
            # if keys[pygame.K_q]: self.em.post(Input_poner_bomba(2))
            for event in pygame.event.get():
                # Salir
                if event.type == pygame.QUIT: 
                    run = False
                # Paso segundo
                # if event.type == SecEvent:
                #     self.em.post(Sec_event())
                # debug
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_UP:
                #         self.cliente.post(Input_move_event("arriba", 1))
                #     elif event.key == pygame.K_DOWN:
                #         self.cliente.post(Input_move_event("abajo", 1))
                #     elif event.key == pygame.K_LEFT:
                #         self.cliente.post(Input_move_event("izquierda", 1))
                #     elif event.key == pygame.K_RIGHT:
                #         self.cliente.post(Input_move_event("derecha", 1))
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     contenido = Pared_rompible(Contenido_dummy())
                #     pos = pygame.mouse.get_pos()
                #     pos = (pos[0], pos[1] - 45)
                #     celda = self.game.mapa.get_celda_desde_posicion(pos)
                #     celda.agregar_contenido(contenido)
                    

                    
            self.vista.recargar_todo()        
            # self.em.post(Tick_event(expected_time))
            # Este pedazo de codigo es para que siempre el tickrate sea el mismo,
            # siendo siempre el msPorTick = 40.
            msPorTick = 40
            clock.tick()
            time_lapsed = clock.get_time()
            time_left_to_tick = msPorTick - time_lapsed
            if time_left_to_tick > 0:
                pygame.time.wait(time_left_to_tick)
            real_clock.tick()
            real_time_lapsed = real_clock.get_time()
            if real_time_lapsed != 40:
                print(real_time_lapsed)
            expected_time = real_time_lapsed
            pygame.display.flip()

    # def notify(self, evento):
    #     if evento.nombre == "personaje_murio":
    #         self.menu.show_stage_menu(1)
    #     if evento.nombre == "defeat_event":
    #         self.start_menu_loop()
    #     if evento.nombre == "win_event":
    #         self.game.ganaron_nivel()
    #         self.em.actualizar_listeners(self.vista, self.game, self)
    #         self.menu.show_stage_menu(2)
    #         self.main_loop()


controlador = Controlador()
