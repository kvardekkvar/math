# -*- coding: utf-8 -*-

# Check that for any 9 remainders modulo 20 there are two pairs of remainders with the same sum

import itertools


list_numbers = [i for i in range(20)]
nine_combinations = itertools.combinations(list_numbers, 9)
for nine_numbers in nine_combinations:
    flag = 0
    for four_numbers in itertools.combinations(nine_numbers, 4):
        t1, t2, t3, t4 = four_numbers
        if ((t1 + t2 - t3 - t4) % 20 == 0):
            flag = 1
        if ((t1 - t2 + t3 - t4) % 20 == 0):
            flag = 1
        if ((t1 - t2 - t3 + t4) % 20 == 0):
            flag = 1
        if ((-t1 + t2 + t3 - t4) % 20 == 0):
            flag = 1
        if ((-t1 + t2 - t3 + t4) % 20 == 0):
            flag = 1
        if ((-t1 - t2 + t3 + t4) % 20 == 0):
            flag = 1
    if (flag == 0):
        print(nine_numbers)
        break
print("ok")
