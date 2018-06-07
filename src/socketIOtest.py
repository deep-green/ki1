import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)

@app.route('/deep-green')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect', namespace='/deep-green')
def connect(sid, environ):
    print("connect ", sid)
    sio.emit('aaa','Test',room=sid)

@sio.on('chat message', namespace='/deep-green')
def message(sid, data):
    print("message ", data)
    sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/deep-green')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
