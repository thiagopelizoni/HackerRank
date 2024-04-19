# https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter
import os

def makingAnagrams(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    
    common_chars = counter_s1 & counter_s2
    common_chars_total = sum(common_chars.values())
    
    return len(s1) + len(s2) - common_chars_total * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
