import sys
import os
import pickle
from pydispatch import dispatcher
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../..'))
from thread_servidor import Thread_servidor
from modelo.game import Game
from event_manager.event_manager_cliente import Event_manager
from event_manager.eventos import Input_move_event, Input_poner_bomba, Tick_event, Sec_event
import socket

MSGLEN = 4096
# server


class Server:
        def __init__(self, sock=None):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
            self.bind("192.168.23.253", 5000)
            self.header = 5
            self.buffsize = 4096
=======
            self.bind("192.168.23.251", 5000)
            self.header = 10
            self.buffsize = 16
>>>>>>> a5c99499107192b1f092f56fa9f10bcc36c9edf2
            self.player1, self.player1_addr = self.esperar_conexion()

        def bind(self, host, port):
            self.sock.bind((host, port))

        def enviar_binario(self, data, con):
            """
            recibe información en binario y lo manda con el header size
            """
            msg = bytes(f"{len(data):<{self.header}}", "utf-8") + data
            con.send(msg)

        def recibir_binario(self, con):
            """
            recibe información en binario codificando el header
            """
            full_msg = b""
            new_msg = True
            while True:
                msg = con.recv(self.buffsize)
                if new_msg:
                    msglen = int(msg[:self.header])
                    new_msg = False
                full_msg += msg
                if len(full_msg) - self.header == msglen:
                    return full_msg[self.header::]

        def mysend(self, msg):
            self.sock.send(msg.encode())

        def recibir_string(self, con):
            string = str(self.recibir_binario(con), "utf-8")
            # print("recibi este string: " + string)
            return string

        def esperar_conexion(self):
            print("Esperando conexión.")
            self.sock.listen(1)
            con, client_addr = self.sock.accept()
            print("Conectado!")
            return con, client_addr

        def enviar_objeto(self, objeto, con):
            binario = pickle.dumps(objeto)
            self.enviar_binario(binario, con)

        def recibir_objeto(self, con):
            return pickle.loads(self.recibir_binario(con))
        # def mandar_objeto(self, player, objeto):
        #     data_string = pickle.dumps(objeto)
        #     self.player1.send(data_string)

        # def server_loop(self):
        #     while True:
        #         mensaje = self.myreceive(self.player1)
        #         if mensaje == "get_game":
        #             print("dame el game")
        #             game = self.game
        #             data_string = pickle.dumps(game)
        #             self.player1.send(data_string)
        #         if mensaje == "evento":
        #             evento = self.myreceive(self.player1)
        #             evento = pickle.loads(evento)
        #             print("hola")

        def notify(self, evento):
            pass

os.chdir(os.path.dirname(__file__))
server = Server()
game = Game(1)
em = Event_manager(game)
game.set_em(em)
thread = Thread_servidor(daemon=True, em=em)
thread.start()
direcciones = {
    "u" : "arriba",
    "d" : "abajo",
    "l" : "izquierda",
    "r" : "derecha"
}
while True:
    """
    0 : pide objeto
    1 : manda  objeto
    """
    # 
    mensaje = server.recibir_string(server.player1)
    if mensaje == "get_todo":
        print("dame el todo")
        info_hud = [game.get_tiempo_restante(),
                    game.get_vidas_pj(),
                    game.get_bombas_posibles(),
                    game.get_score()
        ]
        info_game = [game.get_all_celdas(),
                    game.get_bombas(),
                    game.get_explosiones(),
                    info_hud,
                    game.personajes,
                    game.get_enemigos()
        ]
        server.enviar_objeto(info_game, server.player1)
    
    # if mensaje == "get_all_celdas":
    #     print("dame celdas")
    #     celdas = game.get_all_celdas()
    #     server.enviar_objeto(celdas, server.player1)
    # elif mensaje == "get_bombas":
    #     print("dame bombas")
    #     bombas = game.get_bombas()
    #     server.enviar_objeto(bombas, server.player1)
    # elif mensaje == "get_explosiones":
    #     print("explosiones")
    #     explosiones = game.get_explosiones()
    #     server.enviar_objeto(explosiones, server.player1)
    # elif mensaje == "get_info_hud":
    #     print("hud")
    #     hud = [game.get_tiempo_restante(), game.get_vidas_pj(), game.get_bombas_posibles(), game.get_score()]
    #     server.enviar_objeto(hud, server.player1)
    # elif mensaje == "get_personajes":
    #     print("personajes")
    #     personajes = game.personajes
    #     server.enviar_objeto(personajes, server.player1)
    # elif mensaje == "get_enemigos":
    #     print("enemigos")
    #     enemigos = game.get_enemigos()
    #     server.enviar_objeto(enemigos, server.player1)
    elif mensaje[0] == "E":
        print("eventardo")
        dispatcher.send(signal="xd", evento=Input_move_event(direcciones[mensaje[1]], int(mensaje[2])))
    elif mensaje[0] == "B":
        print("bomba")
        dispatcher.send(signal="xd", evento=Input_poner_bomba(mensaje[1]))

