#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""


#%%

# parameters
page_lines   = int(input('Lines per column: '))
page_columns = int(input('Columns per page: '))
page_entries = page_lines * page_columns

# check which entry is sought
page_number  = int(input('Looking for entry number: '))

# check on what page this entry is located
page_number  = page_number // page_entries 

# print the output
print('\nThis entry is located on page {}.'.format(page_number + 1))
