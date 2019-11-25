import socket
import threading

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
SERVER_PORT1 = 5004

class ServerName1():

	def __init__(self):
		self.retornaServer(MIDD_ADDRESS, SERVERNAME1_PORT)
		#self.retornaServer(ADDRESS_MID, PORT)

	def retornaServer(self, client, port):
		endSoma = '5005' + ' ' +'5004' #quando testar no if mudar o address
		endSoma2 = '127.0.0.1' + ' ' +'127.0.0.1'
		
		udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		address = (client, port)
		udp_socket.bind((address))
		
		while True:
			msg, cli = udp_socket.recvfrom(1024)

			print "entrei aqui 3: ", msg
			if msg == 'Soma':
				print 'teste'
				
				udp_socket.sendto(endSoma, cli)

		udp_socket.close()


if __name__ == "__main__":
	servername1 = ServerName1()
		
