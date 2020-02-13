#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

total_grains = 0
multiplier   = 1
for i in range(1, 65):
    total_grains += multiplier
    multiplier   *= 2
    
print('Total amount of wheat: {}'.format(total_grains))

#%%

print('Weight of wheat (in tons): {}'.format(total_grains * 0.05 / 1000))

#%%

# I don't understand question c