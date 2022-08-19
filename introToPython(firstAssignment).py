# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 20:05:32 2022

@author: ya boy

first assignment: find sum of first 100 integers

8/15/2022 (august)
"""

import numpy as np

#nums = len(100) [failed idea]
list100 = np.linspace(1, 100, 100)#starting num, ending number, number of number
sum100 = sum(list100)
print('the sum of the first 100 numbers is: {}'.format(sum100)) #need to ensure there is a .format connecting the variable
#result is a float



otherSum=0
list100v2 = np.linspace(1, 100, 100)
                                                        #[failed idea]#for x in list100v2:
for i in range(101):   # : indicatees start of loop    #go to 101 since it starts at 0
    otherSum += i                                       #otherSum+=x
print('otherSum = {}'.format(otherSum))
#result is an integer