# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
import os

def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            shifted = ord(char) + k % 26
            if char.islower():
                result.append(chr(shifted if shifted <= ord('z') else shifted - 26))
            else:
                result.append(chr(shifted if shifted <= ord('Z') else shifted - 26))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
