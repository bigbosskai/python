import struct
from socket import *
import sys
SENDDATA=struct.pack("!H8sb5sb",1,"test.jpg".encode("ASCII"),0,"octet".encode("ASCII"),0)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(SENDDATA,("114.213.155.7",69))
imgdata=b""

def recv():
	#表示收到数据的长度
	#如果小于516就结束
	global imgdata
	flag=True
	recv_data=udp_socket.recvfrom(1024)
	downM=struct.unpack("!H",recv_data[0][0:2])[0]
	if downM==5: #data
		print("文件不存在")
		udp_socket.close()
		sys.exit(0)

	datalen=len(recv_data[0])
	if datalen<516:
		flag=False

	print("=>收到多少个字节: %d"%(datalen))
	blackN=struct.unpack("!H",recv_data[0][2:4])[0]
	#取数据
	

	imgdata=imgdata+recv_data[0][4:]
	ami_port=recv_data[1][1]#对方的随即端口
	ami_ip=recv_data[1][0]
	return flag,ami_ip,ami_port,blackN


flag,ami_ip,ami_port,blackN=recv()
while flag==True:
	flag,ami_ip,ami_port,blackN=recv()
	#再次基础上
	udp_socket.sendto( struct.pack("!HH",4,blackN) ,(ami_ip,ami_port))

#写入文件
print(len(imgdata))
imf=open("1test.jpg","wb")
imf.write(imgdata)
imf.close()