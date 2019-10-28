from flask import Flask, jsonify, request, json, redirect, url_for
from flask_cors import CORS
from flask_bcrypt import Bcrypt

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return redirect(url_for('register'))


@app.route('/register/', methods=['POST'])
def register():
    login = request.get_json()['login']
    password = bcrypt.generate_password_hash(
        request.get_json()['password']).decode('utf-8')

    if login == "lukasz":
        resp = jsonify('Login unavailable')
    elif login == '':
        resp = jsonify('Username is required field.')
    else:
        resp = jsonify('Username available')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
