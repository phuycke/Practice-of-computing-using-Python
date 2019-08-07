#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# parameters
time_in_seconds = 70000

# compute the time
seconds = time_in_seconds           % 60
minutes = (time_in_seconds // 60)   % 60
hours   = (time_in_seconds // 3600) % 24

# print the solution
print('In seconds = {0}\nH:M:S = {1}:{2}:{3}'.format(time_in_seconds,
                                                     hours,
                                                     minutes,
                                                     seconds))