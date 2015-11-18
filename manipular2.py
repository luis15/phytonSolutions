from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
pos = 0
vector = [[]]

csvName = "TS_TURMA.TXT" #Put here the CSV name
with open(csvName) as f:
	reader = csv.reader(f,delimiter="\t") 
	#reader.next()
	for row in reader: #
		for (i,v) in enumerate(row): 
			#columns[i].append(v)
			columns[i].append(v[110:112])
			columns[i].append(v[212:221])
			i=i+1

			#columns[i].append()
			
			
out_file = open("turmas.csv", "wt") #The name of out file
writer = csv.writer(out_file)
for i in range(0,len(columns[0])/2):
	columns[0][2*i] = int(columns[0][2*i])
	columns[0][2*i] = int(columns[0][2*i]+1)
	writer.writerow([columns[0][2*i],columns[0][2*i+1]])
	#writer.writerow([columns[0][2*i+1]])

#for i in range(0, len(vector[0])):
#	writer.writerow(vector[0][i])

out_file.close()