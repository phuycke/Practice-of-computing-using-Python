#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

gasoline_gallons = float(input('Gallons of gasoline: '))

gasoline_liters  = gasoline_gallons * 3.78541
gasoline_barrels = gasoline_gallons // 19.5
gasoline_co2     = gasoline_gallons * 20
gasoline_btu     = gasoline_gallons * 115000
ethanol_btu      = gasoline_btu / (gasoline_gallons * 75700)
gasoline_price   = gasoline_gallons * 3

print('Gasoline in liters: {0:.2f}'.format(gasoline_liters))
print('Number of barrels of oil required: ', gasoline_barrels)
print('Number of pounds of CO2 produced: ', gasoline_co2)
print('Equivalent energy amount of ethanol gallons: {0:.2f}'.format(ethanol_btu))
print('Price in U.S. dollars: ', gasoline_price)