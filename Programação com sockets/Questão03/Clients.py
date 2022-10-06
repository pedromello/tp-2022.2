import random
from socket import *
import threading
import time
serverName = 'localhost'
serverPort = 13200

def tcp_thread_func(name):
    count = 1
    while True:
        try:
            clientSocket = socket(AF_INET, SOCK_STREAM) 
            # Random number between 1 and 5
            port = random.randint(1, 5)
            clientSocket.connect((serverName, serverPort + port))
            sentence = str(count)
            count += 1

            clientSocket.send(sentence.encode())

            modifiedSentence = clientSocket.recv(2048)

            print('Thread ', name, ' - From TCP Server ', port, ':', modifiedSentence.decode())

            clientSocket.close()
            time.sleep(2)
        except Exception as e:
            print(e)
            pass


def udp_thread_func(name):
    count = 1
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    while True:
        try:
            # Random number between 6 and 10
            port = random.randint(6, 10)
            message = str(count)
            count += 1

            clientSocket.sendto(message.encode(), (serverName, serverPort + port))

            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            print('Thread ', name, ' - From UDP Server ', port, ':', modifiedMessage.decode())
        except Exception as e:
            print(e)
            pass

# Start 100 No persistent threads 
for i in range(50):
    if i < 25:
        x = threading.Thread(target=tcp_thread_func, args=(i+1,))
        x.start()
    else:  
        x = threading.Thread(target=udp_thread_func, args=(i+1,))
        x.start()



while threading.active_count() > 1:
    time.sleep(1)