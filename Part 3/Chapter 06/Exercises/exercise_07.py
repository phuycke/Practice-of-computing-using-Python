#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def display_menu():
    
    print("\nAvailable options:")
    print("1. Messaging\n2. Contacts\n3. Games\n4. Settings\n5. Media\n6. Web")

    choice = str(input("Please provide your choice: "))
    
    return choice

def messaging():
    print("Call received")

def get_choice(user_choice = str):
    
    if user_choice.lower() == "messaging":
        messaging()

# get the user choice
chosen = display_menu()
get_choice(chosen)
