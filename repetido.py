arq = open('singularidades.csv', 'r')
texto = arq.readlines()
for linha in texto :
    for linha2 in texto:
        if((linha==linha2) and (texto.index(linha)!=texto.index(linha2))):
            print linha
arq.close()
