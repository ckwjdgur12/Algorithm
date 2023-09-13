import sys
from collections import defaultdict
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

priority = {'(' : 0, '+' : 1, '-' : 1, '*' : 2}

def get_postfix_formula(formula):

    postfix_formula = []
    s = []

    for f in formula:
        if f == '+' or f == '-' or f == '*':
            while s:
                if priority[s[-1]] < priority[f]: break
                postfix_formula.append(s.pop())
            s.append(f)
        elif f == '(': 
            s.append(f)
        elif f == ')':
            while True:
                next_elem = s.pop()
                if next_elem == '(': break
                postfix_formula.append(next_elem)
        else:
            postfix_formula.append(f)

    while s:
        postfix_formula.append(s.pop())

    return postfix_formula


def dfs(formula):

    key_str = ''.join(formula)
    if done[key_str]: return

    postfix_formula = get_postfix_formula(formula)
    calc(postfix_formula, key_str)

    skip_cnt = 0

    if formula[0] == '(': start = 6
    else: start = 1

    for i in range(start, len(formula)-1):
        if skip_cnt:
            skip_cnt -= 1
            continue

        if formula[i] == '(':
            skip_cnt = 5
            continue

        if formula[i+1] == '(':
            skip_cnt = 6
            continue

        if formula[i] == '*': continue
        if formula[i] != '+' and formula[i] != '-': continue

        if i == 1:
            next_formula = ['('] + formula[i-1:i+2] + [')'] + formula[i+2:]
        elif i != len(formula)-1:
            next_formula = formula[:i-1] + ['('] + formula[i-1:i+2] + [')'] + formula[i+2:]
        else:
            next_formula = formula[:i-1] + ['('] + formula[i-1:i+2] + [')']
        
        dfs(next_formula)

    return


def calc(formula, key_str):
    global final_ans

    s = []
    for f in formula:
        if f != '+' and f != '-' and f != '*': 
            s.append(int(f))
        else:
            num2 = s.pop()
            num1 = s.pop()
            if f == '+': s.append(num1 + num2)
            elif f == '-': s.append(num1 - num2)
            elif f == '*': s.append(num1 * num2)
    
    final_ans = max(final_ans, s[0])
    done[key_str] = True


N = int(input())

input_formula = list(input().strip())
final_ans = -2**31
done = defaultdict(bool)

dfs(input_formula)
print(final_ans)
