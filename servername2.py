import socket
import threading

MIDD_ADDRESS = "127.0.0.1"
MIDD_PORT = 5000
CLIENT_PORT = 5001
CLIENT_ADRESS = "127.0.0.1"
SERVERNAME1_PORT = 5002
SERVERNAME2_PORT = 5003
SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 5004

class ServerName2():

	def __init__(self):
		self.retornaServer(MIDD_ADDRESS, SERVERNAME2_PORT)

	def retornaServer(self, client, port):
		#vetorSoma = ['127.0.0.1;5004']
		endereco = '127.0.0.1'
		
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		address = (client, port)
		udp_socket.bind((address))
		print "entrei aqui 1"
		while True:
			msg, cli = udp_socket.recvfrom(20)

			print "entrei aqui 3: ", msg
			if msg == 'Soma':
				print 'teste'
				
				udp_socket.sendto(endereco, cli)

		udp_socket.close()


if __name__ == "__main__":
	servername2 = ServerName2()
		