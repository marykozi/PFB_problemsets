#!/usr/bin/env python3

nt_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuples_list = []
tuple_l_s = ()


for nt in nt_list:                      # put size and sequence in tuple
        tuple_l_s = (len(nt),nt)
        tuples_list.append(tuple_l_s)   # for each nt -add tuple in list
print(tuples_list)

