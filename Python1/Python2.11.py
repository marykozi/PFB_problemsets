#! /usr/bin/env python3

test_number = 50

three_test=test_number%3

if test_number > 50 and three_test == 0:
        print(test_number, "is greater than 50 and divisible by 3\n")
elif test_number > 50 and three_test != 0:
        print(test_number, "is greater than 50 and indivisible by 3\n")
elif test_number < 50 and three_test == 0:
        print(test_number, "is less than 50 and divisible by 3\n")
elif test_number <  50 and three_test != 0:
	print(test_number, "is less than 50 and indivisible be 3\n")
else:
        print(test_number, "is 50 and indivisible by 3")
