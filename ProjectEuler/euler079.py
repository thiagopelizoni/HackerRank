# https://www.hackerrank.com/contests/projecteuler/challenges/euler079/problem

def find_password(logins):
    graph = {}
    for login in logins:
        for i, char in enumerate(login):
            if char not in graph:
                graph[char] = set()
            if i > 0:
                graph[login[i - 1]].add(char)
    
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    queue = [u for u in graph if in_degree[u] == 0]
    queue.sort(reverse=True)
    password = ''
    
    while queue:
        u = queue.pop()
        password += u
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                queue.sort(reverse=True)

    if len(password) != len(graph):
        return "SMTH WRONG"
    
    return password

if __name__ == '__main__':
    t = int(input())
    samples = []
    for i in range(t):
        samples.append(input())
        
    answer = find_password(samples)
    print(answer)
