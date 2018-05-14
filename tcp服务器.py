from socket import *
server_socket=socket(AF_INET,SOCK_STREAM)

server_socket.bind(("",8899))
print("----------1-------------")
server_socket.listen(5)# unsigned 最多有五个客户端可以同时和我沟通
print("----------2-------------")
clientSocket,clientInfo=server_socket.accept()# 返回值很重要
#clientSocket 表示这个新的客户端
#clientInfo 表示这个新的客户端的ip以及port

#收数据现在是clientSocket接受数据
print("----------3-------------")
recvData=clientSocket.recv(1024)
print("%s:%s"%(str(clientInfo),recvData.decode("gb2312")))

clientSocket.close()

server_socket.close()





