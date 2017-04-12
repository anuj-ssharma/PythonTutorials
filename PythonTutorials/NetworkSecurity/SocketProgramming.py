'''
Created on 11-Apr-2017

@author: anuj_
'''
import socket

# 1. Address family, for internet its AF_INET
# 2. Kind of Socket
tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind to a port and interface
#multihomed - multiple interfaces therefore each interface could have a different IP address

tcpSocket.bind(("0.0.0.0",8000))

#Start inviting connections to that port and interface

tcpSocket.listen(2)

print "Waiting for a client..."

(client,(ip,port))=tcpSocket.accept()
#By default accept is a blocking call
client.send("welcome to the python course")

data = "dummy"

while len(data):
    data  = client.recv(2048)
    client.send(data)


client.close()