#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def fibo(n_fibos = int):
    
    fibo_list = [1, 1]
        
    while len(fibo_list) < n_fibos:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    
    print("The first {} Fibonacci numbers:".format(n_fibos))
    [print("{0:2d}: {1: >10d}".format(i+1, fibo_list[i])) for i in range(len(fibo_list))]
    
fibo(n_fibos = 20)

#%%

def get_nth_fibo(n = int):
    
    fibo_list = [1, 1]
        
    while len(fibo_list) < n:
        fibo_list.append(fibo_list[-2] + fibo_list[-1])
    
    print("\nThe {}th Fibonacci numbers: {}".format(n, 
                                                  fibo_list[-1]))

get_nth_fibo(n = 17)