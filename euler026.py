#  https://www.hackerrank.com/contests/projecteuler/challenges/euler026/
def find_repeating_cycle_length(n):
    seen_mods = [0] * n
    seen_mods[1] = 1
    multiplier = 1
    i = 2

    while True:
        multiplier *= 10
        remainder = multiplier % n

        if remainder == 0:
            return 0

        if seen_mods[remainder]:
            return i - seen_mods[remainder]

        seen_mods[remainder] = i
        i += 1
        multiplier = remainder

def precalculate_cycles(limit):
    answer = [0] * (limit + 1)
    cycle_length = [0] * (limit + 1)
    answer[3] = 3
    answer[4] = 3
    cycle_length[4] = 1
    cycle_length[3] = 1

    for i in range(5, limit + 1):
        cycle = find_repeating_cycle_length(i)

        if cycle > cycle_length[answer[i - 1]]:
            answer[i] = i
            cycle_length[i] = cycle
        else:
            answer[i] = answer[i - 1]
            cycle_length[i] = cycle_length[i - 1]

    return answer

def main():
    limit = 10000
    answer = precalculate_cycles(limit)

    num_cases = int(input())

    for _ in range(num_cases):
        n = int(input())
        print(answer[n - 1])

if __name__ == "__main__":
    main()
