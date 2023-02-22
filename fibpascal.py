# -*- coding: utf-8 -*-

# Compute Pascal triangle with Fibonacci numbers on boundary cells

import itertools
import numpy as np
import math

n = 20


def fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


a = np.zeros((n, n), dtype=object)
for row in range(n):
    for column in range(n):
        if row == 0 or column == 0:
            a[row, column] = fibonacci(row + column)
        else:
            a[row, column] = a[row, column - 1] + a[row - 1, column]

row_sums = []
for row in range(n):
    sum = 0
    for column in range(row+1):
        sum += a[row-column, column]*(-1)**column
    row_sums.append(sum)

print(row_sums)