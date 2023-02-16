# -*- coding: utf-8 -*-

import numpy as np
from scipy.special import binom
from math import gcd
t = gcd(1, 1)
n = 200
a = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            a[i, j] = 1
        else:
            a[i, j] = (a[i-1, j] + a[i, j-1]
                       )//gcd(int(a[i-1, j]), int(a[i, j-1]))
