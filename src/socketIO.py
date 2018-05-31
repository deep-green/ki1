from socketIO_client import SocketIO, LoggingNamespace

def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_receive_response(*args):
    print('on_aaa_response', args)

socketIO = SocketIO('ec2-54-93-171-91.eu-central-1.compute.amazonaws.com', 5000, LoggingNamespace)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)

# Listen
socketIO.on('receive', on_receive_response)
socketIO.emit('Test')
socketIO.wait(seconds=1)
