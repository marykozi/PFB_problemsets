#!/usr/bin/env python3

import re

file = open ('Python_07_nobody.txt', 'r')	
contents  = file.read()
	
#print(re.search(r"Nobody", contents))

for found in re.finditer(r"(Nobody)", contents)
	whole = found.group(1)
	start = found.start(1) + 1

print(start)



	


