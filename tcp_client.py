from socket import *
clientSocket=socket(AF_INET,SOCK_STREAM)

clientSocket.connect(("114.213.155.7",8899))
clientSocket.send("我是汪凯".encode("gb2312"))

recvData = clientSocket.recv(1024)

print("recv %s"%recvData)
clientSocket.close()