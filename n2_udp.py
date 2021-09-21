# setting up socket using UDP (User Datagram Protocol)
import socket

localIP = '127.0.0.1'
localPort = 20001

bufferSize = 1024 # size of the message
msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

# Creating a socket using the User Datagram Protocol
UDPSERVERSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #1

UDPSERVERSOCKET.bind((localIP, localPort)) #2

print("UDP server up and listening.....")

while True:
    bytesAddressPair = UDPSERVERSOCKET.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from client: {}".format(message)
    clientIP = "Client IP address: {}".format(address)

    print(clientMsg)
    print(clientIP)
    UDPSERVERSOCKET.sendto(bytesToSend, address)

