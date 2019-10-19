#!/usr/bin/env python3

sequences = {}
with open ("Python_06.seq.txt", "r") as strings:    #read line by line
	for line in strings:
		line = line.rstrip()           #remove \n for one last read line
		seq_id, seq = line.split()     #split line for two variables
		sequences[seq_id] = seq        #place them in dictionary


## Reverse-complement
print("SeqName:\t'ReverseComplement\n")
reversed_seq = {}

print(sequences)

#replace nucleotides one by one to make complement
for seq_id in sequences:

#	print("Before", seq)	
	complement_sub_DNA_T_to_P = sequences[seq_id].replace('T','P')          #call seq by seq_id!!!!!!
	complement_sub_DNA_A_to_N = complement_sub_DNA_T_to_P.replace('A','N')
	complement_sub_DNA_G_to_Q = complement_sub_DNA_A_to_N.replace('G','Q')
	complement_sub_DNA_C_to_Y = complement_sub_DNA_G_to_Q.replace('C','Y')

	complement_sub_DNA_P_to_A = complement_sub_DNA_C_to_Y.replace('P','A')
	complement_sub_DNA_N_to_T = complement_sub_DNA_P_to_A.replace('N','T')
	complement_sub_DNA_Q_to_C = complement_sub_DNA_N_to_T.replace('Q','C')
	complement_seq_DNA = complement_sub_DNA_Q_to_C.replace('Y','G')

	reverse_complement_seq = complement_seq_DNA[::-1] #make reverse of complement seq

	reversed_seq[seq_id] = reverse_complement_seq
 
	print(seq_id+'\t'+reverse_complement_seq)






