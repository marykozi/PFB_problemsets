#!/usr/bin/env python3

import re


FASTA = {}

with open ('Python_07.fasta', "r") as file_object:   #reading line by line
	for line in file_object:
		line = line.rstrip()
		if line.startswith(">"):     #read header of FASTA
			[seq_id, parameters]  = line.split(r'\w+\d')   #cut out ID, the rest of trashafter "x.11111.1" place at "parameters"
			FASTA[seq_id] = ''
		else:
			FASTA[seq_id] += line
print(FASTA)


