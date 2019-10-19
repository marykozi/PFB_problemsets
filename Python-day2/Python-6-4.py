#!/usr/bin/env python3


line_count = 0
nt_count = 0
total_nts = 0

with open ("Python_06.fastq", "r") as strings:    #read line by line
	for line in strings:
		line = line.rstrip()           #remove \n for one last read line
		line_count += 1                #each time add 1 for each new line
		nt_count = len(line)            #lenght of line
		total_nts += nt_count          #total number od characters


average_line_length = total_nts/line_count

string = "total number of lines {}  total number of characters {}  average line length {}"
print(string.format(line_count, total_nts, average_line_length))



