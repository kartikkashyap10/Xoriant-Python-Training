# socket.socket(socket_family, type_socket, protocol=value)

# listen()
# bind()
# accept
# connect
# send
# recv
# sendto
# close

# port must be greater than 1024
import asyncio.constants
import socket

host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connection established!", addr)
        while True:
            data = conn.recv(1024)
            print("Received at server", repr(data))
            if not data:
                break
            #conn.sendall(data)
            conn.sendall(b'Hello from server')