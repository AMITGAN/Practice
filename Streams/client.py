import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 3000))
while True:
    n = input()
    sock.send(n.encode())
    pata = sock.recv(1024)
    print (pata.decode())
    if n == "exit":
        break
sock.close()