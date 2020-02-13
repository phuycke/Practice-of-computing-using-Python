#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# check if the number is a palindrome
def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

# check all conditions
for mile in range(100000, 999999):
    if is_palindrome(str(mile)[-4:]) and not is_palindrome(str(mile)[-5:]):
        if is_palindrome(str(mile + 1)[-5:]):
            if is_palindrome(str(mile + 2)[1:5]):
                if is_palindrome(str(mile + 3)):
                    print('Answer: {0}'.format(mile))