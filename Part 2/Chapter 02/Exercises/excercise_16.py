#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

top_num_str = input("What is the upper number for the range:") 
top_num     = int(top_num_str) 
number      = 2 

for number in range(number, top_num + 1):
    sum_of_divisors = 0 
    for divisor in range(1, number): 
        if number % divisor == 0: 
            sum_of_divisors = sum_of_divisors + divisor
    if number == sum_of_divisors:
        print(number,"is perfect")
    elif number < sum_of_divisors: 
        print(number,"is abundant")
    else:        
        print(number,"is deficient")
    number += 1