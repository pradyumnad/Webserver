__author__ = 'pradyumnad'

from socket import *
import sys
from thread import *
import os

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5556  # Arbitrary non-privileged port

s = socket(AF_INET, SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
s.listen(10)
print 'Socket now listening'


def clientthread(conn, addr):
    conn.send('Welcome to the server. Type something and hit enter\n')

    while True:
        # Receiving from client
        data = conn.recv(1024)
        print(addr)
        print(data)

        if os.path.isfile(data):
            f = open(data)
            print "file exist at this time"
            conn.send(f.read())
            print(data+" sent to Client.")
        else:
            conn.send("No such file.")

        # reply = 'OK...' + data
        if not data:
            break
        # conn.sendall(reply)
    conn.close()


while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    start_new_thread(clientthread, (conn, addr))

    # s.close()