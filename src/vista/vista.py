import pygame, sys, os
# casa de valen v
#path = "C:/Users/valen/luna/luna/bomberman/"
# casa de facu
# path = "C:/Users/facun/Desktop/luna/bomberman/"
# huergo

path = "C:/Users/huergo/Desktop/luna/bomberman/"
# huergo arriba
# path = "C:/Users/alumno/Desktop/luna/bomberman/"
HudOffset = 45 
class Vista():
    """
    Clase que se encarga de mostrar en pantalla el modelo.
    """
    def __init__(self):
        pygame.init()
        self.dimensiones = (675, 675)
        self.fondo = None
        self.screen = pygame.display.set_mode(self.dimensiones)
        self.bomberman = None
        imagenesBmBack = []
        imagenesBmFront = []
        imagenesBmSide = []
        self.imagenesBm = {"back" : imagenesBmBack, "front" : imagenesBmFront, "side" : imagenesBmSide}
        imagenesEnemyBack = []
        imagenesEnemyFront = []
        imagenesEnemySide = []
        self.imagenesEnemy = {"back" : imagenesEnemyBack, "front" : imagenesEnemyFront, "side" : imagenesEnemySide}
        pygame.key.set_repeat(10)
        pygame.font.init()
        self.hudFont = pygame.font.SysFont("Comic Sans MS", 25)
        self.stageFont = pygame.font.SysFont("Comic Sans MS", 50)
        self.fontColor = pygame.color.Color(255, 255, 255)

    def set_game(self, game):
        """
        Función que se utiliza para actualizar el game.
        AVISO: esto se hace ya que, cuando el mapa se actualiza, 
        se sigue haciendo referencia al viejo mapa, lo cual generaba
        errores en la vista. Con esta función se resuelve. Cada vez que
        el objeto mapa se vuelve a inicializar(mediante un pickle) se llama
        a esta función.
        """
        self.game = game

    def cargar_sonidos(self):
        path = os.path.join(os.path.dirname(__file__), "../../")
        os.chdir(path)
        pygame.mixer.init()
        self.sonidos = {
            "win" : pygame.mixer.Sound("effects/win.wav"),
            "defeat" : pygame.mixer.Sound("effects/defeat.wav"),
            "muerte_enemigos" : pygame.mixer.Sound("effects/muerte_enemigos.wav"),
            "explosion" : pygame.mixer.Sound("effects/explosion.wav"),
            "power_up" : pygame.mixer.Sound("effects/power_up.wav")
        }

    def cargar_imagenes_menu(self):
        """
        Pone en memoria ram las imagenes del menu sacadas del disco.
        """
        self.imagenesMenu = {"background" : pygame.image.load("img/Menu/title_background.jpg"),
                             "title" : pygame.image.load("img/Menu/title_titletext.png"),
                             "onePlayerText" : pygame.image.load("img/Menu/One_Player_Normal.png"),
                             "twoPlayerText" : pygame.image.load("img/Menu/Two_Players_Normal.png"),
                             "onePlayerHoverText" : pygame.image.load("img/Menu/One_Player_Hover.png"),
                             "twoPlayerHoverText" : pygame.image.load("img/Menu/Two_Players_Hover.png"),
                             "controlPlayerOne" : pygame.image.load("img/Menu/Control_PlayerOne.png"),
                             "controlPlayerTwo" : pygame.image.load("img/Menu/Control_PlayerTwo.png")}

    def cargar_imagenes_enemigo(self):
        """
        Pone en memoria ram las imagenes del enemigo sacadas del disco.
        """
        self.cargar_imagenes_om(self.imagenesEnemy, "enemy", 6)
    
    def cargar_imagenes_bomberman(self):
        """
        Pone en memoria ram las imagenes del bomberman sacadas del disco.
        """
        self.cargar_imagenes_om(self.imagenesBm, "bman", 8)
        self.bomberman = self.imagenesBm["front"][0]
    
    def cargar_imagenes_om(self, lista_om, nombre_om, lenght):
        """
        Pone en memoria ram las imagenes de los obstaculos moviles sacadas del disco.
        """
        for i in range(1, lenght + 1):
            imgP = "img/" + nombre_om + "/Back/" + "b0" + str(i) + ".png"
            lista_om["back"].append(pygame.image.load(imgP))
        for i in range(1, lenght + 1):
            imgP = "img/" + nombre_om + "/Front/" + "f0" + str(i) + ".png"
            lista_om["front"].append(pygame.image.load(imgP))
        for i in range(1, lenght + 1):
            imgP = "img/" + nombre_om + "/Side/" + "s0" + str(i) + ".png"
            lista_om["side"].append(pygame.image.load(imgP))

    def cargar_contenidos(self):
        """
        Pone en memoria ram las imagenes de los contenidos sacadas del disco.
        """
        explosion = []
        for i in range(0, 5):
            explosion.append(pygame.image.load("img/explosion/0"+ str(i) +".png"))
        bombas = []
        for i in range(1, 4):
            bombas.append(pygame.image.load("img/bomb/0"+ str(i) +".png"))
        
        self.contenidos = {"dummy" : pygame.image.load("img/bloques/dummy.png"),
                        "pnr" : pygame.image.load("img/bloques/pared_no_rompible.png"),
                        "pr" : pygame.image.load("img/bloques/pared_rompible.png"),
                        "su" : pygame.image.load("img/power_ups/SpeedPowerUp.png"),
                        "bu" : pygame.image.load("img/power_ups/BombPowerUp.png"),
                        "fu" : pygame.image.load("img/power_ups/FlamePowerUp.png"),
                        "salida" : pygame.image.load("img/bloques/Portal.png"),                        
                        "bomb" : bombas,
                        "explosion" : explosion}

    def cargar_hud(self):
        """
        Pone en memoria ram la imagen del hud sacada del disco.
        """
        self.hud = pygame.image.load("img/Menu/HUD.png")

    def recargar_menu(self, hover = True, onePlayerHovered = False):
        """
        Recarga el menu.
        """
        self.screen.blit(self.imagenesMenu["background"], (0, 0))
        self.screen.blit(self.imagenesMenu["title"], (49, 0))
        if hover:
            if onePlayerHovered:
                self.screen.blit(self.imagenesMenu["onePlayerHoverText"], (337 - 66, 400 + HudOffset))
                self.screen.blit(self.imagenesMenu["twoPlayerText"], (337 - 66, 500 + HudOffset))
            else:
                self.screen.blit(self.imagenesMenu["onePlayerText"], (337 - 66, 400 + HudOffset))
                self.screen.blit(self.imagenesMenu["twoPlayerHoverText"], (337 - 66, 500 + HudOffset))
        else:
            self.screen.blit(self.imagenesMenu["onePlayerText"], (337 - 66, 400 + HudOffset))
            self.screen.blit(self.imagenesMenu["twoPlayerText"], (337 - 66, 500 + HudOffset))

    def recargar_bomberman(self):
        """
        Recarga el bomberman.
        devuelve la lista que contiene la imagen a ser cargada de el/los bomberman
        y la/s posición/es
        """
        rotar = False
        lista = []
        # calculo direccion
        direccs = self.game.get_direccion_bm()
        posImgs = self.game.get_index_bm()
        pos_bombermans = self.game.get_posicion_personaje()
        for i in range(0, self.game.players):
            direcc = direccs[i]
            posImg = posImgs[i]
            pos_bomb = pos_bombermans[i]
            if direcc == "arriba":
                imagenesBm = self.imagenesBm["back"]
            elif direcc == "abajo":
                imagenesBm = self.imagenesBm["front"]
            else:
                if direcc == "izquierda":
                    rotar = True
                imagenesBm = self.imagenesBm["side"]
            imagenBm = imagenesBm[posImg]
            if rotar:
                imagenBm = pygame.transform.flip(imagenBm, True, False)
            pos_bomb = (int(pos_bomb[0]), int(pos_bomb[1]))
            rect = imagenBm.get_rect()
            rect.centerx = pos_bomb[0]
            rect.centery = pos_bomb[1] - 35 + HudOffset
            lista.append((imagenBm, rect))
        return lista

    def recargar_enemigos(self):
        """
        Función que recarga a los enemigos
        Devuelve una lista de tuplas, que contiene la imagen a ser cargada
        de los enemigos y la posición.
        """
        lista = []
        for enemigo in self.game.get_lista_enemigos():
            rotar = False
            # calculo direccion
            direcc = enemigo.get_direccion()
            if direcc == "arriba":
                imagenesEnemy = self.imagenesEnemy["back"]
            elif direcc == "abajo":
                imagenesEnemy = self.imagenesEnemy["front"]
            else:
                if direcc == "izquierda":
                    rotar = True
                imagenesEnemy = self.imagenesEnemy["side"]
            posImg = enemigo.get_index_img()
            enemy = imagenesEnemy[posImg]
            if rotar:
                enemy = pygame.transform.flip(enemy, True, False)
            pos_enemy = enemigo.get_posicion()
            pos_enemy = (int(pos_enemy[0]), int(pos_enemy[1]))
            rect = enemy.get_rect()
            rect.centerx = pos_enemy[0]
            rect.centery = pos_enemy[1] - 20 + HudOffset

            lista.append((enemy, rect))
            # self.screen.blit(enemy, rect)
        return lista
            
    def recargar_om(self):
        """
        Recarga los obstáculos móviles, buscando la lista de imagenes
        y posiciones del bomberman y de los enemigos y antes los ordena por
        posicion en y, para que se bliteen de orden correcto.
        """
        # Me traigo a todos los obstaculos moviels
        lista_om = []
        # Bomberman
        bombermans = self.recargar_bomberman()
        for bm in bombermans:
            lista_om.append(bm)
            
        # Enemigos
        for om in self.recargar_enemigos():
            lista_om.append(om)
        # los ordeno en como tienen que renderizarse(primero los de menor posicion en y)
        lista_om = self.Ordenar(lista_om)
        for om in lista_om:
            self.screen.blit(om[0], om[1])
            # pygame.draw.circle(self.screen, pygame.Color(230, 95, 0), (om[1].centerx, om[1].bottom - 5), 5)

    def recargar_bombas(self):
        """
        Recarga todas las bombas.
        """
        bombas = self.game.get_bombas()
        for bomba in bombas:
            bombSkin = self.contenidos["bomb"][bomba.index]
            self.screen.blit(bombSkin, (bomba.get_pos()[0] - 15, bomba.get_pos()[1] - 15 + HudOffset))

    def recargar_explosiones(self):
        """
        Recarga todas las explosiones.
        """
        for explosion in self.game.get_explosiones():
            self.screen.blit(self.contenidos["explosion"][explosion.index], (explosion.celda.get_pos()[0], explosion.celda.get_pos()[1] + HudOffset))

    def recargar_contenidos(self):
        """
        Recarga todos los contenidos
        """
        celdas = self.game.get_all_celdas()
        cosas_a_cargar = ["pnr", "pr", "dummy", "bu", "su", "fu", "salida"]
        for fila in celdas:
            for celda in fila:
                keys = celda.get_ruta_contenido()
                for key in keys:
                    offset = 0
                    if key in cosas_a_cargar:
                        if key == "bu" or key == "su" or key == "fu":
                            offset = 8
                        self.screen.blit(self.contenidos[key], (celda.get_pos()[0] + offset, celda.get_pos()[1] + offset + HudOffset))

    def recargar_hud(self):
        """
        Recarga el hud.
        """
        self.screen.blit(self.hud, (0, 0))
        # time
        self.screen.blit(self.hudFont.render(self.game.get_tiempo_restante(), False, self.fontColor), (327, 5))
        # lifes
        self.screen.blit(self.hudFont.render(self.game.get_vidas_pj(), False, self.fontColor), (462, 5))
        # bombs
        self.screen.blit(self.hudFont.render(self.game.get_bombas_posibles(), False, self.fontColor), (554, 5))
        # score
        self.screen.blit(self.hudFont.render(self.game.get_score(), False, self.fontColor), (155, 5))    


    def show_stage_menu(self, stage):
        """
        Muestra la pantalla del stage menu.
        """
        self.screen.fill(pygame.color.Color(0, 0, 0))
        self.screen.blit(self.stageFont.render("Stage 1, nivel " + str(stage), False, self.fontColor), (135, 337))

    def Ordenar(self, lista):
        """
        Ordena los obstaculos moviles como tienen que estar(ordenandolos
        en orden creciente segun  su posición en y)
        """
        n = len(lista)

        for i in range(1, n):
            val = lista[i]
            j = i

            while j > 0 and lista[j-1][1].bottom > val[1].bottom:
                lista[j] = lista[j-1]
                j -= 1

            lista[j] = val
        return lista  

    def notify(self, evento):
        if evento.nombre == "tick_event":
            self.recargar_contenidos()
            self.recargar_bombas()
            self.recargar_explosiones()
            self.recargar_hud()
            self.recargar_om()
        elif evento.nombre == "win_event":
            pygame.mixer.Sound.play(self.sonidos["win"])            
        elif evento.nombre == "defeat_event":
            pygame.mixer.Sound.play(self.sonidos["defeat"])            
        elif evento.nombre == "bomba_exploto":
            pygame.mixer.Sound.play(self.sonidos["explosion"])
        elif evento.nombre == "power_up":
            pygame.mixer.Sound.play(self.sonidos["power_up"])
        elif evento.nombre == "se_mato_enemigo":
            pygame.mixer.Sound.play(self.sonidos["muerte_enemigos"])
            