'''
Created on 12-Apr-2017

@author: anuj_
'''
import threading
import socket


class WebServer(threading.Thread):
    def __init__(self,clientConn):
        threading.Thread.__init__(self)
        self.clientConn = clientConn
    def run(self):
        print clientConn
        (client,(ip,port)) = clientConn
        client.send("Welcome to Python multithreaded web server\n")
        data = "dummy"
        while len(data):
            data = client.recv(2048)
            client.send(data)

tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSocket.bind(("0.0.0.0",8000))
tcpSocket.listen(5)
while True:
    clientConn = tcpSocket.accept()
    current = WebServer(clientConn)
    current.start()
