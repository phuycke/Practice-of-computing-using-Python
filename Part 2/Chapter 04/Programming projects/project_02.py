#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# ask for the inputs
adj_1      = str(input("Please provide an adjective: "))
noun_1     = str(input("Please provide a noun: "))
adj_2      = str(input("Please provide an adjective: "))
noun_2     = str(input("Please provide a noun: "))
adj_3      = str(input("Please provide an adjective: "))
noun_3     = str(input("Please provide a noun: "))
girls_name = str(input("Please provide a girl's name: "))

# print the actual story
print("\nOnce upon a time in the middle of a {adj_1} {noun_1} stood a {adj_2} {noun_2}, the home of a {adj_1} {adj_3} {noun_3} known to everyone as {name_girl}.".format(adj_1     = adj_1,
                                                                                                                                                                         adj_2     = adj_2,
                                                                                                                                                                         adj_3     = adj_3,
                                                                                                                                                                         noun_1    = noun_1,
                                                                                                                                                                         noun_2    = noun_2,
                                                                                                                                                                         noun_3    = noun_3,
                                                                                                                                                                         name_girl = girls_name))