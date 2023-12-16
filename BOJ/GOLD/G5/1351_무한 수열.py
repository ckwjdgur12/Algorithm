import sys
from collections import defaultdict

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def dfs(n):
    if n == 0: return 1
    if dp[n]: return dp[n]

    dp[n] = dfs(n//P) + dfs(n//Q)
    return dp[n]


N, P, Q = map(int, input().split())
dp = defaultdict(int)
dp[0] = 1

print(dfs(N))


'''
A[N] = A[N//P] + A[N//Q]

7 2 3

A0 = 1
A1 = A0 + A0 = 1
A2 = 


'''


