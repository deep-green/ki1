from socketIO_client import SocketIO, BaseNamespace

testdata = {
  "FEN": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
  "ID_game": "2",
  "color": "false",
  "turns": [
    "e2e4",
    "c2c4"
  ]
}


class DeepGreenNamespace(BaseNamespace):

    def on_makeMove(*args):
        print('makeMove', args)
    def on_connect(self):
        print('connect')
    def on_disconnect(self):
        print('disconnect')
    def on_reconnect(self):
        print('reconnect')

adress = '54.93.171.91'
#adress = 'localhost'

socketIO = SocketIO(adress, 8008)
deepgreen_namespace = socketIO.define(DeepGreenNamespace, '/deep-green')
deepgreen_namespace.on('move',DeepGreenNamespace.on_makeMove)

deepgreen_namespace.emit('receive',testdata)

# Listen
#socketIO.on('receive', on_receive_response)
#socketIO.emit('Test')
socketIO.wait()
