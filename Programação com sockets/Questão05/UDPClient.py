from socket import *
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    email = input('Insira seu email:')
    senha = input('Insira sua senha:')
    message = email + ' ' + senha

    clientSocket.sendto(message.encode(), (serverName, serverPort))

    serverMessage, serverAddress = clientSocket.recvfrom(2048)
    print(serverMessage.decode())

    if serverMessage.decode().find('Login efetuado com sucesso!') != -1:
        break

clientSocket.close()