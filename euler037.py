#  https://www.hackerrank.com/contests/projecteuler/challenges/euler037/
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def truncatable_primes(n):
    sum_of_primes = 0
    for num in range(11, n, 2):
        str_num = str(num)
        left_to_right = all(is_prime(int(str_num[i:])) for i in range(len(str_num)))
        right_to_left = all(is_prime(int(str_num[:i])) for i in range(len(str_num), 0, -1))

        if left_to_right and right_to_left:
            sum_of_primes += num

    return sum_of_primes

if __name__ == '__main__':
    n = int(input().strip())
    print(truncatable_primes(n))
