#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def determine_result(score_team_1 = int, score_team_2 = int):
    result = "We have a tie between the two teams."
    if score_team_1 > score_team_2:
        result = "Team 1 has won the game."
    elif score_team_1 < score_team_2:
        result = "Team 2 has won the game."
    else:
        pass
    print(result)
    
determine_result(1, 2)
