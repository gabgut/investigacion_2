# status 1. sync from user
# sync recv 2.ack-sync from server
# sync rec 3.ack from user then data


class ThreeWayHandshake:

    def __init__(self, twh=None):

        self.status = None
        self.connected = False

    def Connection(self):
        if self.status == None:
            print "starting 3-way handshake", "status: sync"
            self.status = "sync"
        elif self.status == "sync":
            print "sync received", "status: ack-sync"
            self.status = "ack-sync"
        elif self.status == "ack-sync":
            print "ack-sync received", "status: ack"
            self.status = "ack"
        elif self.status == "ack":
            self.connected = True
            print "connected.", "ready to received data."

    def IsConnected(self):
        return self.connected

    def Reset(self):
        self.status = None
        self.connected = False

    def __str__(self):
        return "status: {self.status}, connection established: {self.connected}."
