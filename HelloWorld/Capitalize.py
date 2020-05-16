#!/bin/python3

import math
import os
import random
import re
import sys

OUTPUT_PATH = 'F:\Dipayan-Work\Python-PyCharm Projects\HelloWorld'

# Complete the solve function below.

def solve(s):
    s = list(s.split(' '))
    result = []
    for i in range(len(s)):
        L = list(s[i])
        L[0] = L[0].upper()
        result.append(''.join(map(str, L)))
    return (' '.join(result))


if __name__ == '__main__':
    s = input()

    print(solve(s))
