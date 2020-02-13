#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

S = "I had a cat named amanda when I was little" 

count = 0 
index = 0

while index < len(S): 
    if S[index] == "a": 
        count += 1
    index += 1
    
print(count)