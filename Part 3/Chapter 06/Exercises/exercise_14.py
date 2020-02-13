#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def get_total_charge(amount_charged = int):
    
    if amount_charged not in [5, 10, 25, 50, 100]:
        raise Exception("\nTry again\nInvalid amount charged.")
    else:
        if amount_charged in [5, 10]:
            print("Success.\nNo benefits are added.")
        elif amount_charged == 25:
            print("Success.\nYou get $3 of extra phone time.")
        elif amount_charged == 50:
            print("Success.\nYou get $8 of extra phone time.")
        else:
            print("Success.\nYou get $20 of extra phone time.")
            
get_total_charge(amount_charged = 100)
        