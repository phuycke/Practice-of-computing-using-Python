#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import math

#%%

# parameters
a = 3
b = 7
c = 9

# calculate angle c
angle_c = (c**2 - a**2 - b**2) / (2 * a * b)
if angle_c < 0:
    angle_c = 180 - math.degrees(math.acos(angle_c))
else:
    angle_c = math.degrees(math.acos(angle_c))
    
# calculate angle a
angle_a = (a**2 - b**2 - c**2) / (2 * b * c)
if angle_a < 0:
    angle_a = 180 - math.degrees(math.acos(angle_a))
else:
    angle_a = math.degrees(math.acos(angle_a))
    
# calculate angle b
angle_b = 180 - angle_a - angle_c

# print result
print('Angle A: {0:.2f}\nAngle B: {1:.2f}\nAngle C: {2:.2f}'.format(angle_a,
                                                                    angle_b,
                                                                    angle_c))