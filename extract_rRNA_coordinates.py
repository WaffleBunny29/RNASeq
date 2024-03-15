#!/usr/bin/env python3
import re
inf = str(input('Enter gff annotation file:\n'))
f = open(inf,'r')
temp = []
for line in f:
    check = re.search('ribosomal RNA', line)
    if check:
        line =line.replace(';','\t').split('\t')
        temp.append(line[0])
        temp.append(line[3])
        temp.append(line[4])
        temp.append(line[-1])
outf = inf[0:-4]+'_coordinates.txt'
o = open(outf, 'w')
for i in temp:
    if '\n' not in i:
        o.write(i+'\t')
    else:
        o.write(i)
f.close()
o.close()
