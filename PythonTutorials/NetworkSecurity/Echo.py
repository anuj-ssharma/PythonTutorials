'''
Created on 11-Apr-2017

@author: anuj_
'''
import socket
import threading

class WorkerThread(threading.Thread):
    def __init__(self,clientConnection):
        threading.Thread.__init__(self)
        self.clientConnection = clientConnection
    
    def run(self):
        (client,(ip,port)) = clientConnection
        client.send("Hello and welcome to Anuj's Python Echo program\n")
        data = "dummy"
        while len(data):
            data = client.recv(2048)
            client.send(data)
        #tcpSocket.close()

# client.send("Hello and welcome to Anuj's Python Echo program\n")
# data= "dummy"
# while len(data):
#     data = client.recv(2048)
#     client.send(data)
# tcpSocket.close()



tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpSocket.bind(("0.0.0.0",8000))
tcpSocket.listen(2)


clientConnection = tcpSocket.accept()
worker = WorkerThread(clientConnection)
worker.setDaemon(True)
worker.start()