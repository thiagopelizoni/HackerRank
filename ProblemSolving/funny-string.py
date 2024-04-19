# https://www.hackerrank.com/challenges/funny-string/problem
import os

def funnyString(s):
    r = s[::-1]
    return "Funny" if [abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s)-1)] == [abs(ord(r[i]) - ord(r[i+1])) for i in range(len(s)-1)] else "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
