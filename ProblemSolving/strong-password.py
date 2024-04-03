# https://www.hackerrank.com/challenges/strong-password/problem
import os

def minimumNumber(n, password):
    count = 0
    if not any(c.isdigit() for c in password):
        count += 1
    if not any(c.islower() for c in password):
        count += 1
    if not any(c.isupper() for c in password):
        count += 1
    if not any(c in "!@#$%^&*()-+" for c in password):
        count += 1
    return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    
    password = input()
    answer = minimumNumber(n, password)
    fptr.write(str(answer) + '\n')
    fptr.close()
