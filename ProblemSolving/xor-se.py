# https://www.hackerrank.com/challenges/xor-se/problem
import os

def xorSequence(l, r):
    def sequence(N):
        rem = N % 8
        if rem == 0 or rem == 1:
            return N
        elif rem == 2 or rem == 3:
            return 2
        elif rem == 4 or rem == 5:
            return N + 2
        else:
            return 0
    return sequence(r) ^ sequence(l - 1) if l > 0 else sequence(r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        lr = input().split()

        l = int(lr[0])

        r = int(lr[1])

        result = xorSequence(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
