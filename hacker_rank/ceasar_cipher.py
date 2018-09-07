#!/bin/python

import math
import os
import random
import re
import sys


# Complete the caesarCipher function below.
def caesarCipher(s, k):
    m = []
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            if (ord(i) + k) > 122:
                m.append(chr(96 + (ord(i) + k) - 122))
            else:
                m.append(chr(ord(i) + k))
        elif ord(i) >= 65 and ord(i) <= 90:
            if (ord(i) + k) > 90:
                m.append(chr(64 + (ord(i) + k) - 90))
            else:
                m.append(chr(ord(i) + k))
        else:
            m.append(i)
    return "".join(j for j in m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    k = int(raw_input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
