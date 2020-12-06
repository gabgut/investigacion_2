#!/usr/bin/python2.7

# imports
import socket
 
# define Client:
userInput = " "
while(userInput != ""): 
    userInput = raw_input("Ingrese el mensaje a enviar o presione Enter para terminar envios: ") # Solicito ingreso de mensaje por terminal
    clientMsg = userInput # Se define mensaje a enviar
    encodedMsg = str.encode(clientMsg) # Se codifica el mensaje
    serverAddrPort = ("127.0.0.1", 20001) #Se define dir y port del server
    bufferSize = 1024

    UDPClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Crea socket de cliente
    UDPClientSocket.sendto(encodedMsg, serverAddrPort) # Donde envio el mensaje?
    serverMsg,server = UDPClientSocket.recvfrom(bufferSize) # Recibo msj del server

    print("\n\tMensaje enviado al servidor: " + clientMsg)
    print("\tMensaje recibido del servidor: " + str(serverMsg) + "\n")

exit()