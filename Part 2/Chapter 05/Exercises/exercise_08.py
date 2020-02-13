#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# open the files
old_file = open("20_words.txt","r") 
new_file = open("20_words_parsed.txt","w")

# write each line
for line in old_file:
    for i in range(0, len(line.split()) // 5 * 5 + 1, 5):
        print(" ".join(line.split()[i:i+5]), file = new_file)
    
# close all files
old_file.close()
new_file.close()