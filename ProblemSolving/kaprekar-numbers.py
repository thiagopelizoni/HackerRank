# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
import math
import os
import random
import re
import sys

def kaprekarNumbers(p, q):
    kaprekar = []
    for i in range(p, q + 1):
        square = str(i * i)
        d = len(str(i))
        l = square[:len(square) - d]
        r = square[len(square) - d:]
        l = int(l) if l != '' else 0
        r = int(r) if r != '' else 0
        if l + r == i:
            kaprekar.append(i)
    if not kaprekar:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, kaprekar)))

if __name__ == '__main__':
    p = int(input().strip())
    q = int(input().strip())
    kaprekarNumbers(p, q)
