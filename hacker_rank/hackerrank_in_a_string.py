#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    j = 0
    for i in 'hackerrank':
        if i in s[j:]:
            j = s.index(i,j) + 1
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()