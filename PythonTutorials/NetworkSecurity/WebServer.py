'''
Created on 12-Apr-2017

@author: anuj_
'''

import SocketServer
import SimpleHTTPServer


class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/admin":
            self.wfile.write("This page is only for admins")
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpServer = SocketServer.TCPServer(("0.0.0.0",10001),HTTPRequestHandler)
httpServer.serve_forever()
