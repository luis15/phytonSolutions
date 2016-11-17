arq = open('singularidades.csv', 'r')
texto = arq.readlines()
import csv

for linha in texto :
    for linha2 in texto:
        if (not(texto.index(linha)==texto.index(linha2))):
            if(linha==linha2) :
                print linha2
arq.close()
