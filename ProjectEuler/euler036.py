#  https://www.hackerrank.com/contests/projecteuler/challenges/euler036/
def is_palindrome(n, k):
    s = ""
    while n:
        n, r = divmod(n, k)
        s += str(r)
    return s[::-1]

def sum_double_base_palindromes(n, k):
    t = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if is_palindrome(i, k) == is_palindrome(i, k)[::-1]:
                t += i
    return t

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(sum_double_base_palindromes(n, k))
