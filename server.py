import socket
import thread
import pickle
import os
import serial
import sys

class Server:
    def __init__(self):
        self.HOST = ''
        self.PORT = 7000
        self.SERIAL_PORT = '/dev/ttyACM0'
        self.BAUD_RATE = 9600
        self.conSerial = serial.Serial(self.SERIAL_PORT, self.BAUD_RATE)
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionOrigin = (self.HOST, self.PORT)
        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpSocket.bind(self.connectionOrigin)
        self.tcpSocket.listen(1)

    def getDataFromArduino(self):
        stringStream = self.conSerial.readline()
        stringSplit = stringStream.split(':')

        temp = stringSplit[0]
        humidity = stringSplit[1]
        luminosity = stringSplit[2]
        rain = stringSplit[3]
        density = stringSplit[4]
        arduinoData = ([temp, humidity, luminosity, rain, density])

        return arduinoData

    def connect_loop(self):
        while True:
            print("Server started!")
            connection, client = self.tcpSocket.accept()
            thread.start_new_thread(self.connect(connection), tuple([connection, client]))

    def connect(self, connection):
        while True:
            print('Server is now listening to port 7000.')
            dataReceive = connection.recv(1024)
            print(dataReceive)
            dataString = pickle.dumps(self.getDataFromArduino())
            dataSend = dataString
            if not dataReceive: break
            connection.sendall(dataSend)
        connection.close()
        thread.exit()
        #sys.exit()

    def disconnect(self):
        return 1

def main():
    server = Server()
    server.connect_loop()

if __name__ == '__main__':
    main()