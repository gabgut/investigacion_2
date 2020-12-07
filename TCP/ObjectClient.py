"""**Constantes**"""
"""Direccion del servidor"""
SERVER_ADDRESS = "127.0.0.1"
"""Puerto del servidor"""
SERVER_PORT = 5000

"""Paquetes importados"""

import socket
import pickle
from twh import ThreeWayHandshake
from time import sleep

class Client():

    """
    Esta clase se utiliza para implementar el cliente de sockets para establecer una comunicacion
    mediante el protocolo TCP

    Atributos:
    ---------
    Ninguno

    Metodos:
    -------
    __init__:
        Constructor de la clase.
    start_protocol:
        Empieza la conexion.
    """

    def __init__(self):
        print "Iniciando cliente, buscando conexion con el server"

    def start_protocol(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (SERVER_ADDRESS, SERVER_PORT)
        conn1 = ThreeWayHandshake()
        sock.connect(address)
        conn1.Connection()
        while conn1.connected != True:
            print "Lado del cliente:", conn1
            sock.sendall(pickle.dumps(conn1))
            if conn1.connected == True:
                break
            del conn1
            data = sock.recv(4096)
            sleep(1)
            conn1 = pickle.loads(data)
            del data
            print "Lado del cliente despues de la respuesta: ", conn1
            conn1.Connection()
            sock.sendall("Esto es un mensaje del cliente al servidor")
            sleep(3)
        data = sock.recv(4096)
        print data
        if conn1.connected == True:
            print "Listo."
        else:
            print "No esta listo"


def main():
    client = Client()
    client.start_protocol()
if __name__ == "__main__":
    main()
