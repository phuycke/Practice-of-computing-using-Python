#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

folds = int(input('The number of folds: '))
width = (1/200) * 2**folds
print('Thickness of paper (in m): {}'.format(width / 100))