# https://www.hackerrank.com/challenges/find-digits/problem
import os

def findDigits(n):
    count = 0
    n_str = str(n)
    
    for digit_char in n_str:
        digit = int(digit_char)
    
        if digit != 0 and n % digit == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')

    fptr.close()
