# https://www.hackerrank.com/challenges/yet-another-minimax-problem/problem
import os

def anotherMinimaxProblem(a):
    if all(x == 0 for x in a): 
        return 0

    n = len(a)
    max_bit = max(a).bit_length()

    for bit in range(max_bit - 1, -1, -1):
        ones, zeros = [], []
        for num in a:
            if num & (1 << bit):
                ones.append(num)
            else:
                zeros.append(num)
        if zeros and ones:
            break

    if not zeros or not ones:
        return min(a[i] ^ a[j] for i in range(n) for j in range(i + 1, n))

    return min(x ^ y for x in zeros for y in ones)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = anotherMinimaxProblem(a)

    fptr.write(str(result) + '\n')

    fptr.close()
