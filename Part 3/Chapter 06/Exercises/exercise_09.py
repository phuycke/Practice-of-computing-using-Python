#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from string import ascii_lowercase as alphabet

def letter_type(string = str):
    
    vowels = "aeiou"
    
    vowel_count     = 0
    consonant_count = 0
    
    # convert the string to avoid uppercase issues
    string = string.lower()
    
    # loop over all letters and determine what they are
    for letter in string:
        if letter in alphabet:
            if letter in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
            
    print("The inputted string contains {} vowels and {} consonants.".format(vowel_count, 
                                                                             consonant_count))
    
letter_type("This is a check.")