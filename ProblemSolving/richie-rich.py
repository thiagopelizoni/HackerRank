# https://www.hackerrank.com/challenges/richie-rich/problem
import os

def highestValuePalindrome(s, n, k):
    s = list(s)
    least_changes = sum(1 for i in range(len(s) // 2) if s[i] != s[len(s) - i - 1])

    if least_changes > k:
        return '-1'

    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            if k > least_changes:
                if s[i] != '9':
                    s[i] = '9'
                    k -= 1
                if s[j] != '9':
                    s[j] = '9'
                    k -= 1
                least_changes -= 1
            else:
                s[i] = max(s[i], s[j])
                s[j] = max(s[i], s[j])
                least_changes -= 1
                k -= 1
        elif k - least_changes >= 2 and s[i] != '9':
            s[i] = '9'
            s[j] = '9'
            k -= 2
        i += 1
        j -= 1

    if k > 0 and len(s) % 2 != 0:
        s[len(s) // 2] = '9'

    return "".join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
