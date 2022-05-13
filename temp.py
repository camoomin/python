# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def add(x):
    a=0
    for t in range(1,x+1):
        a+=t
    return a
    


def times(x):
    a=1
    for t in range(1,x+1):
        a=a*t
    return a
    
z = times(10)
print(z)
