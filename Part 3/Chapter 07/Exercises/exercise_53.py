#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def hole_counter(string = str):
    
    holes = 0
    for letter in string:
        if letter in ["a", "A" "b", "B", "d", "D" "e", "g", "o", "O" "p", "P", "q", "Q"]:
            holes += 1
    return {"Holes counted": holes,
            "No holes": len(string) - holes}

res = hole_counter(string = "right")
print(res)

#%%

def words_with_holes(string = str):
    
    word_list  = string.split(" ")
    word_count = 0
    
    for words in word_list:
        local_count = 0
        for letter in words:
            if letter in ["a", "A" "b", "B", "d", "D", "e", "g", "o", "O" "p", "P", "q", "Q"]:
                local_count += 1
            if local_count >= 2:
                word_count += 1
                break
    return {"Words with 2 or more holes": word_count}

res = words_with_holes(string = "I see I need to go")
print(res)

