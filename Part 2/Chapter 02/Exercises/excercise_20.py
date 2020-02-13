#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: Pieter Huycke
email:   pieter.huycke@ugent.be
GitHub:  phuycke
"""

#%%

from cmath import sqrt as csqrt
from math  import sqrt as msqrt

abc     = str(input('Values for a,b and c (space separated)?\n'))
a, b, c = map(int, abc.split(' '))

if (b**2 - 4*a*c) < 0:
    complex_root = csqrt((b**2 - 4*a*c) + 0j)
    quad1, quad2 = -b + complex_root / 2*a, -b - complex_root / 2*a
    print('The roots are imaginary:\n{0}\n{1}'.format(quad1, 
                                                      quad2))
else:
    if msqrt(b**2 - 4*a*c) == 0:
        print('There is only one solution:\n{}'.format(-b))
    else:
        quad1, quad2 = -b + msqrt(b**2 - 4*a*c) / 2*a, -b - msqrt(b**2 - 4*a*c) / 2*a
        print('There are two solutions:\n{0}\n{1}'.format(quad1, 
                                                          quad2))

    
