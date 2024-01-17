#  https://www.hackerrank.com/contests/projecteuler/challenges/euler022/
def read_names(n):
    names = []
    for _ in range(n):
        name = input()
        names.append(name)
    return names

def calculate_scores(names):
    scores = {}
    names.sort()
    for i, name in enumerate(names, start=1):
        score = 0
        for char in name:
            score += ord(char) - 64
        score *= i
        scores[name] = score
    return scores

def main():
    n = int(input())
    names = read_names(n)
    scores = calculate_scores(names)

    q = int(input())
    for _ in range(q):
        query = input()
        print(scores.get(query, 0))

if __name__ == "__main__":
    main()
