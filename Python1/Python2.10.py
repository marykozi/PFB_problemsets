#! /usr/bin/env python3

test_number = 6

even_test=test_number % 2
#print(even_test)

#if even_test == 1: # = vs ==
#        print(test_number, "is odd")
#else:
#        print(test_number, "is even")

if test_number > 50 and even_test == 1:
	print(test_number, "is greater than 50 and odd\n")
elif test_number > 50 and even_test == 0:
	print(test_number, "is greater than 50 and even\n")
elif test_number < 50 and even_test == 1:
        print(test_number, "is less than 50 and odd\n")
else:
        print(test_number, "is less than 50 and even")
	


