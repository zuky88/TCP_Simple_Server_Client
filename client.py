#!/usr/bin/env python3

import threading
import datetime
import time
import socket
import sys

ADDRESS = '192.168.1.11' # Server Address
PORT = 12345 # Server Port 
BUFSIZE = 4096

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ADDRESS, PORT))

def clientMain():
    data = 0
    while True:
        time.sleep(1)
        data += 1
        server.send(str(data).encode("UTF-8"))
        now = datetime.datetime.now()
        print('[clientA]Send:{0} [{1}]'.format(data, now))

if __name__ == '__main__':
    try:
        s = threading.Thread(target = clientMain,args=())
        s.setDaemon(True)
        s.start()
        while True:
            c = sys.stdin.read(1)
            if c == 'q':
                sys.exit()
    except KeyboardInterrupt:
        server.close()
        print('[main]Socket close.')
        sys.exit(1)

