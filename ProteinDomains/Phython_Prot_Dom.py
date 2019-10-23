#!/usr/bin/env python3

import sys

input_type = input ('Input SS or BLASTP?   ')

print('You choice is:   ', input_type)      #input form user to pick correct files

range_input = input('AA random protein: return 200 or 800?   ')

print("You entered:  ", range_input)

import subprocess
import re


rtn = subprocess.run(['ls'], stdout=subprocess.PIPE )  #capture STDOUT with all available files
bytes = rtn.stdout
stdout = bytes.decode('utf-8')
hits = stdout.splitlines()     #list of filenames

target_files = []     #new empty list for files selected by key words


#MOVE THESE FILES FILTERED BY NAME USING INPUT KEYWORDS TO NEW LIST
for file_name in hits[1:]:
	if re.search(str(input_type), file_name):
		if re.search(str(range_input), file_name):
			target_files.append(file_name)
		else:
			continue
#slit string for list of headers
field_str = 'query_id subject_id perc_identity alignment_length mismatches gap_opens q._start q._end s._start s._end evalue bit_score'
fields = field_str.split(' ')

#OPEN FILES FROM NEW LIST

hits_list = []

print("target files")
print(target_files)

#XYINYA TYT

for hit_file in target_files[1:]:
	with open(hit_file, 'r') as random_results:
		for line in random_results:
			if line[0] == "#":
				continue
			hit_data = dict(zip(fields, line.strip('\n').split('\t')))
			hit_data['file'] = hit_file
			hits_list.append(hit_data)
			break

print('file', 'perc_identity', 'alignment_length', 'evalue', sep='\t')


for hit in hits_list:
#	print('\t'.join([hit[x] for x in ('file', 'perc_identity', 'alignment_length', 'evalue')]))
#	for x in ('file', 'perc_identity', 'alignment_length', 'evalue')
#		print()
	print("hits_list")
	print(hits_list)









