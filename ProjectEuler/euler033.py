# https://www.hackerrank.com/contests/projecteuler/challenges/euler033/problem
import itertools

def generate_strings_with_number(strings, number):
    string_length = len(strings[0]) + 1
    generated_strings = [string[:i] + str(number) + string[i:] for string in strings for i in range(string_length)]
    return generated_strings

def generate_permutations(unordered_list, ordered_list):
    while unordered_list:
        number = unordered_list.pop()
        ordered_list = generate_strings_with_number(ordered_list, number)
    return set(ordered_list)

def list_to_str(sequence):
    return ''.join([str(item) for item in sequence])

def list_to_int(sequence):
    return int(''.join([str(item) for item in sequence]))

n, k = map(int, input().split())

common_combinations = list(itertools.combinations_with_replacement(range(1, 10), r=k))
other_combinations = list(itertools.product(range(10), repeat=n - k))
other_combinations.remove((0,) * (n - k))

unique_fractions = set()
fractions_list = []

for common in common_combinations:
    current_fraction_list = []
    for other in other_combinations:
        current_fraction_list += [(list_to_int(other), int(common_part)) for common_part in generate_permutations(list(common), [list_to_str(other)]) if common_part[0] != '0']
    fractions_list.append(current_fraction_list)

for fraction_group in fractions_list:
    for item in itertools.combinations(fraction_group, r=2):
        if item[0][0] < item[1][0] and item[0][0] * item[1][1] == item[1][0] * item[0][1]:
            unique_fractions.add((item[0][1], item[1][1]))

numerator_sum = sum([fraction[0] for fraction in unique_fractions])
denominator_sum = sum([fraction[1] for fraction in unique_fractions])

print(numerator_sum, denominator_sum)
