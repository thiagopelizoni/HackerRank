# https://www.hackerrank.com/challenges/maximizing-xor/problem
import os

def maximizingXor(l, r):
    maxXor = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            maxXor = max(maxXor, i ^ j)
    return maxXor

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
