#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# parameters
short_parallel = int(input('Length of X in cm: '))
long_parallel  = int(input('Length of Y in cm: '))
height         = int(input('Height in cm: '))

area = int((short_parallel + long_parallel) / 2 * height)
print('\nArea of the trapezoid: {0} cm^2'.format(area))
