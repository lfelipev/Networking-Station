import socket
import thread
import os
import serial
import sys

## Initial fixed configurations

HOST = ''
PORT = 7000
#PORTA_SERIAL = '/dev/ttyUSB1'
BAUD_RATE = 9600
#conSerial = serial.Serial(PORTA_SERIAL, BAUD_RATE)
os.system("clear")

def connect(connection, client):
    print "Connected IP | PORT", client

    while True:
        data = connection.recv(1024)
        if not data: break
        print "Client to Arduino: ", data
        #conSerial.write(data)
        #message = conSerial.readline()
    print "Arduino says: "#, message

    print "Client has terminated connection", client
    print "Terminating..."
    #conSerial.close()
    connection.close()
    thread.exit()
    sys.exit()

def main():
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionOrigin = (HOST, PORT)
    tcpSocket.bind(connectionOrigin)
    tcpSocket.listen(1)

    print "|====================================|"
    print "| Server started: Waiting client     |"
    print "|====================================|"

    while True:

        connection, client = tcpSocket.accept()
        thread.start_new_thread(connect, tuple([connection, client]))

    tcpSocket.close()

if __name__ == '__main__':
    main()