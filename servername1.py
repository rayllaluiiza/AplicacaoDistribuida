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
		#self.retornaServer(MIDD_ADDRESS, SERVERNAME1_PORT)
		self.retornaServer(ADDRESS_SEVERNAME1, PORT)

	def retornaServer(self, client, port):
		#endSoma = '5005' + ' ' +'5004' #quando testar no if mudar o address
		endSoma2 = '10.90.37.18' + ' ' +'127.0.0.1'
		
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		address = (client, port)
		udp_socket.bind((address))
		
		while True:
			msg, cli = udp_socket.recvfrom(1024)

			if msg == 'Soma':
				print 'teste'
				
				udp_socket.sendto(endSoma2, cli)

			elif msg == 'Subtracao':
				print 'teste 2'
				
				udp_socket.sendto(endSoma2, cli)

		udp_socket.close()


if __name__ == "__main__":
	servername1 = ServerName1()
		
