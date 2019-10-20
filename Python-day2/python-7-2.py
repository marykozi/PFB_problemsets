#!/usr/bin/env python3
#In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).

import re

file = open ('Python_07_nobody.txt', 'r')
contents  = file.read()
print(contents)

substituted = ""
substituted = re.sub(r"(Nobody)", r"Kirill", contents)
file.close()
write_replaced = open("Kirill.txt", "w")
write_replaced.write(substituted)

file = open ('Kirill.txt', 'r')
new_text = file.read()

print(new_text)



