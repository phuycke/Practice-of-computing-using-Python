#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

x = "acegikmoqsuwy"
y = "+bdfhjlnprtvxz"

y        = y[1:]
alphabet = ""

for i in range(len(x)):
    alphabet += x[i]
    alphabet += y[i]
    
print(alphabet)
