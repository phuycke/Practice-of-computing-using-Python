#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import string

my_string  = str(input("Inputted string: "))
new_string = ""
 
for ch in my_string:
    if ch in string.ascii_uppercase:
        new_string += ch.swapcase()
    else:
        new_string += ch
        
print("Reformated string: {}".format(new_string))