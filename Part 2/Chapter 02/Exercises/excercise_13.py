#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

asked = str(input('Input an integer: '))

while not asked.isdigit():
    asked = str(input('Error: try again. Input an integer: '))
else:
    print('The integer is : {}'.format(asked))