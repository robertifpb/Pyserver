import socket

def start_client():
    #Configurando o servidor cliente
    host = '127.0.0.1' #Endereço do servidor
    port = 12345 #Porta de comunicação

    #Criando um socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        #Conectando ao servidor
        client_socket.connect((host,port))
        print(f'Conectado ao servidor {host}:{port}')

        while True:
            #Obter a mensagem do usuário
            message = input('Digite uma mensagem (ou sair ou encerrar):')

            if message.lower() == 'sair':
                break

            #Enviar mensagem ao servidor
            client_socket.sendall(message.encode('utf-8'))

            #Receber resposta do servidor
            data = client_socket.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")

        print('Conexão encerrada')

if __name__ == '__main__':
    start_client()