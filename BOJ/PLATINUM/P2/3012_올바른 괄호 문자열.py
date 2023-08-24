import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

def bracket_check(start, end):

    if start > end: return 1
    if dp[start][end] != -1: return dp[start][end]
    if seq[start] in cl: return 0
    if seq[end] in op: return 0

    value = 0
    for i in range(start+1, end+1, 2):
        for j in range(3):
            if not (seq[start] == op[j] or seq[start] == '?'): continue
            if not (seq[i] == cl[j] or seq[i] == '?'): continue
            
            if seq[start] == '?' and seq[i] == '?':
                value += bracket_check(start+1, i-1) * bracket_check(i+1, end) * 3
                break
            elif seq[start] == '?' or seq[i] == '?':
                value += bracket_check(start+1, i-1) * bracket_check(i+1, end)
                break
            else:
                value += bracket_check(start+1, i-1) * bracket_check(i+1, end)

    dp[start][end] = value
    return value


N = int(input())
seq = input().strip()

dp = list([-1] * (N+1) for _ in range(N+1))
op = '({['
cl = ')}]'

print(str(bracket_check(0, N-1))[-5:])
