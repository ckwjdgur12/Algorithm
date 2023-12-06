import sys

# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")


N, M, K = map(int, input().split())

dp = list([1] * (M+1) for _ in range(N+1))

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[-1][-1] < K:
    print(-1)
    exit(0)

ans = ""
while N > 0 and M > 0:
    nxt = dp[N-1][M]

    if K > nxt:
        ans += 'z'
        M -= 1
        K -= nxt
    else:
        ans += 'a'
        N -= 1

ans += 'a'*N + 'z'*M
print(ans)
