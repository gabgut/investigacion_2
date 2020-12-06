#!/usr/bin/python2.7

# imports
import socket

# Defino servidor
localAddrPort = ("127.0.0.1",20001) # Dir y puerto local
bufferSize = 1024 #tamano del datagrama
# msgServer = "Hola Mundo al Cliente" # mensaje a enviar al cliente
# encodedMsg = str.encode(msgServer) # mensaje codificado

UDPServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Creo server socket
UDPServerSocket.bind(localAddrPort) # Hago binding con direccion e IP
print("Servidor UDP escuchando...")

while(True): # ciclo para escuchar datagramas
    rcvdMsg, clientAddr = UDPServerSocket.recvfrom(bufferSize) # Recibo mensaje con direccion IP del cliente
    rcvdMsg.decode()
    clientIP  = clientAddr[0] # Guardo direccion IP del cliente
    print("Mensaje del cliente: " + rcvdMsg)
    print("Direccion del cliente: " + clientIP)
    # Respondo al cliente
    encodedMsg = str.encode(str.upper(rcvdMsg)) # Convierto a mayusculas y codifico
    UDPServerSocket.sendto(encodedMsg, clientAddr) # Envio respuesta al cliente