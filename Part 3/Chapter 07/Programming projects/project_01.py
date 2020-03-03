#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# Word puzzle driver
# Assumes word list.txt file of one word per line
def get_word_list():
    
    """ 
    Return a list of words from a word list.txt file. 
    """
    
    data_file = open("word_list.txt","r")
    word_list = [] # s t a r t with an empty word l i s t

    for word in data_file: # for every word ( l ine ) in the f i l e
        # s t r i p o f f end−of−l i n e characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    
    return word_list


#%%
    

# exercise e
def exercise_e(word_list):
    
    """ 
    Puzzle solution goes here. 
    """
    
    vowels = "aeiuo"
    
    for word in word_list:
        if len(word) != 7:
            continue
        if "s" in word:
            continue
        vowel_count = 0
        for vowel in vowels:
            vowel_count += word.count(vowel)
            if vowel_count > 1:
                break
        if vowel_count == 1:
            return word

word_list = get_word_list()
answer    = exercise_e(word_list)
print(answer)

#%%


# exercise f
def exercise_j(word_list):
    
    """ 
    Puzzle solution goes here. 
    """
    
    nacls = []
    
    for word in word_list:
        if "nacle" in word:
            nacls.append(word)
    return nacls


word_list = get_word_list()
answer    = exercise_j(word_list)
print(answer)