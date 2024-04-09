# https://www.hackerrank.com/challenges/lonely-integer/problem
import os

def lonelyinteger(a):
    result = 0
    for number in a:
        result ^= number
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
