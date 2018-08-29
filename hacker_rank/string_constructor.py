#!/bin/python

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):
    dollar_amount=0
    p=[ ]
    for i in s:
        if i not in p:
            p.append(i)
            dollar_amount=dollar_amount+1
        else:
            p.append(i)
            dollar_amount=dollar_amount
    return dollar_amount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()