import socket
server="127.0.0.1"
port=5999
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((server,port))
message=c.recv(1024)
c.close()

print(message.decode())
