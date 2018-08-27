#!/bin/python
#https://www.hackerrank.com/challenges/camelcase/problem

import math
import os
import random
import re
import sys


# Complete the camelcase function below.
def camelcase(s):
    count = 1
    for i in range(len(s)):
        if s[i].isupper():
            count = count + 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()


