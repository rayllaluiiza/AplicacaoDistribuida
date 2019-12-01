import socket
import threading

PORT = 5000
ADDRESS_CLIENT = "10.90.37.15"
ADDRESS_MID = "10.90.37.16"
ADDRESS_SEVERNAME1 = "10.90.37.17"
ADDRESS_SEVERNAME2 = "10.90.37.19"
ADRESS_SERVER = "10.90.37.18"

class Server():

	def __init__(self):
		self.conectar()

	def conectar(self):
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#tcp_socket.bind((SERVER_ADRESS, SERVER_PORT))
		tcp_socket.bind((ADRESS_SERVER, PORT))
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
