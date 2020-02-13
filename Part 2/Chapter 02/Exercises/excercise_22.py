#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import math

num = int(input('Number: '))
while num <= 2:
    num = int(input('Number: '))
else:
    loop_indx = 1
    while math.sqrt(num) > 2:
        print('Loop {0:.0f}: {1:.3f}'.format(loop_indx, math.sqrt(num)))
        num        = math.sqrt(num)
        loop_indx += 1