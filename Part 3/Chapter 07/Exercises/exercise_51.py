#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def sum_list(l = list):
    
    assert len(l) > 0

    if len(l) == 1:
        return l[0]
    
    result = []
    for i in range(len(l) // 2):
        summation = (l[i] + l[-i - 1])
        result.append(summation)
    if len(l) % 2 != 0:
        result.insert(len(result) // 2, l[len(l) // 2])
        
    return result


res = sum_list(l = [1,2,3,4,5,6,7,8,9])