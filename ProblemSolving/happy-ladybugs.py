# https://www.hackerrank.com/challenges/happy-ladybugs/problem
import os
import collections
import string

def happyLadybugs(b):
    count = collections.Counter(b)

    if any(count[char] < 2 for char in string.ascii_uppercase if char in count):
        return "NO"

    if '_' not in count and any(b.find(char * 2) == -1 for char in count):
        return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())
        b = input()
        result = happyLadybugs(b)
        fptr.write(result + '\n')

    fptr.close()
