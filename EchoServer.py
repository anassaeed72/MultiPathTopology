import SocketServer
import socket
import re
import sys
HOST = "localhost"
PORT = 12321

# this server uses ThreadingMixIn - one thread per connection
# replace with ForkMixIn to spawn a new process per connection
def check_server(address, port):
    # Create a TCP socket
    s = socket.socket()
    print "Attempting to connect to %s on port %s" % (address, port)
    try:
        s.connect((address, port))
        return True
    except socket.error, e:
        return False
while check_server("127.0.0.1",PORT):
    PORT = PORT +1
class EchoServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # no need to override anything - default behavior is just fine
    pass
 
class EchoRequestHandler(SocketServer.StreamRequestHandler):
    """
    Handles one connection to the client.
    """
    def handle(self):
        print "connection from %s" % self.client_address[0]
        while True:
            line = self.rfile.readline()
            if not line: break
            print "%s wrote: %s" % (self.client_address[0], line.rstrip())
            self.wfile.write(line)
        print "%s disconnected" % self.client_address[0]
 
 
# Create the server
server = EchoServer((HOST, PORT), EchoRequestHandler)
 
# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
print "server listening on %s:%s" % server.server_address
server.serve_forever()