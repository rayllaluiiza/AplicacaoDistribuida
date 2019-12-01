import socket
import threading
import time
from datetime import datetime
import sys

PORT = 5000
ADDRESS = "127.0.0.1"
ADDRESS_CLIENT = "10.90.37.15"
ADDRESS_MID = "10.90.37.16"
ADDRESS_SEVERNAME1 = "10.90.37.17"
ADDRESS_SEVERNAME2 = "10.90.37.19"
ADRESS_SERVER = "10.90.37.18"

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
		self.cliente = ""
		self.function = ""
		self.valor1 = ""
		self.valor2 = ""
		self.cache = {}
    		tc = threading.Thread(target=self.start)
    		tc.start()

	def start(self):
		self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#self.tcp_socket.bind((MIDD_ADDRESS, PORT))
		self.tcp_socket.bind((ADDRESS_MID, PORT))
		self.tcp_socket.listen(5)
		while True:
			tc2 = threading.Thread(target=self.nomes, args=(self.tcp_socket.accept()))
			tc2.start()
	
	def nomes(self, connection, client):
		msg = connection.recv(1024)
		msg = msg.split(" ")
		self.cliente = client[0]
		self.function = msg[0]
		self.valor1 = msg[1]
		self.valor2 = msg[2]
		connection.close()

		if self.function != "Soma" and self.function != "Subtracao" and self.function != "Multiplicacao":
			msgCliente = ""
			self.connectCliente(msgCliente)
		else:	
			self.trataCache()

	def trataCache(self):
		hora = datetime.now()
		atual = hora.strftime('%H:%M')

		if self.function in self.cache:
			endereco_cache = self.cache[self.function].split(";")

			total_atual = int(atual.split(":")[1]) + int(atual.split(":")[0])*60
			total_cache = int(endereco_cache[0].split(":")[1]) + int(endereco_cache[0].split(":")[0])*60

			if (total_atual - total_cache) > 5:
				print 'e maior que 5'
				del(self.cache[self.function])
				self.connectServidorNome()

			else:
				print 'entrei no if do dicionario'
				self.connectServer(endereco_cache[1])
		else:
			self.connectServidorNome()
				

	def connectServidorNome(self):
		hora = datetime.now()
		atual = hora.strftime('%H:%M')

		try:
			udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			#address = (MIDD_ADDRESS, SERVERNAME1_PORT)
			address = ((ADDRESS_SEVERNAME1, PORT))
			udp_socket.sendto(str(self.function), address)
			print "entrei aqui 1"
			udp_socket.settimeout(1)
			endereco, cli = udp_socket.recvfrom(1024)
			print endereco
			udp_socket.close()
			enderecos = endereco
		except:
			try:
				udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
				udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				#adress = (MIDD_ADDRESS, SERVERNAME2_PORT)
				adress = ((ADRESS_SERVERNAME2, PORT))
				udp_socket.sendto(str(self.function), adress)
				print "entrei aqui 6"
				udp_socket.settimeout(1)
				end, client = udp_socket.recvfrom(1024)
				print end
				udp_socket.close()
				enderecos = end

			except:
				enderecos = ""
				msgCliente = ""
				self.connectCliente(msgCliente)

		if enderecos != "":
			self.cache.update({self.function: atual+';'+enderecos})
			self.connectServer(enderecos)
		

	def connectServer(self, endereco):
		mensagem = self.function +" " +self.valor1 +" " +self.valor2
		endereco = endereco.split(" ")
		print endereco
		op = 's'
		contador = 0

		while op != 'n':
			for i in range(0,2):
				
				try:
					print 'testandoo ...'
					tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
					tcp_socket.settimeout(5)
					tcp_socket.connect((endereco[contador], PORT))
					#tcp_socket.connect((ADDRESS, int(endereco[contador])))
					tcp_socket.send(mensagem)
					msgCliente = tcp_socket.recv(1024)
					tcp_socket.close()
					op = 'n'
					break

				except:
					pass

			if contador >= len(endereco):
				msgCliente = ""
				op = 'n'

			contador = contador + 1

		self.connectCliente(msgCliente)
		
	def connectCliente(self, msgCliente):
		print msgCliente
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.connect((str(self.cliente), PORT))
		tcp_socket.send(msgCliente)
		
		tcp_socket.close()

if __name__ == "__main__":
	midd = Midd()
