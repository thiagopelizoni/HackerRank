# https://www.hackerrank.com/challenges/sansa-and-xor/problem
import os

def sansaXor(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        if (i + 1) * (n - i) % 2 != 0:
            result ^= arr[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
