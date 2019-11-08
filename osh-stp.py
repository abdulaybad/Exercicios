import random
def gerar():
	recargas =''
	for x in range(0,9):
		i = random.randrange(0,9)
		recargas = recargas + str(i)

		#recargas1 = int(recargas)
		
	return recargas
	

def comprar():
	#criar um ficheiro do tipo Csv no teu diretorio
	data ='D:\Abdu\Programação Python-C\Base de Dados\Recargas.csv'
	data_write = open(data,'w')
	for i in range(0,50):
		recargas_geradas = gerar()
		data_write.write(recargas_geradas + '\n')
			
	data_write.close()
        


