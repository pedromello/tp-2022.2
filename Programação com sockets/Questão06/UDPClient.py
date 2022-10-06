from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto("00".encode(), (serverName, serverPort))

while True:
    response, serverAddress = clientSocket.recvfrom(2048)
    print(response.decode())

    message = input('--> ')

    clientSocket.sendto(message.encode(), (serverName, serverPort))


    

clientSocket.close()