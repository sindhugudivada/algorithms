#!/bin/python

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    temp=[]
    for i in range(len(a)-1,-1,-1):
        temp.append(a[i])
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
