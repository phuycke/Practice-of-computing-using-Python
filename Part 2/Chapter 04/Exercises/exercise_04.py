#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

my_string = str(input("Custom string: "))

if len(my_string) % 2 == 0:
    print("First half of the string: {}".format(my_string[:len(my_string) // 2]))
    print("Second half of the string: {}".format(my_string[len(my_string) // 2:]))
else:
    print("First half of the string: {}".format(my_string[:len(my_string) // 2]))
    print("Middle letter of the string: {}".format(my_string[len(my_string) // 2: len(my_string) // 2 + 1]))
    print("Second half of the string: {}".format(my_string[len(my_string) // 2 + 1:]))
