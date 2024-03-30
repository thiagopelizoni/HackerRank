# https://www.hackerrank.com/challenges/strange-code/problem
import os

def strangeCounter(t):
    if t < 1:
        return 0

    base = 3
    while t > base:
        t -= base
        base *= 2

    return base - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    result = strangeCounter(t)
    fptr.write(str(result) + '\n')
    fptr.close()
