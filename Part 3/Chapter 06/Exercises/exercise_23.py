#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

import time

def draw_progressbar(wait_time = int):
    
    print("\n")
    for i in range(10):
        print("X ", end = "")
        time.sleep(wait_time / 10) 
    
draw_progressbar(wait_time = 15)