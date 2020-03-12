#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def anagram(str_1 : str, 
            str_2 : str) -> bool:
    
    if list(str_1).sort() == list(str_2).sort():
        return True
    else:
        return False
    
#%%
        
def main():
    string_1 = str(input("First word: "))
    string_2 = str(input("Second word: "))
    
    if anagram(string_1, string_2):
        print("These words are anagrams!")
    else:
        print("The provided words are not anagrams.")