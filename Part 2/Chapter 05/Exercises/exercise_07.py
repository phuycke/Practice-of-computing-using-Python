#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import string

#%%

# make a dictionary for each letter
dictionary = {}
for letter in string.ascii_lowercase:
    dictionary[letter] = 0

# open the file
text_file = open("random_100.txt","r") 

for line in text_file:                                        # read each line
    for character in list(line):                              # get characters
        if character.lower() in string.ascii_lowercase:
            dictionary[character.lower()] += 1                # update dict

# close the file when done
text_file.close()

#%%

import matplotlib.pylab as plt

lists = sorted(dictionary.items()) 
x, y  = zip(*lists)

# plot the letter count
plt.plot(x, y)
plt.show()