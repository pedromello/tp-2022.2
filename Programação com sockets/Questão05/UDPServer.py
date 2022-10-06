import email
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("The server is ready")

email = "tp@ic.ufrj.br"
senha = "umasenhamuitoconfidencial"

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()
    # split the message into email and password
    emailClient, senhaClient = decodedMessage.split(' ')
    if emailClient != email:
        serverSocket.sendto("Email incorreto".encode(), clientAddress)
        pass
    
    if senhaClient != senha:
        serverSocket.sendto("Senha incorreta".encode(), clientAddress)
        pass
    
    serverSocket.sendto("Login efetuado com sucesso! A mensagem secreta é: A fuinha corre a meia noite".encode(), clientAddress)