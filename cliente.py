import socket
import threading

MIDD_ADDRESS = "127.0.0.1"
MIDD_PORT = 5000
CLIENT_PORT = 5001
CLIENT_ADDRESS = "127.0.0.1"
SERVERNAME1_PORT = 5002
SERVERNAME2_PORT = 5003
SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 5004

class Cliente:

	def __init__(self):
		self.processar("Soma", '3', '2', MIDD_ADDRESS, MIDD_PORT)

	def processar(self, nome, valor1, valor2, server, port):
		mensagem = nome + " " +valor1 +" " +valor2
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.connect((server, port))
		tcp_socket.send(mensagem)
		print mensagem
		tcp_socket.close()

	def obterResultado(self):
		tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		tcp_socket.bind((CLIENT_ADDRESS, CLIENT_PORT))
		tcp_socket.listen(5)

		con, cliente = tcp_socket.accept()

		msg3 = con.recv(1024)

		con.close() 

		return msg3

if __name__ == "__main__":

	cliente = Cliente()
	
	opcao = 's'
	
	while opcao != 'n':
		msg = cliente.obterResultado()

		if len(msg) == 0:
			opcao = raw_input('Deseja que os dados sejam reenviados? (s/n): ')

			if opcao == 's' or opcao == 'S':
				cliente = Cliente()
		else:
			opcao = 'n'
			print 'Resultado:' ,msg
