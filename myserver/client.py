__author__ = 'pradyumnad'

import socket
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print 'Number of arguments:', len(sys.argv), 'arguments.'
        print 'Argument List:', str(sys.argv)
    else:
        print("Usage:")
        print("python client.py server_host server_port filename")

    s = socket.socket()
    host = socket.gethostbyaddr(sys.argv[1])[0]
    port = int(sys.argv[2])
    filename = sys.argv[3]

    s.connect((host, port))
    request_data = "GET /"+filename+" HTTP/1.1\n"+\
        "Host: "+sys.argv[1]+":"+str(port)+"\n"+\
        "Connection: keep-alive\n"+\
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\n"+\
        "User-Agent: Python Client\n"+\
        "Accept-Encoding: gzip, deflate, sdch\n"+\
        "Accept-Language: en-US,en;q=0.8\n"

    s.send(request_data)

    data = s.recv(1024)
    while len(data) > 0:
        print(data)
        data = s.recv(1024)
    s.close()