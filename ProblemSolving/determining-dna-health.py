# https://www.hackerrank.com/challenges/determining-dna-health/problem
# I couldn't pass on Test Cases cases 7, 8, 9 and 13
def build_tree(genes):
    root = {}

    for i, gene in enumerate(genes):
        current_node = root
        for c in gene:
            current_node = current_node.setdefault(c, {})
        current_node.setdefault('indices', []).append(i)

    return root

def determine_dna(root, health, first, last, d):
    health_sum = 0

    for i in range(len(d)):
        current_node = root
        for j in range(i, len(d)):
            c = d[j]
            if c not in current_node:
                break

            current_node = current_node[c]
            health_sum += get_health_sum(current_node.get('indices', []), health, first, last)

    return health_sum

def get_health_sum(indices, health, first, last):
    total_health = 0
    for index in indices:
        if first <= index <= last:
            total_health += health[index]
    return total_health

def dna_health(genes, health, strands):
    root = build_tree(genes)
    max_health = float('-inf')
    min_health = float('inf')

    for strand in strands:
        first = strand[0]
        last = strand[1]
        d = strand[2]
        health_sum = determine_dna(root, health, first, last, d)

        max_health = max(max_health, health_sum)
        min_health = min(min_health, health_sum)

    print(min_health, max_health)

if __name__ == "__main__":
    n = int(input().strip())
    strands = []
    genes = input().split()
    health = list(map(int, input().split()))
    s = int(input().strip())

    for _ in range(s):
        first, last, d = input().split()
        strands.append((int(first), int(last), d))

    dna_health(genes, health, strands)
