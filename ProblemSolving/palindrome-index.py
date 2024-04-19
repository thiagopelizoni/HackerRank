# https://www.hackerrank.com/challenges/palindrome-index/problem
import os

def is_palindrome(s):
    half = len(s) // 2
    return s[:half] == s[-1:-half-1:-1]
        
def palindromeIndex(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s[:left] + s[left + 1:]):
                return left
            else:
                return right
        left += 1
        right -= 1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')

    fptr.close()
