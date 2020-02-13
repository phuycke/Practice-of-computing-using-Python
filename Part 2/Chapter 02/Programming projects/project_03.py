#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import turtle as T

#%%

sides    = int(input('Number of sides?\n'))
fill_col = str(input('Color of interior?\n'))

#%%

T.color('black', fill_col)
T.begin_fill()
for i in range(sides):
    T.forward(100)
    T.right(180 - (((sides - 2) * 180) / sides))
T.end_fill()

# we keep getting Terminator error otherwise...
try:
    T.exitonclick()
    T.done()
except Exception:
    pass