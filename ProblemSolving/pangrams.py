# https://www.hackerrank.com/challenges/pangrams/problem
import os

def pangrams(s):
    return "pangram" if len(set(s.lower()) - set(" ")) == 26 else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
