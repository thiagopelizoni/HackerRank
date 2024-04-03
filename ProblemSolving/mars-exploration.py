# https://www.hackerrank.com/challenges/mars-exploration/problem
import os

def marsExploration(s):
    return sum(1 for i in range(len(s)) if s[i] != "SOS"[i % 3])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
