#!/usr/bin/python
#coding: utf8
from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
pos = 0

csvName = "/Users/classapp/Desktop/togoogle.csv" #Put here the CSV name
with open(csvName) as f:
	reader = csv.reader(f,delimiter=",") 
	#reader.next()
	for row in reader: 
		for (i,v) in enumerate(row): 
			#columns[i].append(v)
			columns[0].append(v.replace("  ", ""))
			i=i+1
			#columns[i].append()
			
			
out_file = open("/Users/classapp/Desktop/escolas.csv", "wt") #The name of out file
writer = csv.writer(out_file)
for i in range(0,len(columns[0])):
	lista = columns[0][i]
	writer.writerow([lista])


	#writer.writerow([columns[0][2*i+1]])

#for i in range(0, len(vector[0])):
#	writer.writerow(vector[0][i])

out_file.close()
