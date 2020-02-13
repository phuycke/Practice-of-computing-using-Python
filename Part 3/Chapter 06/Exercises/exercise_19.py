#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

def time_printer(input_time = str):
    
    # check whether the format holds (1/3)
    try:
        time_long, time_short = input_time.split(" ")
    except ValueError:
        print("The inputted time should be of the format:\n\tMM/DD/YYYY HR:MIN:SEC")
    
    # check whether the format holds (2/3)
    try: 
        month, day, year = time_long.split(r"/")
    except ValueError:
        print("Months, days and years should be of the format:\n\tMM/DD/YYYY")
    
    # check whether the format holds (3/3)
    try: 
        hour, minute, second = time_short.split(r":")
    except ValueError:
        print("Hours, minutes and days should be of the format:\n\tHR:MIN:SEC")
        
    # check whether the provided inputs are all integers
    all_time = [month, day, year, hour, minute, second]
    
    for i in range(len(all_time)):
        try:
            all_time[i] = int(all_time[i])
        except ValueError:
            print("Your time indication should be an integer")
        
    # check whether the provided numbers make sense
    labels  = ["Month", "Day", "Year", "Hours", "Minutes", "Seconds"]
    allowed = [[1, 12], None, [0, 9999], [0, 24], [0, 60], [0, 60]]

    # helper function
    def time_error(time, value):
        raise ValueError("\n{} = {}\nImplausible value".format(time,
                                                               value))

    # list all days that have 31 days
    days_31 = [1, 3, 5, 7, 8, 10, 12]

    for i in range(len(all_time)):
        # special check for the month/day interaction
        if i == 1:
            # not possible
            if all_time[1] < 1:
                time_error(labels[i], 
                           all_time[i])
            # make a distinction based on the month
            if all_time[0] in days_31:
                if all_time[i] > 31:
                    time_error(labels[i], 
                               all_time[i])
            elif all_time[0] == 2:
                if all_time[i] > 28:
                    time_error(labels[i], 
                               all_time[i])
            else:
                if all_time[i] > 30:
                    time_error(labels[i], 
                               all_time[i])
        # the other checks are easier (e.g. seconds should be in [0, 60])
        else:
            if all_time[i] < allowed[i][0] or all_time[i] > allowed[i][1]:
                time_error(labels[i],
                           all_time[i])
        
    # printing all
    print("{}/{}/{}".format(month, day, year))
    print("{}:{}:{}".format(hour, minute, second))
    print("{}/{}".format(month, year))
    if int(hour) <= 12:
        print("Time: AM")
    else:
        print("Time: PM")
        
# test the function
time_printer("08/31/1990 13:12:12")