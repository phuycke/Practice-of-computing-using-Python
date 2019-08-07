#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

"""
Note 1:
    I did not follow the formula described in the book, as the formula did not 
    appear to be correct. I followed the one described on Wikipedia instead:
        https://en.wikipedia.org/wiki/Passer_rating#NFL_and_CFL_formula

Note 2:
    The formula from wikipedia seemed to work out. I tested it on the stats
    found on this website:
        https://www.teamrankings.com/nfl/player/drew-brees
    and the calculations check out.
"""

# needed parameters
pass_completed = int(input('Passes completed: '))
pass_attempted = int(input('Passes attempted: '))
passing_yards  = int(input('Total passing yards: '))
touchdowns     = int(input('Touchdowns: '))
interceptions  = int(input('Interceptions: '))

# computations
c = ((pass_completed / pass_attempted) - 0.3) * 5
y = ((passing_yards / pass_attempted) - 3) / 4
t = touchdowns / pass_attempted * 20
i = 2.375 - (interceptions / pass_attempted * 25)

# end result
pass_rating = ((c + y + t + i) / 6) * 100

print("\n**\nThe pass rating is {0:.1f} \n**".format(pass_rating))
