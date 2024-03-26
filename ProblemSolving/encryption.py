# https://www.hackerrank.com/challenges/encryption/problem
import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def encryption(s):
    s = s.replace(" ", "")
    l = len(s)
    rows = math.floor(math.sqrt(l))
    cols = math.ceil(math.sqrt(l))
    if rows * cols < l:
        rows += 1

    grid = [s[i:i+cols] for i in range(0, l, cols)]
    encrypted = ""

    for i in range(cols):
        for row in grid:
            if i < len(row):
                encrypted += row[i]
        encrypted += " "

    return encrypted.strip()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
