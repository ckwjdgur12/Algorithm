import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def dfs(w, h):

    if w == -1 or h == -1: return 0
    if w == 0 and h == 0: return 1
    if dp[w][h]: return dp[w][h]    

    dp[w][h] = dfs(w-1, h+1) + dfs(w, h-1)
    return dp[w][h]


dp = list([0] * 31 for _ in range(31))
dfs(30, 0)

while True:
    N = int(input())
    if N == 0: break

    print(dp[N][0])
