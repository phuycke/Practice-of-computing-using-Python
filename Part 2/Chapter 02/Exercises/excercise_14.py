#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

string = '1'
for i in range(1, 10):
    print(int(string) * 8 + i)
    string += str(i + 1)

#%%

string = '1'
for i in range(2, 11):
    print(int(string) * 9 + i)
    string += str(i)

#%%
    
string = '9'
for i in range(7, -1, -1):
    print(int(string) * 9 + i)
    string += str(i + 1)

#%%

for i in range(1, 10):
    print(int('1' * i) * int('1' * i))
