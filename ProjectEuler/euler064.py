# https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem
import math

def calculate_odd_period_count(n):
    square_root_n = int(math.sqrt(n))
    if square_root_n * square_root_n == n:
        return 0
    
    a = 1
    integer_part_list = [square_root_n]
    denominator = n - square_root_n * square_root_n
    inverse_fraction_list = [(math.sqrt(n) + square_root_n) / denominator]
    period_count = 0
    
    while True:
        partial_integer_part = int(inverse_fraction_list[-1])
        square_root_n = (denominator * partial_integer_part) // a - square_root_n
        
        a = denominator // a
        denominator = n - square_root_n * square_root_n
        
        inverse_fraction = a * (math.sqrt(n) + square_root_n) / denominator
        
        integer_part_list.append(partial_integer_part)
        inverse_fraction_list.append(inverse_fraction)
        
        period_count += 1
        
        if inverse_fraction == inverse_fraction_list[0]:
            return period_count

if __name__ == "__main__":
    n = int(input())
    odd_period_count = 0
    
    for k in range(2, n + 1):
        if calculate_odd_period_count(k) % 2 == 1:
            odd_period_count += 1
    
    print(odd_period_count)
