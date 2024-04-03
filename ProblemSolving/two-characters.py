# https://www.hackerrank.com/challenges/two-characters/problem
import os

def alternate(s):
    unique_characters = set(s)
    max_length = 0

    for first in unique_characters:
        for second in unique_characters:
            if first != second:
                filtered = [c for c in s if c == first or c == second]
                if all(filtered[i] != filtered[i + 1] for i in range(len(filtered) - 1)):
                    max_length = max(max_length, len(filtered))

    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
