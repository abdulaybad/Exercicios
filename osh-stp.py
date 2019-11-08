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
        


