#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

my_string = str(input("Custom string: "))

print("First half of the string: {}".format(my_string[:len(my_string) // 2]))
print("Second half of the string: {}".format(my_string[len(my_string) // 2:]))
