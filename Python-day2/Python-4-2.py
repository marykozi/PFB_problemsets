#!/usr/bin/env python3

taxa = 'sapiens, erectus, neanderthalensis'

print(taxa)

print(taxa[1])


species = []

species = taxa.split(',') #delimiter is ,

print(species)

print(species[1])

print(type(species))

species.sort()
print(species)

sorted_list = sorted(species, key=len)
print(sorted_list)
