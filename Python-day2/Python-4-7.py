#!/usr/bin/env python3


list_task = [101,2,15,22,95,33,2,27,72,15,52]
list_task.sort()
print(list_task)
summ_even = 0
summ_odd = 0
for iterating in list_task:
	print(iterating)
	if iterating%2 == 0:
		summ_even += iterating
	else:
		summ_odd += iterating
		
print(summ_even)
print(summ_odd)

