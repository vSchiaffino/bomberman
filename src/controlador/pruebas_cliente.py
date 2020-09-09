import sys,os,pickle
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from cliente import Cliente
from modelo.game import Game


cliente = Cliente()
cliente.conectarse("192.168.0.23", 5000)
print("me conecte")

game = cliente.pedir_algo("get_game")

print("hola")