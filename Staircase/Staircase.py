# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:06:13 2020

@author: Pritam
"""

def staircase(n):
    for i in range(1, n + 1):
        print(str('#'*i).rjust(n))

if __name__ == '__main__':
    n = int(input())

    staircase(n)