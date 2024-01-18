# https://www.hackerrank.com/contests/projecteuler/challenges/euler051/problem

def find_matching_numbers(number, regex, digit, remaining_occurrences, start_position, num_digits, num_occurrences, matches_dict, smallest_prime):
    digit_str = str(digit)
    for i in range(start_position, num_digits):
        if regex[i] != digit_str:
            continue
        if i == 0 and digit_str == '0':
            continue
        regex[i] = '.'
        if remaining_occurrences == 1:
            matching_numbers = matches_dict.setdefault("".join(regex), [])
            matching_numbers.append(number)
            if len(matching_numbers) >= num_occurrences and matching_numbers[0] < smallest_prime[0]:
                smallest_prime[0] = matching_numbers[0]
        else:
            find_matching_numbers(number, regex, digit, remaining_occurrences - 1, i + 1, num_digits, num_occurrences, matches_dict, smallest_prime)
        regex[i] = digit_str

def main():
    num_digits, num_occurrences, num_required_occurrences = map(int, input().split())
    min_number = 1
    for i in range(1, num_digits):
        min_number *= 10
    max_number = min_number * 10 - 1
    is_prime = [True] * (max_number + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(max_number ** 0.5) + 1):
        if is_prime[i]:
            for j in range(2 * i, max_number + 1, i):
                is_prime[j] = False

    matches_dict = {}
    smallest_prime = [99999999]

    for number in range(min_number, max_number + 1):
        if is_prime[number]:
            str_number = str(number)
            for digit in range(10):
                find_matching_numbers(number, list(str_number), digit, num_occurrences, 0, num_digits, num_required_occurrences, matches_dict, smallest_prime)
            if num_digits == 7:
                if num_occurrences == 1 and number > 2 * 10 ** 6:
                    break
                if num_occurrences == 2 and number > 3 * 10 ** 6:
                    break

    result = ""
    for key, values in matches_dict.items():
        if len(values) < num_required_occurrences:
            continue
        if values[0] != smallest_prime[0]:
            continue
        s = " ".join(map(str, values[:num_required_occurrences]))
        if result > s or not result:
            result = s
    print(result)

if __name__ == "__main__":
    main()
