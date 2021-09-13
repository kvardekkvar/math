# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 23:49:06 2021

@author: beelzebub
"""

def step(n):
    M = n
    m = n
    for i in range(n):
        posl = n%10
        n = int(str(posl) + str(n//10))
        if n>M: 
            M=n
        if n<m:
            m=n
    return M-m

x=538
for i in range(10):
    x=step(x)
    print(x)