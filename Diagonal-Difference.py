# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:13:01 2020

@author: Pritam
"""

def diagonalDifference(arr):
   
    prim_diag=0
    sec_diag=0
    length=len(arr)

    for i in range(length):
        prim_diag+=arr[i][i]
        sec_diag+=arr[length-1-i][i]

    return abs(prim_diag-sec_diag)


    return (abs(sum1-sum2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()