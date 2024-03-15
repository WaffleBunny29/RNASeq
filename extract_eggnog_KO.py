#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv('eggnog_KO.csv')
df_dict = df.set_index('query').to_dict()['KEGG_ko']

final_dict = {}
infile = open('protein_ID.txt','r')
outfile = open('ID_KO.txt','w')

for line in infile:
	line=str(line.strip())
	
	if line not in df_dict:
		df_dict[line] = '-'
	
	#outfile.write(str(df_dict[line])+'\n')
	outfile.write(line+'\t'+str(df_dict[line])+'\n')