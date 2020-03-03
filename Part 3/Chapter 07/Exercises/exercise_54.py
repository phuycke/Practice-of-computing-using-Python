#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import numpy as np

#%%

# store the start number
perfect_pairs = []
start_number  = 18

while start_number not in perfect_pairs:
    
    # keep track of all perfect number combinations
    for i in range(2, int(np.ceil(np.sqrt(start_number) + 1))):
        if (i ** 2) - start_number > 0:
            perfect_pairs.extend([start_number, (i ** 2) - start_number])
            break
              
    # decrement the start number with one
    start_number -= 1

# show the couple numbers 
[print(couple) for couple in np.split(np.array(perfect_pairs), len(perfect_pairs) // 2)]
