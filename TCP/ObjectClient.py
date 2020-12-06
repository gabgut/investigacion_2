import socket
import pickle
from twh import ThreeWayHandshake
from time import sleep
SERVER_ADDRES = "127.0.0.1"
SERVER_PORT = 5000


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (SERVER_ADDRES, SERVER_PORT)
    conn1 = ThreeWayHandshake()
    sock.connect(address)
    conn1.Connection()
    while conn1.connected != True:
        print "client side:", conn1
        sock.sendall(pickle.dumps(conn1))
        if conn1.connected == True:
            break
        del conn1
        data = sock.recv(4096)
        sleep(1)
        conn1 = pickle.loads(data)
        del data
        print "client side after response:", conn1
        conn1.Connection()
        sock.sendall("Hola")
        sleep(3)

    if conn1.connected == True:
        print "done."
    else:
        print "not done"


# enable()
main()
