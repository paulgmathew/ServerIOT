import socket 
import sys

# create TCP/IP SOCKET 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost',11500)
print>> sys.stderr,'starting up on %s port %s' %server_address
sock.bind(server_address)
sock.listen(1)
while True:
	#wait for a connection
	print>>sys.stderr,'waiting for a connection'
	connection,client_address = sock.accept()
	try:
		print >>sys.stderr,'connection from',client_address
		#receive the data in small chunks and reransmit it 
		while True:
			data = connection.recv(16)
			print >> sys.stderr,'sending data back to the client'
			if data:
				print >> sys.stderr,'sending data back to the client %s',data
				connection.sendall(data)
			else:
				print >> sys.stderr,'no ____more data from ',client_address
				break
	finally:
		#clean up the connection 
		connection.close()
		 
