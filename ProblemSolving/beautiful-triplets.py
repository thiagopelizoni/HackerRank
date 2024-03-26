# https://www.hackerrank.com/challenges/beautiful-triplets/problem
import os

def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)
    for i in arr:
        if i + d in arr_set and i + 2 * d in arr_set:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
