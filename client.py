# Import socket module
import socket
import time			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect '192.168.122.51',
port = 12345				

# connect to the server on local computer
s.connect(('192.168.122.90', port))
#s.connect(('192.168.122.51', port))
# receive data from the server
msg = s.recv(1024)
# close the connection

print(msg.decode("utf-8"))
s.close()

print("=============================")

s1 = socket.socket()		

# Define the port on which you want to connect '192.168.122.51',
port = 12345				

# connect to the server on local computer
s1.connect(('192.168.122.51', port))
#s.connect(('192.168.122.51', port))
# receive data from the server
msg = s1.recv(1024)
# close the connection

print(msg.decode("utf-8"))
s1.close()


#Referance: https://www.geeksforgeeks.org/socket-programming-python/
#Referance:https://stackoverflow.com/questions/33003498/typeerror-a-bytes-like-object-is-required-not-str
