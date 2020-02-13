#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# ask for input
knuts = int(input("How may knuts do you have?\n"))

# start values
sickles  = 0
galleons = 0

# compute galleons when possible, sickles otherwise
while knuts / (29 * 17) >= 1:
    galleons += 1
    knuts    -= (29 * 17)
else:    
    while knuts >= 29:
        sickles += 1
        knuts   -= 29

# get the output
print("Galleons: {0}\nSickles: {1}\nKnuts: {2}".format(galleons, sickles, knuts))