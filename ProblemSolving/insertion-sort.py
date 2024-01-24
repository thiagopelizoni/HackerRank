# https://www.hackerrank.com/challenges/insertion-sort/problem
import math
import os
import random
import re
import sys

def update_bit_array(index, bit_array):
    while index < len(bit_array):
        bit_array[index] += 1
        index += (index & -index)

def query_bit_array(index, bit_array):
    total = 0
    while index > 0:
        total += bit_array[index]
        index -= (index & -index)
    return total

def insertionSort(arr):
    shifts = 0
    bit_array = [0] * 10000001
    max_index = 10000000
    
    for i in range(len(arr)):
        shifts += query_bit_array(max_index, bit_array) - query_bit_array(arr[i], bit_array)
        update_bit_array(arr[i], bit_array)
    
    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)
        print(result)

        fptr.write(str(result) + '\n')

    fptr.close()
