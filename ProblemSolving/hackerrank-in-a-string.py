# https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
import os

def hackerrankInString(s):
    search = "hackerrank"
    j = 0
    for char in s:
        if j < len(search) and char == search[j]:
            j += 1
    return "YES" if j == len(search) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
