import socket
import time
import threading

def ThreadCommand(inpstring):
    while True:
        print(inpstring)
        time.sleep(1)

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 6311))
    serversocket.listen(5)

    while True:
        (clientsocket, address) = serversocket.accept()
        ct = threading.Thread(args = [clientsocket], target = ThreadCommand)
        ct.daemon = True
        ct.start()
        print('Socket accepted from: ' + address)

main()
