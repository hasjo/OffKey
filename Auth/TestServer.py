from flask import Flask

APP = Flask(__name__)

@APP.route('/api/auth/<username>', methods=['GET'])
def test_rest(username):
    if username == 'jordan':
        return 'UR GOOD'
    else:
        return 'GET OUTTA HERE'

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
