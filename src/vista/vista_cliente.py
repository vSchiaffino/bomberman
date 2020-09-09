import pygame
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
                        "su" : pygame.image.load("img/power_ups/SpeedPowerup.png"),
                        "bu" : pygame.image.load("img/power_ups/BombPowerup.png"),
                        "fu" : pygame.image.load("img/power_ups/FlamePowerup.png"),
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

    def recargar_bomberman(self, personajes):
        rotar = False
        lista = []
        direccs, posImgs, pos_bombermans = [],[],[]
        for i in range(0, len(personajes)):
            direccs.append(personajes[i].direccion)
        for i in range(0, len(personajes)):
            posImgs.append(personajes[i].img_index)
        for i in range(0, len(personajes)):
            pos_bombermans.append(personajes[i].pos)
        for i in range(0, len(personajes)):
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

    def recargar_enemigos(self, enemigos):
        lista = []
        for enemigo in enemigos:
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

    def recargar_om(self, personajes, enemigos):
        # Me traigo a todos los obstaculos moviels
        lista_om = []
        # Bomberman
        bombermans = self.recargar_bomberman(personajes)
        for bm in bombermans:
            lista_om.append(bm)
            
        # Enemigos
        for om in self.recargar_enemigos(enemigos):
            lista_om.append(om)
        # los ordeno en como tienen que renderizarse(primero los de menor posicion en y)
        lista_om = self.Ordenar(lista_om)
        for om in lista_om:
            self.screen.blit(om[0], om[1])
            # pygame.draw.circle(self.screen, pygame.Color(230, 95, 0), (om[1].centerx, om[1].bottom - 5), 5)

    def recargar_bombas(self, bombas):
        for bomba in bombas:
            bombSkin = self.contenidos["bomb"][bomba.index]
            self.screen.blit(bombSkin, (bomba.get_pos()[0] - 15, bomba.get_pos()[1] - 15 + HudOffset))

    def recargar_explosiones(self, explosiones):
        for explosion in explosiones:
            self.screen.blit(self.contenidos["explosion"][explosion.index], (explosion.celda.get_pos()[0], explosion.celda.get_pos()[1] + HudOffset))

    def recargar_contenidos(self, celdas):
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

    def recargar_hud(self, info):
        self.screen.blit(self.hud, (0, 0))
        # time
        self.screen.blit(self.hudFont.render(info[0], False, self.fontColor), (327, 5))
        # lifes
        self.screen.blit(self.hudFont.render(info[1], False, self.fontColor), (462, 5))
        # bombs
        self.screen.blit(self.hudFont.render(info[2], False, self.fontColor), (554, 5))
        # score
        self.screen.blit(self.hudFont.render(info[3], False, self.fontColor), (155, 5))    

    def recargar_todo(self):
        clock = pygame.time.Clock()
        clock2 = pygame.time.Clock()
        clock2.tick()
        # print("pido game")
        # game = self.cliente.pedir_algo("get_game")
        todo = self.cliente.pedir_algo("get_todo")
        # celdas = self.cliente.pedir_algo("get_all_celdas")
        self.recargar_contenidos(todo[0])
        # bombas = self.cliente.pedir_algo("get_bombas")
        self.recargar_bombas(todo[1])
        # explosiones = self.cliente.pedir_algo("get_explosiones")
        self.recargar_explosiones(todo[2])
        # info_hud = self.cliente.pedir_algo("get_info_hud")
        # [time, lifes, bombs, score]
        self.recargar_hud(todo[3])
        # personajes = self.cliente.pedir_algo("get_personajes")
        # enemigos = self.cliente.pedir_algo("get_enemigos")
        self.recargar_om(todo[4], todo[5])
        clock2.tick()
        tiempoTotal = clock2.get_time()
        if tiempoTotal > 40:
           print(tiempoTotal)

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
