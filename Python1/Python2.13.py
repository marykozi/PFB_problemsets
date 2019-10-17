#! /usr/bin/env python3
import sys
the_number = sys.argv[1] #it gets arguments as strings!
test_number = int(the_number) #turns string to integer

three_test = test_number%3
even_test = test_number%2

if test_number > 50 and three_test == 0:
	if even_test == 0:
        	print(test_number, "is greater than 50, divisible by 3 and even\n")
	else:
		print(test_number, "is greater than 50, divisible by 3 and odd\n")
elif test_number < 50 and three_test == 0:
        if even_test == 0:
                print(test_number, "is less than 50, divisible by 3 and even\n")
        else:
                print(test_number, "is less than 50, divisible by 3 and odd\n")
elif test_number > 50 and three_test != 0:
        if even_test == 0:
                print(test_number, "is greater than 50, indivisible by 3 and even\n")
        else:
                print(test_number, "is greater than 50, indivisible by 3 and odd\n")
elif test_number <  50 and three_test != 0:
        if even_test == 0:
                print(test_number, "is less than 50, indivisible by 3 and even\n")
        else:
                print(test_number, "is less than 50, indivisible by 3 and odd\n")
else:
        print(test_number, "is 50, indivisible by 3 and even")
