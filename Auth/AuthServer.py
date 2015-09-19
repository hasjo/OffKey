import socket
import time
import threading
import redis

def ThreadCommand(newSock):
    r = redis.StrictRedis(host='172.17.42.1', port=6379, db=0)
    print('kicked into a thread')
    ClientInput = newSock.recv(2048).decode('UTF-8').rstrip()
    print('Received username: ' + ClientInput)
    UsernameResponse = r.get(ClientInput).decode()
    print(UsernameResponse)
    if UsernameResponse != 'None':
        newSock.sendall(bytes('ACCEPTED', 'UTF-8'))
    else:
        newSock.sendall(bytes('DENIED', 'UTF-8'))
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
