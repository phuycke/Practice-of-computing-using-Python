#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def get_discount(price = float, 
                 member = bool):
    
    # apply father's day discount
    fixed_discount = .95
    price         *= fixed_discount
    
    # additional discount if you are a member
    if member:
        price *= .9
    
    return price

# test the function
discounted_price = get_discount(100, True)
print("Original price: {0} euro\nDiscounted price: {1} euro".format(100, 
                                                                    discounted_price))
    