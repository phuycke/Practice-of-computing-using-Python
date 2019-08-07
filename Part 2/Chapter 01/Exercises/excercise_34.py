#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# part 1: metric measures

weight_metric = float(input('Weight in kg: '))
height_metric = float(input('Height in meter: '))

bmi_metric    = (weight_metric) / (height_metric ** 2)
print('\nCalculated bmi: {0:.2f}'.format(bmi_metric))

#%%

print('\n * * * * * ')

# part 2: imperial measures

weight_imperial  = float(input('Weight in pounds: '))
weight_converted = weight_imperial / 2.2046    # conversion to metric

height_imperial  = float(input('Height in inches: '))
height_converted = height_imperial * 0.0254    # conversion to metric

bmi_imperial    = (weight_converted) / (height_converted ** 2)
print('\nCalculated bmi: {0:.2f}'.format(bmi_imperial))