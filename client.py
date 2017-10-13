import socket
import os

## Initial fixed configurations

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 7000
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionDestination = (self.HOST, self.PORT)

    def connect(self):
        self.tcpSocket.connect(self.connectionDestination)

        os.system("clear")
        #print "|====================================|"
        #print "|        Connected to server         |"
        #print "|====================================|"
        #print "|   Type EXIT to close connection    |"

        data = "button clicked"

        while True:


        self.tcpSocket.sendall(data.encode('utf-8'))
        tcpSocket.close()