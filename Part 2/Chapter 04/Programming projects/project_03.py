#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# ask for the english word
english_word = str(input("Input your English word: "))

# immediately translate if the first letter is a vowel
if english_word[0] in "aeiou":
    pig_latin = english_word + "yay"
    print("Pig latin translation: {}".format(pig_latin))
# loop until a vowel is found, then do the translation
else:
    indx = 1
    while indx < len(english_word):
        if english_word[indx].lower() in "aeiou":
            break
        indx += 1
    print("Pig latin translation: {}".format(english_word[indx:] + english_word[:indx] + "ay"))
