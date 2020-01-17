# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:31:35 2020

@author: Pritam
"""

def plusMinus(arr):
    print (len([x for x in arr if x > 0])/n)
    print (len([x for x in arr if x < 0])/n)
    print (len([x for x in arr if x == 0])/n)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
