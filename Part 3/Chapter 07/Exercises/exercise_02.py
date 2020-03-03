#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

list1 = []
for i in range(100):
    list1.append(0)
  
#%%
    
list2 = [0] * 100

#%%

import numpy as np

list3 = list(np.zeros(100, dtype = int))
