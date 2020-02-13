#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

old_name = "Chapman, Graham Arthur"
lastname, firstname, middlename = old_name.replace(",", "").split()
new_name = " ".join([firstname, middlename, lastname])
