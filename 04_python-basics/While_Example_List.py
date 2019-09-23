# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:46:18 2019

@author: anustubh
borrowing example from Python for Everybody by Charles Severance

"""

numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)