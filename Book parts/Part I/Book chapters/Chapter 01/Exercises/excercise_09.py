#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# ask user input
integer_str = input('Inputted number: ')
integer_int = int(integer_str)

# do computations
result_int  = ((integer_int + 2) * 3 - 6) / 3

# print end result
print('Result after computation: {}'.format(result_int))