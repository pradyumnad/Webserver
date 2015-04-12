import socket

__author__ = 'pradyumnad'

from socket import *
import re

PORT = 12345



def getrequestdata(data):
    string = bytes.decode(data)
    requestdata = {}
    list = string.split(' ')
    request_method = list[0]
    requestdata["Method"] = request_method
    m = re.search("[a-zA-Z0-9]*(.html|.htm)", list[1])

    requestdata["FileName"] = "" if m is None else m.group(0)
    return requestdata

if __name__ == '__main__':
    serverSocket = socket(AF_INET, SOCK_STREAM)
    host = gethostname()
    info = getaddrinfo(host, PORT)
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
            f = open(filename)

            client.send(f.read())
            # client.send("Thank you for connecting")
            print("HTML sent to Client.")
        except IOError:
            print("Exception.")
            client.send("HTTP/1.1 404, File not found.\n")

        client.close()
    serverSocket.close()