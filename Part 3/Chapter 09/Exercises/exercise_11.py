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


def caesar_cipher(input_string: str,
                  shift       : int,
                  decode      : bool) -> str:
    
    # get the dictionary
    letter_dict = dict() 
    for l in string.ascii_lowercase:
        letter_dict[ord(l)] = l
    
    output = ""
    
    if decode:
        for l in input_string:
            if l not in string.ascii_lowercase:
                output += l
            else:
                if ord(l) - shift < min(letter_dict.keys()):
                    output += letter_dict[max(letter_dict.keys()) - (shift - 1)]
                else:
                    output += letter_dict[ord(l) - shift]        
    return output


# main program    
in_str = str(input("String to decode:\n"))
sh     = int(input("Shift parameter:\n"))
print("Decoded string:\n {}".format(caesar_cipher(in_str, 
                                                  sh, 
                                                  True)))