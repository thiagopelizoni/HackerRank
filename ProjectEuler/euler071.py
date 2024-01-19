# https://www.hackerrank.com/contests/projecteuler/challenges/euler071/problem

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b, n = [int(x) for x in input().split()]
        
        inv_a = modular_inverse(a, b)
        
        remainder = n % b
        
        difference = remainder - inv_a
        
        if difference < 0:
            difference += b

        denominator = n - difference
        numerator = (denominator * a - 1) // b
        print(numerator, denominator)
