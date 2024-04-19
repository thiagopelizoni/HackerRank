# https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter
import os

def gameOfThrones(s):
    odd_counts = [count for count in Counter(s).values() if count % 2 != 0]
    return "NO" if len(odd_counts) > 1 else "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = gameOfThrones(s)
    
    fptr.write(result + '\n')
    fptr.close()
