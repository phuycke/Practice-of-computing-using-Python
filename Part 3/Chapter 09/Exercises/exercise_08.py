#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

my_dict = {'a':15 , 'c':35, 'b':20}

[print("Dictionary key: ", key) for key in my_dict.keys()]
print("- - - -")

[print("Dictionary value: ", val) for val in my_dict.values()]
print("- - - -")

[print("Key: {} --> value: {}".format(k, v)) for k,v in my_dict.items()]
print("- - - -")


[print("Key: {} --> value: {}".format(k, v)) for k, v in sorted(my_dict.items(), 
                                                                key = lambda kv: kv[1])]
print("- - - -")
