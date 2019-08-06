#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# parameters
rain_centimeters = 1                                 # rain fall: 1 cm
rain_meters      = rain_centimeters / 100            # cm to meter
hectare          = 10000                             # hectare = 10 000 m^2

# computation
cubic_meter      = rain_meters * hectare             # water in m^3
rain_liters      = cubic_meter / 1000                # from m^3 to liters

# print result
print('Amount of rain fallen in liters: {} l'.format(rain_liters))