#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

text_dict = {121 : "why",
             114 : "are",
             117 : "you", 
             8   : "ate"}

in_str = str(input("Text message:\n"))

decrypted = ""
for l in in_str:
    
    # operation depends on l being an int or not
    checked = ord(l)
    if l.isdigit():
        checked = int(l)
        
    # look up in the dict, else paste the character
    if checked in text_dict:
        decrypted += text_dict[checked]
    else:
        decrypted += l

print("Decrypted message:\n{}".format(decrypted.capitalize()))
            