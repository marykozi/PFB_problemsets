!/usr/bin/env python3

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
