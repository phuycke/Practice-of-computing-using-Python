#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def calculate_energy(mass = float):
    c = 299792458
    return mass * c**2

m = float(input("Please input mass (in kg): "))
print("\nInputted mass: {0}\nCalculated energy: {1}".format(m, calculate_energy(mass = m)))