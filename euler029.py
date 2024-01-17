#  https://www.hackerrank.com/contests/projecteuler/challenges/euler029/
def count_prime_powers(limit):
    is_prime = [True] * (limit + 1)
    total_count = 0

    for number in range(2, limit + 1):
        if is_prime[number]:
            power = 2
            non_prime_multiples = []

            while number ** power <= limit:
                is_prime[number ** power] = False
                non_prime_multiples += [n for n in range(2 * power, limit * power + 1, power) if n > limit]
                power += 1

            total_count += len(set(non_prime_multiples)) + (limit - 1)

    return total_count

if __name__ == "__main__":
    N = int(input())
    result = count_prime_powers(N)
    print(result)
