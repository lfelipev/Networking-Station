import socket
import os

## Initial fixed configurations

HOST = '127.0.0.1'
PORT = 7000

def main():
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectionDestination = (HOST, PORT)
    tcpSocket.connect(connectionDestination)

    os.system("clear")
    print "|====================================|"
    print "|        Connected to server         |"
    print "|====================================|"
    print "|   Type EXIT to close connection    |"

    data = raw_input()

    while data != 'EXIT':
        tcpSocket.send(data)
        data = raw_input()
    tcpSocket.close()

if __name__ == '__main__':
    main()