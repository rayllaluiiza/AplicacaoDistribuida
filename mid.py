import socket
import threading
import time
import sys

ADDRESS = "127.0.0.1"
#PORT = "5000"

MIDD_ADDRESS = "127.0.0.1"
MIDD_PORT = 5000
CLIENT_PORT = 5001
CLIENT_ADRESS = "127.0.0.1"
SERVERNAME1_PORT = 5002
SERVERNAME2_PORT = 5003
SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 5004

class Midd:

	def __init__(self):
		self.tcp_socket = None
		self.function = ""
		self.valor1 = ""
		self.valor2 = ""
		self.cache = []
    		tc = threading.Thread(target=self.start)
    		tc.start()

	def start(self):
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcp_socket.bind((MIDD_ADDRESS, MIDD_PORT))
		self.tcp_socket.listen(5)
		while True:
			tc2 = threading.Thread(target=self.nomes, args=(self.tcp_socket.accept()))
			tc2.start()
	
	def nomes(self, connection, client):
		msg = connection.recv(20)
		msg = msg.split(" ")
		self.function = msg[0]
		self.valor1 = msg[1]
		self.valor2 = msg[2]
		connection.close()
		self.connectServidorNome(msg[0])

	def connectServidorNome(self, funcao):
		#if funcao in self.cache:
		##self.connectServer(funcao)
		#else:
		try:
			udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			address = (MIDD_ADDRESS, SERVERNAME1_PORT)
			udp_socket.sendto(str(funcao), address)
			print "entrei aqui 1"
			endereco, cli = udp_socket.recvfrom(1024)
			print endereco
			udp_socket.close()
			teste = endereco
		except:
			udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			adress = (MIDD_ADDRESS, SERVERNAME2_PORT)
			udp_socket.sendto(str(funcao), adress)
			print "entrei aqui 6"
			end, client = udp_socket.recvfrom(1024)
			print end
			udp_socket.close()
			teste = end

		self.connectServer(teste)

	def connectServer(self, endereco):
		kk = 'Soma'
		mensagem = self.function +" " +self.valor1 +" " +self.valor2
		endereco = endereco.split(" ")
		print endereco

		for i in range(len(endereco)):
			self.cache.append({self.function: endereco[i]})

		print self.cache

		if kk in self.cache[0]:
			print 'ola'
		else:
			print 'ola 2'
		
		'''
		try:
			print 'testandoo ...'
			tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			tcp_socket.settimeout(1)
			#tcp_socket.connect((endereco, SERVER_PORT))
			tcp_socket.connect((ADDRESS, int(endereco)))
			tcp_socket.send(mensagem)
			msgCliente = tcp_socket.recv(1024)
			tcp_socket.close()

		except socket.timeout:
			print 'teste 6'
			msgCliente =""

		self.connectCliente(msgCliente)
		'''
	def connectCliente(self, msgCliente):
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.connect((CLIENT_ADRESS, CLIENT_PORT))
		tcp_socket.send(msgCliente)
		
		tcp_socket.close()

if __name__ == "__main__":
	midd = Midd()
