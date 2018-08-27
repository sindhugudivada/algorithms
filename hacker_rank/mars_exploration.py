#!/bin/python
#https://www.hackerrank.com/challenges/mars-exploration/problem

import math
import os
import random
import re
import sys


# Complete the marsExploration function below.
def marsExploration(s):
    sub_string = 'SOS'
    count = 0
    for i in range(len(s)):
        if s[i] != sub_string[i % 3]:
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
