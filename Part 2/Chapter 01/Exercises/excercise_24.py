#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import turtle

#%%

# define the angle the turtle should make
star_angle  = 60
left_angle  = 180 - star_angle
length_side = 100

for k in range(6):
    turtle.forward(length_side)
    turtle.right(star_angle)
    turtle.forward(length_side)
    turtle.left(left_angle)

turtle.done()
