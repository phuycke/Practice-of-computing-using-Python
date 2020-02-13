#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def leap_year(year = int):
    
    # get the standard string
    is_leap = ""
    
    # decision tree for checking whether it is a leap year
    if year % 400 == 0:
        pass
    else:
        if year % 4 == 0 and year % 100 != 0:
            pass
        else:
            is_leap = " not"
        
    print("The year {} is{} a leap year.".format(year, 
                                                 is_leap))
    

leap_year(1900)