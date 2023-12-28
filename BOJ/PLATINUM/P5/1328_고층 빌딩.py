import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


MOD = 1000000007


def dfs(h, l, r):

    if dp[h][l][r]: return dp[h][l][r] 
    if l == r == 1: return 0
    if l == 0 or r == 0: return 0
    if l+r > h+1: return 0

    dp[h][l][r] = dfs(h-1, l-1, r) + dfs(h-1, l, r-1) + dfs(h-1, l, r)*(h-2)
    return dp[h][l][r]


N, L, R = map(int, input().split())

dp = list(list([0] * (R+1) for _ in range(L+1)) for _ in range(N+1))
dp[1][1][1] = 1

print(dfs(N, L, R) % MOD)
