#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def message_check(message = str):
    
    if len(message) < 160:
        return message
    else:
        return message[:160]
    
longer = message_check("In certain chat programs or messaging applications, there is a limit on the number of characters that you can send in a message. Write a function that takes as input the message (a string) and checks whether the number of characters is less than 160 (or not). If the length of the message is less than 160, the message should be returned. If the length of the message is greater than 160, a string consisting of only the first 160 characters should be returned.")
print(longer)

shorter = message_check("In certain chat programs, there is a limit on the number of characters that you can send in a message.")
print(shorter)

#%%

def first_20_words(message = str):
    
    words = message.split(" ")
    if len(words) > 20:
        raise ValueError("\nError\nThe message can only contain 20 words.")
    else:
        print("\nMessage passed:\n{}".format(message))
        

first_20_words("There is a limit on the number of characters that you can send in a message.")
first_20_words(longer)

    

