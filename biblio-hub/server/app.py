import datetime
import jwt
from flask import Flask, jsonify, request, redirect, url_for, make_response
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'customerobsessed'

CORS(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/register/', methods=['POST'])
def register():
    login = request.get_json()['login']
    if login == "lukasz":
        resp = jsonify('Login unavailable')
    else:
        resp = jsonify('Username available')
    return resp


@app.route('/login/', methods=['POST'])
def login():
    auth = request.json

    if auth and auth['password'] == 'password':
        token = jwt.encode({'user': auth['login'],
                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Authorization failed', 401,
                         {'WWW-Authenticate': 'Basic realm="Login required"'})


@app.route('/hub/')
def hub():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
