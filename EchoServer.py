import SocketServer
import socket
import re
import sys
import socket

host = sys.argv[1]
port = 12321
backlog = 5
size = 1024# this server uses ThreadingMixIn - one thread per connection
# replace with ForkMixIn to spawn a new process per connection
def writeToFile(data):
    with open("Server/File"+host+".txt","a") as myfile:
        myfile.write(data )
        myfile.write("\n")
# def check_server(address, port):
#     # Create a TCP socket
#     s = socket.socket()
#     writeToFile("Attempting to connect to "+str(address)+" on port " +str(port))
#     try:
#         s.bind((host,port))

#         writeToFile('Connection Successful')
#         return True
#     except socket.error, e:
#         writeToFile('Connection Not Successful')
#         return False
# count = 0
# host = HOST
# backlog = 5
# size = 1024
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# while check_server(HOST,PORT) == False:
#     if count>1000:
#         break
#     count = count +1
#     PORT = PORT +1
# s.listen(backlog)
#
# 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
print ("server listening on " +host +" " + str(port))
writeToFile ("server listening on " +host + "  " + str(port))
while 1:
    print "in while loop"
    writeToFile("in while loop")
    client, address = s.accept()
    print "connection estableised"
    writeToFile("connection estableised")
    data = client.recv(size)
    print  "data recivevd " + data
    writeToFile("data recivevd " + data)
    if data:
        client.send(data)
        print "data echoed back"
        writeToFile("data echoed back "+ data)
    client.close() 
    print "connection closed"
    writeToFile("connection closed")
    
