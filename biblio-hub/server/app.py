from flask import Flask, jsonify, request, json, redirect, url_for
# from flask_mysqldb import MySQL
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
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(
        request.get_json()['password']).decode('utf-8')
    result = {
        'email': email,
        'password': password
    }
    if email == "lukasz.knigawka@outlook.com":
        return jsonify({'error': 'Email address already in the database'})
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
