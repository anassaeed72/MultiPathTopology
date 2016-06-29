import time
import random
import socket
import sys
def writeToFile(data):
    with open("Client/File"+host+".txt","a") as myfile:
        myfile.write(data)
        myfile.write("\n")
host = sys.argv[1]
port = int(sys.argv[2])
size = 1024
packetsRecieved =0
for i in range(10):
	for i in range(5):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "establishing connection"
		s.connect((host,port))
		print "establised connection"
		time.sleep(3)
		s.send('Hello, world')
		print "data sent"
		data = s.recv(size)
		print "data recieved " + data
		s.close()
		print " connection closed"
		packetsRecieved = packetsRecieved + 1
		print "packets Received " + str(packetsRecieved)
	print "Packets Received " + str( packetsRecieved)
	writeToFile("Packets Received " + str(packetsRecieved))
	time.sleep(10)

