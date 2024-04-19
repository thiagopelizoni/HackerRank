# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter
import os

def isValid(s):
    counts = Counter(Counter(s).values())
    
    if len(counts) == 1:
        return "YES"
    elif len(counts) == 2:
        t = sorted(counts.items(), reverse=True)
        if t[0][1] == 1 and (t[0][0] - t[1][0]) == 1:
            return "YES"
        elif t[-1] == (1, 1):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
