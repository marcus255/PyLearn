#!python
import socket
import time

host = '127.0.0.1'
port = 6666

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quitting = False
print("Server started.")

while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        dataStr = str(data.decode())
        if "Quit" in dataStr:
            quitting = True
        if addr not in clients:
            clients.append(addr)
        print(time.ctime(time.time()) + str(addr) + " " + dataStr)
        for client in clients:
            s.sendto(data, client)
    except:
        pass
s.close()
