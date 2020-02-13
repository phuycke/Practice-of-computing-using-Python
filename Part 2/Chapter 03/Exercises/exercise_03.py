#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

number = int(input('Your number: '))
if (2 <= number <= 20) and (number % 3 == 0):
    print('Number passes')
else:
    print('Number did not pass')
    
