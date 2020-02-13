#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

my_string = str(input("Inputted string: ")).split()
for i in range(len(my_string)):
    my_string[i] = my_string[i].capitalize()

new_string = " ".join(my_string)
print("Reformatted string: {}".format(new_string))