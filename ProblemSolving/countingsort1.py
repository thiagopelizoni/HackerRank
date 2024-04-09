# https://www.hackerrank.com/challenges/countingsort1/problem
import os

def countingSort(arr):
    count = [0] * 100
    for number in arr:
        count[number] += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
