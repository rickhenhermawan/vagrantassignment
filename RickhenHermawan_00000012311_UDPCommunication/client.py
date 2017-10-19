import socket

UDP_IP = "172.32.119.1"
UDP_PORT = 5005
MESSAGE = "Hello, My Name is Rickhen Hermawan"


print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("Message:", MESSAGE)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))