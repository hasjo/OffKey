import socket
import time
import threading

def ThreadCommand(inpstring):
    print('kicked into a thread')

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 6311))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        ct = threading.Thread(args = [clientsocket], target = ThreadCommand)
        ct.daemon = True
        ct.start()
        print('Socket accepted from: ' + str(address))

main()
