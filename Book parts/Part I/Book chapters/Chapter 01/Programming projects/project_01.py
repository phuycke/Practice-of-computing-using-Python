#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

area   = 8080464.3        # area of 48 contiguous states in km^2
volume = 22810            # volume of water in Great lakes in km^3

height = (volume / area)  # km^3 / km^2  = m

print('Kilometres water on surface if evenly spread: {0:.5f}'.format(height))
print('Metres water on surface if evenly spread: {0:.5f}'.format(height * 1000))
