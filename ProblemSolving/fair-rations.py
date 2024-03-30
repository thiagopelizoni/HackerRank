# https://www.hackerrank.com/challenges/fair-rations/problem
import os

def fairRations(B):
    loaves = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            loaves += 2
    return str(loaves) if B[-1] % 2 == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    fptr.write(result + '\n')
    fptr.close()
