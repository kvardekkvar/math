# -*- coding: utf-8 -*-


import itertools


a = [i for i in range(20)]
b = itertools.combinations(a, 9)
for i in b:
    flag = 0
    for j in itertools.combinations(i, 4):
        t1, t2, t3, t4 = j
        if ((t1+t2 - t3-t4) % 20 == 0):
            flag = 1
        if ((t1-t2 + t3-t4) % 20 == 0):
            flag = 1
        if ((t1-t2 - t3+t4) % 20 == 0):
            flag = 1
        if ((-t1+t2 + t3-t4) % 20 == 0):
            flag = 1
        if ((-t1+t2 - t3+t4) % 20 == 0):
            flag = 1
        if ((-t1-t2 + t3+t4) % 20 == 0):
            flag = 1
    if (flag == 0):
        print(i)
        break
print("ok")
