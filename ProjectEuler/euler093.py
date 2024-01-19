# https://www.hackerrank.com/contests/projecteuler/challenges/euler093/problem
# That's my attempt to solve but not passed on all test cases
import itertools
import operator


ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calculate_all(numbers):
    all_results = set()

    for nums in itertools.permutations(numbers):
        for op_comb in itertools.product(ops, repeat=len(numbers)-1):

            rpn = list(nums)
            for op in op_comb:
                rpn.append(op)
            try:
                all_results |= evaluate_rpn(rpn)
            except Exception:
                pass  # Ignore invalid RPN expressions or math errors
    return all_results

def evaluate_rpn(rpn):
    results = set()
    for i in range(len(rpn)):
        for j in range(i+1, len(rpn)):
            try:
                stack = []
                for token in (rpn[:i] + ['('] + rpn[i:j] + [')'] + rpn[j:]):
                    if token in ops:
                        op2 = stack.pop()
                        op1 = stack.pop()
                        stack.append(ops[token](op1, op2))
                    elif token == '(':
                        pass
                    elif token == ')':
                        op2 = stack.pop()
                        op1 = stack.pop()
                        stack.append(op2)
                        stack.append(op1)
                    else:
                        stack.append(float(token))
                if len(stack) == 1 and stack[0].is_integer():
                    results.add(int(stack[0]))
            except (IndexError, ZeroDivisionError):
                pass
    return results

def find_largest_n(all_results):
    n = 0
    while n + 1 in all_results:
        n += 1
    return n

if __name__ == '__main__':
    t = int(input())
    numbers = list(map(int, input().split()))
    
    all_results = calculate_all(numbers)
    answer = find_largest_n(all_results)
    
    print(answer)

       
