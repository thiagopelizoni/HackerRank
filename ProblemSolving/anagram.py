# https://www.hackerrank.com/challenges/anagram/problem
from collections import Counter
import os

def anagram(s):
    if len(s) % 2:
        return -1
    counterOne = Counter(s[:len(s)//2])
    counterTwo = Counter(s[len(s)//2:])
    
    difference = counterTwo - counterOne
    
    return sum(difference.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
