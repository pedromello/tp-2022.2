from socket import *
import threading
import time
serverName = 'localhost'
serverPort = 12000

def np_thread_func(name):
    count = 1
    while count < 10:
        with socket(AF_INET, SOCK_STREAM) as clientSocket:
            clientSocket.connect((serverName, serverPort))
            sentence = str(count)
            count += 1

            clientSocket.send(sentence.encode())

            modifiedSentence = clientSocket.recv(2048)

            print('Thread ', name, ' - From Server:', modifiedSentence.decode())

            clientSocket.close()
    print('Thread ', name, ' - Finished')

def p_thread_func(name):
    count = 1
    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        #clientSocket.setsockopt(clientSocket.SOL_SOCKET, SO_KEEPALIVE, 2)
        clientSocket.connect((serverName, serverPort))
        while count < 10:
                sentence = str(count)
                count += 1

                clientSocket.send(sentence.encode())

                modifiedSentence = clientSocket.recv(2048)

                print('Thread ', name, ' - From Server:', modifiedSentence.decode())
        print('Thread ', name, ' - Finished')

# Start 100 No persistent threads 
for i in range(100):
    x = threading.Thread(target=p_thread_func, args=("N" + str(i),))
    x.start()

# Start timer
start = time.time()

while threading.active_count() > 1:
    time.sleep(1)
# Stop timer
end = time.time()

print('All threads finished')
print('Time elapsed: ', end - start)