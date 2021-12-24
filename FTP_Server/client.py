import socket

HOST = '127.0.0.1'
PORT = 8082

sock = socket.socket()
sock.connect((HOST, PORT))
#path = str(input("Укажите путь до рабочей директории: "))
path = "C:/Users/amirs/Desktop/Financial University/Practice/FTP_Server/Home"
sock.send(path.encode())
print("Рабочая директория:" + path)
t = True
while t:
    msg2 = str(input("Введите команду (help для вызова инструкции): "))
    if (msg2 == "exit"):
        t = False
        sock.send(msg2.encode())
    else:
        sock.send(msg2.encode())
        msg = sock.recv(2024).decode()
        print(msg)
        if (msg2 != "help"):
            msg3 = input()
            sock.send(msg3.encode())

sock.close()

