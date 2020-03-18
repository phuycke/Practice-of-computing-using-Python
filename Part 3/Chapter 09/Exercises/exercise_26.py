#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from sklearn.datasets import load_iris

import numpy  as np
import pandas as pd

#%%

iris          = load_iris()
df            = pd.DataFrame(iris.data)
df.columns    = iris.feature_names
df["Species"] = iris.target

iris_dict = dict()

for species in set(df["Species"]):
    iris_dict[species] = np.mean(df.loc[df["Species"] == species])