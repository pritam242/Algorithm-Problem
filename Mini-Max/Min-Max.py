# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:13:05 2020

@author: Pritam
"""

def miniMaxSum(arr):
    result=sum(arr)

    print(result-(max(arr)), result-(min(arr)))

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    miniMaxSum(arr)