# https://www.hackerrank.com/contests/projecteuler/challenges/euler059/problem

from itertools import product
from string import ascii_lowercase, printable

def find_key(chars, size):
    valid_chars = " ();:,.'?-" + printable[:63]
    
    for key in product(ascii_lowercase, repeat=3):
        valid_key = True
        for i in range(size):
            xor_result = chr(int(chars[i]) ^ ord(key[i % len(key)]))
            if xor_result not in valid_chars:
                valid_key = False
                break
        
        if valid_key:
            return "".join(key)
    
    return None


if __name__ == '__main__':
    size = int(input())
    chars = list(map(int, input().split()))
    encryption_key = find_key(chars, size)
    print(encryption_key)
