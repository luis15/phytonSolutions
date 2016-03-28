from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
pos = 0
vector = []

csvName = "turmas.csv" #Put here the CSV name
with open(csvName) as f:
	reader = csv.reader(f,delimiter="|") 
	#reader.next()
	for row in reader: 
		for (i,v) in enumerate(row): 
			#columns[i].append(v)
			if(i==6 or i==62):
				#print("to aqui"+ str(i) + v)
				vector.append(v)
			#columns[i].append()
			
			
#print (vector)			
out_file = open("turmas2013.csv", "wt") #The name of out file
writer = csv.writer(out_file)
for i in range(0,len(vector)/2):
	#writer.writerow([columns[i]])
	writer.writerow([vector[2*i],vector[2*i+1]])

#for i in range(0, len(vector[0])):
#	writer.writerow(vector[0][i])

out_file.close()