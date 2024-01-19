# https://www.hackerrank.com/contests/projecteuler/challenges/euler089/problem
def roman_to_int(s):
    ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = None
    for char in reversed(s):
        value = ROMAN[char]
        if prev_value is None or prev_value <= value:
            result += value
        else:
            result -= value
        prev_value = value
    return result

def magnitude_to_roman(mag, chars, r):
    chars = list(chars)
    order = [
        [9 * mag, chars[-1] + chars[0], l1],
        [5 * mag, chars[1], l1],
        [4 * mag, chars[-1] + chars[1], l1],
        [mag, chars[-1], l2]
    ]

    for o in order:
        r = o[-1](r, o[:-1])
    return r

def l1(r, ds):
    return [r[0] + ds[1], r[1] - ds[0]] if r[1] >= ds[0] else r

def l2(r, ds):
    return [r[0] + ds[1] * (r[1] // ds[0]), r[1] % ds[0]]

def int_to_roman(num):
    MAG_ORDER = [
        (100, "MDC"),
        (10, "CLX"),
        (1, "XVI"),
    ]

    r = ['M' * (num // 1000), num % 1000]
    for mag, chars in MAG_ORDER:
        r = magnitude_to_roman(mag, chars, r)
    return r[0]

n = int(input())
for _ in range(n):
    roman_input = input().strip()
    int_value = roman_to_int(roman_input)
    roman_value = int_to_roman(int_value)
    print(roman_value)
