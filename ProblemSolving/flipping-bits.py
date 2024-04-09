# https://www.hackerrank.com/challenges/flipping-bits/problem
import os

def flippingBits(n):
    k = (2**32) - 1
    return k - n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
