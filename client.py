import socket
import os
import time
import pickle

## Initial fixed configurations
# Essa classe realiza a conexao TCP com o servidor

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 7000
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionDestination = (self.HOST, self.PORT)
        self.tcpSocket.connect(self.connectionDestination)

    def getData(self):
        dataSend = "Client request!"
        self.tcpSocket.sendall(dataSend.encode('utf-8'))
        dataReceive = self.tcpSocket.recv(1024)
        dataString = pickle.loads(dataReceive)
        #self.tcpSocket.close()

        return dataString

    def disconnect(self):
        self.tcpSocket.close()

'''
def main():
    client = Client()
    client.connect()

if __name__ == '__main__':
    main()
'''