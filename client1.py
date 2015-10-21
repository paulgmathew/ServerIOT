import socket
import sys

# create a TCP/IP socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('23.251.157.195',11500)
print >> sys.stderr,'connecting to %s port %s'%server_address
sock.connect(server_address)
try:
	#send data 
	message = "this is the message and it will be repeated"
	print >> sys.stderr,'sending"%s"'% message
	sock.sendall(message)
	amount_received = 0 
	amount_expected = len(message)	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >> sys.stderr,'received "%s"' % data
finally: 
	print >> sys.stderr,'closing socket'
	sock.close()
