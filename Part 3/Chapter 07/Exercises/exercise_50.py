#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def transform(list1  = list, list2 = list,
              index1 = int,  index2 = int):
    list2.extend(list1[index1:index2][::-1])
    return list2

res = transform(list1  = [1,2,3,4,5,6,7,8,9], list2 = [100, 200],
                index1 = 4, index2 = 7)
print(res)