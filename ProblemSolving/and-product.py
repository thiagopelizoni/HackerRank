# https://www.hackerrank.com/challenges/and-product/problem
import os

def andProduct(a, b):
    shift = 0
    while a < b:
        a >>= 1
        b >>= 1
        shift += 1
    return a << shift

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = andProduct(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
