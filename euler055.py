# https://www.hackerrank.com/contests/projecteuler/challenges/euler055/problem

def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

def find_max_palindrome_convergence(n):
    palindromes = []

    for num in range(1, n + 1):
        iterations = 0
        while iterations < 60:
            if is_palindrome(num):
                palindromes.append(num)
                break
            num += int(str(num)[::-1])
            iterations += 1

    max_count = 0
    most_frequent_palindrome = None

    for palindrome in sorted(set(palindromes)):
        count = palindromes.count(palindrome)
        if count > max_count:
            most_frequent_palindrome = palindrome
            max_count = count

    print(most_frequent_palindrome, max_count)
    
if __name__ == "__main__":
    n = int(input())
    find_max_palindrome_convergence(n)
