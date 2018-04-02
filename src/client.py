import socket
import sys

PORT = 3000

infos = socket.getaddrinfo('127.0.0.1', PORT)

stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]

client = socket.socket(*stream_info[:3])

client.connect(stream_info[-1])

message = str(sys.argv[1])

client.sendall(message.encode('utf8'))

buffer_length = 8

message_complete = False

server_msg = b''
while not message_complete:
    part = client.recv(buffer_length)
    server_msg += part
    # print(part.decode('utf8'))
    if len(part) < buffer_length:
        break

server_msg = server_msg.decode('utf8')
print(server_msg)

client.close()
