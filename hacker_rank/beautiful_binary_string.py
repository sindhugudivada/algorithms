#!/bin/python

#https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    count=0
    #string is immutable. So convert it into a list of characters.
    c = list(b)
    for i in range(2,len(b)):
        if c[i-2]=='0' and c[i-1] =='1' and c[i] == '0':
            count=count+1
            c[i]=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    b = raw_input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
