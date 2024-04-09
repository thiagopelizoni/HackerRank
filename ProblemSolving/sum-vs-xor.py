# https://www.hackerrank.com/challenges/sum-vs-xor/problem
import os

def sumXor(n):
    zero_bit_count = 0

    while n:
        if n & 1 == 0:
            zero_bit_count += 1
        n >>= 1

    return 2 ** zero_bit_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
