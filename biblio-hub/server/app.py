from flask import Flask, jsonify, request, json, redirect, url_for
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/register/', methods=['POST'])
def register():
    # jesli login lub haslo nie sa w bazie, to nie wpuszczam
    login = request.get_json()['login']
    if login == "lukasz":
        resp = jsonify('Login unavailable')
    else:
        resp = jsonify('Username available')
    return resp


@app.route('/login/', methods=['POST'])
def login():
    # jesli login i haslo sa w bazie, to wpuszczam!
    login = request.get_json()['login']
    if login == "lukasz":
        resp = jsonify('Login unavailable')
    else:
        resp = jsonify('Username available')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')
