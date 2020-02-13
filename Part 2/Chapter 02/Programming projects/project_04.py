#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

computing = True

while computing:
    A = int(input('A: '))
    B = int(input('B: '))
    
    product = 0
    while B > 0:
        if B % 2:
            product += A
        A *= 2
        B  = B // 2
    
    print('Product: ', product)
    user_input = str(input('Compute other product? (y/n): '))
    if user_input.lower()[0] == 'n':
        computing = False
        