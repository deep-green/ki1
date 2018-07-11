import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
import Controller
import json
import chess

testdata = {
    'FEN': 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
    'ID_game': '2',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
}

sio = socketio.Server()

app = Flask(__name__)


#@app.route('/')
#def index():
#    """Serve the client-side application."""
#    return render_template('index.html')


@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)


# data[1] => to change in future
@sio.on('receive')
def message(sid, data):
    jsonstr = json.dumps(data)
    jsonobj = json.loads(jsonstr)
    FEN = jsonobj["FEN"]
    board = chess.Board(FEN)
    print("receive", data)
    ret = Controller.init(data)
    jsonstr1 = json.dumps(ret)
    jsonobj1 = json.loads(jsonstr1)
    move = chess.Move.from_uci(jsonobj1["Move"])
    board.push(move)
    retFEN = board.fen()
    retVal = {"FEN": retFEN,
           "ID_game": jsonobj1["ID_game"]}
    print(retVal)
    sio.emit('makeMove', retVal, room=sid)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('localhost', 8008)), app)
