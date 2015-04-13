import socket

__author__ = 'pradyumnad'

from socket import *
import re
import os

PORT = 12345

def getrequestdata(data):
    string = bytes.decode(data)
    requestdata = {}
    list = string.split(' ')
    request_method = list[0]
    requestdata["Method"] = request_method
    m = re.search("[a-zA-Z0-9_]*(.html|.htm|.gif|.jpg|.png)", list[1])

    requestdata["FileName"] = "" if m is None else m.group(0)
    return requestdata

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    host = gethostname()
    info = getaddrinfo(host, PORT)
    print(info)
    serverSocket.bind((host, PORT))
    serverSocket.listen(5)

    while True:
        print("Ready to serve.")
        client, address = serverSocket.accept()
        print("Connection from ", address)

        try:
            data = client.recv(1024)
            string = bytes.decode(data)
            print(string)
            # Request decoding
            reqdata = getrequestdata(data)
            print(reqdata)

            filename = reqdata["FileName"]
            print("Opening "+filename)

            if filename.endswith(".gif"):
                filename = "images/"+filename

            if filename.endswith(".jpg"):
                filename = "images/"+filename

            if len(filename) == 0:
                filename = "HelloWorld.html"

            if os.path.isfile(filename):
                f = open(filename)
                print "file exist at this time"
                client.send(f.read())
                print("HTML sent to Client.")
            else:
                filename = "404Error.html"
                print("Opening "+filename)
                f = open(filename)
                client.send(f.read())

        except IOError:
            print("Exception.")
            client.send("HTTP/1.1 404, File not found.\n")

        client.close()
    # serverSocket.close()