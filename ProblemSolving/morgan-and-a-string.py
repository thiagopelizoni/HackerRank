#!/bin/python3
# https://www.hackerrank.com/challenges/morgan-and-a-string/problem

import os

def morganAndString(a, b):
    x = a + "z"
    y = b + "z"
    r = ""

    while not r.endswith('z'):
        if x < y:
            r += x[0]
            x = x[1:]
        else:
            r += y[0]
            y = y[1:]
    
    return r[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
