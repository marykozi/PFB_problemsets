#!/usr/bin/env python3

nt_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC'] 

for nt in nt_list:                      ## iterates through each value of list
	print(nt)

for nt in nt_list:
	print(len(nt),nt,sep='\t')      ## prints length and nt in list, separated by tab
