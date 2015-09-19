import socket
import time
import threading
import redis

def ThreadCommand(newSock):
    print('kicked into a thread')
    ClientInput = newSock.recv(2048).decode('UTF-8')
    print('Received message: ' + ClientInput)
    newSock.sendall(bytes('THIS IS A TEST MESSAGE', 'UTF-8'))
    newSock.shutdown(2)
    newSock.close()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 6311))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        print(type(clientsocket))
        ct = threading.Thread(args = ([clientsocket]), target = ThreadCommand)
        ct.daemon = True
        ct.start()
        print('Socket accepted from: ' + str(address))

main()
