#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import string
import random

#%%

# open the files
old_file = open("original_text.txt","r") 
new_file = open("permuted_text.txt","w")

# write each line
for line in old_file:
    for word in line.split():
        for letter in list(word):
            if letter.lower() in string.ascii_lowercase:
                rand_number = random.randint(1, 13)
                if ord(letter) >= ord("n"):
                    letter = chr(ord(letter) - 26 + rand_number)
                else:
                    letter = chr(ord(letter) + rand_number)
            print(letter.strip(), end = "", file = new_file)

# close all files
old_file.close()
new_file.close()