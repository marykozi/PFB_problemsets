#!/usr/bin/env python3

file = open("Python_06.txt", "r")
for line in file:        #read line by line
  line = line.rstrip()   #remove space btw lines
  line_upper = line.upper()   #make capital
  print(line_upper)

#    with open("Python_o6.uc.txt", "w") as fo: 
#      fo.write(str(line_upper)) #modify output in string
#      print("Wrote to file Python_06_uc.txt") #whre we wrote it

fo = open("Python_o6.uc.txt", "w")
fo.write(str(line_upper))
print("Wrote to file Python_06_uc.txt")




