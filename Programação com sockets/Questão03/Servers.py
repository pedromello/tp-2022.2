from socket import *
import threading



def tcpServer(name):
    serverPort = 13200
    totalServed = 0

    serverSocket = socket(AF_INET, SOCK_STREAM)

    serverSocket.bind(('', serverPort + name))
    serverSocket.listen(1)

    print("The server ", name, " is ready to receive")

    while True:
        try:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(2048).decode()
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())
            connectionSocket.close()
            totalServed += 1
            print("Server ", name, " Served a client. Total served: ", totalServed)
        except:
            pass

def udpServer(name):
    serverPort = 13200
    totalServed = 0

    serverSocket = socket(AF_INET, SOCK_DGRAM)

    serverSocket.bind(('', serverPort + name))

    print("The server ", name, " is ready to receive")

    while True:
        try:
            message, clientAddress = serverSocket.recvfrom(2048)
            modifiedMessage = message.decode().upper()
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
            totalServed += 1
            print("Server ", name, " Served a client. Total served: ", totalServed)
        except:
            pass


# Create 10 servers
for i in range(10):
    if i < 5:
        x = threading.Thread(target=tcpServer, args=(i+1,))
    else:
        x = threading.Thread(target=udpServer, args=(i+1,))
    x.start()

print("All servers started, ports from 13201 to 13210")

while True:
    pass