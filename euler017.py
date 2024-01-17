#  https://www.hackerrank.com/contests/projecteuler/challenges/euler017/
import itertools

def number_to_words_large(n):
    if n == 0:
        return 'Zero'

    def small_number_to_words(n):
        up_to_nineteen = [
            'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        tens = [
            'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]

        if n < 20:
            return up_to_nineteen[n-1:n]
        elif n < 100:
            return [tens[n//10-2]] + small_number_to_words(n % 10)
        else:
            return [up_to_nineteen[n//100-1]] + ['Hundred'] + small_number_to_words(n % 100)

    # Divide the number into groups of three digits
    groups = [('Billion', 10**9), ('Million', 10**6), ('Thousand', 10**3), ('', 1)]
    words = []
    for word, value in groups:
        if n >= value:
            words.extend(small_number_to_words(n // value))
            words.append(word)
            n %= value

    return ' '.join(filter(bool, words))

if __name__ == '__main__':
    lenght = int(input().strip())

    for _ in range(lenght):
        n = int(input().strip())
        print(number_to_words_large(n))
