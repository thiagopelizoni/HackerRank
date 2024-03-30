# https://www.hackerrank.com/challenges/absolute-permutation/problem
import os

def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n + 1))

    if (n / k) % 2 == 0:
        return [i + k if ((i - 1) // k) % 2 == 0 else i - k for i in range(1, n + 1)]

    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
