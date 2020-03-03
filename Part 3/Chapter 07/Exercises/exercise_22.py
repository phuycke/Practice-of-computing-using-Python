#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

given_list = [10, 20, 30, 40, 50]
new_list   = []

for i in range(len(given_list)):
    summation  = 0
    self_added = False
    if (i + 1) < len(given_list):
        summation += (given_list[i] + given_list[i + 1]) 
        self_added = True
    if (i - 1) >= 0:
        if self_added:
            summation += given_list[i - 1]
        else:
            summation += given_list[i - 1] + given_list[i]
    new_list.append(summation)