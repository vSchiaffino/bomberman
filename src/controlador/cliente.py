 # # Importamos las librerias necesarias
import socket, pygame
import json
import pickle
# # Establecemos el tipo de socket/conexion
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# port = 5000 # Puerto de comunicacion
# # Realizamos la conexion al la IP y puerto
# sock.connect(('192.168.23.46',port))
# # Leemos los datos del servidor
# data = sock.recv(4096)
# while True:
#     text = input(">")
#     sock.send(text.encode())
   
# # Cerramos el socket
# sock.close()

# # Mostramos los datos recibidos
# print(data.decode())


class Cliente():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.header = 5
        self.buffsize = 4096
    
    def conectarse(self, ip, puerto):
        self.socket.connect((ip,puerto))

    def desconectarse(self):
        self.socket.close()

    def enviar_binario(self, data):
        """
        pide información en binario y lo manda con el header size
        """
        msg = bytes(f"{len(data):<{self.header}}", "utf-8") + data
        self.socket.send(msg)

    def recibir_binario(self):
            """
            recibe información en binario codificando el header
            """
            full_msg = b""
            new_msg = True
            while True:
                msg = self.socket.recv(self.buffsize)
                if new_msg:
                    msglen = int(msg[:self.header])
                    new_msg = False
                full_msg += msg
                if len(full_msg) - self.header == msglen:
                    return full_msg[self.header::]

    def mandar_string(self, texto):
        self.enviar_binario(bytes(texto, "utf-8"))
        
    def recibir_objeto(self):
        return pickle.loads(self.recibir_binario())

    def enviar_objeto(self, objeto):
        binario = pickle.dumps(objeto)
        self.enviar_binario(binario)

    def pedir_algo(self, text):
        clock = pygame.time.Clock()
        clock.tick()
        self.mandar_string(text)
        obj = self.recibir_objeto()
        clock.tick()
        # print(text + " tardo " + str(clock.get_time()))
        return obj

    def post(self, evento):
        if evento.nombre == "input_move_event":
            direcciones = {
                "arriba" : "u",
                "abajo" : "d",
                "derecha" : "r",
                "izquierda" : "l"
            }
            self.mandar_string("E" + direcciones[evento.direccion] + str(evento.player))
        if evento.nombre == "input_poner_bomba":
            self.mandar_string("B" + str(evento.player))
        

