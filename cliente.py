import socket
import threading

PORT = 5000
ADDRESS_CLIENT = "10.90.37.15"
ADDRESS_MID = "10.90.37.16"
ADDRESS_SEVERNAME1 = "10.90.37.17"
ADDRESS_SEVERNAME2 = "10.90.37.19"
ADRESS_SERVER = "10.90.37.18"

class Cliente:

	def __init__(self):
		self.processar("Soma", '3', '2', ADDRESS_MID, PORT)

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
		tcp_socket.bind((ADDRESS_CLIENT, PORT))
		tcp_socket.listen(5)

		con, cliente = tcp_socket.accept()

		msg = con.recv(1024)

		con.close() 

		return msg

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
