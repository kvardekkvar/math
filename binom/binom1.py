# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import math
from PIL import Image


n=1000

a = np.zeros(shape=(n,n), dtype=object)

for i in range (n):
    for j in range(n):
        if (i==0 or j ==0):
            a[i,j]=1
        else:
            if a[i-1,j] > a[i, j-1]:
                a[i,j]=a[i-1,j]-a[i, j-1]
            else:
                a[i,j]=a[i-1,j]+a[i,j-1]
                
b = np.max(a, axis=0)
draw = 0

if draw==1:

    c = np.zeros(shape=(n,n,3), dtype=np.uint8)
    for i in range (1,n):
        for j in range(1,n):
            if( a[i,j]>a[i-1,j]):
                c[i,j,0]=255
                
        L = int(math.floor(i/np.tan(np.deg2rad(20))))
        if L < n:
            c[i,L,1]=255
            pass
        '''
        l1 = int(math.floor(i/np.tan(np.deg2rad(11.7))))
        l2 = int(math.floor(i/np.tan(np.deg2rad(16))))
        l3 = int(math.floor(i/np.tan(np.deg2rad(19.5))))
        if l1 < n:
            #c[i,l1,1]=255
            pass
        if l2 < n:
            #c[i,l2,1]=255
            pass
        if l3 <n:
            #c[i,l3,1]=255
            pass
        '''
    img = Image.fromarray(c)
    #img=img.resize((600,600))
    name = 'binom_1000_where_line_new'
    img.save("C:\\Users\\beelzebub\\Desktop\\binom\\" + name + ".jpg")
