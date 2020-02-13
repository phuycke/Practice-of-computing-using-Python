#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def find(string     = str, 
         substring  = str,
         start_indx = int, 
         stop_indx  = int):
    
    """
    Find the first occurence of 'substring' in 'string'
    Return None if no occurences
    """
    
    # check if the substring is in the specified part of the string
    if substring in string[start_indx:stop_indx]:
        return string[start_indx:stop_indx].index(substring)
    else:
        return None
  
    
def multi_string(string     = str, 
                 substring  = str,
                 start_indx = int, 
                 stop_indx  = int):

    """
    Find all occurences of 'substring' in 'string'
    Return None if no occurences
    """
    
    if find(string, substring, start_indx, stop_indx) is None:
        return None
    else:
        indices = [find(string, substring, start_indx, stop_indx)]
        while find(string, substring, indices[-1] + 1, stop_indx) is not None:
            result  = find(string, substring, indices[-1] + 1, stop_indx)
            indices.append(indices[-1] + result + 1)
        return indices
    
    
#%%
            
string_test = "wolokipiwolokipiwolokipiwolokipi"
substr_test = "olo"

return_val = multi_string(string     = string_test, 
                          substring  = substr_test,
                          start_indx = 0,
                          stop_indx  = len(string_test))
print("Sought indices:\n", return_val)
