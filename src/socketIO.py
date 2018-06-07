from socketIO_client import SocketIO, BaseNamespace

class DeepGreenNamespace(BaseNamespace):

    def on_aaa_response(*args):
        print('on_aaa_response', args)
    def on_connect(self):
        print('connect')
    def on_disconnect(self):
        print('disconnect')
    def on_reconnect(self):
        print('reconnect')

socketIO = SocketIO('localhost', 5000)
deepgreen_namespace = socketIO.define(DeepGreenNamespace, '/deep-green')
deepgreen_namespace.on('aaa',DeepGreenNamespace.on_aaa_response)
deepgreen_namespace.on('reply',DeepGreenNamespace.on_aaa_response)
deepgreen_namespace.emit('chat message','Hello')

# Listen
#socketIO.on('receive', on_receive_response)
#socketIO.emit('Test')
socketIO.wait()
