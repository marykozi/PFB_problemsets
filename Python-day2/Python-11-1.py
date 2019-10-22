#!/usr/bin/env python3

class DNA_sequence (object):
	def __init__ (self, seq, seq_name, organism_name):

		self.seq = seq
		self.seq_name = seq_name
		self.organism_name = organism_name

	def lenght_seq(self):         #same identation for attributes and methods
		lenght = len(self.seq)	
		return lenght


dna_object0 = DNA_sequence('atgatgatg', 'abca4', 'sapiens')
dna_object1 = DNA_sequence('atgatgcctg', 'abca5', 'rabbit')

printstring = "Sequence: {} Gene: {} Organism: {} Lenght of seq: {}"


for n in [dna_object0, dna_object1]:
	print(printstring.format(n.seq, n.seq_name, n.organism_name, n.lenght_seq()))    #i call my object as n, then I call a method lenght_seq, () - show that it is a function; i no ned  to call "seq" bacause this thing is already called inside a method

 


