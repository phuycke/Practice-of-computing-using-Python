#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%


import random
import string


#%%

        
def scramble_text(input_text = str):
    
    input_list     = list(input_text.split(" "))
    scrambled_list = []
    for word in input_list:
        if len(word) < 4:
            scrambled_list.append(word)
        else:
            stop_index = len(word) - 1
            while word[stop_index].lower() not in string.ascii_lowercase:
                stop_index -= 1
            substring = word[1:stop_index]
            scrambled = list(substring)
            random.shuffle(scrambled)
            
            scrambled.insert(0, word[0])
            scrambled.append(word[stop_index])
            
            if stop_index != (len(word) - 1):
                scrambled.extend(list(word[stop_index+1:]))
                
            scrambled = "".join(scrambled)
            
            scrambled_list.append(scrambled)
            
    return " ".join(scrambled_list)


#%%
   
text = "Four score and seven years ago our fathers brought forth on this continent a new nation,"

scrambled = scramble_text(input_text = text)
print(scrambled)