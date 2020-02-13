#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# open the files
this_file = open("thisFile.txt","r") 
that_file = open("thatFile.txt","w")

# write each line
for line_str in this_file:
    print(line_str.strip(), file = that_file)
    
# close all files
this_file.close()
that_file.close()