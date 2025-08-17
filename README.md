# 🖥️  Simulação de Cliente-Servidor em Python 🐍

Demonstração de um sistema básico de comunicação entre cliente e servidor, em Python, utilizando Socket TCP/IP para comunicação em tempo real. Ideal para aplicações que necessitam de troca de mensagens entre cliente e servidor de forma eficiente e escalável, e ajudando a entender como ocorre a comunicação em redes de computadores.

## ✅Funcionalidades

- Comunicação bidirecional via WebSocket.
- Implementação simples e leve.
- Fácil de entender e personalizar.

## 🛠️ Tecnologias Utilizadas

- Python
- Socket (via biblioteca `socket`)

## 📂 Estrutura do projeto

```
Pyserver/
│── src/                # Código-fonte
│   └── server.py       # Script principal do servidor
│   └── client.py       # Script principal do client
│── .gitignore          # Arquivos a serem ignorados pelo Git
└── README.md           # Documentação do projeto
```
## ▶️​​ Como Executar

### Requisitos
- Python 3.x

### 1. (Opcional) Crie e ative um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
1️⃣ Instale a dependência:

 ```
 pip install websocket-client
 ```
2️⃣ Execute o servidor:

 ```
 python server.py
 ```
3️⃣ Execute o cliente (em outro terminal):
 ```
 python client.py
 ```
4️⃣ Teste o chat:

 - Digite uma mensagem no cliente e pressione `Enter`.

 - Veja a mensagem aparecer no servidor.

 - Troque mensagens entre cliente e servidor.
