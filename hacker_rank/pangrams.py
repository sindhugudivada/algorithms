#!/bin/python
#https://www.hackerrank.com/challenges/pangrams/problem

import math
import os
import random
import re
import sys


# Complete the pangrams function below.
def pangrams(s):
    lst = [0] * 26
    s = s.replace(' ', '')
    for i in s:
        if i.isalpha():
            i = i.lower()
            lst[(ord(i) - ord('a'))] = 1
    for i in range(len(lst)):
        if lst[i] != 1:
            return "not pangram"
    return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()