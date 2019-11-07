def add(x,y):
	return x + y

def product(x,y):
	return x * y


def division(x,y):
	msg = 'Erro de calculo, impossivel dividir por 0'
	if y == 0:
		print(msg)
	else:
		result = x/y
	return result

def listas():
	import random
	lista_de_numeros_aleatorios = []
	for i in range(0,9):
		random_number = random.randrange(0,100)
		lista_de_numeros_aleatorios.append(random_number)
	return lista_de_numeros_aleatorios


