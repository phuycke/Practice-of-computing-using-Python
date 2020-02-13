#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%


def player_1(num_beans = int):
        
    return num_beans - 1
  

def player_2(num_beans = int):
        
    return num_beans - 1
  
    
def smart_player(num_beans = int):
    
   for i in range(1, 3):
       if num_beans - i == 1:
           return num_beans - i
   else:
       return num_beans - 1
        

#%%
            
def main():
    
    bean_count = 16
    while True:
        
        bean_count = player_1(bean_count)            
        if bean_count == 1:
            print("Smart player lost.")
            break
        
        bean_count = smart_player(bean_count)
        if bean_count == 1:
            print("Player 1 lost.")
            break
main()