# https://www.hackerrank.com/challenges/counter-game/problem
import os

def counterGame(n):
    count = 0
    n -= 1
    while n:
        n &= n - 1
        count += 1
    return "Louise" if count % 2 else "Richard"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

