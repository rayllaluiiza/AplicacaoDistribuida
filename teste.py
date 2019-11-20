lista = []
dic = {}

lista.append({'soma': 2})
lista.append({'soma': 3})

print lista[0]['soma']

for i in range(0,2):
	if 'soma' in lista[i]:
		print 'ola' , i

	
