import socket
from threading import Thread
from datetime import datetime
import os

def server():
    with open('Settings.txt', 'r') as file:
        k = file.read()
        k = k.split(' ')
    sock = socket.socket()
    try:
        sock.bind(('', int(k[0])))
        print("Запуск сервера. Порт: ", int(k[0]))
    except OSError:
        sock.bind(('', 8080))
        print("Запуск сервера. Порт: ", 8080)
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        thread = Thread(target=to_do, args=(conn, addr))
        thread.start()

def to_do(conn, addr):
    with open('Settings.txt', 'r') as file:
        k = file.read()
        k = k.split(' ')
    with open(k[2], 'rb') as file:
        for_len = file.read()
    resp = f'HTTP/1.1 200 OK\n\
        Server: SelfMadeServer v0.0.1\n\
        Date: {datetime.now()}\n\
        Content-Type: text/html\n\
        Content-length: {len(for_len)}\n\
        Connection: close\n\n'
    user = conn.recv(int(k[1])).decode()
    path = user.split(" ")[1]
    if path == '/' or path == '/index.html':
        with open(k[2], 'rb') as file:
            filename, file_extension = os.path.splitext(k[2])
            if (file_extension != '.html'):
                conn.send(("Error: 403").encode('utf-8'))
            else:
                answer = file.read()
                conn.send(resp.encode('utf-8') + answer)
    else:
        conn.send(("Error: 404").encode('utf-8'))
    print("Connected ", addr)

if __name__ == "__main__":
    server()

#localhost:80