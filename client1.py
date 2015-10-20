import socket
import threading
import socket
import time
import hashlib
import json
import random

TCP_IP = '127.0.0.1'
TCP_PORT = 11500
BUFFER_SIZE = 1024

def connect():
	sock = socket.socket()
	sock.connect((TCP_IP, port))
	sock.listen(1)
	while 1:
		print sock.recv(1024)	
connect()
