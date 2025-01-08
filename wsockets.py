import socketio

sio = socketio.Client()


@sio.event(namespace='/recordInfo')
def connect():
    print("Successfully connected to the server")


@sio.event(namespace='/recordInfo')
def disconnect():
    print("Disconnected from the server")


@sio.on('record', namespace='/recordInfo')
def handle_record(data):
    record_count = data.get('recordCount', 0)
    record_size = data.get('recordSize', 0)
    print(f"Record Count: {record_count:,}")
    print(f"Total File Size: {record_size}")


# Connect to the server
sio.connect('https://waifuvault.moe/recordInfo', socketio_path='socket.io/recordInfo', namespaces=['/recordInfo'])
sio.wait()
