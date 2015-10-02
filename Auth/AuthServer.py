from flask import Flask, render_template
import redis
APP = Flask(__name__)

@APP.route('/api/auth/<user>/<string>/', methods=['GET'])
def auth_user(user, string):
    r = redis.StrictRedis(host='redis', port=6379, db=0)
    UsernameResponse = r.get(user + "-key")
    if UsernameResponse != None:
        UsernameResponse = UsernameResponse.decode()
        Key = float(string) * 6 + 12 / 4
        if int(UsernameResponse) == int(Key):
            return 'SUCCESS'
        else:
            return 'FAILURE'
    else:
        return 'USER DOES NOT EXIST'

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
