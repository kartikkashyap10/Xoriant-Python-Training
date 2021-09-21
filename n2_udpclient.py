import socket

msgFromClient = "hello udp server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ('127.0.0.1', 20001)

bufferSize = 1024

UDPCLIENTSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #1

UDPCLIENTSOCKET.sendto(bytesToSend, serverAddressPort) #2

msgFromServer = UDPCLIENTSOCKET.recvfrom(bufferSize) #3

msg = "message from server: {}".format(msgFromServer[0])
print(msg)