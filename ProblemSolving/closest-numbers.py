# https://www.hackerrank.com/challenges/closest-numbers/problem
import os

def closestNumbers(arr):
    arr.sort()
    min_diff = float('inf')
    pairs = []

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
            pairs = [arr[i], arr[i + 1]]
        elif diff == min_diff:
            pairs.extend([arr[i], arr[i + 1]])

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
