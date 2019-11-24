import datetime
import uuid
import jwt
from flask import Flask, jsonify, request, redirect, url_for, make_response
from flask_cors import CORS
from functools import wraps

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'customerobsessed'

CORS(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Missing token'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token'})
        return f(*args, **kwargs)
    return decorated


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


@app.route('/logout/', methods=['POST'])
def logout():
    return make_response('Logged out', 200)


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'year': 1998
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'year': 2008
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'year': 1887
    }
]


@app.route('/hub/', methods=['GET', 'POST'])
def hub():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'year': post_data.get('year')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/hub/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'year': post_data.get('year')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
