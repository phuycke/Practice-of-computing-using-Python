#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

n = int(input('Inputted number (Int):\n'))

#%%

# Part a
print('Sum of all integers from 1 to {0}: {1}'.format(n, int(n*(n+1)/2)))

#%%

# Part b
print('Sum of consecutive numbers')
for i in range(1, n+1):
    print(sum(range(1,i+1)))
    
#%%
    
# Part c
print('Sum of consecutive numbers if divisible')
for i in range(1, n+1):
    if sum(range(1,i+1)) % len(range(1,i+1)) == 0:
        print(sum(range(1,i+1)))