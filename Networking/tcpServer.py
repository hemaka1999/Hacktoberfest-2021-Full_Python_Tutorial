import socket
from socket import *
import json

serverPort = 6108
serverSocket = socket(AF_INET, SOCK_STREAM)



serverSocket.bind(("", serverPort))
serverSocket.listen(1)

# TCP Server
print("listening on PORT 6108.......")

while 1:

	connectionSocket, addr = serverSocket.accept()
	data = connectionSocket.recv(1024)

	# De-serializing data
	data_loaded = json.loads(data)
	
	print(" Sent : ", data_loaded)
	
	# Sending response
	connectionSocket.send(str.encode("he he"))


connectionSocket.close()