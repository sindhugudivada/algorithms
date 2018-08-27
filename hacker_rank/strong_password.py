#!/bin/python
#https://www.hackerrank.com/challenges/strong-password/problem

import math
import os
import random
import re
import sys


# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count = 0
    p = 0
    if not contains_digit(password):
        count = count + 1
    print count
    if not contains_lowercase(password):
        count = count + 1
    print count
    if not contains_uppercase(password):
        count = count + 1
    print count
    if not contains_special_character(password):
        count = count + 1
    print count
    """
    To find minimum characters that need be added.
    """
    if n + count < 6:
        p = 6 - n - count
    return p + count


def contains_digit(password):
    numbers = "0123456789"
    for c in password:
        if c in numbers:
            return True
    return False


def contains_lowercase(password):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    for c in password:
        if c in lower_case:
            return True
    return False


def contains_uppercase(password):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in password:
        if c in upper_case:
            return True
    return False


def contains_special_character(password):
    special_characters = "!@#$%^&*()-+"
    for c in password:
        if c in special_characters:
            return True
    return False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    password = raw_input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
