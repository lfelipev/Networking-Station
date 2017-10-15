import socket
import os

## Initial fixed configurations
# Essa classe realiza a conexao TCP com o servidor

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 7000
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionDestination = (self.HOST, self.PORT)

    def connect(self):
        self.tcpSocket.connect(self.connectionDestination)
        data = "button clicked"
        self.tcpSocket.sendall(data.encode('utf-8'))
        self.tcpSocket.close()