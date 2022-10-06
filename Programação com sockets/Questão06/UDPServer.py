userName = ""
global_state = 0

def nextState(message):
    if state == 6:
        state = 0

    if state == 0:
        state = 1
        return "Olá! Bem-vindo! Qual o seu nome?"
    if state == 1:
        userName = message
        state = 2
        return "Certo, " + userName + "! Digite o número que corresponde a opção desejada: (1) Agendar um horario de monitoria (2) Listar proximas atividades da disciplina (3) Email do professor (4) Sair"
    if state == 2:
        if message == "1":
            state = 6
            return "Para agendar a monitoria basta enviar um email para cainafigueiredo@poli.ufrj.br"
        if message == "2":
            state = 6
            return "Fique atento para as datas das proximas atividades que vem por ai! P1: 26 de maio de 2022. Lista 3: 29 de maio de 2022"
        if message == "3":
            state = 6
            return "Quer falar com o professor? O email é sadoc@dcc.ufrj.br"
        state = 6
    if state == 6:
        return "Obrigado por utilizar o nosso serviço! Até a próxima!"



from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print("The server is ready")


# States:
# 0 - waiting
# 1 - welcome
# 2 - services
# 3 - schedule a meeting
# 4 - pending tasks
# 5 - professor email
# 6 - exit


while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    response = nextState(message.decode())
    serverSocket.sendto(response.encode(), clientAddress)