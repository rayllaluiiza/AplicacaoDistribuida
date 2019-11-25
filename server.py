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
SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 5004

class Server():

	def __init__(self):
		self.conectar()

	def conectar(self):
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.bind((SERVER_ADDRESS, SERVER_PORT))
		#tcp_socket.connect((ADRESS_SERVER, PORT))
		tcp_socket.listen(5) 
		while True:
			tc2 = threading.Thread(target=self.retornaValor, args=(tcp_socket.accept()))
			tc2.start()

	def retornaValor(self, connection, client):
		nomeFuncao = connection.recv(1024)
		nomeFuncao = nomeFuncao.split(" ")

		dynamic_module = __import__("funcoes")
		dynamic_class = getattr(dynamic_module, nomeFuncao[0])
		dynamic_function = getattr(dynamic_class(), "compute")
		result = dynamic_function(int(nomeFuncao[1]), int(nomeFuncao[2]))
		print result
		connection.send(str(result))
		connection.close()

if __name__ == "__main__":
	server = Server()
