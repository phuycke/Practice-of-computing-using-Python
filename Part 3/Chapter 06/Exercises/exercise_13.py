#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# I don't really get the assignment?
def make_payment(payment = float):
    
    if payment < 20 or payment > 1000:
        print("Retry.")
    else:
        print("Success.")
    