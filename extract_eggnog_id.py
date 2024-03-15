#!/usr/bin/env python3

infile = open('prokka_annot.txt','r')
outfile = open('protein_id.txt','w')
 
count=1
for line in infile:	
	line=line.split(';')
	outfile.write(line[0]+'\n')
	count+=1
	
outfile.close()
infile.close()