from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.bind(('', serverPort))

message = input('Input lowercase sentence:')

#clientSocket.sendto(message.encode(), (serverName, serverPort))

while True:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

clientSocket.close()