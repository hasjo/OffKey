import socket
import time
import threading
import redis

def ThreadCommand(newSock):
    r = redis.StrictRedis(host='172.17.42.1', port=6379, db=0)
    ClientInput = newSock.recv(2048).decode('UTF-8').rstrip()
    print('Received command: ' + ClientInput)
    if ClientInput.split(' ')[0] == 'AUTH':
        Username = ClientInput.split(' ')[1]
        UsernameResponse = r.get(Username)
        if UsernameResponse != None:
            newSock.sendall(bytes(Username, 'UTF-8'))
            UsernameResponse = UsernameResponse.decode()
            r.set(Username + '-session', 'ACTIVE')
            print('Session set for ' + Username)
        else:
            newSock.sendall(bytes('DENIED', 'UTF-8'))
    if ClientInput.split(' ')[0] == 'SESS':
        Username = ClientInput.split(' ')[1]
        print('Session Request for: ' + Username)
        UsernameResponse = r.get(Username + '-session')
        print(UsernameResponse)
        if UsernameResponse != None:
            UsernameResponse = UsernameResponse.decode()
            if UsernameResponse == 'ACTIVE':
                print('Session request for ' + Username + ' successful')
                newSock.sendall(bytes('ACTIVE', 'UTF-8'))
            else:
                print('Session request for ' + Username + ' unsuccessful')
                newSock.sendall(bytes('INACTIVE', 'UTF-8'))

    newSock.shutdown(2)
    newSock.close()

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 6311))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        ct = threading.Thread(args = ([clientsocket]), target = ThreadCommand)
        ct.daemon = True
        ct.start()
        print('Socket accepted from: ' + str(address))

main()
