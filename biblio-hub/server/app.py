from flask import Flask, jsonify, request, redirect, url_for, make_response, send_file, send_from_directory
from flask_cors import CORS
from functools import wraps
import datetime
import uuid
import jwt
import redis

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'customerobsessed'
db = redis.Redis(host='redis', port=6379, decode_responses=True)
db.flushdb()

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


@app.route('/register/', methods=['POST', 'PUT'])
def register():
    req = request.get_json()
    login = req['login']
    if login and db.hget(login, 'login') == login:
        resp = jsonify('Login unavailable')
        return resp
    else:
        resp = jsonify('Username available')
    if request.method == 'PUT':
        password, email = req['password'], req['email']
        db.hset(login, 'login', login)
        db.hset(login, 'password', password)
        db.hset(login, 'email', email)
    return resp


@app.route('/login/', methods=['POST'])
def login():
    auth = request.get_json()
    login, password = auth['login'], auth['password']
    if auth and db.hget(login, 'password') == password:
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
        'year': 1998,
        'file': ''
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'year': 2008,
        'file': ''
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'year': 1887,
        'file': ''
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
            'year': post_data.get('year'),
            'file': post_data.get('file'),
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
            'year': post_data.get('year'),
            'file': post_data.get('file')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


def save_file(file):
    path = "files/" + file.filename
    file.save(path)
    db.hset(file.filename, "filename", file.filename)
    db.hset(file.filename, "path", path)
    db.hset("filenames", 'filename', file.filename)


@app.route('/file/', methods=['POST', 'PUT'])
def file():
    if request.method == 'POST':
        file = request.files['file']
        save_file(file)
        return make_response('File uploaded', 200)
    if request.method == 'PUT':
        filename = db.hget('filenames', 'filename')
        return send_file('files/' + filename, mimetype='application/pdf',
                         as_attachment=True, attachment_filename=filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
