#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

inputted = "Who's on first"
print("First index: ", inputted.find("o"))
print("Second index: ", inputted.find("o", inputted.find("o") + 1))
