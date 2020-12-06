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

class Server():

    def __init__(self):
        self.hanler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (SERVER_ADDRESS, SERVER_PORT)
        print "Servidor {SERVER_ADDRESS} en el puerto {SERVER_PORT}"
        self.hanler.bind(self.address)
        self.hanler.listen(1)

    def start_protocol(self):
        con = (self.hanler.accept()[0])
        connection = False
        while connection != True:
            print "Esperando por conexion"
            data = con.recv(4096)
            obj = pickle.loads(data)
            del data
            print "Recibida"
            obj.Connection()
            print "Lado del servidor: ", obj
            con.sendall(pickle.dumps(obj))
            connection = obj.IsConnected()
            data = con.recv(4096)
        print data
        print "El three way handshake fue realizado con exito"
        con.close()

def main():
    server = Server()
    server.start_protocol()
if __name__ == "__main__":
    main()
