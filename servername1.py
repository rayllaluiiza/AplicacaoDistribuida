import socket
import threading

PORT = 5000
ADDRESS_CLIENT = "10.90.37.15"
ADDRESS_MID = "10.90.37.16"
ADDRESS_SEVERNAME1 = "10.90.37.17"
ADDRESS_SEVERNAME2 = "10.90.37.19"
ADRESS_SERVER = "10.90.37.18"

class ServerName1():

	def __init__(self):
		self.retornaServer(ADDRESS_SEVERNAME1, PORT)

	def retornaServer(self, client, port):
		endereco = '10.90.37.18' + ' '
		
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		address = (client, port)
		udp_socket.bind((address))
		
		while True:
			msg, cli = udp_socket.recvfrom(1024)

			if msg == 'Soma':
				udp_socket.sendto(endereco, cli)

			elif msg == 'Subtracao':
				udp_socket.sendto(endereco, cli)

			elif msg == 'Multiplicacao':
				udp_socket.sendto(endereco, cli)

		udp_socket.close()


if __name__ == "__main__":
	servername1 = ServerName1()
		
