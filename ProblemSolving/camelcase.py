# https://www.hackerrank.com/challenges/camelcase/problem
import os

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1 if s else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
