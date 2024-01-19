# https://www.hackerrank.com/contests/projecteuler/challenges/euler104/problem
# That's my attempt to solve but not passed on all test cases resulting in timeout
def is_k_pandigital(n, k):
    """Check if a number n is k-pandigital on both ends."""
    digits = str(n)
    return set(digits[:k]) == set(digits[-k:]) == set(str(i) for i in range(1, k+1))

def pandigital_fibonacci(a, b, k):
    """Find the index n of the generalized Fibonacci number."""
    fib1, fib2 = a, b  # Initialize the first two terms of the sequence
    n = 2
    while True:
        # Calculate next Fibonacci number
        fib_next = fib1 + fib2
        # Only check pandigital property when the number of digits is sufficient
        if len(str(fib_next)) >= k:
            if is_k_pandigital(fib_next, k):
                return n + 1  # Return the index of the pandigital number
        fib1, fib2 = fib2, fib_next
        n += 1
        if n > 2 * 10**6:  # Break if the limit is reached
            return 'no solution'

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    k = int(input().strip())
    answer = pandigital_fibonacci(a, b, k)
    print(answer)
