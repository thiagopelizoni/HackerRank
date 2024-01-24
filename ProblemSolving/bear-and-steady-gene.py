#!/bin/python3
# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
import math
import os
import random
import re
import sys

def steadyGene(gene):
    def is_valid_substring_size(size):
        for i in range(n - size + 1):
            start, end = i, i + size - 1
            for j in range(4):
                x = 0
                if start != 0:
                    x = dp[j][start - 1]
                if dp[j][-1] - (dp[j][end] - x) > min_required_count:
                    break
            else:
                return True
        return False

    n = len(gene)
    dp = [[0 for _ in range(n)] for _ in range(4)]

    for i in range(n):
        char_index = 'ACGT'.index(gene[i])
        for j in range(4):
            dp[j][i] = dp[j][i - 1]
        dp[char_index][i] += 1

    min_required_count = n // 4
    min_substring_length = n
    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2
        if is_valid_substring_size(mid):
            min_substring_length = mid
            high = mid - 1
        else:
            low = mid + 1

    return min_substring_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
