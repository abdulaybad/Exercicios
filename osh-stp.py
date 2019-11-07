import random
def gerar():
	recargas =''
	for x in range(0,9):
		i = random.randrange(0,9)
		recargas = recargas + str(i)

		#recargas1 = int(recargas)
		
	return recargas
	

def comprar():
	data ='D:\Abdu\Programação Python-C\Base de Dados\Recargas.csv'
	data_write = open(data,'w')
	recargas = ''
	for i in range(0,50):
		recargas_geradas = gerar()
		if len(recargas_geradas) == 9:
			#print(recargas_geradas)
			data_write.write(recargas_geradas + '\n')
		else:
			pass
			
	data_write.close()
        


def love():
	from time import sleep

	for string in 'I Love You':
		print(string)
		sleep(0.5)


def verificar():
	data ='D:\Abdu\Programação Python-C\Base de Dados\Recargas.txt'
	read_data = open(data,'r')
	recargas ={}
	for recargas_validas in read_data:
		recargas = recargas[recargas_validas]
	for repetidos in recargas:
		ad = recargas.count(repetidos)
		if ad > 1:
			recargas[repetidos] = str(ad) + ' ' + 'vezes'
		else:
			recargas[repetidos] = str(ad) + ' ' + 'vez'
	print(recargas)

#love()

#gerar()
#comprar()
#verificar()
