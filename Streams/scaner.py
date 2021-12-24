import os
import socket
import threading
import pyprind


print(threading.active_count())
ports = []
done = []
for i in range (0, 100):
    ports.append(0)
for i in range (0, 100):
    done.append(0)

def open (port):
    sock = socket.socket()
    sock.settimeout(0.5)
    try:
        sock.connect(('www.mail.ru', port))
    except:
        sock.close()
        done[port] = 1
    else:
        ports[port] = 1
        done[port] = 1
        sock.close()


t = [threading.Thread(target=open, args=[i]) for i in range(1, 100)]
[t1.start() for t1 in t]

print(threading.active_count())
a = 0
bar = pyprind.ProgBar(99)
while a < 99:
    b = 0
    for i in range(0, 100):
    	b += done[i]
    n = b - a
    for i in range(n):
        bar.update()
    a = b

[t1.join() for t1 in t]
for i in range (0, 100):
    if ports[i] == 1:
        print ("Port ", i + 1, "opened")
