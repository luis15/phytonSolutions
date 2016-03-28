arq = open('turmas2013.csv', 'r')
texto = arq.readlines()
for linha in texto : 
	print linha
#print texto[138390]
arq.close() 