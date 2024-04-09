# https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
import os

def theLoveLetterMystery(s):
    return sum(abs(ord(s[i]) - ord(s[-i - 1])) for i in range(len(s) // 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
