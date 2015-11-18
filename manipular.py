#!/usr/bin/python
#coding: utf8
from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
pos = 0
vector = [[]]

csvName = "TS_ESCOLA.TXT" #Put here the CSV name
with open(csvName) as f:
	reader = csv.reader(f,delimiter="\t") 
	#reader.next()
	for row in reader: #
		for (i,v) in enumerate(row): 
			#columns[i].append(v)

			columns[i].append(v[5:14])
			columns[i].append(v[14:114])
			columns[i].append(v[183:185])
			columns[i].append(v[185:194])
			columns[i].append(v[194:203])
			columns[i].append(v[203])
			columns[i].append(v[205])
			columns[i].append(v[209])
			columns[i].append(v[210])
			columns[i].append(v[213])
			columns[i].append(v[244])
			columns[i].append(v[245])
			columns[i].append(v[246])
			columns[i].append(v[247])
			columns[i].append(v[249])
			columns[i].append(v[250])
			columns[i].append(v[254])
			columns[i].append(v[266])
			columns[i].append(v[271])
			columns[i].append(v[279:284])
			columns[i].append(v[339:344])
			columns[i].append(v[344:349])
			columns[i].append(v[349:354])
			columns[i].append(v[355])
			columns[i].append(v[357:362])
			i=i+1

			#columns[i].append()
			
			
out_file = open("escolas.csv", "wt") #The name of out file
writer = csv.writer(out_file)
for i in range(0,len(columns[0])/25):
	columns[0][25*i+1].replace('\xAA'," ")
	writer.writerow([columns[0][25*i],columns[0][25*i+1],columns[0][25*i+2],columns[0][25*i+3],columns[0][25*i+4],columns[0][25*i+5],columns[0][25*i+6],columns[0][25*i+7],columns[0][25*i+8],columns[0][25*i+9],columns[0][25*i+10],columns[0][25*i+11],columns[0][25*i+12],columns[0][25*i+13],columns[0][25*i+14],columns[0][25*i+15],columns[0][25*i+16],columns[0][25*i+17],columns[0][25*i+18],columns[0][25*i+19],columns[0][25*i+20],columns[0][25*i+21],columns[0][25*i+22],columns[0][25*i+23],columns[0][25*i+24]])
	#writer.writerow([columns[0][2*i+1]])

#for i in range(0, len(vector[0])):
#	writer.writerow(vector[0][i])

out_file.close()

