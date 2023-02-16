# -*- coding: utf-8 -*-

import itertools
import numpy as np
import math

n = 20


def fib(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a


t = np.zeros((n, n), dtype=object)
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            t[i, j] = fib(i+j)
        else:
            t[i, j] = t[i, j-1]+t[i-1, j]

srow = []
for i in range(n):
    add = 0
    for j in range(i+1):
        add += t[i-j, j]*(-1)**j
    srow.append(add)
