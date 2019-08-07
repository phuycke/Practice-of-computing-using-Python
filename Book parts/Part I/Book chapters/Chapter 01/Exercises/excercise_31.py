#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

# parameters
radius_earth    = 6378    * 10**3
mass_earth      = 5.9742  * 10**24
gravitational_c = 6.67300 * 10**-11

mass_mr_jones   = float(input('Mass of Mr. Jones (m, in kg): '))

# computation
gravitational_force = gravitational_c * (mass_earth) * (mass_mr_jones) \
                      / (radius_earth ** 2)

# result
print("F:\n\t{0:.4f}\ng (F / m):\n\t {1:.4f}".format(gravitational_force,
                                                     gravitational_force / mass_mr_jones))
