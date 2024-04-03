# https://www.hackerrank.com/challenges/reduced-string/problem
import os

def superReducedString(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    reduced_string = ''.join(stack)

    return reduced_string if reduced_string else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = superReducedString(s)
    fptr.write(result + '\n')
    fptr.close()
