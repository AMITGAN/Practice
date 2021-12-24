import socket
from DH_protocol import DH_Endpoint

with open('Ports.txt', 'w') as file:
    file.write("Порты:\n")

HOST = '127.0.0.1'
PORT = 8082

sock = socket.socket()
sock.connect((HOST, PORT))

clientDH = DH_Endpoint()
clientDH.bunch_of_public_keys()

keys = str(clientDH.client_public_key)+' '+str(clientDH.server_public_key)
sock.send(keys.encode())


msg = sock.recv(1024).decode()
if msg == "Access is allowed":
    print(msg+"\nДля выхода напишите \"exit\"" + "\nЧтобы сменить протр напишите \"Change port\"")
    server_key_partial = int(sock.recv(1024).decode())


    client_partial_key = clientDH.generate_partial_key()
    sock.send(str(client_partial_key).encode())

    clientDH.generate_full_key(server_key_partial)

    while True:
        msg = input(""">>""")
        if msg == 'exit' or msg == 'Exit':
            sock.send(clientDH.encrypt_message(msg).encode())
            break

        sock.send(clientDH.encrypt_message(msg).encode())
        if msg == 'Change port':
            msg2 = input("""Введите новый порт: """)
            sock.send(clientDH.encrypt_message(msg2).encode())
            sock.close()
            HOST = '127.0.0.1'
            PORT = int(msg2)
            sock = socket.socket()
            sock.connect((HOST, PORT))
            with open('Ports.txt', 'a+') as file:
                in_file = file.read()
                file.write(msg2 + "\n")
                file.close()


    sock.close()

else:
    print("Провал подключения")
    sock.close()