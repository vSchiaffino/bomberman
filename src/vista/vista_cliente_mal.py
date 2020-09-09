import pygame
import json
# casa de valen v
#path = "C:/Users/valen/luna/luna/bomberman/"
# casa de facu
# path = "C:/Users/facun/Desktop/luna/bomberman/"
# huergo
# huergo arriba
# path = "C:/Users/alumno/Desktop/luna/bomberman/"
HudOffset = 45 
class Vista():
    def __init__(self, cliente):
        pygame.init()
        self.cliente = cliente
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

    def cargar_imagenes_menu(self):
        self.imagenesMenu = {"background" : pygame.image.load("img/Menu/title_background.jpg"),
                             "title" : pygame.image.load("img/Menu/title_titletext.png"),
                             "onePlayerText" : pygame.image.load("img/Menu/One_Player_Normal.png"),
                             "twoPlayerText" : pygame.image.load("img/Menu/Two_Players_Normal.png"),
                             "onePlayerHoverText" : pygame.image.load("img/Menu/One_Player_Hover.png"),
                             "twoPlayerHoverText" : pygame.image.load("img/Menu/Two_Players_Hover.png"),
                             "controlPlayerOne" : pygame.image.load("img/Menu/Control_PlayerOne.png"),
                             "controlPlayerTwo" : pygame.image.load("img/Menu/Control_PlayerTwo.png")}

    def cargar_imagenes_enemigo(self):
        self.cargar_imagenes_om(self.imagenesEnemy, "enemy", 6)
    
    def cargar_imagenes_bomberman(self):
        self.cargar_imagenes_om(self.imagenesBm, "bman", 8)
        self.bomberman = self.imagenesBm["front"][0]
        self.recargar_bomberman()
    
    def cargar_imagenes_om(self, lista_om, nombre_om, lenght):
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
        self.hud = pygame.image.load("img/Menu/HUD.png")

    def recargar_menu(self, hover = True, onePlayerHovered = False):
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

    def recargar_todo(self):
        self.recargar_contenidos()
        self.recargar_bombas()
        self.recargar_explosiones()
        self.recargar_hud()
        self.recargar_om()

    def recargar_bomberman(self):
        rotar = False
        lista = []
        # calculo direccion
        direccs = self.cliente.pedir_algo("get_direccion_bm")
        posImgs = self.cliente.pedir_algo("get_index_bm")
        pos_bombermans = self.cliente.pedir_algo("get_posicion_personaje")
        players = self.cliente.pedir_algo("get_players")
        for i in range(0, players):
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
        lista = []
        direcciones = self.cliente.pedir_algo("get_direcciones_enemigos")
        indexes_imgs = self.cliente.pedir_algo("get_index_enemigos")
        posiciones = self.cliente.pedir_algo("get_posiciones_enemigos")
        for i in range(0, len(direcciones)):
            rotar = False
            direcc = direcciones[i]
            if direcc == "arriba":
                imagenesEnemy = self.imagenesEnemy["back"]
            elif direcc == "abajo":
                imagenesEnemy = self.imagenesEnemy["front"]
            else:
                if direcc == "izquierda":
                    rotar = True
                imagenesEnemy = self.imagenesEnemy["side"]
            index_img = indexes_imgs[i]
            enemy = imagenesEnemy[index_img]
            if rotar:
                enemy = pygame.transform.flip(enemy, True, False)
            pos_enemy = posiciones[i]
            pos_enemy = (int(pos_enemy[0]), int(pos_enemy[1]))
            rect = enemy.get_rect()
            rect.centerx = pos_enemy[0]
            rect.centery = pos_enemy[1] - 20 + HudOffset

            lista.append((enemy, rect))
            # self.screen.blit(enemy, rect)
        return lista
            
    def recargar_om(self):
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
        self.cliente.mandar("get_index_bombs")
        index = self.cliente.recibir()
        for i in range(0, len(index)):
            bombSkin = self.contenidos["bomb"][bomba.index]
            self.screen.blit(bombSkin, (bomba.get_pos()[0] - 15, bomba.get_pos()[1] - 15 + HudOffset))

    def recargar_explosiones(self):
        indexes = self.cliente.pedir_algo("get_index_explosiones")
        celda_exps_pos = self.cliente.pedir_algo("get_pos_explosiones")
        # explosion.celda.get_pos()
        for i in range(0, len(index)):
            index = indexes[i]
            celda_exp_pos = celda_exps_pos[i]
            self.screen.blit(self.contenidos["explosion"][index[i]], (celda_exp_pos[0], celda_exp_pos[1] + HudOffset))

    def recargar_contenidos(self):
        celdas = self.cliente.pedir_algo("get_contenidos")
        cosas_a_cargar = ["pnr", "pr", "dummy", "bu", "su", "fu", "salida"]
        for fila in celdas:
            for celda in fila:
                keys = celda[0]
                for key in keys:
                    offset = 0
                    if key in cosas_a_cargar:
                        if key == "bu" or key == "su" or key == "fu":
                            offset = 8
                        self.screen.blit(self.contenidos[key], (celda[1][0] + offset, celda[1][1] + offset + HudOffset))

    def recargar_hud(self):
        self.screen.blit(self.hud, (0, 0))
        # time
        tiempo = self.cliente.pedir_algo("get_tiempo_restante")
        vidas_pj = self.cliente.pedir_algo("get_vidas_pj")
        bombas_posibles = self.cliente.pedir_algo("get_bombas_posibles")
        score = self.cliente.pedir_algo("get_score")
        self.screen.blit(self.hudFont.render(tiempo, False, self.fontColor), (327, 5))
        # lifes
        self.screen.blit(self.hudFont.render(vidas_pj, False, self.fontColor), (462, 5))
        # bombs
        self.screen.blit(self.hudFont.render(bombas_posibles, False, self.fontColor), (554, 5))
        # score
        self.screen.blit(self.hudFont.render(score, False, self.fontColor), (155, 5))    


    def show_stage_menu(self, stage):
        self.screen.fill(pygame.color.Color(0, 0, 0))
        self.screen.blit(self.stageFont.render("Stage 1, nivel " + str(stage), False, self.fontColor), (135, 337))

    def Ordenar(self, lista):
        n = len(lista)

        for i in range(1, n):
            val = lista[i]
            j = i

            while j > 0 and lista[j-1][1].bottom > val[1].bottom:
                lista[j] = lista[j-1]
                j -= 1

            lista[j] = val
        return lista  

    # def notify(self, evento):
    #     if evento.nombre == "tick_event":
    #         self.recargar_contenidos()
    #         self.recargar_bombas()
    #         self.recargar_explosiones()
    #         self.recargar_hud()
    #         self.recargar_om()