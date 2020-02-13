#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

try:
    file_str = input("Open what file:")
    while True:
       try: 
           input_file = open(file_str)     # potential user error 9
           break
       except IOError:
            print("The file",file_str,"doesn't exist.")
            file_str= input("Open what file:")
    
    find_line_str = input("Which line (integer):")
    find_line_int = int(find_line_str) # potential user error
    
    line_count_int = 1
    for line_str in input_file:
        if line_count_int == find_line_int: 
            print("Line {} of file {} is {}".format(find_line_int, file_str, line_str)) 
            break
        line_count_int += 1
    else:
        print("Line {} of file {} not found".format(find_line_int, file_str)) 
    input_file.close() 
except ValueError: 
    print("Line",find_line_str,"isn't a legal line number.")
print("End of the program")