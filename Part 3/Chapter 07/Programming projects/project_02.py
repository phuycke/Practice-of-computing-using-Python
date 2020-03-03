#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

def pascals_triangle(rows = int):
    
    if rows < 1:
        return None
    elif rows == 1:
        return [1]
    else:
        triangle = [[1]]
        for i in range(rows - 1):
            # make a copy and add zeros to the beginning and end of the list
            root = triangle[i][:]
            root.extend([0])
            root.insert(0, 0)
            
            # compute the new rows
            new_row = []
            indx    = 0
            while indx != len(root) - 1:
                new_row.append(root[indx] + root[indx + 1])
                indx +=  1
            
            triangle.append(new_row)
    
        return triangle
    
    
result = pascals_triangle(rows = 20)
[print(r) for r in result]