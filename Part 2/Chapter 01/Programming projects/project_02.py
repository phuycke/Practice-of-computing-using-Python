#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

distance_from_sun = 16637000000   # distance at 25/09/2009 in miles
voyager_velocity  = 38241         # voyager velocity in miles/hour

days_since_september  = int(input('Days passed since 25/09/2009: '))
hours_since_september = days_since_september * 24

# report 1: current distance from sun in miles
current_distance_imperial = (hours_since_september * voyager_velocity) + \
                             distance_from_sun
print('Current distance from sun: {0} miles'.format(current_distance_imperial))

# report 2: current distance from sun in km
current_distance_metric = current_distance_imperial * 1.609344
print('Current distance from sun: {0:.2f} km'.format(current_distance_metric))

# report 3: current distance from sun in astronomical units
current_distance_au = current_distance_metric * (6.6845871226706 * 10**-9)
print('Current distance from sun: {0:.2f} AU'.format(current_distance_au))

# report 4: round-trip time for radio communication
radio_speed_m  = 299792458              # speed of light in m/s
radio_speed_km = radio_speed_m / 1000   # speed of light in km/s

radio_time_sec = current_distance_metric / radio_speed_km   # time in seconds
radio_time_h   = radio_time_sec * 3600
print("Round-trip time for radio communication: {0:.2f} hour".format(radio_time_h))
