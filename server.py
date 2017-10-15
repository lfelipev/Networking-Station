import socket
import thread
import os
import serial
import sys

class Server:
    def __init__(self):
        self.HOST = ''
        self.PORT = 7000
        #self.SERIAL_PORT = '/dev/ttyUSB0'
        #self.BAUD_RATE = 9600
        self.conSerial = serial.Serial(self.SERIAL_PORT, self.BAUD_RATE)
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionOrigin = (self.HOST, self.PORT)
        self.tcpSocket.bind(self.connectionOrigin)
        self.tcpSocket.listen(1)

    def connect_loop(self):
        while True:
            connection, client = self.tcpSocket.accept()
            thread.start_new_thread(self.connect(connection), tuple([connection, client]))

    def connect(self, connection):
        data = connection.recv(1024)
        self.conSerial.write(data)
        message = self.conSerial.readline()
        connection.close()
        thread.exit()
        sys.exit()

    def disconnect(self):

def main():

    while True:

        connection, client = tcpSocket.accept()
        thread.start_new_thread(server.connect, tuple([connection, client]))

    tcpSocket.close()

if __name__ == '__main__':
    main()