#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def reverse(string : str) -> str:
    """
    Reverse an inputted string

    Parameters
    ----------
    string : str
        The string we want to reverse.

    Returns
    -------
    str
        The reversed string.

    """
    
    return string[::-1]

#%%

print(reverse("stressed"))