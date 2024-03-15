#!/usr/bin/env python3

# This code can be used to extract any gene sequence

# This section will store the (rRNA) coordinates  

file_dict = dict()
count=1
co_in = str(input('Enter coordinate filename with extension: '))
infile = open(co_in,'r')
for line in infile:
    line = line.rstrip().split('\t')
    key=line[0] 
    start=line[1]
    stop=line[2]
    name=line[-1]
    if key not in file_dict:
        file_dict[key] = {}
        file_dict[key]['start'] = start
        file_dict[key]['stop'] = stop
        file_dict[key][''] = name
    else:
        key=str(count)+key
        count+=1
        file_dict[key] = {}
        file_dict[key]['start'] = start
        file_dict[key]['stop'] = stop
        file_dict[key][''] = name     
infile.close()

#This section will extract contigs containing the (rRNA) sequences

print('\nHeader of draft genome file must only contain acc. no matching coordinate file Fx:\n\n>AGQU01000001.1\nATCTGTATGTA...\n')
seq_in = str(input('Enter draft genome filename with extension: '))
seq_file = open(seq_in,'r')
seq =''
seq_dict = dict()
for line in seq_file:
    if line.startswith('>'):
        if seq != '':
            seq_dict[headline] = seq
        seq =''
        headline =line[1:-1]
    else:
        seq +=line.rstrip()
if seq != '':
    seq_dict[headline]=seq
seq_file.close()

o = str(input('Enter a name for output contig file with extension: '))
outfile = open(o,'w')
for i in file_dict:
    if i in seq_dict:
        outfile.write(i+'\n'+seq_dict[i]+'\n')
outfile.close()


cds_file = str(input('Enter a name for output CDS sequence file with extension: '))
cds = open(cds_file ,'w')
temp =''
tempo =''
for j in file_dict: 
    if j in seq_dict:
        start = int(file_dict[j]['start'])-1
        stop = int(file_dict[j]['stop']) # python does not take into consideration upper limit
        temp += seq_dict[j]
        tempo += temp[start:stop]
        cds.write('>'+j+' start='+str(start+1)+' stop='+str(stop)+' '+file_dict[j]['']+'\n')
        for i in range(0,len(tempo)-1,70):     
            cds.write(tempo[i:i+70]+'\n')
        temp = ''
        tempo =''
    else:
        print(file_dict)
        k = j[1:]
        start = int(file_dict[j]['start'])-1
        stop = int(file_dict[j]['stop'])
        print(start,stop)
        temp += seq_dict[k]
        tempo += temp[start:stop]
        cds.write('>'+k+' start='+str(start+1)+' stop='+str(stop)+' '+file_dict[j]['']+'\n')
        for i in range(0,len(tempo)-1,70):     
            cds.write(tempo[i:i+70]+'\n')
        temp = ''
        tempo =''
cds.close()
