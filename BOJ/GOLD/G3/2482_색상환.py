import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


MOD = 1000000003


def dfs(n, k):
    if k > n//2: return 0
    if dp[n][k] != -1: return dp[n][k]

    dp[n][k] = dfs(n-1, k) + dfs(n-2, k-1)
    return dp[n][k]


N = int(input())
K = int(input())

dp = list([-1] * (K+1) for _ in range(N+1))

for i in range(N+1):
    dp[i][1] = i
    dp[i][0] = 1

print(dfs(N, K)%MOD)

