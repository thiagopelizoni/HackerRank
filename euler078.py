# https://www.hackerrank.com/contests/projecteuler/challenges/euler078/problem
MOD = 10**9 + 7

def partition_function(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1

    pentagonal_numbers = []
    limit = int((2 * n) ** 0.5) + 1
    for i in range(1, limit):
        a = i * (3 * i - 1) // 2
        b = i * (3 * i + 1) // 2
        pentagonal_numbers.append(a)
        pentagonal_numbers.append(b)

    for i in range(1, n + 1):
        partitions[i] = 0
        
        for j, pent in enumerate(pentagonal_numbers):
            if pent > i:
                break

            sign = -1 if j // 2 % 2 else 1
            partitions[i] = (partitions[i] + sign * partitions[i - pent]) % MOD

    return partitions[n]

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(partition_function(n))
