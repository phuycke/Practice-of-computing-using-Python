#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# some units
birth_per_year     = 60//7  * 60 * 24 * 365   # a birth every 7 seconds
death_per_year     = 60//13 * 60 * 24 * 365   # a death every 13 seconds
immigrant_per_year = 60//35 * 60 * 24 * 365   # an immigrant every 35 seconds

current_population = 307357870                # current census

years = int(input('Years passed: '))
updated_population = current_population + \
                     3 * (birth_per_year - death_per_year + immigrant_per_year)
print("The estimated population count in {0} years is {1}".format(years,
                                                                  updated_population))