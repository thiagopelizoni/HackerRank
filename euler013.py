if __name__ == '__main__':
    t = int(input())

    numbers = []
    [numbers.append(int(input())) for i in range(t)]
    answer = str(sum(numbers))[:10]
    
    print(answer)
