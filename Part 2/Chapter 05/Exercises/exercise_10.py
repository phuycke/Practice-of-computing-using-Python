#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

numbers = []

# collect the 3 numbers
for i in range(3):
    number = input("Please provide a number: ")
    while True:
        try:
            number = int(number)
            numbers.append(number)
            break
        except ValueError:
            print("\n* * *\nWrong input provided\n* * *")
            number = input("Please provide a number: ")

# catch the 0 division error
try:
    result = (numbers[0] / numbers[1]) + numbers[2]
    print("Result: {0:.2f}".format(result))
except ZeroDivisionError:
    print("\nThe second number is 0.\nIllegal action.")