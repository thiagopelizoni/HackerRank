# https://www.hackerrank.com/challenges/the-great-xor/problem
import math
import os

def theGreatXor(x):
    return 2 ** (math.floor(math.log(x, 2)) + 1) - x - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        x = int(input().strip())

        result = theGreatXor(x)

        fptr.write(str(result) + '\n')

    fptr.close()