import sys
# input = sys.stdin.readline
sys.stdin = open("BOJ/input.txt", "r")

N, M = map(int, input().split())

items = []
for i in range(N):
    V, C, K = map(int, input().split())

    cnt = 1
    while K > 0:
        next = min(cnt, K)
        items.append((V*next, C*next))

        K -= next
        cnt *= 2

dp = [0] * (M+1)
for w, v in items:
    for i in range(M, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[M])
