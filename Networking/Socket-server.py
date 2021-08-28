import socket

server="127.0.0.1"
port=5999
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s1.bind((server,port))
s1.listen()
while True:
    client,address=s1.accept()
    print(f"connect to {address}")
    client.send("you are connected".encode())
    client.close()