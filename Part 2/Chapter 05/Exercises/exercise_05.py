#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# keep asking the filename until an existing file is found
file_str = input("Open what file:")
while True:
   try: 
       input_file = open(file_str)     # potential user error 9
       break
   except IOError:
        print("The file",file_str,"doesn't exist.")
        file_str= input("Open what file:")
       
line_count_int = 1
for line_str in input_file:
    line_count_int += 1

# keep asking a row number until an int is provided
find_line_str = input("Which line (integer):")
while True:
   try: 
       find_line_int = int(find_line_str)     # potential user error 9
       if find_line_int <= line_count_int:
           break
   except ValueError: 
       print("Line",find_line_str,"isn't a legal line number.")
       find_line_str = input("Which line (integer):")
           
line_count_int = 1
for line_str in input_file:
    if line_count_int == find_line_int: 
        print("Line {} of file {} is {}".format(find_line_int, file_str, line_str)) 
        break
    line_count_int += 1

input_file.close() 
print("End of the program")