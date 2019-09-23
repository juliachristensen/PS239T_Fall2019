# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:42:40 2019

@author: anustubh agnihotri 
borrowing example from Python for Everybody by Charles Severance
"""

total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('Average:', average)