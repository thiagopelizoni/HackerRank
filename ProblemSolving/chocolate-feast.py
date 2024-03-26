# https://www.hackerrank.com/challenges/chocolate-feast/problem
import os

def chocolateFeast(n, c, m):
    chocolates = n // c
    wrappers = chocolates
    while wrappers >= m:
        exchange = wrappers // m
        chocolates += exchange
        wrappers = wrappers % m + exchange
    return chocolates
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        c = int(first_multiple_input[1])
        m = int(first_multiple_input[2])
        result = chocolateFeast(n, c, m)
        fptr.write(str(result) + '\n')
    fptr.close()
