#!/usr/bin/env python3

import sys

seq_id = " "
parameters = " "
seq = " "
in_file = sys.argv[1]

print("User provided file:", in_file)
print("seq_name\tA \tG \tC \tT")
nucleo_count = {}
FASTA = {}
with open (in_file, "r") as file_object:   #reading line by line
	for line in file_object:
		line = line.rstrip()
		
		if line.startswith(">"):     #read header of FASTA
			[seq_id, parameters]  = line.split(' len')   #cut out ID, the rest of trashafter "len" place at "parameters"
			FASTA[seq_id] = ''                           #important!! 
			nucleo_count[seq_id] = {"A":0, "G":0, "C":0, "T":0}
		else:
			#seq+= line
			#FASTA[seq_id] += line
			#nucleo_count[seq_id] = {"A":0, "G":0, "C":0, "T":0}			  
			for nt in line:
				nucleo_count[seq_id][nt] += 1
		
	for seq_id in nucleo_count:
 
		print(seq_id, nucleo_count[seq_id]["A"], nucleo_count[seq_id]["G"], nucleo_count[seq_id]["C"], nucleo_count[seq_id]["T"], sep='\t')


#print(FASTA)

#print("Dictionary of FASTA:", FASTA)

#import re
#nuc_count = {}
#FASTA_count = {}
#for seq_id in FASTA:
#	FASTA_count[seq_id] = {}
#	nucA_count = len(re.findall(r"A", FASTA[seq_id]))
#	nucG_count = len(re.findall(r"G", FASTA[seq_id]))
#	nucC_count = len(re.findall(r"C", FASTA[seq_id]))
#	nucT_count = len(re.findall(r"T", FASTA[seq_id]))
#	FASTA_count[seq_id]["A"]=[nucA_count]	
#	FASTA_count[seq_id]["G"]=[nucG_count]
#	FASTA_count[seq_id]["C"]=[nucC_count]
#	FASTA_count[seq_id]["T"]=[nucT_count]
#print(FASTA_count)




#nuc_count.append({})
#FASTA_count[seq_id] = 
#nuc_count.update()


	













 

