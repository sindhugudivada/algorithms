#!/bin/python

import math
import os
import random
import re
import sys


# Complete the superReducedString function below.
def superReducedString(s):
    c = []
    for ch in s:
        if c and c[len(c) - 1] == ch:
            c.pop()
        else:
            c.append(ch)
    c = ''.join(c)
    return c or 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()