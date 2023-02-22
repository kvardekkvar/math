# -*- coding: utf-8 -*-

# The program looks for cyclic Kaprekar numbers. Cyclic Kaprekar number is obtained in the following way: take a number n and move its last digit to the first position n times, keeping track of largest and smallest values obtained this way. Cyclic Kaprekar numbers are fixed points of function mapping n to difference of the largest and the smallest values.


def iteration(n):
    largest_number = n
    smallest_number = n
    for i in range(n):
        last_digit = n % 10
        n = int(str(last_digit) + str(n // 10))
        if n > largest_number:
            largest_number = n
        if n < smallest_number:
            smallest_number = n
    return largest_number-smallest_number


x = 538
for i in range(10):
    x = iteration(x)
    print(x)
