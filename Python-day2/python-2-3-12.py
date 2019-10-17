#!/usr/bin/env python3

DNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT'


DNA_uppercase = DNA.upper() #move the seq to new variable with same case characters
#print(DNA_uppercase)

#DNA_length = len(DNA_uppercase)

sub_DNA_uppercase = DNA_uppercase[99:199] #cut 100-200bp

complement_sub_DNA_T_to_P = sub_DNA_uppercase.replace('T','P') #replace nucleotides one by one to make complement
complement_sub_DNA_A_to_N = complement_sub_DNA_T_to_P.replace('A','N')
complement_sub_DNA_G_to_Q = complement_sub_DNA_A_to_N.replace('G','Q')
complement_sub_DNA_C_to_Y = complement_sub_DNA_G_to_Q.replace('C','Y')

complement_sub_DNA_P_to_A = complement_sub_DNA_C_to_Y.replace('P','A')
complement_sub_DNA_N_to_T = complement_sub_DNA_P_to_A.replace('N','T')
complement_sub_DNA_Q_to_C = complement_sub_DNA_N_to_T.replace('Q','C')
complement_sub_DNA = complement_sub_DNA_Q_to_C.replace('Y','G')


reverse_complement_sub_DNA = sub_DNA_uppercase[::-1] #make reverse of complement seq

string = 'Original 100bp seq:\n{}\nComplement:\n{}\nReverse Complement\n{}' #Make empty template for result line

final_data = string.format(sub_DNA_uppercase, complement_sub_DNA, reverse_complement_sub_DNA)

print(final_data)


