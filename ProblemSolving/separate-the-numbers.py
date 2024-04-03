# https://www.hackerrank.com/challenges/separate-the-numbers/problem
def separateNumbers(s):
    for initial_length in range(1, len(s)):
        first_number = int(s[:initial_length])
        next_number = first_number
        sequence = ''

        while len(sequence) < len(s):
            sequence += str(next_number)
            next_number += 1

        if sequence == s:
            print(f"YES {first_number}")
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
