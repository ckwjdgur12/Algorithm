import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


def dfs(l, r, turn):
    if turn > N: return 0
    if dp[l][r]: return dp[l][r]
    
    if turn%2 == 1:
        dp[l][r] = max(dfs(l+1, r, turn+1)+cards[l], dfs(l, r-1, turn+1)+cards[r])
    else:
        dp[l][r] = min(dfs(l+1, r, turn+1), dfs(l, r-1, turn+1))
        
    return dp[l][r]


T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    dp = list([0] * N for _ in range(N))

    print(dfs(0, N-1, 1))
