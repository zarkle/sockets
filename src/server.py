from datetime import datetime
import socket

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
    socket.IPPROTO_TCP)

PORT = 3000

address = ('127.0.0.1', PORT)

sock.bind(address)

try:
    sock.listen(1)

# time_date = datetime.now().strftime('%H:%M:%S %d-%m-%y')

    print('--- Starting server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))
    conn, addr = sock.accept()

    buffer_length = 8

    message_complete = False

    message = b''
    while not message_complete:
        part = conn.recv(buffer_length)
        # print(part.decode('utf8'))
        message += part
        if len(part) < buffer_length:
            break

    message = message.decode('utf8')
    print(message)
    # message = 'thanks for the note'

    conn.sendall(message.encode('utf8'))

except KeyboardInterrupt:
    try:
        conn.close()
    except NameError:
        pass

    sock.close()
    print('--- Stopping server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))

conn.close()
sock.close()
print('--- Stopping server on port {} at {} ---'.format(PORT, datetime.now().strftime('%H:%M:%S %d-%m-%y')))
