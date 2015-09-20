from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
import socket
APP = Flask(__name__)

@APP.route('/')
def index():
    return render_template('index.html')

@APP.route('/testenc')
def testenc():
    return render_template('testenc.html')

@APP.route('/user/<username>')
def userpage(username):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('172.17.42.1', 6311))
    s.sendall(bytes('SESS ' + username, 'UTF-8'))
    ServResp = s.recv(2048).decode('UTF-8').rstrip()
    print('Server Response is: ' + ServResp)
    if ServResp == 'ACTIVE':
        return "<h1> YOU ARE AUTHENTICATED </h1>"
    else:
        return "<h1> GET OUTTA HERE </h1>"

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
