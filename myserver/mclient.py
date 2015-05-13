__author__ = 'pradyumnad'

import socket
import sys

HOST = ''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print 'Number of arguments:', len(sys.argv), 'arguments.'
        print 'Argument List:', str(sys.argv)
    else:
        print("Usage:")
        print("python client.py server_host server_port filename")

    s = socket.socket()

    print("Attempting to connect " + sys.argv[1])
    # host = socket.gethostbyaddr(sys.argv[1])[0]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    s.connect((HOST, port))
    s.send(filename)

    data = s.recv(1024)
    while len(data) > 0:
        print(data)
        data = s.recv(1024)
    s.close()