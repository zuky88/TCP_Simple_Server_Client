#!/usr/bin/env python3

import threading
import datetime
import socket
import sys

ADDRESS = '192.168.1.11' # Server Address
PORT = 12345 # Server Port
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDRESS, PORT))
server.listen()

def serverMain(clientno, client):
    while True:
        msg = client.recv(BUFSIZE).decode()
        if len(msg) == 0:
            break
        now = str(datetime.datetime.now())
        print("[server ]Recv (client:{0}):{1}[{2}]".format(clientno, msg, now))
    server.close()
    print('[server]Socket close.')
    sys.exit(1)

def thread_start():
    clientno = 0
    while True:
        print('[server]Waiting access from client.')
        client, address = server.accept()
        now = str(datetime.datetime.now())
        clientno += 1
        print("[server]Conected client({0}, {1}, {2})[{3}]".format(clientno, client, address, now))
        t = threading.Thread(target = serverMain, args=(clientno, client,))
        t.setDaemon(True)
        t.start()


if __name__ == '__main__':
    try:
        thread_start()
    except KeyboardInterrupt:
        server.close()
        print('[clientA]Socket close.')
        sys.exit(1)





