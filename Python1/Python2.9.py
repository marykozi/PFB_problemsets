#! /usr/bin/env python3

test_number = 5
if test_number > 0:
	if test_number > 50:
		print(test_number, "is positive, greater than 50\n")
	else:
		print(test_number, "is positive, less than 50\n")
elif test_number < 0:
	print(test_number, "is negative\n")
else:
	print(test_number, "is zero")
