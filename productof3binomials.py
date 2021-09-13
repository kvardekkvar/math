# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 01:42:25 2021

@author: beelzebub
"""

import scipy.special as scp

for n in range(1, 2):
    s=0
    for a in range(-n, n+1):
        for b in range(-n, n+1):
            for c in range(-n, n+1):
                if (a+b+c==0 and a!=0 and b!=0):
                    ma = int(abs(a))
                    mb = int(abs(b))
                    mc = int(abs(c))
                    s+= scp.binom(n,ma)*scp.binom(n,mb)*scp.binom(n,mc)
                    print(a, b, c)
'''  
    s=int(s)
    print(str(s)+", ")
'''