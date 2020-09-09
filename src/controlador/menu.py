import pygame, sys, os

class Menu:
    """
    Clase que se encarga de gestionar el menú del usuario.
    """
    def __init__(self, vista, controles):
        self.vista = vista
        self.controles = controles
    
    def show(self):
        pass

    def show_stage_menu(self, stage):
        """
        Visualización del nivel y la stage.
        """
        run = True
        tickActual = 0
        tickLimite = 2000
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if str(event.key) == "32":
                        run = False
            tickActual += 1
            if tickActual == tickLimite:
                run = False
            self.vista.show_stage_menu(stage)
            pygame.display.flip()
            pygame.time.wait(1)


    def show_start_menu(self):
        """
        Función que sirve para mostrar el menú inicial, es decir
        el de elección de un jugador o dos jugadores.
        """
        run = True
        pygame.key.set_repeat(1000)
        os.chdir(os.path.join(os.path.dirname(__file__), "../../"))
        self.vista.cargar_imagenes_menu()
        change_tickrate = 30
        tick_actual = 0
        selected = 1
        ShowHover = False
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if str(event.key) == "274":
                        if selected == 1: selected = 2
                    if str(event.key) == "273":
                        if selected == 2: selected = 1
                    if str(event.key) == "13":
                        run = False
            self.vista.recargar_menu(ShowHover, selected == 1)
            tick_actual += 1
            if tick_actual == change_tickrate:
                tick_actual = 0
                ShowHover = not ShowHover
            pygame.display.flip()
        self.show_stage_menu(1)
        return selected

        