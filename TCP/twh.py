# status 1. sync from user
# sync recv 2.ack-sync from server
# sync rec 3.ack from user then data


class ThreeWayHandshake:

    """
    Esta clase se utiliza para implementar el protocolo de Three Way Handshakes

    Atributos:
    ---------
    status: Python String
        String para almacenar el estado.
    connected: Python tuple
        Booleano para ver si la conexion se establece.

    Metodos:
    -------
    __init__:
        Constructor de la clase.
    Connection:
        Empieza la conexion.
    IsConnected:
        Retorna el estado de la conexion.
    Reset:
        Reinicia los atributos de la clase.  
    """

    def __init__(self, twh=None):
        self.status = None
        self.connected = False

    def Connection(self):
        if self.status == None:
            print "Empezando el protocolo de 3-way handshake", "estado: sync"
            self.status = "sync"
        elif self.status == "sync":
            print "sync recibido", "estado: ack-sync"
            self.status = "ack-sync"
        elif self.status == "ack-sync":
            print "ack-sync recibido", "estado: ack"
            self.status = "ack"
        elif self.status == "ack":
            self.connected = True
            print "Conectado.", "Listo para recibir datos"

    def IsConnected(self):
        return self.connected

    def Reset(self):
        self.status = None
        self.connected = False

    def __str__(self):
        return "Estadi: {self.status}, conexion establecida: {self.connected}."
