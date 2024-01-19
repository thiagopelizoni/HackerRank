# https://www.hackerrank.com/contests/projecteuler/challenges/euler056/problem

def calculate_digital_sum(num):
    return sum(int(digit) for digit in str(num))

def find_maximum_digital_sum(N):
    """ Find and print the maximum digital sum """
    max_digital_sum = 0

    for a in range(1, N):
        for b in range(1, N):
            power = a ** b
            digital_sum = calculate_digital_sum(power)
            if digital_sum > max_digital_sum:
                max_digital_sum = digital_sum

    return max_digital_sum

if __name__ == "__main__":
    m = int(input())
    print(find_maximum_digital_sum(m))
