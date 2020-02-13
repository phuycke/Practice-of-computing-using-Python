#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

import math

# ask for input
number = int(input('Inputted number:\n'))

# reprompt until a perfect square is provided
while number != (int(math.sqrt(number))**2):
    number = int(input('Inputted number:\n'))
print('This is a perfect square')