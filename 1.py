#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: alexogilvie

Project Euler Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

import time
def compute():    
    timer = time.time()
    ans = sum(i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0))

    print ("Answer is " + str(ans) + ". Completed in "+str(time.time()-timer)+" seconds.")
    return ans