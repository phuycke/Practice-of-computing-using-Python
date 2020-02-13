#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from random import sample

#%%

# get the computer to choose the correct sequence
options = list("abcdef".upper())
chosen  = sample(options, 4)

# keep track of the game's progress
counting = 1
game_won = False

# ask the player for a sequence each round until the game is determined
while counting <= 12:
    
    print("\n* * * Round {0:02d} * * *".format(counting))
    my_guess    = str(input("Please provide your input.\nUppercase case letters separated by a space: "))
    my_sequence = my_guess.split()
    
    # check the inputted sequence and determine feedback
    black_pegs, white_pegs = 0, 0
    for i in range(len(my_sequence)):
        if my_sequence[i] in chosen:
            if my_sequence[i] == chosen[i]:
                black_pegs += 1
            else:
                white_pegs +=1
    feedback = "black pegs: {0} / white pegs: {1}".format(black_pegs, white_pegs)
    
    print("Player's guess: {0: <12s}Feedback: {1:s}".format(my_guess, 
                                                            feedback))
    
    # stop if the game is won, or continue as long as round number < 12
    if black_pegs == 4:
        game_won = True
        break

    counting += 1

# print the final feedback
if game_won:
    print("\n- - - -\nCongratulations, you have won the game using the combination {}".format(my_guess))
else:
    print("\n- - - -\nWe're sorry, you lost.\nThe correct sequence was: {}".format(" ".join(chosen)))