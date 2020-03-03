#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def shift(l          = list,
          places     = int,
          direction  = str):
    
    assert direction.lower() in ["left", "right"]
    
    if direction.lower() == "left":
        return l[places:] + l[:places]
    else:
        return l[-places:] + l[:-places]

res = shift(l         = [1,2,3,4,5,6,7,8,9],
            places    = 2,
            direction = "right")
print(res)