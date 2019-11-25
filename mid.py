import socket
import threading
import time
import sys

ADDRESS = "127.0.0.1"
#PORT = "5000"
#ADDRESS_MID = ""
#ADDRESS_CLIENT = ""
#ADDRESS_SEVERNAME1 = ""
#ADDRESS_SEVERNAME2 = ""
#ADRESS_SERVER = ""

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
		self.cache = {}
    		tc = threading.Thread(target=self.start)
    		tc.start()

	def start(self):
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcp_socket.bind((MIDD_ADDRESS, MIDD_PORT))
		#self.tcp_socket.connect((ADRESS_MID, PORT))
		self.tcp_socket.listen(5)
		while True:
			tc2 = threading.Thread(target=self.nomes, args=(self.tcp_socket.accept()))
			tc2.start()
	
	def nomes(self, connection, client):
		msg = connection.recv(1024)
		msg = msg.split(" ")
		self.function = msg[0]
		self.valor1 = msg[1]
		self.valor2 = msg[2]
		connection.close()
		self.connectServidorNome()

	def connectServidorNome(self):
		if self.function in self.cache:
			print 'entrei no if do dicionario'
			self.connectServer(self.cache[self.function])

		else:
		
			try:
				udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				address = (MIDD_ADDRESS, SERVERNAME1_PORT)
				#address = ((ADRESS_MID, PORT))
				udp_socket.sendto(str(self.function), address)
				print "entrei aqui 1"
				udp_socket.settimeout(1)
				endereco, cli = udp_socket.recvfrom(1024)
				print endereco
				udp_socket.close()
				enderecos = endereco
			except:
				udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				adress = (MIDD_ADDRESS, SERVERNAME2_PORT)
				#adress = ((ADRESS_MID, PORT))
				udp_socket.sendto(str(self.function), adress)
				print "entrei aqui 6"
				end, client = udp_socket.recvfrom(1024)
				print end
				udp_socket.close()
				enderecos = end

			if self.function in self.cache:
				if self.cache[self.function] != enderecos:
					self.cache.update({self.function: enderecos})

			else:
				self.cache.update({self.function: enderecos})

			self.connectServer(enderecos)

	def connectServer(self, endereco):
		mensagem = self.function +" " +self.valor1 +" " +self.valor2
		self.cache = {self.function: endereco}
		endereco = endereco.split(" ")

		op = 's'

		while op != 'n':
			for i in range(len(endereco)):
				
				try:
					print 'testandoo ...'
					tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
					tcp_socket.settimeout(5)
					#tcp_socket.connect((endereco, PORT))
					tcp_socket.connect((ADDRESS, int(endereco[i])))
					tcp_socket.send(mensagem)
					msgCliente = tcp_socket.recv(1024)
					tcp_socket.close()
					op = 'n'

				except:
					print 'teste 6'
					msgCliente =""

		self.connectCliente(msgCliente)
		
	def connectCliente(self, msgCliente):
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.connect((CLIENT_ADRESS, CLIENT_PORT))
		#tcp_socket.connect((ADRESS_CLIENT, PORT))
		tcp_socket.send(msgCliente)
		
		tcp_socket.close()

if __name__ == "__main__":
	midd = Midd()
